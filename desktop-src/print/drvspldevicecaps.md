---
Description: A printer interface DLL's DrvSplDeviceCaps function queries a printer for its capabilities.
ms.assetid: 3d129a30-a892-4f4d-b8e3-f277d97980f4
title: DrvSplDeviceCaps function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DrvSplDeviceCaps function

A printer interface DLL's **DrvSplDeviceCaps** function queries a printer for its capabilities.

## Syntax


```C++
DWORD DrvSplDeviceCaps(
            HANDLE   hPrinter,
  _In_      PWSTR    pwDeviceName,
            WORD     DeviceCap,
  _Out_opt_ PVOID    pvOutput,
            DWORD    cchBuf,
  _In_opt_  PDEVMODE pDM
);
```



## Parameters

<dl> <dt>

*hPrinter* 
</dt> <dd>

Caller-supplied handle to the printer.

</dd> <dt>

*pwDeviceName* \[in\]
</dt> <dd>

Caller-supplied pointer to a Unicode string that contains the printer name.

</dd> <dt>

*DeviceCap* 
</dt> <dd>

Caller-supplied bit flag that indicates the capability to query for. (The flags are defined in header file wingdi.h.) This function is not required to support all of the DC\_*XXX* flags, but it must support those listed in the following table.



| Flag                      | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DC\_MEDIAREADY<br/> | The *pvOutput* parameter points to a buffer that the function should fill with an array of string buffers, each 64 characters in length. Each array element should contain a NULL-terminated string representing a name for a paper form that is available for use. <br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/> |
| DC\_PAPERNAMES<br/> | The *pvOutput* parameter points to a buffer that the function should fill with an array of string buffers, each 64 characters in length. Each array element should contain a NULL-terminated string representing a name for a paper form. <br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/>                           |



 

</dd> <dt>

*pvOutput* \[out, optional\]
</dt> <dd>

Caller-supplied pointer to a buffer that receives function-supplied information. The buffer's use depends on the value of the *DeviceCap* parameter. The caller is responsible for allocating and freeing this buffer.

</dd> <dt>

*cchBuf* 
</dt> <dd>

Caller-supplied size (in characters) of the buffer pointed to by the *pvOutput* parameter.

</dd> <dt>

*pDM* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure that describes the current print job characteristics. If **NULL**, the function should use the driver's internal default DEVMODEW structure.

</dd> </dl>

## Return value

The return value depends on the *DeviceCap* parameter. If *DeviceCap* indicates a capability that the driver does not support, or if an error is encountered, the function should return GDI\_ERROR.

## Remarks

The **DrvSplDeviceCaps** function is available in Microsoft Windows Server 2003 and later.

For descriptions of the DC\_*XXX* flags, see [**DrvDeviceCapabilities**](drvdevicecapabilities.md).

This function must be defined in the .def file as DrvSplDeviceCaps @ 254, because the spooler uses the ordinal number 254 to obtain the driver function pointer.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvDeviceCapabilities**](drvdevicecapabilities.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvSplDeviceCaps%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





