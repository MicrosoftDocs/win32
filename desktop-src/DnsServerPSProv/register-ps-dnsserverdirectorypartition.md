---
title: Register method of the PS\_DnsServerDirectoryPartition class
description: Adds the DNS server to the specified directory partition\\'s replica set.
audience: developer
ms.assetid: 5b09af98-571c-4702-bb66-8665eb9487bc
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Register method
- Register method, PS_DnsServerDirectoryPartition class
- PS_DnsServerDirectoryPartition class, Register method
topic_type:
- apiref
api_name:
- PS_DnsServerDirectoryPartition.Register
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Register method of the PS\_DnsServerDirectoryPartition class

Adds the DNS server to the specified directory partition\\'s replica set. This operation allows application directory partitions to be added to from the Application Directory Partition Table, and also allows the DNS server to be directed to add itself from the replication scope of an existing application directory partition.

## Syntax


```mof
uint32 Register(
  [in]  string                      ComputerName,
  [in]  boolean                     PassThru,
  [in]  string                      Name,
  [out] DnsServerDirectoryPartition cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The fully qualified domain name of the DNS application directory partition that will be created.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded instance of the current object. This parameter returns a value only if *PassThru* is set to **true**.

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

[**PS\_DnsServerDirectoryPartition**](ps-dnsserverdirectorypartition.md)
</dt> </dl>

 

 





