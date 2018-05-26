---
title: MSiSCSI\_TargetMappings structure
description: The MSiSCSI\_TargetMappings structure contains a set of logical unit number (LUN) mappings that are associated with an initiator instance.
ms.assetid: 6bddeaeb-9913-4c90-b8ac-3a9f7b384b80
keywords:
- MSiSCSI_TargetMappings structure Storage Devices
- PMSiSCSI_TargetMappings structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_TargetMappings
api_location:
- iscsiop.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSiSCSI\_TargetMappings structure

The MSiSCSI\_TargetMappings structure contains a set of logical unit number (LUN) mappings that are associated with an initiator instance.

## Syntax


```C++
typedef struct _MSiSCSI_TargetMappings {
  ULONGLONG           UniqueAdapterId;
  ULONG               TargetMappingCount;
  ULONG               Reserved;
  ISCSI_TargetMapping TargetMappings[1];
} MSiSCSI_TargetMappings, *PMSiSCSI_TargetMappings;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID). The initiator reports this value in the **UniqueAdapterId** member of the [**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md) structure.

</dd> <dt>

**TargetMappingCount**
</dt> <dd>

The number of mappings in the **TargetMappings** member.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for Microsoft use only.

</dd> <dt>

**TargetMappings**
</dt> <dd>

A variable-length array of [**ISCSI\_TargetMapping**](iscsi-targetmapping.md) structures, each of which provides a list of LUN mappings that are associated with a particular iSCSI session that is associated with the adapter ID.

</dd> </dl>

## Remarks

You must implement this class.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_TargetMapping**](iscsi-targetmapping.md)
</dt> <dt>

[**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md)
</dt> <dt>

[MSiSCSI\_TargetMappings WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563147)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_TargetMappings%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






