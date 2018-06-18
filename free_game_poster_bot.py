import random
from time import sleep

from email_logic import get_unread_mail
from poster import post_message
from settings import WHITELIST_EMAIL_WORDS, WHITELIST_WORDS, BLACKLIST_WORDS, URL_WORD_LIST
from templates import FREE_GAME_MSG_TEMPLATE, fill_free_game_title_template


def free_game_bot():
    print("info: starting free game bot")
    while True:
        try:
            # fetch unread email
            admitted_email_address = False
            admitted_email_subj = False
            for fro, subj, msg in get_unread_mail():
                # email address filter
                for white_email_word in WHITELIST_EMAIL_WORDS:
                    if white_email_word in fro.lower():
                        admitted_email_address = True
                # subject filter
                # whitelist
                for white_content_word in WHITELIST_WORDS:
                    if white_content_word in subj.lower():
                        admitted_email_subj = True
                # blacklist
                for black_content_word in BLACKLIST_WORDS:
                    if black_content_word in subj.lower():
                        admitted_email_subj = False

                if admitted_email_address and admitted_email_subj:
                    # then create and post

                    ulr_line_no = None
                    stop_for_flag = False
                    msg_lines = msg.split("\n")
                    for line_no, line_content in enumerate(msg_lines):
                        if stop_for_flag:
                            break
                        for url_word in URL_WORD_LIST:
                            if url_word in line_content:
                                ulr_line_no = line_no
                                stop_for_flag = True
                                break
                    if ulr_line_no is None:
                        raise Exception("warning: didn't find url with pattern {}".format(URL_WORD_LIST))

                    url = msg_lines[ulr_line_no]
                    title = msg_lines[ulr_line_no - 1]
                    clean_title = title.split("*")[1]
                    platform = clean_title.split("]")[0].replace("[", "")
                    clean_title = clean_title.split("]")[1].split("(")[0]
                    clean_title = clean_title.strip()

                    msg_title = fill_free_game_title_template(
                        {"platform": platform,
                         "title": clean_title}
                    )

                    msg_content = random.choice(FREE_GAME_MSG_TEMPLATE).format(url)
                    post_message(url, "Utilidad Pública"
                                 , msg_title, msg_content, True)
                else:
                    print("info: email from {} received but discarded")
        except Exception as e:
            sleep_time = 5
            print("warning: email reader thrown exception, sleeping for {} seconds.".format(sleep_time))
            print("exception info:")
            print(e)
            print()
            sleep(sleep_time)


if __name__ == "__main__":
    free_game_bot()
