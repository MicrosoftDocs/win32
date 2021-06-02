---
title: IMsRdpClient8 Reconnect method
description: Reconnects to the remote session with the new desktop width and height.
ms.assetid: A2C4101D-780A-4973-B87C-025D9140C4BC
ms.tgt_platform: multiple
keywords:
- Reconnect method Remote Desktop Services
- Reconnect method Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , Reconnect method
- Reconnect method Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , Reconnect method
- Reconnect method Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , Reconnect method
topic_type:
- apiref
api_name:
- IMsRdpClient8.Reconnect
- IMsRdpClient9.Reconnect
- IMsRdpClient10.Reconnect
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient8::Reconnect method

Reconnects to the remote session with the new desktop width and height. The control must already be connected to a remote session for this method to succeed.

## Syntax


```C++
HRESULT Reconnect(
  [in]          ULONG                  ulWidth,
  [in]          ULONG                  ulHeight,
  [out, retval] ControlReconnectStatus *pReconnectStatus
);
```



## Parameters

<dl> <dt>

*ulWidth* \[in\]
</dt> <dd>

Type: **ULONG**

The new desktop width, in pixels. See the [**DesktopWidth**](imstscax-desktopwidth.md) property for value restrictions.

</dd> <dt>

*ulHeight* \[in\]
</dt> <dd>

Type: **ULONG**

The new desktop height, in pixels. See the [**DesktopHeight**](imstscax-desktopheight.md) property for value restrictions.

</dd> <dt>

*pReconnectStatus* \[out, retval\]
</dt> <dd>

Type: **[**ControlReconnectStatus**](controlreconnectstatus.md)\***

A pointer to a [**ControlReconnectStatus**](controlreconnectstatus.md) variable that receives the status of the reconnect operation.

</dd> </dl>

## Return value

Type: **HRESULT**

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
</dt> <dt>

[**ControlReconnectStatus**](controlreconnectstatus.md)
</dt> </dl>

 

 





