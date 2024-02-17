# -*- coding: utf-8 -*-

import os
import configparser
import shutil
import psutil

# function to call the file path that compiled inside exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Patch Configuration
skin_font = " Arial (Default)"
app_version = '2.0.1.478'
fileloc = ''

def browseFiles():
        global fileloc
        global folderin
        global total_row
        global basefile
        dpath = os.getcwd()
        fileloc = filedialog.askdirectory(initialdir = dpath, title = "Select a Folder")
        basefile = os.path.basename(fileloc)
        t.set(fileloc)
        if basefile  == 'res':
            # print('directory valid')
            folderin = 1
            pcs.set('Ready')

def patcher():
    app_version
    patch_int = int(app_version.replace(".",""))
    # the folder path compiled inside exe
    vloc = resource_path('vsecure')
    
    if os.path.basename(fileloc) != 'res':
        pcs.set('Invalid Directory')
        return 'Path_Incorrect'
    
    ploc = os.path.dirname(fileloc)
    pversion = os.path.join(ploc, r'updater\updater_cfg\version.ini')
    purl_conf = os.path.join(ploc, r'updater\updater_cfg')
    
    # check if app file exist
    isfxapp = os.path.exists(os.path.join(ploc, r'bin64\fxapp.exe'))
    isurlconf = os.path.exists(os.path.join(ploc, r'updater\updater_cfg\url_config.ini'))
    isfxlaunch = os.path.exists(os.path.join(ploc, r'fxlaunch.exe'))

    if not (isfxapp and isurlconf and isfxlaunch):
        pcs.set('Invalid Directory')
        # print('Path incorrect. Please browse and locate correct app res folder!')
        return 'Path_Incorrect'
    
    
    # PSUTIL check if app or launcher running (all other clients)
    islauncher = "fxupdate.exe" in (i.name() for i in psutil.process_iter()) #process_exists('fxupdate.exe')
    isapp = "fxapp.exe" in (i.name() for i in psutil.process_iter()) #process_exists('fxapp.exe')
    
    if islauncher or isapp:
        # print('Please close all app client and try again!')
        return 'App_Not_Closed'

    # check if version compatible
    read_config = configparser.ConfigParser()
    read_config.read(pversion)
    vers = read_config.get("main", "version")

    if vers == app_version:
        pass
    elif int(vers.replace(".","")) < patch_int:
        # print('Please update app client and try again!')
        return 'Update_Client'
    elif int(vers.replace(".","")) > patch_int:
        # print('English patch outdated! Applying text only')
        return 'Patch_Outdated'
    else:
        # print('Version file error')
        return 'Version_File_Bug'
    
    # copy 64-bit url config file to app directory
    if chg64bit.get() == 1:
        # pcs.set('Upgrading Cliet to 64-Bit')
        # print('Applying 64-bit config')
        try:
            os.rename(os.path.join(purl_conf, 'url_config.ini'), os.path.join(purl_conf, 'url_config.bak'))
        except:
            pass
        shutil.copyfile(os.path.join(vloc, r'vupdater\updater_cfg\url_config.ini'),os.path.join(purl_conf, 'url_config.ini'))
        
               
    # copy patch into folder
    def applier(source, dest, package_name):
        # creating backup folder and move old file into it
        bak_path = os.path.join(ploc, 'backup_'+app_version)
        if not os.path.exists(bak_path):
            os.makedirs(bak_path)
        try:
            os.rename(os.path.join(ploc, dest, package_name+'.package'), os.path.join(ploc, 'backup_'+app_version, package_name+'.package'))
        except:
            pass
        shutil.copy(os.path.join(vloc, source, package_name+'.package'), os.path.join(ploc, dest))

    # print('Applying Patch Files')
    # pcs.set('Copying gui..')
    applier('vres', 'res', 'gui')
    # pcs.set('Copying gui_language..')
    applier('vres', 'res', 'gui_language')
    # pcs.set('Copying gui_special..')
    applier('vres', 'res', 'gui_special')
    # pcs.set('Copying ini..')
    applier('vres', 'res', 'ini')
    # pcs.set('Copying lua..')
    #applier('vres', 'res', 'lua')
    # pcs.set('Copying lua..')
    applier('vres', 'res', 'lua64')
    # pcs.set('Copying text..')
    applier('vres', 'res', 'text')
    # pcs.set('Copying updater_res..')
    applier('vupdater', 'updater', 'updater_res')
    
    # to redirect skin source according to skin_font selected
    if skin_font == " Arial (Default)":
        # pcs.set('Copying skin..')
        applier('vres', 'res', 'skin')
        # print('Applying Default Skin')
    elif skin_font == " GBK (Chinese)":
        # pcs.set('Copying skin (GBK)..')
        applier('vres/GBK', 'res', 'skin')
        # print('Applying GBK Skin')
    else:
        # print('Skin font selection error')
        return 'Skin selection error'
    return 'patching'

#--------------------------------------------------------------------------------------    
import time
import threading
# try:
    # import Tkinter as tkinter
    # import ttk
# except ImportError:
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog


class GUI(object):

    def __init__(self):
        global app_version
        global t
        global pcs
        global chg64bit
        mycolor = '#e6ffff'
        self.root = tkinter.Tk()
        self.root.resizable(False, False)
        self.root.configure(bg=mycolor)
        self.root.title('App English Patch')
        self.root.geometry('350x450+700+200')
        topic = "App English Patch \n Version " + app_version
        self.text1 = tkinter.Label(self.root, text= topic, font=('Arial', 12, 'bold'), bg=mycolor)
        self.text1.pack(padx=0, pady=10)
        
        
        # Browse directory ui
        self.locate = Label(self.root, text='Select Res Folder', font=('Arial', 9), bg=mycolor).place(x=20, y=51) 
        self.btn_browse = tkinter.Button(self.root, text='Browse', font='arial 9 bold', bg='#002db3', fg='white', command = browseFiles).place(x=273, y=70)
        t = StringVar()
        self.dir_entry = Entry(self.root, textvariable=t, width=40, bg='white', state="disabled").place(x=30, y=71, height=25)

        chg64bit = IntVar(value=1) 
        self.Button1 = Checkbutton(self.root, text = "Upgrade to\n64-Bit Client", 
                      variable = chg64bit,
                      onvalue = 1,
                      offvalue = 1,
                      bg = mycolor,
                      height = 1,
                      width = 8).place(x=215, y=125)
         
                
        #select skin type combo button
        self.text2 = tkinter.Label(self.root, text = "Select Skin Font Style:",font = ("Arial", 9), bg=mycolor).place(x=35, y=112)
        self.combox = ttk.Combobox(self.root, width = 15, values = [' Arial (Default)',' GBK (Chinese)'], state="readonly")
        self.combox.current(0)
        # self.combox.pack(padx=0, pady=17)
        self.combox.place(x=48, y=132)
        # print(self.combox.get())
        
        
        # process status text
        pcs =StringVar(value="Idle..") 
        self.process_label = Label(self.root, textvariable=pcs, font=('Arial', 9), fg='#330000', bg=mycolor).pack(pady=100)

        
        # proggress bar
        self.progbar = ttk.Progressbar(self.root, length = 200)
        self.progbar.config(maximum=10, mode='determinate')
        # self.progbar.pack(padx=0, pady=20)
        self.progbar.place(x=75, y=185)
        self.i = 0
        
        # start patch button
        self.b_start = tkinter.Button(self.root, text='Start Patch', font='arial 9 bold', bg='#006600', fg='white')
        self.b_start['command'] = self.run_patcher
        self.b_start.place(x=137, y=220)
        # self.b_start.pack(padx=0, pady=10)
        
        # instructions
        self.text3 = tkinter.Label(self.root, text = "Instructions:",font = ("Arial", 9, 'bold'), bg=mycolor).place(x=0, y=245)
        note1 = '1. Ensure app client is updated and working correctly.'
        note2 = '2. Close all app clients.'
        note3 = '3. Click "Browse" select app "res" folder correctly.'
        note4 = '4. Skin style: you can leave it as default or select \'GBK\' if you want bold app text as in Chinese client.'
        note5 = '5. Check the 64-Bit option for better performance.'
        note6 = '6. Click \'Start Patch\' and wait for patching complete.'
        noteT = note1 +'\n' + note2 +'\n' + note3 + '\n' + note4 + '\n' + note5 + '\n' + note6
        self.text4 = tkinter.Label(self.root, text = noteT, justify='left', wraplengt=350, font = ("Arial", 9), bg=mycolor).place(x=5, y=260)
        
        # extra info
        info1 = '*For update, visit @ yiuzen.com.'
        info2 = '*New updates may delay depend on contents.'
        info3 = '*Fallback text file will be provided for immediate use.'
        infoT = info1 +'\n' + info2 +'\n' + info3
        self.text5 = tkinter.Label(self.root, text = infoT, justify='left', wraplengt=350, font = ("Arial", 8), bg=mycolor).place(x=5, y=372)
        self.text6 = tkinter.Label(self.root, text = "Bug Report/Contact:\ngiru_han \n",justify='right', font = ("Arial", 8), bg=mycolor).place(x=230, y=415)
    
    # master function
    def run_patcher(self):
        # accessing/declare global variable (variable will be created if not yet exists)
        global skin_font
        self.b_start["state"] = DISABLED
        pcs.set('Patching..Please wait, DON\'T interrupt the program!')
        self.root.update_idletasks()
        skin_font = self.combox.get()
        # print(skin_font)
        
        # run patcher function
        situation = patcher()
        if situation == 'Path_Incorrect':
            messagebox.showwarning('Path Error', 'Unable to locate app directory.\nPlease Browse and select correct app \'res\' folder!')
            self.b_start["state"] = NORMAL
            # self.root.destroy()
            # MsgBox = tkinter.messagebox.askyesno('Yes|No', 'Do you want to proceed?')
        elif situation == 'App_Not_Closed':
            messagebox.showwarning('Client Error', 'Please close all app client and try again!')
            self.root.destroy()
        elif situation == 'Update_Client':
            messagebox.showwarning('Client Outdated', 'Please update app client and try again!')
            self.root.destroy()
        elif situation == 'Patch_Outdated':
            messagebox.showwarning('Patch Error', 'English patch outdated! Applying text only!')
            self.root.destroy()
        elif situation == 'Version_File_Bug':
            messagebox.showwarning('Version Error', 'Something went wrong!!')
            self.root.destroy()
        elif situation == 'patching':
            self.start_thread()
        else:
            messagebox.showerror('Unknown Error', 'Something went wrong!')
            self.root.destroy()
            

    def start_thread(self):
        self.b_start['state'] = 'disable'
        self.work_thread = threading.Thread(target=work)
        self.work_thread.start()
        self.root.after(50, self.check_thread)
        self.root.after(50, self.update)
        
    def check_thread(self):
        if self.work_thread.is_alive():
            self.root.after(50, self.check_thread)
        else:
            pcs.set('Complete')
            messagebox.showinfo('App English Patch', 'Patching Successfull!')
            self.root.destroy()        

    def update(self):
        #Updates the progressbar
        self.progbar["value"] = self.i
        if self.work_thread.is_alive():
            self.root.after(50, self.update)#method is called all 50ms

gui = GUI()
def work():
    #Do the work :D
    for i in range(11):
        gui.i = i
        time.sleep(0.1)
gui.root.mainloop()

