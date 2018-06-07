---
title: HBA\_ScsiId structure
description: The HBA\_ScsiId structure contains information used by the operating system to identify a SCSI logical unit.
ms.assetid: c2acb40c-cb6e-45b4-b0be-911f6b37094e
keywords:
- HBA_ScsiId structure Storage Devices
- HBA_SCSIID structure Storage Devices
- PHBA_SCSIID structure pointer Storage Devices
topic_type:
- apiref
api_name:
- HBA_SCSIID
api_location:
- hbaapi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# HBA\_ScsiId structure

The HBA\_ScsiId structure contains information used by the operating system to identify a SCSI logical unit.

## Syntax


```C++
typedef struct HBA_ScsiId {
  char       OSDeviceName[256];
  HBA_UINT32 ScsiBusNumber;
  HBA_UINT32 ScsiTargetNumber;
  HBA_UINT32 ScsiOSLun;
} HBA_SCSIID, *PHBA_SCSIID;
```



## Members

<dl> <dt>

**OSDeviceName**
</dt> <dd>

Contains a name assigned to the device by the operating system. For example: "\\device\\ScsiPort3."

</dd> <dt>

**ScsiBusNumber**
</dt> <dd>

Contains the number assigned by the operating system to SCSI bus that the device is on.

</dd> <dt>

**ScsiTargetNumber**
</dt> <dd>

Contains the target ID number assigned by the operating system to the target device.

</dd> <dt>

**ScsiOSLun**
</dt> <dd>

Contains the logical unit number assigned by the operating system to the logical unit.

</dd> </dl>

## Remarks

For a detailed discussion of how the data assigned to members of this structure should be formatted, see the T11 committee's *Fibre Channel HBA API* specification.

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_GetFCPStatistics**](hba-getfcpstatistics.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_ScsiId%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






