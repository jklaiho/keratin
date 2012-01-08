import argparse

def main(override_args=[]):
    """
    Entry point for the ``keratin`` CLI script.
    """
    parser = argparse.ArgumentParser(description="Site and content skeleton creation helper for Keratin.")
    parser.add_argument('command', help="the command to run")
    # Look at manually provided args instead of sys.argv (for testing, mostly)
    args = parser.parse_args(override_args or None)
    print args
