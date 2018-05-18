---
title: AddByType method of the PS\_DnsServerDirectoryPartition class
description: Create a DNS application directory partition.
audience: developer
ms.assetid: 'd1a2797d-4874-4890-a14a-40d0d47708a8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByType method", "AddByType method, PS_DnsServerDirectoryPartition class", "PS_DnsServerDirectoryPartition class, AddByType method"]
topic_type:
- apiref
api_name:
- PS_DnsServerDirectoryPartition.AddByType
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByType method of the PS\_DnsServerDirectoryPartition class

Create a DNS application directory partition.

## Syntax


```mof
uint32 AddByType(
  [in]  string                      ComputerName,
  [in]  string                      Type,
  [in]  boolean                     PassThru,
  [out] DnsServerDirectoryPartition cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a remote DNS server. The acceptable values for this parameter are: an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Specifies a type of DNS application directory partition. Valid values are Domain and Forest.

To create a default domain-wide DNS application directory partition for the Active Directory domain where the specified DNS server is located, specify Domain. To create a default forest-wide DNS application directory partition for the Active Directory forest where the specified DNS server is located, specify Forest. The ComputerName parameter is ignored for AllDomains DNS application directory partition. The computer from where you run this command must be joined to a domain in the forest where you want to create all of the default domain-wide application directory partitions.

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDirectoryPartition**](ps-dnsserverdirectorypartition.md)
</dt> </dl>

 

 





