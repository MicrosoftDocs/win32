---
title: Get method of the PS\_DnsServerScavenging class
description: Retrieves DNS aging and scavenging settings.
audience: developer
ms.assetid: 'cf2c9450-86d7-463f-868a-e4c1eb6c63dd'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DnsServerScavenging class", "PS_DnsServerScavenging class, Get method"]
topic_type:
- apiref
api_name:
- PS_DnsServerScavenging.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DnsServerScavenging class

Retrieves DNS aging and scavenging settings.

## Syntax


```mof
uint32 Get(
  [in]  string              ComputerName,
  [out] DnsServerScavenging cmdletOutput
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

An embedded instance of the [**DnsServerScavenging**](dnsserverscavenging.md) class.

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

[**PS\_DnsServerScavenging**](ps-dnsserverscavenging.md)
</dt> </dl>

 

 





