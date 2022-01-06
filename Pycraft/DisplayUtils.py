if not __name__ == "__main__":
    print("Started <Pycraft_DisplayUtils>")
    class DisplayUtils:
        def __init__(self):
            pass
                
                
        def UpdateDisplay(self): # Run tests to make sure windows not too small
            self.Data_aFPS = []
            self.Data_CPUUsE = []
            self.Data_eFPS = []
            self.Data_MemUsE = []
            
            self.Timer = 0
            
            self.Data_aFPS_Min = 60
            self.Data_aFPS_Max = 1

            self.Data_CPUUsE_Min = 60
            self.Data_CPUUsE_Max = 1

            self.Data_eFPS_Min = 60
            self.Data_eFPS_Max = 1

            self.Data_MemUsE_Min = 60
            self.Data_MemUsE_Max = 1
            
            try:
                try:
                    self.FullscreenX, self.FullscreenY = self.mod_Pyautogui__.size()
                    icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
                    self.mod_Pygame__.display.set_icon(icon)
                    if self.Fullscreen == False:
                        self.Fullscreen = True
                        self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)
                    elif self.Fullscreen == True:
                        self.Fullscreen = False
                        self.Display = self.mod_Pygame__.display.set_mode((self.FullscreenX, self.FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE)
                except Exception as Message:
                    print("DisplayUtils > DisplayUtils > UpdateDisplay: "+ str(Message))
                    self.Fullscreen = True
                    self.SavedWidth = 1280
                    self.SavedHeight = 720
                    self.mod_Pygame__.display.quit()
                    self.mod_Pygame__.init()
                    self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))
                icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
                self.mod_Pygame__.display.set_icon(icon)
            except Exception as Message:
                self.ErrorMessage = "DisplayUtils > DisplayUtils > UpdateDisplay: "+str(Message)

        def SetDisplay(self):
            self.Data_aFPS = []
            self.Data_CPUUsE = []
            self.Data_eFPS = []
            self.Data_MemUsE = []
            
            self.Timer = 0
            
            self.Data_aFPS_Min = 60
            self.Data_aFPS_Max = 1

            self.Data_CPUUsE_Min = 60
            self.Data_CPUUsE_Max = 1

            self.Data_eFPS_Min = 60
            self.Data_eFPS_Max = 1

            self.Data_MemUsE_Min = 60
            self.Data_MemUsE_Max = 1

            try:
                try:
                    self.FullscreenX, self.FullscreenY = self.mod_Pyautogui__.size()
                    if self.Fullscreen == True:
                        self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)
                    elif self.Fullscreen == False:
                        self.Display = self.mod_Pygame__.display.set_mode((self.FullscreenX, self.FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE)
                except Exception as Message:
                    print("DisplayUtils:", Message)
                    self.SavedWidth = 1280
                    self.SavedHeight = 720
                    self.mod_Pygame__.display.quit()
                    self.mod_Pygame__.init()
                    self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))
                icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
                self.mod_Pygame__.display.set_icon(icon)
            except Exception as Message:
                self.ErrorMessage = "DisplayUtils > DisplayUtils > SetDisplay: "+str(Message)


        def GenerateMinDisplay(self, width, height):
            try:
                self.Display = self.mod_Pygame__.display.set_mode((width, height), self.mod_Pygame__.RESIZABLE)
                icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
                self.mod_Pygame__.display.set_icon(icon)
            except Exception as Message:
                self.ErrorMessage = "DisplayUtils > DisplayUtils > GenerateMinDisplay: "+str(Message)


        def GetDisplayLocation(self):
            hwnd = self.mod_Pygame__.display.get_wm_info()["window"]

            prototype = self.mod_Ctypes__.WINFUNCTYPE(self.mod_Ctypes__.wintypes.BOOL, self.mod_Ctypes__.wintypes.HWND, self.mod_Ctypes__.POINTER(self.mod_Ctypes__.wintypes.RECT))
            paramflags = (1, "hwnd"), (2, "lprect")

            GetWindowRect = prototype(("GetWindowRect", self.mod_Ctypes__.windll.user32), paramflags)

            rect = GetWindowRect(hwnd)

            return rect.left+8, rect.top+31


        def GetPlayStatus(self):
            if self.mod_Pygame__.display.get_active() == True:
                tempFPS = self.FPS
                self.mod_Pygame__.mixer.Channel(2).unpause()
                if self.mod_Pygame__.mixer.Channel(2).get_busy() == 0 and self.LoadMusic == True:
                    if self.music == True and self.CurrentlyPlaying == None:
                        self.CurrentlyPlaying = "InvSound"
                        self.LoadMusic = False
                        MusicThread = self.mod_Threading__.Thread(target=self.mod_SoundUtils__.PlaySound.PlayInvSound, args=(self,))
                        MusicThread.start()
            else:
                self.LoadMusic = True
                tempFPS = 15
                self.mod_Pygame__.mixer.Channel(2).pause()
            return tempFPS
        
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()