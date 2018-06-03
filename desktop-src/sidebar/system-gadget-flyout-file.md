---
title: System.Gadget.Flyout.file property
description: Gets or sets the HTML filename for the gadget Flyout UI.
ms.assetid: d6023605-45bd-4ed0-a919-2af9b9f9e0e0
keywords:
- file property Windows Sidebar
- file property Windows Sidebar , System.Gadget.Flyout object
- System.Gadget.Flyout object Windows Sidebar , file property
topic_type:
- apiref
api_name:
- System.Gadget.Flyout.file
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

# System.Gadget.Flyout.file property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the HTML filename for the gadget **Flyout** UI.

This property is read/write.

## Syntax


```JScript
strfile = System.Gadget.Flyout.file
System.Gadget.Flyout.file = strfile
```



## Property value

A **String** that specifies or receives the HTML filename.

## Remarks

A gadget Flyout is shown with a call to [**show**](system-gadget-flyout-show.md).

A gadget has one Flyout available at any time. The content of the Flyout can modified dynamically using the [**document**](system-gadget-flyout-document.md) object or by specifying a new HTML file with the **file** property.

## Examples

The following example demonstrates how to set the gadget Flyout UI from the gadget script file.


```JScript
// --------------------------------------------------------------------
// Initialize the gadget.
// --------------------------------------------------------------------
function Init()
{
    // Specify the flyout root.
    System.Gadget.Flyout.file = "example.html";
    
    // Initialize the Flyout state display.
    if (!System.Gadget.Flyout.show)
    {
        sFlyoutFeedback.innerText = "Flyout hidden.";
    }
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



 

 





