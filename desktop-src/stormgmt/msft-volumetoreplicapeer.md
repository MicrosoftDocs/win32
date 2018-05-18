---
title: MSFT\_VolumeToReplicaPeer class
description: Association between MSFT\_Volume and MSFT\_ReplicaPeer .
ms.assetid: 'FB7BF33C-21F1-4DAB-B45E-F2126ACC10BF'
keywords: ["MSFT_VolumeToReplicaPeer class Windows Storage Management API", "MSFT_VolumeToReplicaPeer class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_VolumeToReplicaPeer
- MSFT_VolumeToReplicaPeer.Volume
- MSFT_VolumeToReplicaPeer.FileShare
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_VolumeToReplicaPeer class

Association between [**MSFT\_Volume**](msft-volume.md) and [**MSFT\_ReplicaPeer**](msft-replicapeer.md) .

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_VolumeToReplicaPeer : MSFT_Synchronized
{
  MSFT_Volume      REF Volume;
  MSFT_ReplicaPeer REF FileShare;
};
```

## Members

The **MSFT\_VolumeToReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VolumeToReplicaPeer** class has these properties.

<dl> <dt>

**FileShare**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_ReplicaPeer**](msft-replicapeer.md)**
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

[**MSFT\_Synchronized**](wmi-meta_qualifie)
</dt> <dt>

[**MSFT\_ReplicaPeer**](msft-replicapeer.md)
</dt> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





