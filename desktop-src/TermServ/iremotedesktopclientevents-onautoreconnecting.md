---
title: IRemoteDesktopClientEvents OnAutoReconnecting method
description: Called when the client control attempts to automatically reestablish a connection to a remote session.
ms.assetid: 299408A9-ED14-42F4-B324-AF4C86FEDABE
ms.tgt_platform: multiple
keywords:
- OnAutoReconnecting method Remote Desktop Services
- OnAutoReconnecting method Remote Desktop Services , IRemoteDesktopClientEvents interface
- IRemoteDesktopClientEvents interface Remote Desktop Services , OnAutoReconnecting method
topic_type:
- apiref
api_name:
- IRemoteDesktopClientEvents.OnAutoReconnecting
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IRemoteDesktopClientEvents::OnAutoReconnecting method

Called when the client control attempts to automatically reestablish a connection to a remote session.

## Syntax


```C++
void OnAutoReconnecting(
  [in] long         disconnectReason,
  [in] long         ExtendedDisconnectReason,
  [in] BSTR         disconnectErrorMessage,
  [in] VARIANT_BOOL networkAvailable,
  [in] long         attemptCount,
  [in] long         maxAttemptCount
);
```



## Parameters

<dl> <dt>

*disconnectReason* \[in\]
</dt> <dd>

The reason for the disconnect event.

</dd> <dt>

*ExtendedDisconnectReason* \[in\]
</dt> <dd>

Extended information for the disconnect event.

</dd> <dt>

*disconnectErrorMessage* \[in\]
</dt> <dd>

The error message for the disconnect event.

</dd> <dt>

*networkAvailable* \[in\]
</dt> <dd>

Whether the network is available.

</dd> <dt>

*attemptCount* \[in\]
</dt> <dd>

Which attempt this is.

</dd> <dt>

*maxAttemptCount* \[in\]
</dt> <dd>

The maximum number of reconnect attempts will be performed.

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

 

 





