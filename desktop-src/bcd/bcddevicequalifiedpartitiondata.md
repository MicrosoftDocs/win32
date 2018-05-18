---
title: BcdDeviceQualifiedPartitionData class
description: Represents a qualified partition device element.
ms.assetid: '34140ed4-df47-4da7-8302-d6f93839452a'
keywords: ["BcdDeviceQualifiedPartitionData class Boot Config", "BcdDeviceQualifiedPartitionData class Boot Config , described"]
topic_type:
- apiref
api_name:
- BcdDeviceQualifiedPartitionData
- BcdDeviceQualifiedPartitionData.PartitionStyle
- BcdDeviceQualifiedPartitionData.DiskSignature
- BcdDeviceQualifiedPartitionData.PartitionIdentifier
api_location:
- Root\WMI
api_type:
- Schema
---

# BcdDeviceQualifiedPartitionData class

Represents a qualified partition device element.

## Syntax

``` syntax
class BcdDeviceQualifiedPartitionData : BcdDeviceData
{
  uint32 PartitionStyle;
  string DiskSignature;
  string PartitionIdentifier;
};
```

## Members

The **BcdDeviceQualifiedPartitionData** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdDeviceQualifiedPartitionData** class has these properties.

<dl> <dt>

**DiskSignature**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the **PartitionStyle** property is a GUID partition table (GPT), the **DiskSignature** property is the disk signature as a GUID in string format (for example, "{7c69a706-eda5-11dd-bc09-001e4ce28b8f}"). If the **PartitionStyle** property is a master boot record (MBR), the **DiskSignature** property is the decimal MBR disk signature in string format (for example, "402653184" for 0x18000000).

</dd> <dt>

**PartitionIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the **PartitionStyle** property is GPT, the **PartitionIdentifier** property is the partition signature as a GUID in string format (for example, "{6efb52bf-1766-41db-a6b3-0ee5eff72bd7}" ). If the **PartitionStyle** property is MBR, the **PartitionIdentifier** property is the decimal MBR partition offset in string format (for example, "82837504" for 0x4F00000).

</dd> <dt>

**PartitionStyle**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The partition style. This property can be one of the following values.



| Value                                                                                                                                                                                 | Meaning                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <span id="GPT"></span><span id="gpt"></span><dl> <dt>**GPT**</dt> <dt>1</dt> </dl> | The partition is described in a GPT.<br/>  |
| <span id="MBR"></span><span id="mbr"></span><dl> <dt>**MBR**</dt> <dt>0</dt> </dl> | The partition is described in an MBR.<br/> |



 

</dd> </dl>

## Remarks

The **BcdDeviceQualifiedPartitionData** class uniquely identifies a boot partition by its partition style, disk signature, and partition identifier. An application can enumerate a qualified partition by using the [**GetElementWithFlags**](getelementwithflags-bcdobject.md) method of the [**BcdObject**](bcdobject.md) class with *Flags* parameter set to Qualified (1).

To set a qualified partition device, use the [**SetQualifiedPartitionDeviceElement**](setqualifiedpartitiondeviceelement-bcdobject.md) method of the [**BcdObject**](bcdobject.md) class and specify a partition style, disk signature, and partition identifier.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**GetElementWithFlags**](getelementwithflags-bcdobject.md)
</dt> <dt>

[**SetQualifiedPartitionDeviceElement**](setqualifiedpartitiondeviceelement-bcdobject.md)
</dt> </dl>

 

 





