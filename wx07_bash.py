import wx
import paramiko

# fix for problems with paramiko from
# https://github.com/pyinstaller/pyinstaller/issues/2013
from cryptography.hazmat import backends
try:
    from cryptography.hazmat.backends.commoncrypto.backend import backend as be_cc
except ImportError:
    be_cc = None
try:
    from cryptography.hazmat.backends.openssl.backend import backend as be_ossl
except ImportError:
    be_ossl = None
backends._available_backends_list = [
    be for be in (be_cc, be_ossl) if be is not None
    ]
# end fix
paramiko.util.log_to_file("transport_log.txt")
class SSHFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "SSHCMD")
        panel = wx.Panel(self)
        topLbl = wx.StaticText(panel, -1, "Connection Information")
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit")
        self.Bind(wx.EVT_MENU, self.close, id=wx.ID_EXIT)
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)
        hostLbl = wx.StaticText(panel, -1, "Host:")
        host = wx.TextCtrl(panel, -1, "");
        portLbl = wx.StaticText(panel, -1, "Port:")
        port = wx.TextCtrl(panel, -1, "22");
        usernameLbl = wx.StaticText(panel, -1, "Username:")
        username = wx.TextCtrl(panel, -1, "");
        passwordLbl = wx.StaticText(panel, -1, "Password:")
        password = wx.TextCtrl(panel, -1, "", style=wx.TE_PASSWORD);
        commandLbl = wx.StaticText(panel, -1, "Command:")
        command = wx.TextCtrl(panel, -1, "");
        output = wx.TextCtrl(panel, -1, style=wx.TE_MULTILINE|wx.EXPAND|wx.BORDER_SUNKEN|wx.TE_DONTWRAP,size=(500, 400))
        # works on linux
        # outputfont = wx.Font(10, wx.MODERN, wx.TELETYPE, wx.NORMAL, False,"")
        # works on windows
        outputfont = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        output.SetFont(outputfont)
        self.command = command
        self.password = password
        self.username = username
        self.host = host
        self.port = port
        self.output = output
        goBtn = wx.Button(panel, -1, "Go")
        clearBtn = wx.Button(panel, -1, "Clear")
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topLbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        addrSizer.Add(hostLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(host, 0, wx.EXPAND)
        addrSizer.Add(portLbl, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(port, 0, wx.EXPAND)
        addrSizer.Add(usernameLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(username, 0, wx.EXPAND)
        addrSizer.Add(passwordLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(password, 0, wx.EXPAND)
        addrSizer.Add(commandLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(command, 0, wx.EXPAND)
        mainSizer.Add(addrSizer, 0, wx.EXPAND|wx.ALL, 10)
        addrSizer.Add((10, 10))  # some empty space
        addrSizer.Add(output, 0, wx.EXPAND)
        addrSizer.Add((10, 10))  # some empty space
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(goBtn)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(clearBtn)
        btnSizer.Add((20,20), 1)
        mainSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)
        goBtn.Bind(wx.EVT_BUTTON, self.inserttext)
        clearBtn.Bind(wx.EVT_BUTTON, self.clear)

    def clear(self, event):
        self.output.SetValue("")

    def inserttext(self, event):
        command = self.command.GetValue()
        host = self.host.GetValue()
        port = int(self.port.GetValue())
        username = self.username.GetValue()
        password = self.password.GetValue()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        try:
            ssh.connect(host, port=port, username=username, password=password)
            stdin, stdout, stderr = ssh.exec_command(command)
            for line in stdout.read().splitlines():
                self.output.AppendText(line + "\n")
            for line in stderr.read().splitlines():
                self.output.AppendText(line + "\n")
            stdin.close()
            stderr.close()
        except paramiko.AuthenticationException as error:
            self.output.AppendText(str(error)+'\n')
        except IOError as error:
            self.output.AppendText(str(error)+'\n')
        except:
            self.output.AppendText("Generic Fail\n")
        ssh.close()

    def close(self, evt):
        self.Close()

app = wx.App()
SSHFrame().Show()
app.MainLoop()
