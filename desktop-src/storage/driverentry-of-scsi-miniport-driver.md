---
title: DriverEntry of SCSI Miniport Driver routine
description: Each miniport driver must have a routine explicitly named DriverEntry in order to be loaded.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: dda79363-06a9-4902-8e04-186293b6c9d4
keywords:
- DriverEntry routine Storage Devices
topic_type:
- apiref
api_name:
- DriverEntry
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DriverEntry of SCSI Miniport Driver routine

Each miniport driver must have a routine explicitly named **DriverEntry** in order to be loaded.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
ULONG DriverEntry(
  _In_ PVOID Argument1,
  _In_ PVOID Argument2
);
```



## Parameters

<dl> <dt>

*Argument1* \[in\]
</dt> <dd>

Is a pointer with which the miniport driver must call **ScsiPortInitialize**.

</dd> <dt>

*Argument2* \[in\]
</dt> <dd>

Is a pointer with which the miniport driver must call **ScsiPortInitialize**.

</dd> </dl>

## Return value

**DriverEntry** returns the value returned by **ScsiPortInitialize**. If it calls **ScsiPortInitialize** more than once, **DriverEntry** returns the lowest value returned by **ScsiPortInitialize**.

## Remarks

A miniport driver's **DriverEntry** routine allocates memory on the stack and initializes a HW\_INITIALIZATION\_DATA structure with zeros. **DriverEntry** must zero all members in the HW\_INITIALIZATION\_DATA structure before initializing it with values appropriate to the HBA(s) the miniport driver supports.

**DriverEntry** should set the **HwInitializationDataSize** member to **sizeof**(HW\_INITIALIZATION\_DATA) to indicate which version of this structure it is using, as well as initializing all members appropriately for its HBA(s).

Next, **DriverEntry** calls **ScsiPortInitialize**. If a miniport driver supports HBA(s) that can be connected on more than one type of I/O bus, such as both **MicroChannel** and **Isa** type buses, it should call **ScsiPortInitialize** once for each type of I/O bus. Such a miniport driver must return the lowest value returned by its calls to **ScsiPortInitialize** from the **DriverEntry** routine. A miniport driver writer can make no assumptions about the values returned by **ScsiPortInitialize**.

## See also

<dl> <dt>

[**HW\_INITIALIZATION\_DATA**](hw-initialization-data--scsi-.md)
</dt> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> <dt>

[**ScsiPortInitialize**](scsiportinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DriverEntry%20of%20SCSI%20Miniport%20Driver%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





