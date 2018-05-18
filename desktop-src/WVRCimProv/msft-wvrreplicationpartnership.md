---
title: MSFT\_WvrReplicationPartnership class
description: Represents an association between a source replication group and a partner destination replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '07fdd832-5b6e-4f05-8739-d502fd538654'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WvrReplicationPartnership class", "MSFT_WvrReplicationPartnership class, described"]
topic_type:
- apiref
api_name:
- MSFT_WvrReplicationPartnership
- MSFT_WvrReplicationPartnership.SourceRGName
- MSFT_WvrReplicationPartnership.DestinationRGName
- MSFT_WvrReplicationPartnership.SourceComputerName
- MSFT_WvrReplicationPartnership.DestinationComputerName
- MSFT_WvrReplicationPartnership.Id
api_location:
- WvrCimProv.dll
api_type:
- DllExport
---

# MSFT\_WvrReplicationPartnership class

Represents an association between a source replication group and a partner destination replication group.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("wvrcimprov"), AMENDMENT]
class MSFT_WvrReplicationPartnership
{
  string SourceRGName;
  string DestinationRGName;
  string SourceComputerName;
  string DestinationComputerName;
  string Id;
};
```

## Members

The **MSFT\_WvrReplicationPartnership** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WvrReplicationPartnership** class has these properties.

<dl> <dt>

**DestinationComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The FQDN or NetBIOS name of the computer hosting the destination replication group.

</dd> <dt>

**DestinationRGName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The destination replication group within this partnership.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ID for the partnership.

</dd> <dt>

**SourceComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The fully qualified domain name (FQDN) or NetBIOS name of the computer hosting the source replication group.

</dd> <dt>

**SourceRGName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The source replication group within this partnership.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrReplicationGroup**](msft-wvrreplicationgroup.md)
</dt> </dl>

 

 





