---
title: MSFT\_StorageSubSystemToMaskingSet class
description: Association between StorageSubSystem and MaskingSet.
ms.assetid: '38E7838B-E9CB-4FDF-9952-A4DB47F57FE0'
keywords: ["MSFT_StorageSubSystemToMaskingSet class Windows Storage Management API", "MSFT_StorageSubSystemToMaskingSet class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToMaskingSet
- MSFT_StorageSubSystemToMaskingSet.StorageSubSystem
- MSFT_StorageSubSystemToMaskingSet.MaskingSet
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageSubSystemToMaskingSet class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**MaskingSet**](msft-maskingset.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToMaskingSet
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_MaskingSet       REF MaskingSet;
};
```

## Members

The **MSFT\_StorageSubSystemToMaskingSet** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToMaskingSet** class has these properties.

<dl> <dt>

**MaskingSet**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_MaskingSet**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageSubSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MaskingSet**](msft-maskingset.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





