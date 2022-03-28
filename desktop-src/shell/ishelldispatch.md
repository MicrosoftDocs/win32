---
description: Represents an object in the Shell.
title: IShellDispatch object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 9B429C03-7F80-45db-B8CD-58D19FAD2E61

---

# IShellDispatch object

Represents an object in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects.

> [!Note]  
> **IShellDispatch** is implemented and accessed through the [**Shell**](shell.md) object.

 

## Members

The **IShellDispatch** object has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **IShellDispatch** object has these methods.




| Method | Description | 
|--------|-------------|
| <a href="ishelldispatch-browseforfolder.md"><strong>BrowseForFolder</strong></a> | Creates a dialog box that enables the user to select a folder and then returns the selected folder's <a href="folder.md"><strong>Folder</strong></a> object.<br /> | 
| <a href="ishelldispatch-cascadewindows.md"><strong>CascadeWindows</strong></a> | Cascades all of the windows on the desktop. This method has the same effect as right-clicking the taskbar and selecting <strong>Cascade windows</strong>.<br /> | 
| <a href="ishelldispatch-controlpanelitem.md"><strong>ControlPanelItem</strong></a> | Runs the specified Control Panel application. If the application is already open, it will activate the running instance. <br /><blockquote><p>[!Note]<br />As of Windows Vista, most Control Panel applications are Shell items and cannot be opened with this function. To open those Control Panel applications, pass the canonical name to control.exe. For example:</p><pre class="syntax" data-space="preserve"><code>control.exe /name Microsoft.Personalization</code></pre></blockquote><br /> | 
| <a href="ishelldispatch-ejectpc.md"><strong>EjectPC</strong></a> | Ejects the computer from its docking station. This is the same as clicking the <strong>Start</strong> menu and selecting <strong>Eject PC</strong>, if your computer supports this command.<br /> | 
| <a href="ishelldispatch-explore.md"><strong>Explore</strong></a> | Opens a specified folder in a Windows Explorer window.<br /> | 
| <a href="ishelldispatch-filerun.md"><strong>FileRun</strong></a> | Displays the <strong>Run</strong> dialog to the user.<br /> | 
| <a href="ishelldispatch-findcomputer.md"><strong>FindComputer</strong></a> | Displays the <strong>Search Results: Computers</strong> dialog box. The dialog box shows the result of the search for a specified computer.<br /> | 
| <a href="ishelldispatch-findfiles.md"><strong>FindFiles</strong></a> | Displays the <strong>Find: All Files</strong> dialog box. This is the same as clicking the <strong>Start</strong> menu and then selecting <strong>Search</strong>.<br /> | 
| <a href="ishelldispatch-help.md"><strong>Help</strong></a> | Displays the Windows Help and Support window. This method has the same effect as clicking the <strong>Start</strong> menu and selecting <strong>Help and Support</strong>.<br /> | 
| <a href="ishelldispatch-minimizeall.md"><strong>MinimizeAll</strong></a> | Minimizes all of the windows on the desktop. This method has the same effect as right-clicking the taskbar and selecting <strong>Minimize All Windows</strong> on older systems or clicking the <strong>Show Desktop</strong> icon on the taskbar.<br /> | 
| <a href="ishelldispatch-namespace.md"><strong>NameSpace</strong></a> | Creates and returns a <a href="folder.md"><strong>Folder</strong></a> object for the specified folder.<br /> | 
| <a href="ishelldispatch-open.md"><strong>Open</strong></a> | Opens the specified folder.<br /> | 
| <a href="ishelldispatch-refreshmenu.md"><strong>RefreshMenu</strong></a> | Refreshes the contents of the <strong>Start</strong> menu. Used only with systems preceding Windows XP.<br /> | 
| <a href="ishelldispatch-settime.md"><strong>SetTime</strong></a> | Displays the <strong>Date and Time</strong> dialog box. This method has the same effect as right-clicking the clock in the taskbar status area and selecting <strong>Adjust date/time</strong>.<br /> | 
| <a href="ishelldispatch-shutdownwindows.md"><strong>ShutdownWindows</strong></a> | Displays the <strong>Shut Down Windows</strong> dialog box. This is the same as clicking the <strong>Start</strong> menu and selecting <strong>Shut Down</strong>.<br /> | 
| <a href="ishelldispatch-suspend.md"><strong>Suspend</strong></a> | td | 
| <a href="ishelldispatch-tilehorizontally.md"><strong>TileHorizontally</strong></a> | Tiles all of the windows on the desktop horizontally. This method has the same effect as right-clicking the taskbar and selecting <strong>Show windows stacked</strong>.<br /> | 
| <a href="ishelldispatch-tilevertically.md"><strong>TileVertically</strong></a> | Tiles all of the windows on the desktop vertically. This method has the same effect as right-clicking the taskbar and selecting <strong>Show windows side by side</strong>.<br /> | 
| <a href="ishelldispatch-trayproperties.md"><strong>TrayProperties</strong></a> | Displays the <strong>Taskbar and Start Menu Properties</strong> dialog box. This method has the same effect as right-clicking the taskbar and selecting <strong>Properties</strong>.<br /> | 
| <a href="ishelldispatch-undominimizeall.md"><strong>UndoMinimizeALL</strong></a> | Restores all desktop windows to the state they were in before the last <a href="shell-minimizeall.md"><strong>MinimizeAll</strong></a> command. This method has the same effect as right-clicking the taskbar and selecting <strong>Undo Minimize All Windows</strong> (on older systems) or a second clicking of the <strong>Show Desktop</strong> icon in the taskbar.<br /> | 
| <a href="ishelldispatch-windows.md"><strong>Windows</strong></a> | Creates and returns a <a href="shellwindows.md"><strong>ShellWindows</strong></a> object. This object represents a collection of all of the open windows that belong to the Shell.<br /> | 




 

### Properties

The **IShellDispatch** object has these properties.



| Property                                                     | Access type          | Description                                                                      |
|:-------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------|
| [**Application**](ishelldispatch-application.md)<br/> | Read-only<br/> | Contains an object that represents an application.<br/>                    |
| [**Parent**](ishelldispatch-parent.md)<br/>           | Read-only<br/> | Retrieves an object that represents the parent of the current object.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)
</dt> <dt>

[**Shell Object**](shell.md)
</dt> </dl>

 

 
