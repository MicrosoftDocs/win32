---
title: IMsRdpClient9 detachEvent method
description: Detaches an event.
ms.assetid: 6a3ca713-1d5c-4070-a527-ad4f532a4cbf
ms.tgt_platform: multiple
keywords:
- detachEvent method Remote Desktop Services
- detachEvent method Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , detachEvent method
- detachEvent method Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , detachEvent method
topic_type:
- apiref
api_name:
- IMsRdpClient9.detachEvent
- IMsRdpClient10.detachEvent
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient9::detachEvent method

Detaches an event.

## Syntax


```C++
HRESULT detachEvent(
  [in] BSTR      eventName,
  [in] IDispatch *callback
);
```



## Parameters

<dl> <dt>

*eventName* \[in\]
</dt> <dd>

Name of the event.

</dd> <dt>

*callback* \[in\]
</dt> <dd>

The callback associated with the event.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                                                                                                                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                                                                                                                                                                                       |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>                                                                                                                                                                                  |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>                                                                                                                                                                                  |
| IID<br/>                      | CLSID\_MsRdpClient9 is defined as 301B94BA-5D25-4A12-BFFE-3B6E7A616585<br/> CLSID\_MsRdpClient9NotSafeForScripting is defined as 8B918B82-7985-4C24-89DF-C33AD2BBFBCD<br/> IID\_IMsRdpClient9 is defined as 28904001-04B6-436C-A55B-0AF1A0883DC9<br/> |



## See also

<dl> <dt>

[**IMsRdpClient10**](imsrdpclient10.md)
</dt> <dt>

[**IMsRdpClient9**](imsrdpclient9.md)
</dt> </dl>

 

 





