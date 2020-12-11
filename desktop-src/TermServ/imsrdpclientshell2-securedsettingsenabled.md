---
title: IMsRdpClientShell2 SecuredSettingsEnabled property
description: Retrieves a value that indicates whether the current webpage is in a trusted Internet Explorer URL security zone.
ms.assetid: 51988473-fff7-4574-bd6e-d05ca452da54
ms.tgt_platform: multiple
keywords:
- SecuredSettingsEnabled property Remote Desktop Services
- SecuredSettingsEnabled property Remote Desktop Services , IMsRdpClientShell2 interface
- IMsRdpClientShell2 interface Remote Desktop Services , SecuredSettingsEnabled property
topic_type:
- apiref
api_name:
- IMsRdpClientShell2.SecuredSettingsEnabled
- IMsRdpClientShell2.get_SecuredSettingsEnabled
api_location:
- MsRdpWebAccess.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientShell2::SecuredSettingsEnabled property

Retrieves a value that indicates whether the current webpage is in a trusted Internet Explorer URL security zone.

This property is read-only.

## Syntax


```C++
HRESULT get_SecuredSettingsEnabled(
  [out, retval] BOOL *pSecuredSettingsEnabled
);
```



## Property value

A pointer to a Boolean value that indicates whether the current webpage is in a trusted Internet Explorer URL security zone.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                             |
| DLL<br/>                      | <dl> <dt>MsRdpWebAccess.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsRdpClientShell2**](imsrdpclientshell2.md)
</dt> </dl>

 

 





