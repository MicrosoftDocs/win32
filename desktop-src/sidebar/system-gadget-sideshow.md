---
title: System.Gadget.SideShow object
description: Defines the properties, methods, and events that provide Windows Sidebar functionality on Windows Vista SideShow devices.
ms.assetid: b28a0df0-b766-40e4-ab64-0f9fe47dc970
keywords:
- System.Gadget.SideShow object Windows Sidebar
- System.Gadget.SideShow object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Gadget.SideShow
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# System.Gadget.SideShow object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties, methods, and events that provide Windows Sidebar functionality on Windows Vista SideShow devices.

## Members

The **System.Gadget.SideShow** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)

### Events

The **System.Gadget.SideShow** object has these events.



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
<td style="text-align: left;">[<strong>applicationEvent</strong>](system-gadget-sideshow-applicationevent.md)</td>
<td style="text-align: left;">Event fired when a SideShow device event occurs. <br/>
<blockquote>
[!Note]<br />
[<strong>applicationEvent</strong>](system-gadget-sideshow-applicationevent.md) is not fully supported in Sidebar.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### Methods

The **System.Gadget.SideShow** object has these methods.



| Method                                                            | Description                                               |
|:------------------------------------------------------------------|:----------------------------------------------------------|
| [**addImage**](system-gadget-sideshow-addimage.md)               | Adds an image element to the SideShow device. <br/> |
| [**addText**](system-gadget-sideshow-addtext.md)                 | Adds a text element to the SideShow device. <br/>   |
| [**enabled**](system-gadget-sideshow-enabled.md)                 | Retrieves whether SideShow is supported. <br/>      |
| [**remove**](system-gadget-sideshow-remove.md)                   | Removes an element specified by a content ID. <br/> |
| [**removeAll**](system-gadget-sideshow-removeall.md)             | Removes all gadget content. <br/>                   |
| [**setFriendlyName**](system-gadget-sideshow-setfriendlyname.md) | The display name for the SideShow gadget. <br/>     |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Other Resources**
</dt> <dt>

[Windows SideShow: MSDN](http://msdn.microsoft.com/library/ms744202.aspx)
</dt> <dt>

[Windows SideShow: Windows Hardware Developer Central](http://www.microsoft.com/whdc/device/sideshow/default.mspx)
</dt> </dl>

 

 





