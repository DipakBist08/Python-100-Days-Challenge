class ChallengeAccepted:
    def __init__(self, do, donot):
        self.Do = do
        self.DoNot = donot

    def AcceptedChallenge(self):
        print(f"I Accepted the 100 Days Coding Challenge.")
        try:
            if self.Do.lower() in ['yes', 'y', 'true', '1']:
                print("I am gonna do it!")
            elif self.DoNot.lower() in ['yes', 'y', 'true', '1']:
                print("At least I tried it!")
            else:
                print("Let's see what will happen.")
        except Exception as e:
            print(f"I won't give up! Error: {e}")

do_input = input("Are you going to do the challenge? (yes/no): ")
donot_input = input("Are you not going to do the challenge? (yes/no): ")

challenge = ChallengeAccepted(do_input, donot_input)
challenge.AcceptedChallenge()
