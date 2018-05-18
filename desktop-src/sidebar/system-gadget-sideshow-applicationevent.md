---
title: System.Gadget.SideShow.applicationEvent event
description: Event fired when a SideShow device event occurs.
ms.assetid: 'cf5d5d03-3c95-4b9e-b6d5-ffa15306c4cd'
keywords: ["applicationEvent event Windows Sidebar", "applicationEvent event Windows Sidebar , System.Gadget.SideShow object", "System.Gadget.SideShow object Windows Sidebar , applicationEvent event"]
topic_type:
- apiref
api_name:
- System.Gadget.SideShow.applicationEvent
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Gadget.SideShow.applicationEvent event

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when a SideShow device event occurs.

> [!Note]  
> **applicationEvent** is not fully supported in Windows Sidebar.

 

## Syntax


```JScript
iRetVal = System.Gadget.SideShow.applicationEvent(
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

Three SideShow application events are sent to the computer when it is online: navigation events, menu action events, and context menu action events.

Verify that [**System.Gadget.SideShow.enabled**](system-gadget-sideshow-enabled.md) returns `true` before using other [**System.Gadget.SideShow**](system-gadget-sideshow.md) object members.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Windowssideshowapi.h</dt> </dl>                |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

[**System.Gadget.SideShow**](system-gadget-sideshow.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[Windows SideShow: MSDN](http://msdn.microsoft.com/library/ms744202.aspx)
</dt> <dt>

[Windows SideShow: Windows Hardware Developer Central](http://www.microsoft.com/whdc/device/sideshow/default.mspx)
</dt> </dl>

 

 





