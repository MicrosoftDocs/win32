---
title: IMsRdpClient9 attachEvent method
description: Attaches an event.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3a887aeb-a74f-4477-8cf3-8ac43a31fa26'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["attachEvent method Remote Desktop Services", "attachEvent method Remote Desktop Services , IMsRdpClient9 interface", "IMsRdpClient9 interface Remote Desktop Services , attachEvent method", "attachEvent method Remote Desktop Services , IMsRdpClient10 interface", "IMsRdpClient10 interface Remote Desktop Services , attachEvent method"]
topic_type:
- apiref
api_name:
- IMsRdpClient9.attachEvent
- IMsRdpClient10.attachEvent
api_location:
- MsTscAx.dll
api_type:
- COM
---

# IMsRdpClient9::attachEvent method

Attaches an event.

## Syntax


```C++
HRESULT attachEvent(
  [in] BSTR      eventName,
  [in] IDispatch *callback
);
```



## Parameters

<dl> <dt>

*eventName* \[in\]
</dt> <dd>

The event to attach.

</dd> <dt>

*callback* \[in\]
</dt> <dd>

The callback.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                                                                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                                                                                                                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                                                                                                                                                                                       |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>                                                                                                                                                                                  |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>                                                                                                                                                                                  |
| IID<br/>                      | CLSID\_MsRdpClient9 is defined as 301B94BA-5D25-4A12-BFFE-3B6E7A616585<br/> CLSID\_MsRdpClient9NotSafeForScripting is defined as 8B918B82-7985-4C24-89DF-C33AD2BBFBCD<br/> IID\_IMsRdpClient9 is defined as 28904001-04B6-436C-A55B-0AF1A0883DC9<br/> |



## See also

<dl> <dt>

[**IMsRdpClient10**](imsrdpclient10.md)
</dt> <dt>

[**IMsRdpClient9**](imsrdpclient9.md)
</dt> </dl>

 

 





