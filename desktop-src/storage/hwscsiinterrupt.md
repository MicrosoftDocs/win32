---
title: PHW\_INTERRUPT routine
description: HwScsiInterrupt is called when the HBA generates an interrupt.
ms.assetid: 89eebf18-59d3-4551-9fe3-36b37838273e
keywords:
- HwScsiInterrupt routine Storage Devices
- PHW_INTERRUPT
topic_type:
- apiref
api_name:
- HwScsiInterrupt
api_location:
- miniport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PHW\_INTERRUPT routine

*HwScsiInterrupt* is called when the HBA generates an interrupt. Miniport drivers of HBAs that do not generate interrupts do not have this routine.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN HwScsiInterrupt(
  _In_ PVOID DeviceExtension
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Points to the miniport driver's per-HBA storage area.

</dd> </dl>

## Return value

If the miniport driver finds that its HBA did not generate the interrupt, *HwScsiInterrupt* should return **FALSE** as soon as possible.

## Remarks

*HwScsiInterrupt* is responsible for completing interrupt-driven I/O operations. This routine must clear the interrupt on the HBA before it returns **TRUE**.

Miniport drivers of HBAs that require interrupt processing that takes more than 50 microseconds should have a pair of *HwScsi..InterruptsCallback* routines. Such a driver's *HwScsiInterrupt* routine should do the following, rather than calling **ScsiPortStallExecution** to tie up the processor while its HBA updates hardware state:

1.  Disable interrupts on the HBA.

2.  Set up the *DeviceExtension* with any context necessary to complete the operation.

3.  Call **ScsiPortNotification** with the *NotificationType* value **CallEnableInterrupts** and the entry point for the driver's *HwScsiEnableInterruptsCallback* routine.

4.  Return control.

Using this technique improves overall I/O throughput, including that of any other HBAs the miniport driver supports.

If a miniport driver's *HwScsiInterrupt* routine cannot disable interrupts on its HBA but its interrupt-driven transfer operations take more than 50 microseconds in the *HwScsiInterrupt* routine, the miniport driver should limit the maximum size for transfers that it accepts. Such a miniport driver's *HwScsiFindAdapter* routine can set the **MaximumTransferLength** member of the PORT\_CONFIGURATION\_INFORMATION structure to a value that restricts execution time in the *HwScsiInterrupt* routine for transfers. The miniport driver writer should adjust this value during driver development so there is no user-noticeable impact on the performance of the mouse, serial, and/or parallel drivers. Otherwise, the mouse pointer can appear to "jump" or the serial/parallel throughput to degrade noticeably whenever that miniport driver is transferring data.

The name *HwScsiInterrupt* is just a placeholder. The actual prototype of this routine is defined in *srb.h* as follows:


```
typedef
BOOLEAN
(*PHW_INTERRUPT) (
  IN PVOID  DeviceExtension
  );
```



For more information about the *HwScsiInterrupt* routine, see [SCSI Miniport Driver's HwScsiInterrupt Routine](https://msdn.microsoft.com/library/windows/hardware/ff565329).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwScsiDisableInterruptsCallback**](hwscsidisableinterruptscallback.md)
</dt> <dt>

[**HwScsiEnableInterruptsCallback**](hwscsienableinterruptscallback.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> <dt>

[**ScsiPortStallExecution**](scsiportstallexecution.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_INTERRUPT%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






