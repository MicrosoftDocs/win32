---
title: OnApplicationOpen event
description: Called when a new application is created.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3ab21b33-ff02-4e7a-b6b9-17bc5596d9c1
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnApplicationOpen event RDP
topic_type:
- apiref
api_name:
- OnApplicationOpen
api_location:
- RdpEncom.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnApplicationOpen event

Called when a new application is created.

## Syntax


```C++
void OnApplicationOpen(
  [in] IDispatch *pApplication
);
```



## Parameters

<dl> <dt>

*pApplication* \[in\]
</dt> <dd>

The application that was created. Query the **IDispatch** interface for the [**IRDPSRAPIApplication**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiapplication) interface that you use to retrieve information about the application.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

You should process this event and update your user interface accordingly. Note that this event is always followed by a [**OnWindowOpen**](onwindowopen.md) event.

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

 

 





