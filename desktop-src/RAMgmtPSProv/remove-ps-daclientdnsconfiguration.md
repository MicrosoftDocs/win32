---
title: Remove method of the PS\_DAClientDnsConfiguration class
description: This cmdlet removes the NRPT entry corresponding to the specified DNS suffix from the NRPT table.
audience: developer
ms.assetid: '891f4f04-7949-437f-95e6-7723a71a5901'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_DAClientDnsConfiguration class", "PS_DAClientDnsConfiguration class, Remove method"]
topic_type:
- apiref
api_name:
- PS_DAClientDnsConfiguration.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Remove method of the PS\_DAClientDnsConfiguration class

This cmdlet removes the NRPT entry corresponding to the specified DNS suffix from the NRPT table.

## Syntax


```mof
uint32 Remove(
  [in]  string            DnsSuffix[],
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [out] DnsClientNrptRule cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*DnsSuffix* \[in\]
</dt> <dd>

Specifies a list of DNS suffixes

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the DNS client NRPT object. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

NRPT object for the NRPT entry that was removed

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

 

 





