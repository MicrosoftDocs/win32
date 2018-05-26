---
title: OnApplicationUpdate event
description: Called when the shared property on the application object is changed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ff2229f8-9214-49df-b03d-73d89520ac06
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnApplicationUpdate event RDP
topic_type:
- apiref
api_name:
- OnApplicationUpdate
api_location:
- RdpEncom.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnApplicationUpdate event

Called when the [**shared**](/windows/win32/RdpEncomAPI/nf-rdpencomapi-irdpsrapiapplication-get_shared?branch=master) property on the application object is changed.

## Syntax


```C++
void OnApplicationUpdate(
  [in] IDispatch *pApplication
);
```



## Parameters

<dl> <dt>

*pApplication* \[in\]
</dt> <dd>

The application whose [**shared**](/windows/win32/RdpEncomAPI/nf-rdpencomapi-irdpsrapiapplication-get_shared?branch=master) property was updated. Query the **IDispatch** interface for the [**IRDPSRAPIApplication**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiapplication?branch=master) interface that you use to retrieve information about the application.

</dd> </dl>

## Return value

This event does not return a value.

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

[**\_IRDPSessionEvents**](/windows/win32/RdpEncomAPI/?branch=master)
</dt> </dl>

 

 





