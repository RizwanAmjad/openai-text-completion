from ChatReply import get_reply_suggestions


def main():
    messages = [
        ("Ali", "Hi how are you?"),
        ("Rizwan", "I'm fine, How are you?"),
        ("Ali", "Fine! What are your plans for weekend")
    ]
    replies = get_reply_suggestions(messages)
    print(replies)


if __name__ == '__main__':
    main()
