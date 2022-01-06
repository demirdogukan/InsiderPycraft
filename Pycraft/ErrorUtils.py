if not __name__ == "__main__":
    print("Started <Pycraft_ErrorUtils>")
    class GenerateErrorScreen:
        def __init__(self):
            pass
        
        def ErrorScreen(self):
            import tkinter as tk
            import sys
            from tkinter import messagebox
            self.Stop_Thread_Event.set()
            try:
                self.Thread_StartLongThread.join()
                self.Thread_AdaptiveMode.join()
                self.Thread_GetCPUMetrics.join()
                self.Thread_Get_Outdated.join()
            except Exception as Error:
                print("ErrorUtils > GenerateErrorScreen > ErrorScreen: "+str(Error))
                pass
            try:
                self.mod_Pygame__.quit()
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror("Pycraft closed because an error occurred", self.ErrorMessage)
                sys.exit()
            except Exception as Message:
                sys.exit(f"Pycraft was unable to load the error-screen because {Message}")