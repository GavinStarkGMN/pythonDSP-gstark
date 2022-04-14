message = """Letter of Recommendation -

       While working with Mr. Xxxxxx, I have always found him
       working studiously and sincerely at his table without idling or
       gossiping with colleagues in the office.  He seldom
       wastes his time on useless things.  Given a job, he always
       finishes the given assignment in time.  He is always
       deeply engrossed in his official work, and can never be
       found chitchatting in the canteen.  He has absolutely no
       vanity in spite of his high accomplishment and profound
       knowledge of his field.  I think he can easily be
       classed as outstanding, and should on no account be
       dispensed with.  I strongly feel that Mr. Xxxxxx should be
       pushed to accept promotion, and a proposal to administration be
       sent away as soon as possible.

   Jim YYYYY
       Branch Manager """

lines = message.split('\n')
for i in range(0, len(lines), 2):
    print(lines[i])