---
title: GetByCustom method of the PS\_DnsServerDirectoryPartition class
description: Retrieve DNS server directory partition.
audience: developer
ms.assetid: '8755335b-16d8-42e2-9212-2f99776304c8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByCustom method", "GetByCustom method, PS_DnsServerDirectoryPartition class", "PS_DnsServerDirectoryPartition class, GetByCustom method"]
topic_type:
- apiref
api_name:
- PS_DnsServerDirectoryPartition.GetByCustom
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# GetByCustom method of the PS\_DnsServerDirectoryPartition class

Retrieve DNS server directory partition.

## Syntax


```mof
uint32 GetByCustom(
  [in]  boolean                     Custom,
  [in]  string                      ComputerName,
  [out] DnsServerDirectoryPartition cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Custom* \[in\]
</dt> <dd>

Retrieves custom directory partitions.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a list of [**DnsServerDirectoryPartition**](dnsserverdirectorypartition.md) classes.

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

[**PS\_DnsServerDirectoryPartition**](ps-dnsserverdirectorypartition.md)
</dt> </dl>

 

 





