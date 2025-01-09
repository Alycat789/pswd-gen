# pswd-gen
A simple password generator and its evolutions.

password_gen_05:

    A Password Generator
    An application, run through a GUI, that provides options to create any kind of password that you would like. 
    Choose strong, medium, weak, or custom:
        weak = 8 lowercase letters
        medium = 9-14 numbers and letters
        strong = 15-20 symbols, numbers, and letters
        custom = choose which of the 3 char types you want, length, and case preference (if letters is chosen).

    PassGenerator class
        __repr_ - returns the result of running generate() with the current parameters
        get_char() - handles what gets included in the password for strong med, weak options
        custom() - handles what gets put in the pswd for custom strength option, if needed implements case()
        case() - handles the case preferences of the user, Starts off as combo, action only needed if upper or lower is selected.
        generate() - the list created by get_char() is made into a string

    Interface class ( imports PassGenerator )
        build() - creates and runs the GUI
        custom() - builds a Toplevel widget box for the custom options
            on_letters() - enables/disables l_case options depending on state of letters checkbox
        on_click_create() - creates pswd object, creates area at bottom of window that displays object OR executes on_custom()
        on_custom_create() - creates pswd object, creates area at bottom of window that displays object
        main() - run app