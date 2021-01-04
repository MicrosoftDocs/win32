---
title: IMsRdpDevice RedirectionState property
description: Indicates the redirection state of the device.
ms.assetid: 967734c9-64d8-4604-a133-4649279f4475
ms.tgt_platform: multiple
keywords:
- RedirectionState property Remote Desktop Services
- RedirectionState property Remote Desktop Services , IMsRdpDevice interface
- IMsRdpDevice interface Remote Desktop Services , RedirectionState property
topic_type:
- apiref
api_name:
- IMsRdpDevice.RedirectionState
- IMsRdpDevice.get_RedirectionState
- IMsRdpDevice.put_RedirectionState
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDevice::RedirectionState property

Indicates the redirection state of the device.

This property is read/write.

## Syntax


```C++
HRESULT put_RedirectionState(
  [in]  VARIANT_BOOL vboolRedirState
);

HRESULT get_RedirectionState(
  [out] VARIANT_BOOL *pvboolRedirState
);
```



## Property value

Set this parameter to **VARIANT\_FALSE** to disable redirection or **VARIANT\_TRUE** to enable redirection.

## Error codes

If the method succeeds, **S\_OK** is returned. Any other **HRESULT** value indicates that the call failed.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpDevice is defined as 60c3b9c8-9e92-4f5e-a3e7-604a912093ea<br/>        |



## See also

<dl> <dt>

[**IMsRdpDevice**](imsrdpdevice.md)
</dt> </dl>

 

 





