---
title: Get method of the PS\_DnsServer class
description: Retrieves entire DNS Server Configuration.
audience: developer
ms.assetid: 'c6014903-554b-4a83-91fc-53f7b1afc676'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DnsServer class", "PS_DnsServer class, Get method"]
topic_type:
- apiref
api_name:
- PS_DnsServer.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DnsServer class

Retrieves entire DNS Server Configuration.

## Syntax


```mof
uint32 Get(
  [in]  string    ComputerName,
  [out] DnsServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServer**](dnsserver.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServer**](ps-dnsserver.md)
</dt> </dl>

 

 





