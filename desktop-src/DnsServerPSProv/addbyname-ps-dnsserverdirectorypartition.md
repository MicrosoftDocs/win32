---
title: AddByName method of the PS\_DnsServerDirectoryPartition class
description: Create a DNS application directory partition.
audience: developer
ms.assetid: 249220cc-aaf3-43be-8113-2513ea433216
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByName method
- AddByName method, PS_DnsServerDirectoryPartition class
- PS_DnsServerDirectoryPartition class, AddByName method
topic_type:
- apiref
api_name:
- PS_DnsServerDirectoryPartition.AddByName
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByName method of the PS\_DnsServerDirectoryPartition class

Create a DNS application directory partition.

## Syntax


```mof
uint32 AddByName(
  [in]  string                      Name,
  [in]  string                      ComputerName,
  [in]  boolean                     PassThru,
  [out] DnsServerDirectoryPartition cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The fully qualified domain name of the DNS application directory partition that will be created.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerDirectoryPartition**](dnsserverdirectorypartition.md) class.

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

 

 





