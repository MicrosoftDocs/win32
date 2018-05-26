---
title: System.Gadget.visible property
description: Gets the visibility state of the gadget.
ms.assetid: 56d0f4fc-5252-40df-901b-595e8b58f46a
keywords:
- visible property Windows Sidebar
- visible property Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , visible property
topic_type:
- apiref
api_name:
- System.Gadget.visible
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

# System.Gadget.visible property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the visibility state of the gadget.

This property is read-only.

## Syntax


```JScript
bvisible = System.Gadget.visible
```



## Property value

A **Boolean** that receives the visibility state of the gadget.

<dt>



 (TRUE)


</dt> <dd>

Gadget is visible.

</dd> <dt>



 (FALSE)


</dt> <dd>

Gadget is not visible.

</dd> </dl>

## Remarks

This property is updated by the [**visibilityChanged**](system-gadget-visibilitychanged.md) event.

## Examples

The following example demonstrates how to use the [**visibilityChanged**](system-gadget-visibilitychanged.md) event to suspend or resume a timer based on the gadget visibility.


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

[**visibilityChanged**](system-gadget-visibilitychanged.md)
</dt> </dl>

 

 





