#!/usr/bin/python
import json, sys, hashlib


def usage():
    print ("""Usage:
        python get_pri_key.py student_id (i.e., ***********3)""")
    sys.exit ( 1 )


# TODO -- get n's factors
# reminder: you can cheat ;-), as long as you can get p and q
def get_factors(n):
    p = 0
    q = 0

    # your code starts here


    p = 961756051
    q = 961751321
    # your code ends here
    return (p, q)

# some parts of the real answers will be hidden with *** so the code will not be miss used, since the class might still has same projects
# TODO: write code to get d from p, q and e
def get_key(p, q, e):
    d = 0

    # your code starts here
    # Extended Euclidean algorthim
def egcd(a, b):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            ******* = *****
            gcd = b
        return gcd, x, y

def get_key(p, q, e):
        # compute n
        n = p * q

        # We try to Compute phi(n)
        phi = (*****) * (*****)

        # Compute modular inverse of e
        *****
        *****
        if (d < 0):
            d += phi

        # your code ends here
        return d


def main():
    if len ( sys.argv ) != 2:
        usage ()

    n = 0
    e = 0

    all_keys = None
    with open ( "keys4student.json", 'r' ) as f:
        all_keys = json.load ( f )

    name = ******( sys.argv[1].strip () ).hexdigest ()
    if name not in all_keys:
        print (sys.argv[1], "not in keylist")
        usage ()
        # your code starts here
        # some parts of code deleted try to figure it out :)
        # your code ends here
    pub_key = all_keys[name]
    n = int ( pub_key['N'], 16 )
    e = int ( pub_key['e'], 16 )

    print ("your public key: (", hex ( n ).rstrip ( "L" ), ",", hex ( e ).rstrip ( "L" ), ")")

    (p, q) = get_factors ( n )
    d = get_key ( p, q, e )
    print (d)
    print ("your private key:", hex ( d ).rstrip ( "L" ))


if __name__ == "__main__":
    main ()
