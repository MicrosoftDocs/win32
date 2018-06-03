---
title: GetByName method of the PS\_DnsServerDirectoryPartition class
description: Retrieve DNS server directory partition.
audience: developer
ms.assetid: 51515d2a-7cbb-483f-8d2b-9fd8d8544b8d
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByName method
- GetByName method, PS_DnsServerDirectoryPartition class
- PS_DnsServerDirectoryPartition class, GetByName method
topic_type:
- apiref
api_name:
- PS_DnsServerDirectoryPartition.GetByName
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByName method of the PS\_DnsServerDirectoryPartition class

Retrieve DNS server directory partition.

## Syntax


```mof
uint32 GetByName(
  [in]  string                      Name,
  [in]  string                      ComputerName,
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
| Header<br/>                   | <dl> <dt>Wmp.h</dt> </dl>                   |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDirectoryPartition**](ps-dnsserverdirectorypartition.md)
</dt> </dl>

 

 





