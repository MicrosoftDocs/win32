---
title: IMsRdpClientShell RdpFileContents property
description: Specifies or retrieves the Remote Desktop Protocol (RDP) file content to be launched from Remote Desktop Web Access (RD Web Access) or from some other web portal.
ms.assetid: fcf37221-0fd5-41fd-83da-7fafc1aff944
ms.tgt_platform: multiple
keywords:
- RdpFileContents property Remote Desktop Services
- RdpFileContents property Remote Desktop Services , IMsRdpClientShell interface
- IMsRdpClientShell interface Remote Desktop Services , RdpFileContents property
topic_type:
- apiref
api_name:
- IMsRdpClientShell.RdpFileContents
- IMsRdpClientShell.get_RdpFileContents
- IMsRdpClientShell.put_RdpFileContents
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientShell::RdpFileContents property

Specifies or retrieves the Remote Desktop Protocol (RDP) file content to be launched from Remote Desktop Web Access (RD Web Access) or from some other web portal.

This property is read/write.

## Syntax


```C++
HRESULT put_RdpFileContents(
  [in]  BSTR newVal
);

HRESULT get_RdpFileContents(
  [out] BSTR *pszRdpFile
);
```



## Property value

Specifies the RDP file content to be launched from the web portal.

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

 

 





