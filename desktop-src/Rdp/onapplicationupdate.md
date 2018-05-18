---
title: OnApplicationUpdate event
description: Called when the shared property on the application object is changed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ff2229f8-9214-49df-b03d-73d89520ac06'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnApplicationUpdate event RDP"]
topic_type:
- apiref
api_name:
- OnApplicationUpdate
api_location:
- RdpEncom.dll
api_type:
- COM
---

# OnApplicationUpdate event

Called when the [**shared**](irdpsrapiapplication-shared.md) property on the application object is changed.

## Syntax


```C++
void OnApplicationUpdate(
  [in] IDispatch *pApplication
);
```



## Parameters

<dl> <dt>

*pApplication* \[in\]
</dt> <dd>

The application whose [**shared**](irdpsrapiapplication-shared.md) property was updated. Query the **IDispatch** interface for the [**IRDPSRAPIApplication**](irdpsrapiapplication.md) interface that you use to retrieve information about the application.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>RdpEncomAPI.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RdpEncomAPI.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RdpEncomAPI.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RdpEncom.dll</dt> </dl>    |



## See also

<dl> <dt>

[**\_IRDPSessionEvents**](-irdpsessionevents.md)
</dt> </dl>

 

 





