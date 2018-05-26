---
title: System.Gadget.visibilityChanged event
description: Event fired when the gadget visibility changes due to the Windows Sidebar being hidden or displayed.
ms.assetid: d01c0bcb-bd0d-4872-a05e-31051f3d4fd6
keywords:
- visibilityChanged event Windows Sidebar
- visibilityChanged event Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , visibilityChanged event
topic_type:
- apiref
api_name:
- System.Gadget.visibilityChanged
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

# System.Gadget.visibilityChanged event

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the gadget visibility changes due to the Windows Sidebar being hidden or displayed.

## Syntax


```JScript
iRetVal = System.Gadget.visibilityChanged(
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

This event can be used to suspend or resume gadget execution as appropriate.

This event is fired only when the gadget is docked to the Sidebar.

This event updates the gadget [**visible**](system-gadget-visible.md) property.

## Examples

The following example demonstrates how to use the **visibilityChanged** event to suspend or resume a timer based on the gadget visibility.


```JScript
// Delegate for the gadget visibility changed event.
System.Gadget.visibilityChanged = checkVisibility;

// --------------------------------------------------------------------
// Handle the gadget visiblity changed event.
// event = Event argument.
// --------------------------------------------------------------------
function VisibilityChanged(event)
{
    if (!System.Gadget.visible)
    {
        // Stop the timer;
    }
    else
    {
        // Start the timer;
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



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**System.Gadget**](system-gadget.md)
</dt> <dt>

[**visible**](system-gadget-visible.md)
</dt> </dl>

 

 





