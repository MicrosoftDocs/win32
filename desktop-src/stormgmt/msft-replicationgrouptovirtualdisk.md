---
title: MSFT\_ReplicationGroupToVirtualDisk class
description: Association between an MSFT\_ReplicationGroup and its MSFT\_VirtualDisk objects.
ms.assetid: '21D7BD95-14EC-4869-80A9-50238B32BC27'
keywords: ["MSFT_ReplicationGroupToVirtualDisk class Windows Storage Management API", "MSFT_ReplicationGroupToVirtualDisk class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroupToVirtualDisk
- MSFT_ReplicationGroupToVirtualDisk.ReplicationGroup
- MSFT_ReplicationGroupToVirtualDisk.VirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_ReplicationGroupToVirtualDisk class

Association between an [**MSFT\_ReplicationGroup**](msft-replicationgroup.md) and its [**MSFT\_VirtualDisk**](msft-virtualdisk.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_ReplicationGroupToVirtualDisk
{
  MSFT_ReplicationGroup REF ReplicationGroup;
  MSFT_VirtualDisk      REF VirtualDisk;
};
```

## Members

The **MSFT\_ReplicationGroupToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ReplicationGroupToVirtualDisk** class has these properties.

<dl> <dt>

**ReplicationGroup**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**VirtualDisk**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_VirtualDisk**](msft-virtualdisk.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
</dt> <dt>

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





