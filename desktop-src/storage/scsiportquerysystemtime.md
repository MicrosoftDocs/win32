---
title: ScsiPortQuerySystemTime routine
description: The ScsiPortQuerySystemTime routine obtains the current system time.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: '6f6afe6d-8f57-4c08-97ea-b327622a4e39'
keywords: ["ScsiPortQuerySystemTime routine Storage Devices"]
topic_type:
- apiref
api_name:
- ScsiPortQuerySystemTime
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
---

# ScsiPortQuerySystemTime routine

The **ScsiPortQuerySystemTime** routine obtains the current system time.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiPortQuerySystemTime(
  _Out_ PLARGE_INTEGER CurrentTime
);
```



## Parameters

<dl> <dt>

*CurrentTime* \[out\]
</dt> <dd>

Pointer to the current time, on return.

</dd> </dl>

## Return value

None

## Remarks

The system time returned in *CurrentTime* is the number of 100-nanosecond intervals that have elapsed since January 1, 1601. System time is typically updated approximately every ten milliseconds. This value is computed for the GMT time zone.

## Requirements



|                            |                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>      |
| Header<br/>          | <dl> <dt>Srb.h</dt> </dl>        |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl> |
| IRQL<br/>            | Any level<br/>                                                                    |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortQuerySystemTime%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





