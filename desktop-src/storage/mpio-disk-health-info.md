---
title: MPIO\_DISK\_HEALTH\_INFO structure
description: The MPIO\_DISK\_HEALTH\_INFO structure is used to query the available health information for every multi-path disk in the system.
ms.assetid: '20813e29-907f-42b0-9229-a9ef78f46e1d'
keywords: ["MPIO_DISK_HEALTH_INFO structure Storage Devices", "PMPIO_DISK_HEALTH_INFO structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MPIO_DISK_HEALTH_INFO
api_location:
- mpiowmi.h
api_type:
- HeaderDef
---

# MPIO\_DISK\_HEALTH\_INFO structure

The MPIO\_DISK\_HEALTH\_INFO structure is used to query the available health information for every multi-path disk in the system.

## Syntax


```C++
typedef struct _MPIO_DISK_HEALTH_INFO {
  ULONG                  NumberDiskPackets;
  ULONG                  Reserved;
  MPIO_DISK_HEALTH_CLASS DiskHealthPackets[1];
} MPIO_DISK_HEALTH_INFO, *PMPIO_DISK_HEALTH_INFO;
```



## Members

<dl> <dt>

**NumberDiskPackets**
</dt> <dd>

An unsigned 32-bitfield that returns the number of available health packets that correspond to the number of multi-path disks under MPIO control.

</dd> <dt>

**Reserved**
</dt> <dd>

Should be zero.

</dd> <dt>

**DiskHealthPackets**
</dt> <dd>

An array of health information packets for all the available multi-path disks under MPIO control. The number of elements in the array is given by NumberDiskPackets, and each element of the array is an instance of an MPIO\_DISK\_HEALTH\_CLASS structure.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_DISK_HEALTH_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





