---
title: System.Gadget.Flyout.onHide event
description: Event fired when the gadget Flyout is hidden.
ms.assetid: 4722a72c-ad5c-41fc-99f8-a23e23e20dcc
keywords:
- onHide event Windows Sidebar
- onHide event Windows Sidebar , System.Gadget.Flyout object
- System.Gadget.Flyout object Windows Sidebar , onHide event
topic_type:
- apiref
api_name:
- System.Gadget.Flyout.onHide
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Gadget.Flyout.onHide event

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the gadget **Flyout** is hidden.

## Syntax


```JScript
iRetVal = System.Gadget.Flyout.onHide(
  handler
)
```



## Parameters

<dl> <dt>

*handler* 
</dt> <dd>

The name of the function to call when the event is fired.

</dd> </dl>

## Remarks

This event updates the Flyout [**show**](system-gadget-flyout-show.md) property.

## Examples

The following example demonstrates how to listen for the **onHide** and [**onShow**](system-gadget-flyout-onshow.md) events of the gadget Flyout.


```JScript
var oGadgetDocument = System.Gadget.document;
System.Gadget.Flyout.onShow = showFlyout;
System.Gadget.Flyout.onHide = hideFlyout;

// --------------------------------------------------------------------
// Display the Flyout state in the gadget.
// --------------------------------------------------------------------
function showFlyout()
{
    oGadgetDocument.getElementById("strFlyoutFeedback").innerText = "Flyout visible.";
}

// --------------------------------------------------------------------
// Hide the flyout and display the Flyout state in the gadget.
// --------------------------------------------------------------------
function hideFlyout()
{
    oGadgetDocument.getElementById("strFlyoutFeedback").innerText = "Flyout hidden.";
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



 

 





