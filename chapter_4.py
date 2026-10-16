# chapter_4.py, final recruit
import os, sys, time, msvcrt # The new backend coder from chapter 3 arrives and executes the headers...
os.environ["KIVY_NO_CONSOLELOG"] = "1" # And then directly following the architecture up by removing fluff outputs

#They speak, "Let me make our outputs progress like a typewriter"
def typewriter_effect(text, delay=0.03):
    """Prints text one letter at a time"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def finish_for_now():
    print()
    terminal_story_text = [
        "The system blinked: Sequence initialized, new collaborator recruited.\n"
        "The new collaborator comes forward and says, 'I think we will need a Kivy interface for this.'\n\n"
        "The terminal pinged: 'Initializing GUI...'"
    ]

    for line in terminal_story_text:
        typewriter_effect(line)
        print("\n[Press any key to continue...]", end="", flush=True)
        msvcrt.getch()
        print()

def build_gui():
    # The new recruit says, "Let me import the first needed libraries.""
    from kivy.app import App
    from kivy.uix.label import Label

    # And then they establish the GUI...
    class StoryInApp(App):
        title = "Story In App"

        def build(self):
            #The story now materializes in a GUI window
            story_text = (
                "The new collaborator succesfully imported the initial needed libraries\n"
                "The team watches as they ponder upon the future of the application.\n\n"
                "Then the terminal outputs:\n"
                "[color=#00FF00]Sequence progressing. Progress to phase 5.[/color]\n\n"
                "To be continued..."
            )
            return Label(text=story_text, font_size=20, markup=True)

    StoryInApp().run()

#Execute Phase 4
finish_for_now()
build_gui()