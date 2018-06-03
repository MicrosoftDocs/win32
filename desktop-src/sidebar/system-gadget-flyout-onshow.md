---
title: System.Gadget.Flyout.onShow event
description: Event fired when the gadget Flyout is shown.
ms.assetid: b356e14b-94df-4a96-9d8f-55eca18664ed
keywords:
- onShow event Windows Sidebar
- onShow event Windows Sidebar , System.Gadget.Flyout object
- System.Gadget.Flyout object Windows Sidebar , onShow event
topic_type:
- apiref
api_name:
- System.Gadget.Flyout.onShow
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

# System.Gadget.Flyout.onShow event

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the gadget **Flyout** is shown.

## Syntax


```JScript
iRetVal = System.Gadget.Flyout.onShow(
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

The following example demonstrates how to listen for the [**onHide**](system-gadget-flyout-onhide.md) and **onShow** events of the gadget Flyout.


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



 

 





