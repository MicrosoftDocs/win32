---
title: MSFT\_StorageNodeToVolume class
description: Association between MSFT\_StorageNode and MSFT\_Volume.
ms.assetid: '7C19ED8C-34E7-409D-AF09-62C1FE49D7D7'
keywords: ["MSFT_StorageNodeToVolume class Windows Storage Management API", "MSFT_StorageNodeToVolume class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageNodeToVolume
- MSFT_StorageNodeToVolume.StorageNode
- MSFT_StorageNodeToVolume.Volume
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageNodeToVolume class

Association between [**MSFT\_StorageNode**](msft-storagenode.md) and [**MSFT\_Volume**](msft-volume.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToVolume
{
  MSFT_StorageNode REF StorageNode;
  MSFT_Volume      REF Volume;
};
```

## Members

The **MSFT\_StorageNodeToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToVolume** class has these properties.

<dl> <dt>

**StorageNode**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_Volume**](msft-volume.md)**
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

[**MSFT\_StorageNode**](msft-storagenode.md)
</dt> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





