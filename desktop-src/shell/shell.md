---
description: Represents the objects in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects.
title: Shell object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 75fc151e-5b9e-476b-b4e5-b848917357a8

---

# Shell object

Represents the objects in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects.

## Members

The **Shell** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Shell** object has these methods.




| Method | Description | 
|--------|-------------|
| <a href="/windows/desktop/shell/shell-addtorecent"><strong>AddToRecent</strong></a> | Adds a file to the most recently used (MRU) list.<br /> | 
| <a href="shell-browseforfolder.md"><strong>BrowseForFolder</strong></a> | Creates a dialog box that enables the user to select a folder and then returns the selected folder's <a href="folder.md"><strong>Folder</strong></a> object.<br /> | 
| <a href="/windows/desktop/shell/shell-canstartstopservice"><strong>CanStartStopService</strong></a> | Determines if the current user can start and stop the named service.<br /> | 
| <a href="shell-cascadewindows.md"><strong>CascadeWindows</strong></a> | Cascades all of the windows on the desktop. This method has the same effect as right-clicking the taskbar and selecting <strong>Cascade Windows</strong>.<br /> | 
| <a href="shell-controlpanelitem.md"><strong>ControlPanelItem</strong></a> | Runs the specified Control Panel (*.cpl) application. If the application is already open, it will activate the running instance. <br /><blockquote><p>[!Note]<br />As of Windows Vista, most Control Panel applications are Shell items and cannot be opened with this function. To open those Control Panel applications, pass the canonical name to control.exe. For example:</p><pre class="syntax" data-space="preserve"><code>control.exe /name Microsoft.Personalization</code></pre></blockquote><br /> | 
| <a href="shell-ejectpc.md"><strong>EjectPC</strong></a> | Ejects the computer from its docking station. This is the same as clicking the <strong>Start</strong> menu and selecting <strong>Eject PC</strong>, if your computer supports this command.<br /> | 
| <a href="shell-explore.md"><strong>Explore</strong></a> | Opens a specified folder in a Windows Explorer window.<br /> | 
| <a href="shell-explorerpolicy.md"><strong>ExplorerPolicy</strong></a> | Gets the value for a specified Internet Explorer policy.<br /> | 
| <a href="shell-filerun.md"><strong>FileRun</strong></a> | Displays the <strong>Run</strong> dialog to the user. This method has the same effect as clicking the <strong>Start</strong> menu and selecting <strong>Run</strong>.<br /> | 
| <a href="shell-findcomputer.md"><strong>FindComputer</strong></a> | Displays the <strong>Search Results: Computers</strong> dialog box. The dialog box shows the result of the search for a specified computer.<br /> | 
| <a href="shell-findfiles.md"><strong>FindFiles</strong></a> | Displays the <strong>Find: All Files</strong> dialog box. This is the same as clicking the <strong>Start</strong> menu and then selecting <strong>Search</strong> (or its equivalent under systems earlier than Windows XP.<br /> | 
| <a href="/windows/desktop/shell/shell-findprinter"><strong>FindPrinter</strong></a> | Displays the <strong>Find Printer</strong> dialog box.<br /> | 
| <a href="/windows/desktop/shell/shell-getsetting"><strong>GetSetting</strong></a> | Retrieves a global Shell setting.<br /> | 
| <a href="/windows/desktop/shell/shell-getsysteminformation"><strong>GetSystemInformation</strong></a> | Retrieves system information.<br /> | 
| <a href="shell-help.md"><strong>Help</strong></a> | Displays the Windows Help and Support Center. This method has the same effect as clicking the <strong>Start</strong> menu and selecting <strong>Help and Support</strong>.<br /> | 
| <a href="/windows/desktop/shell/shell-isrestricted"><strong>IsRestricted</strong></a> | Retrieves a group's restriction setting from the registry.<br /> | 
| <a href="/windows/desktop/shell/shell-isservicerunning"><strong>IsServiceRunning</strong></a> | Returns a value that indicates whether a particular service is running.<br /> | 
| <a href="shell-minimizeall.md"><strong>MinimizeAll</strong></a> | Minimizes all of the windows on the desktop. This method has the same effect as right-clicking the taskbar and selecting <strong>Minimize All Windows</strong> on older systems or clicking the <strong>Show Desktop</strong> icon in the Quick Launch area of the taskbar in Windows 2000 or Windows XP.<br /> | 
| <a href="shell-namespace.md"><strong>NameSpace</strong></a> | Creates and returns a <a href="folder.md"><strong>Folder</strong></a> object for the specified folder.<br /> | 
| <a href="shell-open.md"><strong>Open</strong></a> | Opens the specified folder.<br /> | 
| <a href="shell-refreshmenu.md"><strong>RefreshMenu</strong></a> | Refreshes the contents of the <strong>Start</strong> menu. Used only with systems preceding Windows XP.<br /> | 
| <a href="shell-searchcommand.md"><strong>SearchCommand</strong></a> | Displays the Apps Search pane.<br /> | 
| <a href="/windows/desktop/shell/shell-servicestart"><strong>ServiceStart</strong></a> | Starts a named service.<br /> | 
| <a href="/windows/desktop/shell/shell-servicestop"><strong>ServiceStop</strong></a> | Stops a named service.<br /> | 
| <a href="shell-settime.md"><strong>SetTime</strong></a> | Displays the <strong>Date and Time Properties</strong> dialog box. This method has the same effect as right-clicking the clock in the taskbar status area and selecting <strong>Adjust Date/Time</strong>.<br /> | 
| <a href="/windows/desktop/shell/shell-shellexecute"><strong>ShellExecute</strong></a> | Performs a specified operation on a specified file.<br /> | 
| <a href="/windows/desktop/shell/shell-showbrowserbar"><strong>ShowBrowserBar</strong></a> | Displays a browser bar.<br /> | 
| <a href="shell-shutdownwindows.md"><strong>ShutdownWindows</strong></a> | Displays the <strong>Shut Down Windows</strong> dialog box. This is the same as clicking the <strong>Start</strong> menu and selecting <strong>Shut Down</strong>.<br /> | 
| <a href="shell-suspend.md"><strong>Suspend</strong></a> | td | 
| <a href="shell-tilehorizontally.md"><strong>TileHorizontally</strong></a> | Tiles all of the windows on the desktop horizontally. This method has the same effect as right-clicking the taskbar and selecting <strong>Tile Windows Horizontally</strong>.<br /> | 
| <a href="shell-tilevertically.md"><strong>TileVertically</strong></a> | Tiles all of the windows on the desktop vertically. This method has the same effect as right-clicking the taskbar and selecting <strong>Tile Windows Vertically</strong>.<br /> | 
| <a href="shell-toggledesktop.md"><strong>ToggleDesktop</strong></a> | Displays or hides the desktop.<br /> | 
| <a href="shell-trayproperties.md"><strong>TrayProperties</strong></a> | Displays the <strong>Taskbar and Start Menu Properties</strong> dialog box. This method has the same effect as right-clicking the taskbar and selecting <strong>Properties</strong>.<br /> | 
| <a href="shell-undominimizeall.md"><strong>UndoMinimizeALL</strong></a> | Restores all desktop windows to the same state they were in before the last <a href="shell-minimizeall.md"><strong>MinimizeAll</strong></a> command. This method has the same effect as right-clicking the taskbar and selecting <strong>Undo Minimize All Windows</strong> on older systems or a second clicking of the <strong>Show Desktop</strong> icon in the Quick Launch area of the taskbar in Windows 2000 or Windows XP.<br /> | 
| <a href="shell-windows.md"><strong>Windows</strong></a> | Creates and returns a <a href="shellwindows.md"><strong>ShellWindows</strong></a> object. This object represents a collection of all of the open windows that belong to the Shell.<br /> | 
| <a href="shell-windowssecurity.md"><strong>WindowsSecurity</strong></a> | Displays the <strong>Windows Security</strong> dialog box.<br /> | 
| <a href="shell-windowswitcher.md"><strong>WindowSwitcher</strong></a> | Displays your open windows in a 3D stack that you can flip through.<br /> | 




 

### Properties

The **Shell** object has these properties.



| Property                                            | Access type          | Description                                                                 |
|:----------------------------------------------------|:---------------------|:----------------------------------------------------------------------------|
| [**Application**](shell-application.md)<br/> | Read-only<br/> | Contains the object's Application object.<br/>                        |
| [**Parent**](shell-parent.md)<br/>           | Read-only<br/> | Gets an object that represents the parent of the current object.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 
