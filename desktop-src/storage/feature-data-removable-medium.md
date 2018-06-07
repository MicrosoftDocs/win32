---
title: FEATURE\_DATA\_REMOVABLE\_MEDIUM structure
description: The FEATURE\_DATA\_REMOVABLE\_MEDIUM structure contains data for the removable medium feature.
ms.assetid: b25feb68-75bb-4a9d-b842-e15f619a18c4
keywords:
- FEATURE_DATA_REMOVABLE_MEDIUM structure Storage Devices
- PFEATURE_DATA_REMOVABLE_MEDIUM structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_REMOVABLE_MEDIUM
api_location:
- ntddmmc.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# FEATURE\_DATA\_REMOVABLE\_MEDIUM structure

The FEATURE\_DATA\_REMOVABLE\_MEDIUM structure contains data for the removable medium feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_REMOVABLE_MEDIUM {
  FEATURE_HEADER Header;
  UCHAR          Lockable  :1;
  UCHAR          Reserved1  :1;
  UCHAR          DefaultToPrevent  :1;
  UCHAR          Eject  :1;
  UCHAR          Reserved2  :1;
  UCHAR          LoadingMechanism  :3;
  UCHAR          Reserved3[3];
} FEATURE_DATA_REMOVABLE_MEDIUM, *PFEATURE_DATA_REMOVABLE_MEDIUM;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**Lockable**
</dt> <dd>

Indicates, when set to 1, that the initiator can lock the medium into the device. When set to zero, this bit indicates that the medium cannot be locked into the device.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**DefaultToPrevent**
</dt> <dd>

Indicates, when set to zero, that the prevent jumper is present. This overrides the lock command, so that locking the device shall not prevent the insertion of media.

</dd> <dt>

**Eject**
</dt> <dd>

Indicates, when set to 1, that the device can eject the medium or magazine. When set to zero, this bit indicates that the device cannot eject the medium or magazine by means of the normal start/stop command sequence.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**LoadingMechanism**
</dt> <dd>

Indicates the type of loading mechanism. See the *SCSI Multimedia - 4 (MMC-4)* specification for the list of values that this member can take.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

This structure holds data for the feature named "Removable Medium" by the *MMC-3* specification. Devices that support this feature allow the medium to be removed from the device. They also can communicate to the initiator that the user wants to eject the medium or has inserted a new medium.

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> <dt>

[**FEATURE\_NUMBER**](feature-number.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_REMOVABLE_MEDIUM%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






