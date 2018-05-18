---
title: DnsServerDirectoryPartition class
description: Represents an application directory partition on a DNS server.
audience: developer
ms.assetid: '249220cc-aaf3-43be-8113-2513ea433216'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerDirectoryPartition class", "DnsServerDirectoryPartition class, described"]
topic_type:
- apiref
api_name:
- DnsServerDirectoryPartition
- DnsServerDirectoryPartition.DirectoryPartitionName
- DnsServerDirectoryPartition.DirectoryPartitionDistinguishedName
- DnsServerDirectoryPartition.CrossReferenceDistinguishedName
- DnsServerDirectoryPartition.Flags
- DnsServerDirectoryPartition.ZoneCount
- DnsServerDirectoryPartition.State
- DnsServerDirectoryPartition.Replica
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerDirectoryPartition class

Represents an application directory partition on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerDirectoryPartition
{
  string DirectoryPartitionName;
  string DirectoryPartitionDistinguishedName;
  string CrossReferenceDistinguishedName;
  string Flags;
  uint32 ZoneCount;
  uint32 State;
  string Replica[];
};
```

## Members

The **DnsServerDirectoryPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerDirectoryPartition** class has these properties.

<dl> <dt>

**CrossReferenceDistinguishedName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cross reference distinguished name of the directory partition.

</dd> <dt>

**DirectoryPartitionDistinguishedName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The distinguished name of the directory partition.

</dd> <dt>

**DirectoryPartitionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fully qualified domain name of the directory partition.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The properties of the directory partition.

</dd> <dt>

**Replica**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An arrays that contains information about each replica for the directory partition.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the directory partition.

</dd> <dt>

**ZoneCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zones from the directory partition that are loaded into memory of the DNS server.

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

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





