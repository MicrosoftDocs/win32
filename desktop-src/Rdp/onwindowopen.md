---
title: OnWindowOpen event
description: Called when a sharable top-level window is created by an application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7ccb66c7-ab3b-47b7-aba3-3e04a774a49b
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnWindowOpen event RDP
topic_type:
- apiref
api_name:
- OnWindowOpen
api_location:
- RdpEncom.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnWindowOpen event

Called when a sharable top-level window is created by an application.

## Syntax


```C++
void OnWindowOpen(
  [in] IDispatch *pWindow
);
```



## Parameters

<dl> <dt>

*pWindow* \[in\]
</dt> <dd>

The sharable top-level window that was created. Query the **IDispatch** interface for the [**IRDPSRAPIWindow**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiwindow) interface that you use to retrieve information about the window.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

If this is the first window object associated with the application, then this event immediately follows the [**OnApplicationOpen**](onapplicationopen.md) event for the application.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>RdpEncomAPI.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RdpEncomAPI.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RdpEncomAPI.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RdpEncom.dll</dt> </dl>    |



## See also

<dl> <dt>

[**\_IRDPSessionEvents**](/windows/desktop/api/RdpEncomAPI/)
</dt> </dl>

 

 





