---
title: Get method of the PS\_DnsServerForwarder class
description: Retrieves DNS Forwarder Settings.
audience: developer
ms.assetid: '34f300ea-3f7d-4751-b99f-a196d686562e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DnsServerForwarder class", "PS_DnsServerForwarder class, Get method"]
topic_type:
- apiref
api_name:
- PS_DnsServerForwarder.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DnsServerForwarder class

Retrieves DNS Forwarder Settings.

## Syntax


```mof
uint32 Get(
  [in]  string             ComputerName,
  [out] DnsServerForwarder cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of [**DnsServerForwarder**](dnsserverforwarder.md).

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

[**PS\_DnsServerForwarder**](ps-dnsserverforwarder.md)
</dt> </dl>

 

 





