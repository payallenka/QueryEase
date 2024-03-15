def jiya():
    print()
    print("Hi There! I am Jiya")
    print("Here is the list of things i can do for you")
    print()
    print("pyql -------------- to use mysql in a different interface")
    print("cryptograhy-------- to create password and decode password of a specific kind")
    print("scale correction -- to convert farenheit scale to celcius and ")
    print()
    print("once you are done enter \"done\" for the asked question - \"how may i help you?\"")
    print()
    _number=17
    while _number==17:
        print()
        vir=input("How may I help you? ")
        print()
        if vir=="pyql":
            from main_ import pyql
            pyql()
        elif vir=="cryptography":
            t=input("you want to create or crack a code?")
            print()
            if t=="create":
                print("AVOID USE OF PUNCTUATION MARKS")
                print()
                from cryptography_ import encode
                encode()
            elif t=="crack":
                from cryptography_ import decode
                decode()
        elif vir=="scale correction":
            
            import scale_correction
        elif len(vir)==0:
            print("maybe i can help you later")
        elif vir=="done":
            _number+=18
        else:
            print("sorry it is not in my program")
    print("bye")


jiya()
