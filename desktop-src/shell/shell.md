---
Description: 'Represents the objects in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects.'
title: Shell object
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
<td style="text-align: left;">[<strong>AddToRecent</strong>](shell.Shell_AddToRecent)</td>
<td style="text-align: left;">Adds a file to the most recently used (MRU) list.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>BrowseForFolder</strong>](shell-browseforfolder.md)</td>
<td style="text-align: left;">Creates a dialog box that enables the user to select a folder and then returns the selected folder's [<strong>Folder</strong>](folder.md) object.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>CanStartStopService</strong>](shell.Shell_CanStartStopService)</td>
<td style="text-align: left;">Determines if the current user can start and stop the named service.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>CascadeWindows</strong>](shell-cascadewindows.md)</td>
<td style="text-align: left;">Cascades all of the windows on the desktop. This method has the same effect as right-clicking the taskbar and selecting <strong>Cascade Windows</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>ControlPanelItem</strong>](shell-controlpanelitem.md)</td>
<td style="text-align: left;">Runs the specified Control Panel (*.cpl) application. If the application is already open, it will activate the running instance. <br/>
<blockquote>
<p>[!Note]<br />
As of Windows Vista, most Control Panel applications are Shell items and cannot be opened with this function. To open those Control Panel applications, pass the canonical name to control.exe. For example:</p>
<pre class="syntax" data-space="preserve"><code>control.exe /name Microsoft.Personalization</code></pre>
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>EjectPC</strong>](shell-ejectpc.md)</td>
<td style="text-align: left;">Ejects the computer from its docking station. This is the same as clicking the <strong>Start</strong> menu and selecting <strong>Eject PC</strong>, if your computer supports this command.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Explore</strong>](shell-explore.md)</td>
<td style="text-align: left;">Opens a specified folder in a Windows Explorer window.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ExplorerPolicy</strong>](shell-explorerpolicy.md)</td>
<td style="text-align: left;">Gets the value for a specified Internet Explorer policy.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>FileRun</strong>](shell-filerun.md)</td>
<td style="text-align: left;">Displays the <strong>Run</strong> dialog to the user. This method has the same effect as clicking the <strong>Start</strong> menu and selecting <strong>Run</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>FindComputer</strong>](shell-findcomputer.md)</td>
<td style="text-align: left;">Displays the <strong>Search Results: Computers</strong> dialog box. The dialog box shows the result of the search for a specified computer.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>FindFiles</strong>](shell-findfiles.md)</td>
<td style="text-align: left;">Displays the <strong>Find: All Files</strong> dialog box. This is the same as clicking the <strong>Start</strong> menu and then selecting <strong>Search</strong> (or its equivalent under systems earlier than Windows XP.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>FindPrinter</strong>](shell.Shell_FindPrinter)</td>
<td style="text-align: left;">Displays the <strong>Find Printer</strong> dialog box.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>GetSetting</strong>](shell.Shell_GetSetting)</td>
<td style="text-align: left;">Retrieves a global Shell setting.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>GetSystemInformation</strong>](shell.Shell_GetSystemInformation)</td>
<td style="text-align: left;">Retrieves system information.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Help</strong>](shell-help.md)</td>
<td style="text-align: left;">Displays the Windows Help and Support Center. This method has the same effect as clicking the <strong>Start</strong> menu and selecting <strong>Help and Support</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>IsRestricted</strong>](shell.Shell_IsRestricted)</td>
<td style="text-align: left;">Retrieves a group's restriction setting from the registry.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>IsServiceRunning</strong>](shell.Shell_IsServiceRunning)</td>
<td style="text-align: left;">Returns a value that indicates whether a particular service is running.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>MinimizeAll</strong>](shell-minimizeall.md)</td>
<td style="text-align: left;">Minimizes all of the windows on the desktop. This method has the same effect as right-clicking the taskbar and selecting <strong>Minimize All Windows</strong> on older systems or clicking the <strong>Show Desktop</strong> icon in the Quick Launch area of the taskbar in Windows 2000 or Windows XP.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>NameSpace</strong>](shell-namespace.md)</td>
<td style="text-align: left;">Creates and returns a [<strong>Folder</strong>](folder.md) object for the specified folder.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Open</strong>](shell-open.md)</td>
<td style="text-align: left;">Opens the specified folder.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RefreshMenu</strong>](shell-refreshmenu.md)</td>
<td style="text-align: left;">Refreshes the contents of the <strong>Start</strong> menu. Used only with systems preceding Windows XP.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>SearchCommand</strong>](shell-searchcommand.md)</td>
<td style="text-align: left;">Displays the Apps Search pane.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>ServiceStart</strong>](shell.Shell_ServiceStart)</td>
<td style="text-align: left;">Starts a named service.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ServiceStop</strong>](shell.Shell_ServiceStop)</td>
<td style="text-align: left;">Stops a named service.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>SetTime</strong>](shell-settime.md)</td>
<td style="text-align: left;">Displays the <strong>Date and Time Properties</strong> dialog box. This method has the same effect as right-clicking the clock in the taskbar status area and selecting <strong>Adjust Date/Time</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ShellExecute</strong>](shell.Shell_ShellExecute)</td>
<td style="text-align: left;">Performs a specified operation on a specified file.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>ShowBrowserBar</strong>](shell.Shell_ShowBrowserBar)</td>
<td style="text-align: left;">Displays a browser bar.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ShutdownWindows</strong>](shell-shutdownwindows.md)</td>
<td style="text-align: left;">Displays the <strong>Shut Down Windows</strong> dialog box. This is the same as clicking the <strong>Start</strong> menu and selecting <strong>Shut Down</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Suspend</strong>](shell-suspend.md)</td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>TileHorizontally</strong>](shell-tilehorizontally.md)</td>
<td style="text-align: left;">Tiles all of the windows on the desktop horizontally. This method has the same effect as right-clicking the taskbar and selecting <strong>Tile Windows Horizontally</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>TileVertically</strong>](shell-tilevertically.md)</td>
<td style="text-align: left;">Tiles all of the windows on the desktop vertically. This method has the same effect as right-clicking the taskbar and selecting <strong>Tile Windows Vertically</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ToggleDesktop</strong>](shell-toggledesktop.md)</td>
<td style="text-align: left;">Displays or hides the desktop.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>TrayProperties</strong>](shell-trayproperties.md)</td>
<td style="text-align: left;">Displays the <strong>Taskbar and Start Menu Properties</strong> dialog box. This method has the same effect as right-clicking the taskbar and selecting <strong>Properties</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>UndoMinimizeALL</strong>](shell-undominimizeall.md)</td>
<td style="text-align: left;">Restores all desktop windows to the same state they were in before the last [<strong>MinimizeAll</strong>](shell-minimizeall.md) command. This method has the same effect as right-clicking the taskbar and selecting <strong>Undo Minimize All Windows</strong> on older systems or a second clicking of the <strong>Show Desktop</strong> icon in the Quick Launch area of the taskbar in Windows 2000 or Windows XP.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Windows</strong>](shell-windows.md)</td>
<td style="text-align: left;">Creates and returns a [<strong>ShellWindows</strong>](shellwindows.md) object. This object represents a collection of all of the open windows that belong to the Shell.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WindowsSecurity</strong>](shell-windowssecurity.md)</td>
<td style="text-align: left;">Displays the <strong>Windows Security</strong> dialog box.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WindowSwitcher</strong>](shell-windowswitcher.md)</td>
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



 

 




