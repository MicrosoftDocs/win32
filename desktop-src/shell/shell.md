---
Description: Represents the objects in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects.
title: Shell object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
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
---

# Shell object

Represents the objects in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects.

## Members

The **Shell** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Shell** object has these methods.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537735(v=VS.85).aspx"><strong>AddToRecent</strong></a></td>
<td style="text-align: left;">Adds a file to the most recently used (MRU) list.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-browseforfolder"><strong>BrowseForFolder</strong></a></td>
<td style="text-align: left;">Creates a dialog box that enables the user to select a folder and then returns the selected folder's <a href="folder"><strong>Folder</strong></a> object.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537736(v=VS.85).aspx"><strong>CanStartStopService</strong></a></td>
<td style="text-align: left;">Determines if the current user can start and stop the named service.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-cascadewindows"><strong>CascadeWindows</strong></a></td>
<td style="text-align: left;">Cascades all of the windows on the desktop. This method has the same effect as right-clicking the taskbar and selecting <strong>Cascade Windows</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-controlpanelitem"><strong>ControlPanelItem</strong></a></td>
<td style="text-align: left;">Runs the specified Control Panel (*.cpl) application. If the application is already open, it will activate the running instance. <br/>
<blockquote>
<p>[!Note]<br />
As of Windows Vista, most Control Panel applications are Shell items and cannot be opened with this function. To open those Control Panel applications, pass the canonical name to control.exe. For example:</p>
<pre class="syntax" data-space="preserve"><code>control.exe /name Microsoft.Personalization</code></pre>
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-ejectpc"><strong>EjectPC</strong></a></td>
<td style="text-align: left;">Ejects the computer from its docking station. This is the same as clicking the <strong>Start</strong> menu and selecting <strong>Eject PC</strong>, if your computer supports this command.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-explore"><strong>Explore</strong></a></td>
<td style="text-align: left;">Opens a specified folder in a Windows Explorer window.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-explorerpolicy"><strong>ExplorerPolicy</strong></a></td>
<td style="text-align: left;">Gets the value for a specified Internet Explorer policy.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-filerun"><strong>FileRun</strong></a></td>
<td style="text-align: left;">Displays the <strong>Run</strong> dialog to the user. This method has the same effect as clicking the <strong>Start</strong> menu and selecting <strong>Run</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-findcomputer"><strong>FindComputer</strong></a></td>
<td style="text-align: left;">Displays the <strong>Search Results: Computers</strong> dialog box. The dialog box shows the result of the search for a specified computer.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-findfiles"><strong>FindFiles</strong></a></td>
<td style="text-align: left;">Displays the <strong>Find: All Files</strong> dialog box. This is the same as clicking the <strong>Start</strong> menu and then selecting <strong>Search</strong> (or its equivalent under systems earlier than Windows XP.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537738(v=VS.85).aspx"><strong>FindPrinter</strong></a></td>
<td style="text-align: left;">Displays the <strong>Find Printer</strong> dialog box.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537739(v=VS.85).aspx"><strong>GetSetting</strong></a></td>
<td style="text-align: left;">Retrieves a global Shell setting.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537740(v=VS.85).aspx"><strong>GetSystemInformation</strong></a></td>
<td style="text-align: left;">Retrieves system information.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-help"><strong>Help</strong></a></td>
<td style="text-align: left;">Displays the Windows Help and Support Center. This method has the same effect as clicking the <strong>Start</strong> menu and selecting <strong>Help and Support</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537741(v=VS.85).aspx"><strong>IsRestricted</strong></a></td>
<td style="text-align: left;">Retrieves a group's restriction setting from the registry.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537742(v=VS.85).aspx"><strong>IsServiceRunning</strong></a></td>
<td style="text-align: left;">Returns a value that indicates whether a particular service is running.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-minimizeall"><strong>MinimizeAll</strong></a></td>
<td style="text-align: left;">Minimizes all of the windows on the desktop. This method has the same effect as right-clicking the taskbar and selecting <strong>Minimize All Windows</strong> on older systems or clicking the <strong>Show Desktop</strong> icon in the Quick Launch area of the taskbar in Windows 2000 or Windows XP.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-namespace"><strong>NameSpace</strong></a></td>
<td style="text-align: left;">Creates and returns a <a href="folder"><strong>Folder</strong></a> object for the specified folder.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-open"><strong>Open</strong></a></td>
<td style="text-align: left;">Opens the specified folder.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-refreshmenu"><strong>RefreshMenu</strong></a></td>
<td style="text-align: left;">Refreshes the contents of the <strong>Start</strong> menu. Used only with systems preceding Windows XP.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-searchcommand"><strong>SearchCommand</strong></a></td>
<td style="text-align: left;">Displays the Apps Search pane.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537743(v=VS.85).aspx"><strong>ServiceStart</strong></a></td>
<td style="text-align: left;">Starts a named service.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537744(v=VS.85).aspx"><strong>ServiceStop</strong></a></td>
<td style="text-align: left;">Stops a named service.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-settime"><strong>SetTime</strong></a></td>
<td style="text-align: left;">Displays the <strong>Date and Time Properties</strong> dialog box. This method has the same effect as right-clicking the clock in the taskbar status area and selecting <strong>Adjust Date/Time</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537745(v=VS.85).aspx"><strong>ShellExecute</strong></a></td>
<td style="text-align: left;">Performs a specified operation on a specified file.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="https://msdn.microsoft.com/en-us/library/Gg537746(v=VS.85).aspx"><strong>ShowBrowserBar</strong></a></td>
<td style="text-align: left;">Displays a browser bar.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-shutdownwindows"><strong>ShutdownWindows</strong></a></td>
<td style="text-align: left;">Displays the <strong>Shut Down Windows</strong> dialog box. This is the same as clicking the <strong>Start</strong> menu and selecting <strong>Shut Down</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-suspend"><strong>Suspend</strong></a></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-tilehorizontally"><strong>TileHorizontally</strong></a></td>
<td style="text-align: left;">Tiles all of the windows on the desktop horizontally. This method has the same effect as right-clicking the taskbar and selecting <strong>Tile Windows Horizontally</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-tilevertically"><strong>TileVertically</strong></a></td>
<td style="text-align: left;">Tiles all of the windows on the desktop vertically. This method has the same effect as right-clicking the taskbar and selecting <strong>Tile Windows Vertically</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-toggledesktop"><strong>ToggleDesktop</strong></a></td>
<td style="text-align: left;">Displays or hides the desktop.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-trayproperties"><strong>TrayProperties</strong></a></td>
<td style="text-align: left;">Displays the <strong>Taskbar and Start Menu Properties</strong> dialog box. This method has the same effect as right-clicking the taskbar and selecting <strong>Properties</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-undominimizeall"><strong>UndoMinimizeALL</strong></a></td>
<td style="text-align: left;">Restores all desktop windows to the same state they were in before the last <a href="shell-minimizeall"><strong>MinimizeAll</strong></a> command. This method has the same effect as right-clicking the taskbar and selecting <strong>Undo Minimize All Windows</strong> on older systems or a second clicking of the <strong>Show Desktop</strong> icon in the Quick Launch area of the taskbar in Windows 2000 or Windows XP.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-windows"><strong>Windows</strong></a></td>
<td style="text-align: left;">Creates and returns a <a href="shellwindows"><strong>ShellWindows</strong></a> object. This object represents a collection of all of the open windows that belong to the Shell.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shell-windowssecurity"><strong>WindowsSecurity</strong></a></td>
<td style="text-align: left;">Displays the <strong>Windows Security</strong> dialog box.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shell-windowswitcher"><strong>WindowSwitcher</strong></a></td>
<td style="text-align: left;">Displays your open windows in a 3D stack that you can flip through.<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **Shell** object has these properties.



| Property                                            | Access type          | Description                                                                 |
|:----------------------------------------------------|:---------------------|:----------------------------------------------------------------------------|
| [**Application**](shell-application.md)<br/> | Read-only<br/> | Contains the object's Application object.<br/>                        |
| [**Parent**](shell-parent.md)<br/>           | Read-only<br/> | Gets an object that represents the parent of the current object.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




