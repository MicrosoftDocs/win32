---
title: Get method of the PS\_DAClientDnsConfiguration class
description: This cmdlet displays all the NRPT table entries and the local name resolution property.
audience: developer
ms.assetid: '4ad6d201-41d9-467c-9633-cb9c297f1071'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DAClientDnsConfiguration class", "PS_DAClientDnsConfiguration class, Get method"]
topic_type:
- apiref
api_name:
- PS_DAClientDnsConfiguration.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DAClientDnsConfiguration class

This cmdlet displays all the NRPT table entries and the local name resolution property.

## Syntax


```mof
uint32 Get(
  [in]  string                   ComputerName,
  [out] DAClientDnsConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. List of NRPT objects for the NRPT table entries entries. 2. Property of local name resolution

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAClientDnsConfiguration**](ps-daclientdnsconfiguration.md)
</dt> </dl>

 

 





