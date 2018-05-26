---
title: AddByAfsdb method of the PS\_DnsServerResourceRecord class
description: Adds an Andrew File System cell database server (AFSDB) resource record type in the specified zone.
audience: developer
ms.assetid: 60744275-18c5-4177-aa46-68fccd11bb5c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByAfsdb method
- AddByAfsdb method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, AddByAfsdb method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByAfsdb
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByAfsdb method of the PS\_DnsServerResourceRecord class

Adds an Andrew File System cell database server (AFSDB) resource record type in the specified zone.

## Syntax


```mof
uint32 AddByAfsdb(
  [in]  uint16                  SubType,
  [in]  string                  ZoneName,
  [in]  string                  ServerName,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 Afsdb,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*SubType* \[in\]
</dt> <dd>

Specifies whether the server is an AFS volume location server. Use a value of 1 indicate that the server is an AFS version 3.0 volume location server for the specified AFS cell. Use a value of 2 to indicate that the server is an authenticated name server that holds the cell-root directory node for the server that uses either Open Software Foundation's (OSF) DCE authenticated cell-naming system or HP/Apollo's Network Computing Architecture (NCA).

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the DNS zone.

</dd> <dt>

*ServerName* \[in\]
</dt> <dd>

Specifies the subtype of a host AFS server. For subtype 1 (value=1), the host has an AFS version 3.0 Volume Location Server for the named AFS cell. For subtype 2 (value=2), the host has an authenticated name server holding the cell-root directory node for the named DCE/NCA cell.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the Time to Live (TTL) value, in seconds, for a resource record. Other DNS servers use this length of time to determine how long to cache a record.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Indicates that any authenticated user can update a resource record that has the same owner name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of a DNS server resource record object.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

Indicates that the DNS server uses a time stamp for the resource record that this method adds. A DNS server can scavenge resource records that have become stale based on a time stamp.

</dd> <dt>

*Afsdb* \[in\]
</dt> <dd>

If specified, creates a DNS Server Resource Record AFSDB.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

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

 

 





