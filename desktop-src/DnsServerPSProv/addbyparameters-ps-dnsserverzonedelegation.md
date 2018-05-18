---
title: AddByParameters method of the PS\_DnsServerZoneDelegation class
description: Adds a new delegated DNS zone to an existing zone.
audience: developer
ms.assetid: '0fc49553-ad09-4330-8bf8-e430ec0d758c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByParameters method", "AddByParameters method, PS_DnsServerZoneDelegation class", "PS_DnsServerZoneDelegation class, AddByParameters method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneDelegation.AddByParameters
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByParameters method of the PS\_DnsServerZoneDelegation class

Adds a new delegated DNS zone to an existing zone.

## Syntax


```mof
uint32 AddByParameters(
  [in]  string                  ChildZoneName,
  [in]  string                  IPAddress[],
  [in]  string                  NameServer,
  [in]  string                  ComputerName,
  [in]  string                  Name,
  [in]  string                  VirtualizationInstance,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [out] DnsServerZoneDelegation cmdletOutput
);
```



## Parameters

<dl> <dt>

*ChildZoneName* \[in\]
</dt> <dd>

Specifies the name of the child zone.

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

Specifies an array of IP addresses for DNS servers for the child zone.

</dd> <dt>

*NameServer* \[in\]
</dt> <dd>

Specifies the name of the DNS server that hosts the child zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the parent zone. The child zone will be part of this zone.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is unavailable prior to Windows Server 2016.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerZoneDelegation**](dnsserverzonedelegation.md) class.

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

[**PS\_DnsServerZoneDelegation**](ps-dnsserverzonedelegation.md)
</dt> </dl>

 

 





