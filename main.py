# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import serial
import serial.tools.list_ports


###########################################################################
## Class MyFrame1
###########################################################################
m_comboBox1Choices = []
port_list = []
numport = ""


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(701, 546), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        port_list = list(serial.tools.list_ports.comports())

        for i in range(len(m_comboBox1Choices)):
            m_comboBox1Choices.pop()

        for i in range(len(port_list)):
            m_comboBox1Choices.append(port_list[i][0])

        self.m_comboBox1 = wx.ComboBox(self, wx.ID_ANY, u"COM1\nCOM2", wx.Point(-1, -1), wx.DefaultSize,
                                       m_comboBox1Choices, wx.CB_READONLY)
        self.m_comboBox1.SetSelection(1)
        self.m_comboBox1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        bSizer2.Add(self.m_comboBox1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button3, 0, wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_comboBox1.Bind(wx.EVT_COMBOBOX, self.m_comboBox1OnCombobox)
        self.m_comboBox1.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.m_comboBox1OnRightDClick)
        self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)
        self.m_button3.Bind(wx.EVT_BUTTON, self.m_button3OnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_comboBox1OnRightDClick(self, event):
        """
        Combobox点击中断函数
        :param event:
        """
        global port_list
        port_list = list(serial.tools.list_ports.comports())

        for i in range(len(m_comboBox1Choices)):
            m_comboBox1Choices.pop()
            self.m_comboBox1.Delete(0)
        for i in range(len(port_list)):
            m_comboBox1Choices.append(port_list[i][0])
            self.m_comboBox1.Append(port_list[i][0])
            print(port_list[i][0])

#        str1 = self.m_comboBox1.GetStringSelection()
#        self.m_comboBox1.SetItems(m_comboBox1Choices)
        event.Skip()

    def m_comboBox1OnCombobox(self, event):
        """
        Combobox选中选项中断函数
        :param event:
        """
        global numport
        numport = self.m_comboBox1.GetStringSelection()
        event.Skip()

    def m_button2OnButtonClick(self, event):
        """
        确定键按下中断函数
        :param event:
        """
        global numport
        serialName = str(numport)
        port = serial.Serial(serialName, 115200)
#        ser = serial.Serial('COM3', 38400, timeout=0,
#                           parity = serial.PARITY_EVEN, rtscts = 1)
#        serial.Serial(serialName, 9600, timeout=60)
        event.Skip()

    def m_button3OnButtonClick(self, event):
        """
        取消键按下中断函数
        :param event:
        """
        event.Skip()


if __name__ == '__main__':

    app = wx.App()
    frame = MyFrame1(None)
    frame.Show(True)
    app.MainLoop()
