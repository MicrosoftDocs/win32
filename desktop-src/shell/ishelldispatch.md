---
Description: Represents an object in the Shell.
title: IShellDispatch object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
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
---

# IShellDispatch object

Represents an object in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects.

> [!Note]  
> **IShellDispatch** is implemented and accessed through the [**Shell**](shell.md) object.

 

## Members

The **IShellDispatch** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IShellDispatch** object has these methods.



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
<td style="text-align: left;"><a href="ishelldispatch-browseforfolder"><strong>BrowseForFolder</strong></a></td>
<td style="text-align: left;">Creates a dialog box that enables the user to select a folder and then returns the selected folder's <a href="folder"><strong>Folder</strong></a> object.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="ishelldispatch-cascadewindows"><strong>CascadeWindows</strong></a></td>
<td style="text-align: left;">Cascades all of the windows on the desktop. This method has the same effect as right-clicking the taskbar and selecting <strong>Cascade windows</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="ishelldispatch-controlpanelitem"><strong>ControlPanelItem</strong></a></td>
<td style="text-align: left;">Runs the specified Control Panel application. If the application is already open, it will activate the running instance. <br/>
<blockquote>
<p>[!Note]<br />
As of Windows Vista, most Control Panel applications are Shell items and cannot be opened with this function. To open those Control Panel applications, pass the canonical name to control.exe. For example:</p>
<pre class="syntax" data-space="preserve"><code>control.exe /name Microsoft.Personalization</code></pre>
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="ishelldispatch-ejectpc"><strong>EjectPC</strong></a></td>
<td style="text-align: left;">Ejects the computer from its docking station. This is the same as clicking the <strong>Start</strong> menu and selecting <strong>Eject PC</strong>, if your computer supports this command.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="ishelldispatch-explore"><strong>Explore</strong></a></td>
<td style="text-align: left;">Opens a specified folder in a Windows Explorer window.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="ishelldispatch-filerun"><strong>FileRun</strong></a></td>
<td style="text-align: left;">Displays the <strong>Run</strong> dialog to the user.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="ishelldispatch-findcomputer"><strong>FindComputer</strong></a></td>
<td style="text-align: left;">Displays the <strong>Search Results: Computers</strong> dialog box. The dialog box shows the result of the search for a specified computer.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="ishelldispatch-findfiles"><strong>FindFiles</strong></a></td>
<td style="text-align: left;">Displays the <strong>Find: All Files</strong> dialog box. This is the same as clicking the <strong>Start</strong> menu and then selecting <strong>Search</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="ishelldispatch-help"><strong>Help</strong></a></td>
<td style="text-align: left;">Displays the Windows Help and Support window. This method has the same effect as clicking the <strong>Start</strong> menu and selecting <strong>Help and Support</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="ishelldispatch-minimizeall"><strong>MinimizeAll</strong></a></td>
<td style="text-align: left;">Minimizes all of the windows on the desktop. This method has the same effect as right-clicking the taskbar and selecting <strong>Minimize All Windows</strong> on older systems or clicking the <strong>Show Desktop</strong> icon on the taskbar.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="ishelldispatch-namespace"><strong>NameSpace</strong></a></td>
<td style="text-align: left;">Creates and returns a <a href="folder"><strong>Folder</strong></a> object for the specified folder.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="ishelldispatch-open"><strong>Open</strong></a></td>
<td style="text-align: left;">Opens the specified folder.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="ishelldispatch-refreshmenu"><strong>RefreshMenu</strong></a></td>
<td style="text-align: left;">Refreshes the contents of the <strong>Start</strong> menu. Used only with systems preceding Windows XP.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="ishelldispatch-settime"><strong>SetTime</strong></a></td>
<td style="text-align: left;">Displays the <strong>Date and Time</strong> dialog box. This method has the same effect as right-clicking the clock in the taskbar status area and selecting <strong>Adjust date/time</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="ishelldispatch-shutdownwindows"><strong>ShutdownWindows</strong></a></td>
<td style="text-align: left;">Displays the <strong>Shut Down Windows</strong> dialog box. This is the same as clicking the <strong>Start</strong> menu and selecting <strong>Shut Down</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="ishelldispatch-suspend"><strong>Suspend</strong></a></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="ishelldispatch-tilehorizontally"><strong>TileHorizontally</strong></a></td>
<td style="text-align: left;">Tiles all of the windows on the desktop horizontally. This method has the same effect as right-clicking the taskbar and selecting <strong>Show windows stacked</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="ishelldispatch-tilevertically"><strong>TileVertically</strong></a></td>
<td style="text-align: left;">Tiles all of the windows on the desktop vertically. This method has the same effect as right-clicking the taskbar and selecting <strong>Show windows side by side</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="ishelldispatch-trayproperties"><strong>TrayProperties</strong></a></td>
<td style="text-align: left;">Displays the <strong>Taskbar and Start Menu Properties</strong> dialog box. This method has the same effect as right-clicking the taskbar and selecting <strong>Properties</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="ishelldispatch-undominimizeall"><strong>UndoMinimizeALL</strong></a></td>
<td style="text-align: left;">Restores all desktop windows to the state they were in before the last <a href="shell-minimizeall"><strong>MinimizeAll</strong></a> command. This method has the same effect as right-clicking the taskbar and selecting <strong>Undo Minimize All Windows</strong> (on older systems) or a second clicking of the <strong>Show Desktop</strong> icon in the taskbar.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="ishelldispatch-windows"><strong>Windows</strong></a></td>
<td style="text-align: left;">Creates and returns a <a href="shellwindows"><strong>ShellWindows</strong></a> object. This object represents a collection of all of the open windows that belong to the Shell.<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **IShellDispatch** object has these properties.



| Property                                                     | Access type          | Description                                                                      |
|:-------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------|
| [**Application**](ishelldispatch-application.md)<br/> | Read-only<br/> | Contains an object that represents an application.<br/>                    |
| [**Parent**](ishelldispatch-parent.md)<br/>           | Read-only<br/> | Retrieves an object that represents the parent of the current object.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx)
</dt> <dt>

[**Shell Object**](shell.md)
</dt> </dl>

 

 




