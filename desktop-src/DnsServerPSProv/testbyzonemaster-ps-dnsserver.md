---
title: TestByZoneMaster method of the PS\_DnsServer class
description: Tests that the computers with the specified addresses are functioning DNS servers.
audience: developer
ms.assetid: '9c339ee1-dd05-4a00-ab9f-70693d49b52b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["TestByZoneMaster method", "TestByZoneMaster method, PS_DnsServer class", "PS_DnsServer class, TestByZoneMaster method"]
topic_type:
- apiref
api_name:
- PS_DnsServer.TestByZoneMaster
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# TestByZoneMaster method of the PS\_DnsServer class

Tests that the computers with the specified addresses are functioning DNS servers.

## Syntax


```mof
uint32 TestByZoneMaster(
  [in]  string            IPAddress[],
  [in]  string            ComputerName,
  [in]  string            ZoneName,
  [out] DnsServerValidity cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

IP address of DNS server

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

If specified, validates if the server hosts the specified zone.

</dd> <dt>

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

 

 





