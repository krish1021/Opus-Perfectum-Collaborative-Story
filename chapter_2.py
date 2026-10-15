# chapter_2.py
# The terminal room was silent till that message came
import os, msvcrt #The overseer types...
os.environ["KIVY_NO_CONSOLELOG"] = "1" # And mutes fluff output.

def respond_to_sequence():
    print()
    print("The system blinked: Sequence initialized, collaborator recruited.\n")
    #They come forward and spoke,
    print("The collaborator comes forward and says, 'I think we will need a Kivy interface for this.'\n")

def build_kivy_interface():
    #The recruit imports the first needed libraries,
    from kivy.app import App
    from kivy.uix.label import Label

    class StoryInApp(App):
        title = "Story In App"

        def build(self):
            #The story now materializes in a GUI window
            story_text = (
                "The collaborator succesfully imported the initial needed libraries\n"
                "The overseer watches as they ponder upon recruiting more collaborators.\n\n"
                "Then the terminal spoke:\n"
                "'Sequence progressing. Progress to phase 3...'"
            )
            return Label(text=story_text, font_size=20)
    
    print("The terminal pinged: 'Initializing GUI...'\n")
    print("Press any key to continue...", end="", flush=True)
    msvcrt.getch()
    print()

    StoryInApp().run()

#Execute Phase 2
respond_to_sequence()
build_kivy_interface()