#panagaram

string = "The quick brown fox jumps over the lazy dog"
string = string.lower()
nedozvoljeno = ';,:.!?'

skup = {x for x in string if x != ' ' and x not in nedozvoljeno}
if len(skup) == 26:
    print("JESTE")
else:
    print("NIJE")
