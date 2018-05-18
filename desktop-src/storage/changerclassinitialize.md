---
title: ChangerClassInitialize routine
description: The ChangerClassInitialize routine initializes the driver.
ms.assetid: 'b19f85f7-fe51-4539-8c36-e3c6a299faad'
keywords: ["ChangerClassInitialize routine Storage Devices"]
topic_type:
- apiref
api_name:
- ChangerClassInitialize
api_location:
- Mcd.lib
- Mcd.dll
api_type:
- LibDef
---

# ChangerClassInitialize routine

The **ChangerClassInitialize** routine initializes the driver.

## Syntax


```C++
NTSTATUS ChangerClassInitialize(
  _In_ PDRIVER_OBJECT  DriverObject,
  _In_ PUNICODE_STRING RegistryPath,
  _In_ PMCD_INIT_DATA  MCDInitData
);
```



## Parameters

<dl> <dt>

*DriverObject* \[in\]
</dt> <dd>

Pointer to the changer miniclass driver object. This is passed as a parameter to the miniclass driver's **DriverEntry** routine. The format of this object is operating system-specific and should not be interpreted by the miniclass driver.

</dd> <dt>

*RegistryPath* \[in\]
</dt> <dd>

Pointer to the registry path for changer miniclass driver. This is also passed as a parameter to the miniclass driver's **DriverEntry** routine. The format of this is operating system-specific and should not be interpreted by the miniclass driver.

</dd> <dt>

*MCDInitData* \[in\]
</dt> <dd>

Pointer to an [**MCD\_INIT\_DATA**](mcd-init-data.md) structure containing miniclass driver-specific information such as the entry points for the changer miniclass driver's command processing routines.

</dd> </dl>

## Return value

**ChangerClassInitialize** returns a value indicating the success or failure of the driver initialization. If initialization is successful, **ChangerClassInitialize** returns STATUS\_SUCCESS. Otherwise, **ChangerClassInitialize** returns an appropriate error message. Minidrivers should *not* interpret this error value, but should just return this value from their **DriverEntry** routine.

## Remarks

**ChangerClassInitialize** is a changer class driver routine that miniclass drivers can call in Microsoft Windows XP and later operating systems.

Changer miniclass drivers call **ChangerClassInitialize** from within their **DriverEntry** routines to initialize the driver. **ChangerClassInitialize** performs many tasks formerly performed by the changer class driver's **DriverEntry** routine such as registering the miniclass driver's dispatch routines. It allocates a driver object extension and copies the data contained in *MCDInitData* into the driver object extension along with other initialization data such as the driver's registry path and pointers to certain changer class driver routines that are operating system-specific.

Changer miniclass drivers must allocate an [**MCD\_INIT\_DATA**](mcd-init-data.md) structure, zero the structure by calling [**RtlZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563610), and then assign values to the appropriate members, before passing the structure's address to **ChangerClassInitialize** by means of the *MCDInitData* parameter.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Mcd.lib</dt> </dl>                             |



## See also

<dl> <dt>

[**MCD\_INIT\_DATA**](mcd-init-data.md)
</dt> <dt>

[**RtlZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563610)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerClassInitialize%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






