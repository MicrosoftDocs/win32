---
title: IMsRdpClient8 SendRemoteAction method
description: Causes an action to be performed in the remote session.
ms.assetid: d6a43662-7e51-404a-a3f9-a8b51cbc69d1
ms.tgt_platform: multiple
keywords:
- SendRemoteAction method Remote Desktop Services
- SendRemoteAction method Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , SendRemoteAction method
- SendRemoteAction method Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , SendRemoteAction method
- SendRemoteAction method Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , SendRemoteAction method
topic_type:
- apiref
api_name:
- IMsRdpClient8.SendRemoteAction
- IMsRdpClient9.SendRemoteAction
- IMsRdpClient10.SendRemoteAction
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient8::SendRemoteAction method

Causes an action to be performed in the remote session.

## Syntax


```C++
HRESULT SendRemoteAction(
  [in] RemoteSessionActionType actionType
);
```



## Parameters

<dl> <dt>

*actionType* \[in\]
</dt> <dd>

A value of the [**RemoteSessionActionType**](remotesessionactiontype.md) enumeration that specifies the action to send to the remote session.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpClient8 is defined as 4247E044-9271-43A9-BC49-E2AD9E855D62<br/>       |



## See also

<dl> <dt>

[**IMsRdpClient8**](imsrdpclient8.md)
</dt> <dt>

[**IMsRdpClient9**](imsrdpclient9.md)
</dt> <dt>

[**IMsRdpClient10**](imsrdpclient10.md)
</dt> </dl>

 

 





