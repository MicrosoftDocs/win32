---
title: Unregister method of the PS\_DnsServerDirectoryPartition class
description: Remove a server from Directory partition.
audience: developer
ms.assetid: cc25f0c0-0a44-4502-a927-6a23c0dd095a
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Unregister method
- Unregister method, PS_DnsServerDirectoryPartition class
- PS_DnsServerDirectoryPartition class, Unregister method
topic_type:
- apiref
api_name:
- PS_DnsServerDirectoryPartition.Unregister
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Unregister method of the PS\_DnsServerDirectoryPartition class

Remove a server from Directory partition. This operation allows application directory partitions to be deleted from the Application Directory Partition Table, and also allows the DNS server to be directed to remove itself from the replication scope of an existing application directory partition.

## Syntax


```mof
uint32 Unregister(
  [in]  string                      ComputerName,
  [in]  boolean                     PassThru,
  [in]  string                      Name,
  [in]  boolean                     Force,
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

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The fully qualified domain name of the DNS application directory partition that will be created.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**true** to not require user confirmation before continuing with the operation; **false** to require user confirmation. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

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

 

 





