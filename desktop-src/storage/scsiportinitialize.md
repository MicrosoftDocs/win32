---
title: ScsiPortInitialize routine
description: For a non-Plug and Play miniport driver, the ScsiPortInitialize routine sets up the PORT\_CONFIGURATION\_INFORMATION structure and calls the miniport drivers HwScsiFindAdapter routine.
ms.assetid: f6adca68-e016-4725-bd8e-691c71d1d471
keywords:
- ScsiPortInitialize routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortInitialize
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ScsiPortInitialize routine

For a non-Plug and Play miniport driver, the **ScsiPortInitialize** routine sets up the PORT\_CONFIGURATION\_INFORMATION structure and calls the miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine. **ScsiPortInitialize** also sets up system objects and resources on behalf of miniport drivers. For a Plug and Play miniport driver, **ScsiPortInitialize** stores the miniport driver's initialization data for future use.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
ULONG ScsiPortInitialize(
  _In_ PVOID                          Argument1,
  _In_ PVOID                          Argument2,
  _In_ struct _HW_INITIALIZATION_DATA *HwInitializationData,
  _In_ PVOID                          HwContext
);
```



## Parameters

<dl> <dt>

*Argument1* \[in\]
</dt> <dd>

Pointer to the driver object that the operating system passed to the miniport driver in the first argument of its **DriverEntry** routine.

</dd> <dt>

*Argument2* \[in\]
</dt> <dd>

Pointer to some context information that the operating system passed to the miniport driver in the second argument of its **DriverEntry**.

</dd> <dt>

*HwInitializationData* \[in\]
</dt> <dd>

Pointer to the initialization and configuration information supplied by **DriverEntry**.

</dd> <dt>

*HwContext* \[in\]
</dt> <dd>

Specifies the address of a context value to be passed to the miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine. Only legacy miniport drivers that scan the bus for HBAs rather than receiving configuration information from the port driver can use this parameter to store state between calls to *HwScsiFindAdapter*.

</dd> </dl>

## Return value

**ScsiPortInitialize** returns a status value that is used as the return value from the miniport driver's **DriverEntry** routine.

## Remarks

Every miniport driver's **DriverEntry** routine must call **ScsiPortInitialize** after the miniport driver has first zeroed and then set up the HW\_INITIALIZATION\_DATA.

If a miniport driver can support HBAs on different types of I/O buses, such as both **Isa** and **MicroChannel** type I/O buses, the miniport driver should call **ScsiPortInitialize** for each supported interface type.

A miniport driver that calls **ScsiPortInitialize** more than once should check the value returned by **ScsiPortInitialize** at each call and save the lowest value for all its calls. The **DriverEntry** routine must return the lowest value when it returns control to the system. Miniport driver writers can make no assumptions about the values returned by **ScsiPortInitialize**.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**DriverEntry of SCSI Miniport Driver**](driverentry-of-scsi-miniport-driver.md)
</dt> <dt>

[**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md)
</dt> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortInitialize%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






