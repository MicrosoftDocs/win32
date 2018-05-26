---
title: ScsiReportLuns\_IN structure
description: The ScsiReportLuns\_IN structure is used to deliver input parameter data to the ScsiReportLuns WMI method.
ms.assetid: 6de38cf4-a543-4cc9-aa6f-1804fc858040
keywords:
- ScsiReportLuns_IN structure Storage Devices
- PScsiReportLuns_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ScsiReportLuns_IN
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ScsiReportLuns\_IN structure

The ScsiReportLuns\_IN structure is used to deliver input parameter data to the [**ScsiReportLuns**](https://msdn.microsoft.com/library/windows/hardware/ff564911) WMI method.

## Syntax


```C++
typedef struct _ScsiReportLuns_IN {
  UCHAR     Cdb[12];
  UCHAR     HbaPortWWN[8];
  UCHAR     DiscoveredPortWWN[8];
  ULONGLONG FcLun;
} ScsiReportLuns_IN, *PScsiReportLuns_IN;
```



## Members

<dl> <dt>

**Cdb**
</dt> <dd>

Contains the command descriptor block that holds the SCSI report LUNs command to be sent to the target device.

</dd> <dt>

**HbaPortWWN**
</dt> <dd>

Contains a worldwise name for the HBA through which the target is accessed.

</dd> <dt>

**DiscoveredPortWWN**
</dt> <dd>

Contains a worldwide name for the port through which the target device is accessed.

</dd> <dt>

**FcLun**
</dt> <dd>

Indicates the logical unit number of the logical unit that will receive the SCSI report luns command.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the ScsiReportLuns\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ScsiReportLuns**](https://msdn.microsoft.com/library/windows/hardware/ff564911)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiReportLuns_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






