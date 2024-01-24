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

---

# ShellUIHelper object

Implemented by the Shell to help script and Microsoft Visual Basic developers use some of the features available in the Shell. The **ShellUIHelper** object does not have any properties or events. Methods are provided to add items to the Shell.

## Members

The **ShellUIHelper** object has these types of members:

-   [Methods](#methods)

### Methods

The **ShellUIHelper** object has these methods.




| Method | Description | 
|--------|-------------|
| [**AddChannel**](shelluihelper-addchannel.md) | Adds a new channel to the list of channels in the Internet Explorer **Favorites** menu and to the **Channel** bar on the desktop.<br> **Note:** This method is no longer supported under Windows Vista. Under that operating system, it returns E_NOTIMPL.<br> | 
| <a href="shelluihelper-adddesktopcomponent.md"><strong>AddDesktopComponent</strong></a> | Adds an item to the Active Desktop.<br /> | 
| <a href="shelluihelper-addfavorite.md"><strong>AddFavorite</strong></a> | Displays the default user interface for creating a favorite item. The user interface is initialized to the specified parameters.<br /> | 
| <a href="shelluihelper-issubscribed.md"><strong>IsSubscribed</strong></a> | Indicates whether a specified URL is subscribed to.<br /> | 




 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Exdisp.h</dt> </dl>                            |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




