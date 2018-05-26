---
title: StorPortInitialize routine
description: The StorPortInitilize routine initializes the port driver parameters and extension data. StorPortInitilize also saves the adapter information provided from the miniport driver.
ms.assetid: b560ce42-3c5c-4766-bb9c-6590b7113ecd
keywords:
- StorPortInitialize routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortInitialize
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortInitialize routine

The **StorPortInitilize** routine initializes the port driver parameters and extension data. **StorPortInitilize** also saves the adapter information provided from the miniport driver.

## Syntax


```C++
STORPORT_API ULONG StorPortInitialize(
  _In_     PVOID                   Argument1,
  _In_     PVOID                   Argument2,
  _In_     PHW_INITIALIZATION_DATA HwInitializationData,
  _In_opt_ PVOID                   HwContext
);
```



## Parameters

<dl> <dt>

*Argument1* \[in\]
</dt> <dd>

The first pointer with which the operating system called the miniport's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.

</dd> <dt>

*Argument2* \[in\]
</dt> <dd>

The second pointer with which the operating system called the miniports's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.

</dd> <dt>

*HwInitializationData* \[in\]
</dt> <dd>

Pointer to the initialization and configuration information set by the miniport driver in it's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.

</dd> <dt>

*HwContext* \[in, optional\]
</dt> <dd>

Is the address of a context value to be passed to the miniport driver's [**HwStorFindAdapter**](hwstorfindadapter.md) routine. Only legacy miniport drivers that scan the bus for HBAs rather than receiving configuration information from the port driver can use this parameter to store state between calls to **HwStorFindAdapter**.

</dd> </dl>

## Return value

The result of the initialization actions performed by **StorPortInitilize**. The miniport driver will return this value as the return value for its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.

**StorPortInitilize** returns one of the following status codes:



| Return code                                                                                                    | Description                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STATUS\_INVALID\_PARAMETER**</dt> </dl>      | *Argument1* is NULL.<br/> -or-<br/> *Argument2* is NULL.<br/> -or-<br/> *HwInitializationData* is NULL.<br/> |
| <dl> <dt>**STATUS\_SUCCESS**</dt> </dl>                 | The driver extension data and adapter information were initialized successfully.<br/>                                                |
| <dl> <dt> **STATUS\_NO\_MEMORY**</dt> </dl>             | No memory is available to store an initialization parameter.<br/>                                                                    |
| <dl> <dt> **STATUS\_REVISION\_MISMATCH**</dt> </dl>     | The version of the structure pointed to by *HwInitializationData* is invalid for the current operating system.<br/>                  |
| <dl> <dt> **STATUS\_INSUFFICENT\_RESOURCES**</dt> </dl> | The allocation failed for the driver object extension data.<br/>                                                                     |



 

## Remarks

This routine must be called from the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.

Because Storport miniport drivers must support PnP, the Storport driver does not use the *HwContext* parameter passed to **StorPortInitilize**.

Every miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine must call **StorPortInitilize** after the miniport driver has first zeroed and then set the members of [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md)
</dt> <dt>

[**HwStorFindAdapter**](hwstorfindadapter.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInitialize%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






