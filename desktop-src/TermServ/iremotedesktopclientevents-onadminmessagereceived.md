---
title: IRemoteDesktopClientEvents OnAdminMessageReceived method
description: Called when the client control receives an administrative message.
ms.assetid: CD580207-CEC1-493B-989E-7C1D4FA71228
ms.tgt_platform: multiple
keywords:
- OnAdminMessageReceived method Remote Desktop Services
- OnAdminMessageReceived method Remote Desktop Services , IRemoteDesktopClientEvents interface
- IRemoteDesktopClientEvents interface Remote Desktop Services , OnAdminMessageReceived method
topic_type:
- apiref
api_name:
- IRemoteDesktopClientEvents.OnAdminMessageReceived
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IRemoteDesktopClientEvents::OnAdminMessageReceived method

Called when the client control receives an administrative message.

## Syntax


```C++
void OnAdminMessageReceived(
  [in] BSTR adminMessage
);
```



## Parameters

<dl> <dt>

*adminMessage* \[in\]
</dt> <dd>

The message.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>         |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>         |
| IID<br/>                      | DIID\_IRemoteDesktopClientEvents is defined as 079863B7-6D47-4105-8BFE-0CDCB360E67D<br/> |



## See also

<dl> <dt>

[**IRemoteDesktopClientEvents**](iremotedesktopclientevents.md)
</dt> </dl>

 

 





