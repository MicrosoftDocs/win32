---
description: Implemented by the Shell to help script and Microsoft Visual Basic developers use some of the features available in the Shell. The ShellUIHelper object does not have any properties or events. Methods are provided to add items to the Shell.
title: ShellUIHelper object (Exdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellUIHelper
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 9fffebc8-29b9-4064-b60c-c8c63690a79e
api_name: 
 - ShellUIHelper
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# ShellUIHelper object

Implemented by the Shell to help script and Microsoft Visual Basic developers use some of the features available in the Shell. The **ShellUIHelper** object does not have any properties or events. Methods are provided to add items to the Shell.

## Members

The **ShellUIHelper** object has these types of members:

-   [Methods](#methods)

### Methods

The **ShellUIHelper** object has these methods.



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
<td style="text-align: left;"><a href="shelluihelper-addchannel.md"><strong>AddChannel</strong></a></td>
<td style="text-align: left;">Adds a new channel to the list of channels in the Internet Explorer <strong>Favorites</strong> menu and to the <strong>Channel</strong> bar on the desktop.<br/>
<blockquote>
[!Note]<br />
This method is no longer supported under Windows Vista. Under that operating system, it returns E_NOTIMPL.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shelluihelper-adddesktopcomponent.md"><strong>AddDesktopComponent</strong></a></td>
<td style="text-align: left;">Adds an item to the Active Desktop.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="shelluihelper-addfavorite.md"><strong>AddFavorite</strong></a></td>
<td style="text-align: left;">Displays the default user interface for creating a favorite item. The user interface is initialized to the specified parameters.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="shelluihelper-issubscribed.md"><strong>IsSubscribed</strong></a></td>
<td style="text-align: left;">Indicates whether a specified URL is subscribed to.<br/></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Exdisp.h</dt> </dl>                            |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




