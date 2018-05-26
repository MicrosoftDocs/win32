---
title: MSFT\_PartitionToVolume class
description: Association between Partition and Volume.
ms.assetid: 739714d6-683a-468f-b404-cb78991383af
keywords:
- MSFT_PartitionToVolume class Windows Storage Management API
- MSFT_PartitionToVolume class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_PartitionToVolume
- MSFT_PartitionToVolume.Partition
- MSFT_PartitionToVolume.Volume
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_PartitionToVolume class

Association between [**Partition**](msft-partition.md) and [**Volume**](msft-volume.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_PartitionToVolume
{
  MSFT_Partition REF Partition;
  MSFT_Volume    REF Volume;
};
```

## Members

The **MSFT\_PartitionToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_PartitionToVolume** class has these properties.

<dl> <dt>

**Partition**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_Partition**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_Volume**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Partition**](msft-partition.md)
</dt> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





