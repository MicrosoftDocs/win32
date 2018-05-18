---
title: ScsiPortStallExecution routine
description: The ScsiPortStallExecution routine stalls in the miniport driver.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: '2b033cfe-9649-4993-b348-6c9af2d0f4bc'
keywords: ["ScsiPortStallExecution routine Storage Devices"]
topic_type:
- apiref
api_name:
- ScsiPortStallExecution
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
---

# ScsiPortStallExecution routine

The **ScsiPortStallExecution** routine stalls in the miniport driver.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiPortStallExecution(
  _In_ ULONG Delay
);
```



## Parameters

<dl> <dt>

*Delay* \[in\]
</dt> <dd>

Specifies the delay interval in microseconds. The given value must be less than a full millisecond.

</dd> </dl>

## Return value

None

## Remarks

**ScsiPortStallExecution** should be called as seldom as possible and the total stall time in a miniport driver routine must be less than one millisecond. This call ties up a processor, doing no useful work while stalling in the driver.

In general, a miniport driver should call **ScsiPortStallExecution** only if the driver must wait for a state change on the HBA that cannot cause an interrupt, or if the driver must delay for a very short interval between accesses to the HBA.

If a miniport driver's [**HwScsiInterrupt**](hwscsiinterrupt.md) routine must stall between accesses to the HBA and the total delay time in the ISR might be more than one millisecond, *HwScsiInterrupt* should call **ScsiPortNotification** with the *NotificationType***CallEnableInterrupts** instead of calling **ScsiPortStallExecution**. Such a miniport driver has a pair of *HwScsi..InterruptsCallback* routines to manage its interrupt-driven I/O processing without tying up a processor and degrading the I/O performance of other HBAs that miniport driver might support in the same machine.

A miniport driver-supplied [*HwScsiTimer*](hwscsitimer.md) routine also can be passed in calls to **ScsiPortNotification** with a specified interval that is not limited to one millisecond.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[*HwScsiTimer*](hwscsitimer.md)
</dt> <dt>

[**HwScsiDisableInterruptsCallback**](hwscsidisableinterruptscallback.md)
</dt> <dt>

[**HwScsiEnableInterruptsCallback**](hwscsienableinterruptscallback.md)
</dt> <dt>

[**HwScsiInterrupt**](hwscsiinterrupt.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortStallExecution%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






