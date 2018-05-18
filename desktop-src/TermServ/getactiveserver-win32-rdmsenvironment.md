---
title: GetActiveServer method of the Win32\_RDMSEnvironment class
description: Retrieves the fully qualified domain name (FQDN) of the Remote Desktop Management Services (RDMS) environment.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '87e25d11-de1d-41d1-974d-2871dde444b5'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["GetActiveServer method Remote Desktop Services", "GetActiveServer method Remote Desktop Services , Win32_RDMSEnvironment class", "Win32_RDMSEnvironment class Remote Desktop Services , GetActiveServer method"]
topic_type:
- apiref
api_name:
- Win32_RDMSEnvironment.GetActiveServer
api_location:
- RDMS.dll
api_type:
- COM
---

# GetActiveServer method of the Win32\_RDMSEnvironment class

Retrieves the fully qualified domain name (FQDN) of the Remote Desktop Management Services (RDMS) environment.

## Syntax


```mof
uint32 GetActiveServer(
  [out] string ServerName
);
```



## Parameters

<dl> <dt>

*ServerName* \[out\]
</dt> <dd>

Receives the retrieved FQDN.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSEnvironment**](win32-rdmsenvironment.md)
</dt> </dl>

 

 





