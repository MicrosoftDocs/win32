---
title: MSFT\_StorageEnclosureToPhysicalDisk class
description: Association between StorageEnclosure and PhysicalDisk.
ms.assetid: 'B2FDB260-CD0D-4481-B002-572D58D0CF84'
keywords: ["MSFT_StorageEnclosureToPhysicalDisk class Windows Storage Management API", "MSFT_StorageEnclosureToPhysicalDisk class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageEnclosureToPhysicalDisk
- MSFT_StorageEnclosureToPhysicalDisk.StorageEnclosure
- MSFT_StorageEnclosureToPhysicalDisk.PhysicalDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageEnclosureToPhysicalDisk class

Association between [**StorageEnclosure**](msft-storageenclosure.md) and [**PhysicalDisk**](msft-physicaldisk.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageEnclosureToPhysicalDisk
{
  MSFT_StorageEnclosure REF StorageEnclosure;
  MSFT_PhysicalDisk     REF PhysicalDisk;
};
```

## Members

The **MSFT\_StorageEnclosureToPhysicalDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageEnclosureToPhysicalDisk** class has these properties.

<dl> <dt>

**PhysicalDisk**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

</dd> <dt>

**StorageEnclosure**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)
</dt> <dt>

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
</dt> </dl>

 

 





