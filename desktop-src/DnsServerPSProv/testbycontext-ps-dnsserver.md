---
title: TestByContext method of the PS\_DnsServer class
description: Tests that the computers with the addresses that you specify are functioning DNS servers.
audience: developer
ms.assetid: '484822ea-7109-412d-a2f8-3d4e3400cdfa'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["TestByContext method", "TestByContext method, PS_DnsServer class", "PS_DnsServer class, TestByContext method"]
topic_type:
- apiref
api_name:
- PS_DnsServer.TestByContext
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# TestByContext method of the PS\_DnsServer class

Tests that the computers with the addresses that you specify are functioning DNS servers.

## Syntax


```mof
uint32 TestByContext(
  [in]  string            IPAddress[],
  [in]  string            ComputerName,
  [in]  string            Context,
  [out] DnsServerValidity cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

IP address of DNS server.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*Context* \[in\]
</dt> <dd>

Details of functionality to be tested.

<dl><span id="DnsServer"></span><span id="dnsserver"></span><span id="DNSSERVER"></span><dt>

**DnsServer**
</dt><span id="Forwarder"></span><span id="forwarder"></span><span id="FORWARDER"></span><dt>

**Forwarder**
</dt><span id="RootHints"></span><span id="roothints"></span><span id="ROOTHINTS"></span><dt>

**RootHints**
</dt> </dl> </dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerValidity**](dnsservervalidity.md) class.

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

 

 





