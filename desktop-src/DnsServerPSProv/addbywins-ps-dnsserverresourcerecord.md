---
title: AddByWins method of the PS\_DnsServerResourceRecord class
description: Adds the record to a specified zone in a DNS server.
audience: developer
ms.assetid: 39e9e807-9f20-4808-ae1c-7e3878e08527
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByWins method
- AddByWins method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, AddByWins method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByWins
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByWins method of the PS\_DnsServerResourceRecord class

Adds the record to a specified zone in a DNS server.

## Syntax


```mof
uint32 AddByWins(
  [in]  datetime                LookupTimeout,
  [in]  boolean                 Replicate,
  [in]  string                  WinsServers[],
  [in]  string                  ZoneName,
  [in]  string                  ComputerName,
  [in]  datetime                CacheTimeout,
  [in]  boolean                 PassThru,
  [in]  boolean                 Force,
  [in]  boolean                 Wins,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*LookupTimeout* \[in\]
</dt> <dd>

Specifies the lookup time-out value for a resource record.

</dd> <dt>

*Replicate* \[in\]
</dt> <dd>

WINS flag to allow or disallow replication

</dd> <dt>

*WinsServers* \[in\]
</dt> <dd>

Specifies one or more IP addresses of WINS servers that you want to use for a resource record.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name of the DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*CacheTimeout* \[in\]
</dt> <dd>

// Time, in seconds, that a DNS Server using WINS Look up may cache the WINS server's response.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Adds a resource record without prompting you for confirmation. By default, the method prompts you for confirmation before it proceeds.

</dd> <dt>

*Wins* \[in\]
</dt> <dd>

IF specified, creates a WINS DNS Server resource record.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is unavailable prior to Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerResourceRecord**](ps-dnsserverresourcerecord.md)
</dt> </dl>

 

 





