---
title: IMsRdpClientShell PublicMode property
description: Specifies or retrieves whether public mode is enabled.
ms.assetid: 983d3e46-f09e-4425-88a1-9d4ae0d9c70a
ms.tgt_platform: multiple
keywords:
- PublicMode property Remote Desktop Services
- PublicMode property Remote Desktop Services , IMsRdpClientShell interface
- IMsRdpClientShell interface Remote Desktop Services , PublicMode property
topic_type:
- apiref
api_name:
- IMsRdpClientShell.PublicMode
- IMsRdpClientShell.get_PublicMode
- IMsRdpClientShell.put_PublicMode
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientShell::PublicMode property

Specifies or retrieves whether public mode is enabled.

This property is read/write.

## Syntax


```C++
HRESULT put_PublicMode(
  [in]  VARIANT_BOOL fPublicMode
);

HRESULT get_PublicMode(
  [out] VARIANT_BOOL *pfPublicMode
);
```



## Property value

Specifies whether public mode is enabled.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpClientShell is defined as d012ae6d-c19a-4bfe-b367-201f8911f134<br/>   |



## See also

<dl> <dt>

[**IMsRdpClientShell**](imsrdpclientshell.md)
</dt> </dl>

 

 





