---
title: MSFT\_StorageSubSystemToReplicationCapabilities class
description: Association between an MSFT\_StorageSubSystem and MSFT\_ReplicationCapabilities.
ms.assetid: '73AC3F3F-645B-4D0C-AA7E-2CAAB47E27D8'
keywords: ["MSFT_StorageSubSystemToReplicationCapabilities class Windows Storage Management API", "MSFT_StorageSubSystemToReplicationCapabilities class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToReplicationCapabilities
- MSFT_StorageSubSystemToReplicationCapabilities.StorageSubSystem
- MSFT_StorageSubSystemToReplicationCapabilities.ReplicationCapabilities
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageSubSystemToReplicationCapabilities class

Association between an [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToReplicationCapabilities
{
  MSFT_StorageSubSystem        REF StorageSubSystem;
  MSFT_ReplicationCapabilities REF ReplicationCapabilities;
};
```

## Members

The **MSFT\_StorageSubSystemToReplicationCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToReplicationCapabilities** class has these properties.

<dl> <dt>

**ReplicationCapabilities**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
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

[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





