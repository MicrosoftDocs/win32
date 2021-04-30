---
title: IRemoteDesktopClientEvents OnStatusChanged method (Locationapi.h)
description: Called when the client control has updated its status.
ms.assetid: AAFBDC9E-C8B5-4924-AA69-82EF09996AF7
ms.tgt_platform: multiple
keywords:
- OnStatusChanged method Remote Desktop Services
- OnStatusChanged method Remote Desktop Services , IRemoteDesktopClientEvents interface
- IRemoteDesktopClientEvents interface Remote Desktop Services , OnStatusChanged method
topic_type:
- apiref
api_name:
- IRemoteDesktopClientEvents.OnStatusChanged
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IRemoteDesktopClientEvents::OnStatusChanged method

Called when the client control has updated its status.

## Syntax


```C++
void OnStatusChanged(
   long statusCode,
   BSTR statusMessage
);
```



## Parameters

<dl> <dt>

*statusCode* 
</dt> <dd>

The new status code.

</dd> <dt>

*statusMessage* 
</dt> <dd>

The status message text.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Header<br/>                   | <dl> <dt>Locationapi.h</dt> </dl>       |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>         |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>         |
| IID<br/>                      | DIID\_IRemoteDesktopClientEvents is defined as 079863B7-6D47-4105-8BFE-0CDCB360E67D<br/> |



## See also

<dl> <dt>

[**IRemoteDesktopClientEvents**](iremotedesktopclientevents.md)
</dt> </dl>

 

 





