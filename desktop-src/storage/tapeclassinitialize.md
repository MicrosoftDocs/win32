---
title: TapeClassInitialize routine
description: The TapeClassInitialize routine performs much of the driver and device initialization on behalf of a miniclass driver.
ms.assetid: 'f1c70ca5-2caf-4758-99bb-221af0a79211'
keywords: ["TapeClassInitialize routine Storage Devices"]
topic_type:
- apiref
api_name:
- TapeClassInitialize
api_location:
- Tape.lib
- Tape.dll
api_type:
- LibDef
---

# TapeClassInitialize routine

The **TapeClassInitialize** routine performs much of the driver and device initialization on behalf of a miniclass driver. **TapeClassInitialize** loads the tape class driver entry points for tape I/O requests into the miniclass driver data structure, locates and claims unclaimed tape devices that the miniclass driver supports, and allocates and initializes the operating system resources for the miniclass driver and its devices. **TapeClassInitialize** uses miniclass-driver-specific information supplied in *TapeInitData* and calls back to the tape miniclass driver for driver-specific operations.

## Syntax


```C++
ULONG TapeClassInitialize(
  _In_ PVOID              Argument1,
  _In_ PVOID              Argument2,
  _In_ PTAPE_INIT_DATA_EX TapeInitData
);
```



## Parameters

<dl> <dt>

*Argument1* \[in\]
</dt> <dd>

Pointer to driver context information that was passed to the tape miniclass driver's **DriverEntry** routine. The format of the information is operating system-specific and must not be interpreted by a tape miniclass driver.

</dd> <dt>

*Argument2* \[in\]
</dt> <dd>

Pointer to the second driver context structure that was passed to the tape miniclass driver's **DriverEntry** routine. The format of the information is operating system-specific and must not be interpreted by a tape miniclass driver.

</dd> <dt>

*TapeInitData* \[in\]
</dt> <dd>

Pointer to a TAPE\_INIT\_DATA\_EX structure containing driver-specific information such as the entry points for the tape miniclass driver's command processing routines.

</dd> </dl>

## Return value

**TapeClassInitialize** returns a value indicating the success or failure of the driver initialization. The tape miniclass driver passes this value, uninterpreted, as the return value from its **DriverEntry** routine.

## Remarks

A tape miniclass driver calls **TapeClassInitialize** from its **DriverEntry** routine and passes driver-specific information in *TapeInitData*. **TapeClassInitialize** performs a large part of the driver initialization on behalf of the miniclass driver and insulates the miniclass driver from operating system-specific details.

**TapeClassInitialize** calls the tape miniclass driver for driver-specific activities required during initialization. For example, **TapeClassInitialize** calls the tape miniclass driver's TapeMiniVerifyInquiry routine to determine whether the driver supports a given tape device. **TapeClassInitialize** also calls the tape miniclass driver's TapeMiniExtensionInit routine to initialize the minitape extension, if the miniclass driver requested one.

A tape miniclass driver allocates a TAPE\_INIT\_DATA\_EX structure on the stack, clears it with **TapeClassZeroMemory**, fills in all the appropriate members, and passes it to **TapeClassInitialize**.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Tape.lib</dt> </dl>                        |



## See also

<dl> <dt>

[**TAPE\_INIT\_DATA\_EX**](tape-init-data-ex.md)
</dt> <dt>

[**DriverEntry of Tape Miniclass Driver**](driverentry-of-tape-miniclass-driver.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TapeClassInitialize%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






