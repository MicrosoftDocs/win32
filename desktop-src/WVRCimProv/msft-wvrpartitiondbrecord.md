---
title: MSFT\_WvrPartitionDbRecord class
description: This class represents an entry in the Storage Replica partition database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d78e0955-2cce-43a9-bb47-b32273c0269c
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WvrPartitionDbRecord class
- MSFT_WvrPartitionDbRecord class, described
topic_type:
- apiref
api_name:
- MSFT_WvrPartitionDbRecord
- MSFT_WvrPartitionDbRecord.DiskGuid
- MSFT_WvrPartitionDbRecord.PartitionGuid
- MSFT_WvrPartitionDbRecord.GroupId
api_location:
- wvrcimprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_WvrPartitionDbRecord class

This class represents an entry in the Storage Replica partition database.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("wvrcimprov"), AMENDMENT]
class MSFT_WvrPartitionDbRecord
{
  string DiskGuid;
  string PartitionGuid;
  string GroupId;
};
```

## Members

The **MSFT\_WvrPartitionDbRecord** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WvrPartitionDbRecord** class has these properties.

<dl> <dt>

**DiskGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

GUID for the disk.

</dd> <dt>

**GroupId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ID of the replication group.

</dd> <dt>

**PartitionGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

GUID for the partition.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



 

 





