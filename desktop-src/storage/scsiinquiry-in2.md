---
title: ScsiInquiry\_IN structure
description: The ScsiInquiry\_IN structure is used by a miniport driver to deliver input parameter data to the ScsiInquiry WMI method.
ms.assetid: 'f7690483-8269-4fb4-9960-9abdbb128b94'
keywords: ["ScsiInquiry_IN structure Storage Devices", "PScsiInquiry_IN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ScsiInquiry_IN
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
---

# ScsiInquiry\_IN structure

The ScsiInquiry\_IN structure is used by a miniport driver to deliver input parameter data to the [**ScsiInquiry**](https://msdn.microsoft.com/library/windows/hardware/ff564585) WMI method.

## Syntax


```C++
typedef struct _ScsiInquiry_IN {
  UCHAR     Cdb[6];
  UCHAR     HbaPortWWN[8];
  UCHAR     DiscoveredPortWWN[8];
  ULONGLONG FcLun;
} ScsiInquiry_IN, *PScsiInquiry_IN;
```



## Members

<dl> <dt>

**Cdb**
</dt> <dd>

Contains the command descriptor block that holds the SCSI inquiry command to be sent to the target device.

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

Indicates the logical unit number of the logical unit that will receive the SCSI inquiry command.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the ScsiInquiry\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ScsiInquiry**](https://msdn.microsoft.com/library/windows/hardware/ff564585)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiInquiry_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






