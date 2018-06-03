---
title: PS\_DnsServerDirectoryPartition class
description: DNS Server Directory Partition definition.
audience: developer
ms.assetid: 249220cc-aaf3-43be-8113-2513ea433216
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerDirectoryPartition class
- PS_DnsServerDirectoryPartition class, described
topic_type:
- apiref
api_name:
- PS_DnsServerDirectoryPartition
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerDirectoryPartition class

DNS Server Directory Partition definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerDirectoryPartition
{
};
```

## Members

The **PS\_DnsServerDirectoryPartition** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerDirectoryPartition** class has these methods.



| Method                                                            | Description                                                                                                                                                                                                                                                                                                                                     |
|:------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddByName**](addbyname-ps-dnsserverdirectorypartition.md)     | Create a DNS application directory partition.<br/>                                                                                                                                                                                                                                                                                        |
| [**AddByType**](addbytype-ps-dnsserverdirectorypartition.md)     | Create a DNS application directory partition.<br/>                                                                                                                                                                                                                                                                                        |
| [**GetByCustom**](getbycustom-ps-dnsserverdirectorypartition.md) | Retrieve DNS server directory partition.<br/>                                                                                                                                                                                                                                                                                             |
| [**GetByName**](getbyname-ps-dnsserverdirectorypartition.md)     | Retrieve DNS server directory partition.<br/>                                                                                                                                                                                                                                                                                             |
| [**Register**](register-ps-dnsserverdirectorypartition.md)       | Adds the DNS server to the specified directory partition's replica set. This operation allows application directory partitions to be added to from the Application Directory Partition Table, and also allows the DNS server to be directed to add itself from the replication scope of an existing application directory partition.<br/> |
| [**Remove**](remove-ps-dnsserverdirectorypartition.md)           | Remove a directory partition.<br/>                                                                                                                                                                                                                                                                                                        |
| [**Unregister**](unregister-ps-dnsserverdirectorypartition.md)   | Un Enlist a server from Directory partition. This operation allows application directory partitions to be deleted from the Application Directory Partition Table, and also allows the DNS server to be directed to remove itself from the replication scope of an existing application directory partition.<br/>                          |



 

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

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





