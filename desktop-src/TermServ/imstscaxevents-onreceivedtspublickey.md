---
title: IMsTscAxEvents OnReceivedTSPublicKey method
description: Called during the connection sequence when the client retrieves the public key from the server. This event is only called if the NotifyTSPublicKey property is VARIANT\_TRUE.
ms.assetid: 1db98b8b-2f08-4252-ad8b-6764fa25b300
ms.tgt_platform: multiple
keywords:
- OnReceivedTSPublicKey method Remote Desktop Services
- OnReceivedTSPublicKey method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnReceivedTSPublicKey method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnReceivedTSPublicKey
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnReceivedTSPublicKey method

Called during the connection sequence when the client retrieves the public key from the server. This event is only called if the **NotifyTSPublicKey** property is **VARIANT\_TRUE**. This is after [**OnConnecting**](imstscaxevents-onconnecting.md), but before [**OnAuthenticationWarningDisplayed**](imstscaxevents-onauthenticationwarningdisplayed.md) and [**OnConnected**](imstscaxevents-onconnected.md).

## Syntax


```C++
void OnReceivedTSPublicKey(
  [in]  BSTR         publicKey,
  [out] VARIANT_BOOL *pfContinueLogon
);
```



## Parameters

<dl> <dt>

*publicKey* \[in\]
</dt> <dd>

Contains the public key of the remote machine.

</dd> <dt>

*pfContinueLogon* \[out\]
</dt> <dd>

A pointer to a **VARIANT\_BOOL** variable that receives whether the logon process should continue.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008, Windows Server 2008 with SP1<br/>                           |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





