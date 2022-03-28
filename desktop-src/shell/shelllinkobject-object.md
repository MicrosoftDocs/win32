---
description: Manages Shell links. This object makes much of the functionality of the IShellLink interface available to scripting applications.
title: ShellLinkObject object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellLinkObject
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: d3c0ccf8-0f83-42f7-9d6f-1fb293da6364

---

# ShellLinkObject object

Manages Shell links. This object makes much of the functionality of the [**IShellLink**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka) interface available to scripting applications.

## Members

The **ShellLinkObject** object has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **ShellLinkObject** object has these methods.



| Method                                                     | Description                                                                                    |
|:-----------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**GetIconLocation**](shelllinkobject-geticonlocation.md) | Gets the location of the icon assigned to the link.<br/>                                 |
| [**Resolve**](shelllinkobject-resolve.md)                 | Looks for the target of a Shell link, even if the target has been moved or renamed.<br/> |
| [**Save**](shelllinkobject-save.md)                       | Saves all changes to the link.<br/>                                                      |
| [**SetIconLocation**](shelllinkobject-seticonlocation.md) | Sets the location of the icon assigned to the link.<br/>                                 |



 

### Properties

The **ShellLinkObject** object has these properties.



| Property                                                                | Access type           | Description                                                                                               |
|:------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------|
| [**Arguments**](shelllinkobject-arguments.md)<br/>               | Read/write<br/> | Contains a link's arguments.<br/>                                                                   |
| [**Description**](shelllinkobject-description.md)<br/>           | Read/write<br/> | Gets or sets the description of the link.<br/>                                                      |
| [**Hotkey**](shelllinkobject-hotkey.md)<br/>                     | Read/write<br/> | Gets or sets the keyboard shortcut for the link.<br/>                                               |
| [**Path**](shelllinkobject-path.md)<br/>                         | Read/write<br/> | Gets or sets the path to the link object.<br/>                                                      |
| [**ShowCommand**](shelllinkobject-showcommand.md)<br/>           | Read/write<br/> | Gets or sets the initial display state (sized, minimized, or maximized) of the link's command.<br/> |
| [**WorkingDirectory**](shelllinkobject-workingdirectory.md)<br/> | Read/write<br/> | Gets or sets the working directory specified in the link.<br/>                                      |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[Shell Links](./links.md)
</dt> </dl>

 

 
