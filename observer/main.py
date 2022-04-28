from Profile import Profile


def main():
    lscantelbury = Profile("lscantelbury")
    diogeles = Profile("diogeles")
    diogeles.follow(lscantelbury)
    lscantelbury.add_tweet()
main()