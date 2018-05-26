---
title: MSiSCSI\_LUNMappingInformation structure
description: This MSiSCSI\_LUNMappingInformation structure provides the SCSI address information that the operating system assigns to a particular logical unit.
ms.assetid: abe4b0fe-3918-4139-9c35-d9399287ce03
keywords:
- MSiSCSI_LUNMappingInformation structure Storage Devices
- PMSiSCSI_LUNMappingInformation structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_LUNMappingInformation
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

# MSiSCSI\_LUNMappingInformation structure

This MSiSCSI\_LUNMappingInformation structure provides the SCSI address information that the operating system assigns to a particular logical unit.

## Syntax


```C++
typedef struct _MSiSCSI_LUNMappingInformation {
  ULONGLONG UniqueAdapterId;
  ULONGLONG UniqueSessionId;
  ULONG     OSBus;
  ULONG     OSTarget;
  ULONG     OSLUN;
} MSiSCSI_LUNMappingInformation, *PMSiSCSI_LUNMappingInformation;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID). The initiator reports this value in the **UniqueAdapterId** member of the [**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md) structure.

</dd> <dt>

**UniqueSessionId**
</dt> <dd>

A session ID that uniquely identifies the session for which the LUN mapping is valid. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in the *UniqueSessionId* parameter. Do not confuse this value with the values in the ISID and TSID members.

</dd> <dt>

**OSBus**
</dt> <dd>

The number that the operating system assigns to the bus that the adapter is attached to.

</dd> <dt>

**OSTarget**
</dt> <dd>

The device number that the operating system assigns to the target.

</dd> <dt>

**OSLUN**
</dt> <dd>

The logical unit number (LUN) that the operating system assigns to the logical unit.

</dd> </dl>

## Remarks

You must implement this class.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> <dt>

[**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md)
</dt> <dt>

[MSiSCSI\_LUNMappingInformation WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563067)
</dt> <dt>

[**MSiSCSI\_TargetMappings**](msiscsi-targetmappings.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_LUNMappingInformation%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






