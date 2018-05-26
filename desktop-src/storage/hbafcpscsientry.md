---
title: HBAFCPScsiEntry structure
description: The HBAFCPScsiEntry structure is used with GetFcpTargetMapping method of the MSFC\_HBAFCPInfo WMI Class to define a binding between the operating system information that uniquely identifies a logical unit and the fibre channel protocol (FCP) identifier that identifies the logical unit.
ms.assetid: 718431f9-e4cc-4e79-84d3-a59f5399e711
keywords:
- HBAFCPScsiEntry structure Storage Devices
- PHBAFCPScsiEntry structure pointer Storage Devices
topic_type:
- apiref
api_name:
- HBAFCPScsiEntry
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HBAFCPScsiEntry structure

The HBAFCPScsiEntry structure is used with [**GetFcpTargetMapping**](https://msdn.microsoft.com/library/windows/hardware/ff554948) method of the [MSFC\_HBAFCPInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562509) to define a binding between the operating system information that uniquely identifies a logical unit and the fibre channel protocol (FCP) identifier that identifies the logical unit.

## Syntax


```C++
typedef struct _HBAFCPScsiEntry {
  HBAFCPID  FCPId;
  UCHAR     Luid[256];
  HBAScsiID ScsiId;
} HBAFCPScsiEntry, *PHBAFCPScsiEntry;
```



## Members

<dl> <dt>

**FCPId**
</dt> <dd>

Contains a structure of type [**HBAFCPID**](hbafcpid.md) that contains the FCP identifier for the logical unit and information about the port to be queried for information about the device.

</dd> <dt>

**Luid**
</dt> <dd>

Contains the logical unit descriptor for the device that the operating system derives from SCSI inquiry data.

</dd> <dt>

**ScsiId**
</dt> <dd>

Contains a structure of type [**HBAScsiID**](hbascsiid.md) that contains the information that uniquely identifies a logical unit for the operating system.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetFcpTargetMapping**](https://msdn.microsoft.com/library/windows/hardware/ff554948)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBAFCPScsiEntry%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






