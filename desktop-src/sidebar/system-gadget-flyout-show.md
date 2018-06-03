---
title: System.Gadget.Flyout.show property
description: Gets or sets whether a gadget Flyout is visible.
ms.assetid: 3bbd1df3-d25d-431b-a71e-a948ef15b1cb
keywords:
- show property Windows Sidebar
- show property Windows Sidebar , System.Gadget.Flyout object
- System.Gadget.Flyout object Windows Sidebar , show property
topic_type:
- apiref
api_name:
- System.Gadget.Flyout.show
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Gadget.Flyout.show property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets whether a gadget **Flyout** is visible.

This property is read/write.

## Syntax


```JScript
bshow = System.Gadget.Flyout.show
System.Gadget.Flyout.show = bshow
```



## Property value

A **Boolean** that specifies or receives the gadget Flyout visibility state.

## Remarks

A gadget has one Flyout available at any time. The content of the Flyout can modified dynamically using the [**document**](system-gadget-flyout-document.md) object or by specifying a new HTML file with the [**file**](system-gadget-flyout-file.md) property.

## Examples

The following example demonstrates how to hide a flyout using the **show** property.


```JScript
// --------------------------------------------------------------------
// Hide the flyout.
// --------------------------------------------------------------------
function hideFlyout()
{
    System.Gadget.Flyout.show = false;
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





