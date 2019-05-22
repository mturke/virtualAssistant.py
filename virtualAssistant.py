import wx
import wikipedia
import wolframalpha
#from espeak import espeak

#espeak.synth("Greetings, Mike")

app_id = "GHJ43Q-998X58LJX7"
client = wolframalpha.Client(app_id)

# GUI
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(500, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Mike's Assistant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello, Mike. I am your assistant, P-VA, powered by Python. How can I help you?")

        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        user_input = self.txt.GetValue()
        user_input = user_input.lower()
        try:
            # wolfram
            #app_id = "******-**********"
            #client = wolframalpha.Client(app_id)
            res = client.query(user_input)
            answer = next(res.results).text
            #ssl._create_default_https_context = ssl._create_unverified_context
            print("Answer: ", answer)
            print()
            #espeak.synth("The answer is, ", answer)
       	except:
            try:
                # wiki
                user_input = user_input.split(' ')
                user_input = ' '.join(user_input[2:])
                print("Answer: ", wikipedia.summary(user_input))
                print()
       	    except:
                print("Unfortunately I don't know that")
       			
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()

'''
import wx

import wikipedia
import wolframalpha


#input = input("Question?: ")
# wikipedia.set_lang("en") set language to fr for french, es for spanish


app_id = "GHJ43Q-998X58LJX7"
client = wolframalpha.Client(app_id)
# GUI
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size =
            wx.Size(450, 100), style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU |
            wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title = "virtualAssistant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label = "Hello, I am your virtual assistant powered by Python")

        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, stle=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            #wolfram
            res = client.query(input)
            answer = next(res.results).text
            #ssl._create_default_https_context = ssl._create_unverified_context
            print(answer)
        except:
                try:
                        input = input.split(' ')
                        input = ' '.join(input[2:])
                        print(wikipedia.summary(input, sentences = 3))
                except:
                        print("I don't have the answer")
                                    

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()

'''





