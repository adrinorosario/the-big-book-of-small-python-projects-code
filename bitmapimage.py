import sys


def generate_image(display_message: str):
    bitmap = """
     ....................................................................
        **************   *  *** **  *      ******************************
       ********************* ** ** *  * ****************************** *
      **      *****************       ******************************
               *************          **  * **** ** ************** *
                *********            *******   **************** * *
                 ********           ***************************  *
        *        * **** ***         *************** ******  ** *
                    ****  *         ***************   *** ***  *
                      ******         *************    **   **  *
                      ********        *************    *  ** ***
                        ********         ********          * *** ****
                        *********         ******  *        **** ** * **
                        *********         ****** * *           *** *   *
                          ******          ***** **             *****   *
                          *****            **** *            ********
                         *****             ****              *********
                         ****              **                 *******   *
                         ***                                       *    *
                         **     *                    *
     ....................................................................
     """
    for line in bitmap.splitlines():
        for i, bit in enumerate(line):
            if bit == ' ':
                print(' ', end='')
            else:
                print(display_message[i % len(display_message)], end='')
        print()


def generate_bitmap_image():
    message = input("Enter the bitmap message: \n>")
    if message == ' ' or message == '':
        sys.exit()
    else:
        generate_image(message)


generate_bitmap_image()