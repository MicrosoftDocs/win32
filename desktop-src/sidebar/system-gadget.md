---
title: System.Gadget object
description: Defines the properties, methods, and events that provide basic gadget functionality.
ms.assetid: 3e71e04a-5c43-4280-86d9-e1f48fcc73f3
keywords:
- System.Gadget object Windows Sidebar
- System.Gadget object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Gadget
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Gadget object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties, methods, and events that provide basic gadget functionality.

## Members

The **System.Gadget** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **System.Gadget** object has these events.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Event</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>onDock</strong>](system-gadget-ondock.md)</td>
<td style="text-align: left;">Event fired when the gadget is docked on the Sidebar. <br/>
<blockquote>
[!Note]<br />
For Windows 7, because there is no Sidebar associated with the Gadget Platform, the [<strong>onDock</strong>](system-gadget-ondock.md) and [<strong>onUndock</strong>](system-gadget-onundock.md) event listeners are linked to a new gadget icon (&quot;Larger size&quot; or &quot;Smaller size&quot;). Clicking this icon resizes the gadget and raises the dock (&quot;Smaller size&quot;) or undock (&quot;Larger size&quot;) event.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>onSettingsClosed</strong>](system-gadget-onsettingsclosed.md)</td>
<td style="text-align: left;">Event fired when the gadget <strong>Settings</strong> dialog is closed. <br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>onSettingsClosing</strong>](system-gadget-onsettingsclosing.md)</td>
<td style="text-align: left;">Event fired when the gadget <strong>Settings</strong> dialog begins the process of closing. <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>onShowSettings</strong>](system-gadget-onshowsettings.md)</td>
<td style="text-align: left;">Event fired when the gadget <strong>Settings</strong> dialog is requested. <br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>onUndock</strong>](system-gadget-onundock.md)</td>
<td style="text-align: left;">Event fired when the gadget is docked on the Sidebar. <br/>
<blockquote>
[!Note]<br />
For Windows 7, because there is no Sidebar associated with the Gadget Platform, the [<strong>onDock</strong>](system-gadget-ondock.md) and [<strong>onUndock</strong>](system-gadget-onundock.md) event listeners are linked to a new gadget icon (&quot;Larger size&quot; or &quot;Smaller size&quot;). Clicking this icon resizes the gadget and raises the dock (&quot;Smaller size&quot;) or undock (&quot;Larger size&quot;) event.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>visibilityChanged</strong>](system-gadget-visibilitychanged.md)</td>
<td style="text-align: left;">Event fired when the gadget visibility changes due to the Sidebar being hidden or displayed. <br/></td>
</tr>
</tbody>
</table>



 

### Methods

The **System.Gadget** object has these methods.



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
<td style="text-align: left;">[<strong>beginTransition</strong>](system-gadget-begintransition.md)</td>
<td style="text-align: left;">Suspends all gadget updates, animations, and effects until a docking or undocking transition has completed. <br/>
<blockquote>
[!Note]<br />
For Windows 7, calls to the System.Gadget.beginTransition and System.Gadget.endTransition methods are ignored.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>close</strong>](system-gadget-close.md)</td>
<td style="text-align: left;">Ends a running instance of a gadget. <br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>endTransition</strong>](system-gadget-endtransition.md)</td>
<td style="text-align: left;">Refreshes the gadget view and resumes updates, animations, and effects once a gadget docking or undocking transition has completed. <br/>
<blockquote>
[!Note]<br />
For Windows 7, calls to the System.Gadget.beginTransition and System.Gadget.endTransition methods are ignored.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **System.Gadget** object has these properties.



| Property                                                            | Access type           | Description                                                                       |
|:--------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------|
| [**background**](system-gadget-background.md)<br/>           | Read/write<br/> | Gets or sets the file path for the gadget background image. <br/>           |
| [**docked**](system-gadget-docked.md)<br/>                   | Read-only<br/>  | Gets the dock state of the gadget in relation to the Sidebar. <br/>         |
| [**document**](system-gadget-document.md)<br/>               | Read-only<br/>  | Gets an object that represents the DOM of the gadget HTML file. <br/>       |
| [**name**](system-gadget-name.md)<br/>                       | Read-only<br/>  | Gets the gadget name as specified in the gadget manifest file. <br/>        |
| [**opacity**](system-gadget-opacity.md)<br/>                 | Read-only<br/>  | Gets the gadget opacity. <br/>                                              |
| [**path**](system-gadget-path.md)<br/>                       | Read-only<br/>  | Gets the UNC location of the gadget source files. <br/>                     |
| [**platformVersion**](system-gadget-platformversion.md)<br/> | Read-only<br/>  | Gets the Sidebar version. <br/>                                             |
| [**settingsUI**](system-gadget-settingsui.md)<br/>           | Read/write<br/> | Gets or sets the HTML filename for the gadget **Settings** dialog UI. <br/> |
| [**version**](system-gadget-version.md)<br/>                 | Read-only<br/>  | Gets the gadget version as specified in the gadget manifest file. <br/>     |
| [**visible**](system-gadget-visible.md)<br/>                 | Read-only<br/>  | Gets the visibility state of the gadget. <br/>                              |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





