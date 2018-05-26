---
Description: The IPrintOemUniDriverDMS method allows a rendering plug-in for Unidrv to indicate that it uses a device-managed drawing surface.
ms.assetid: b62e6752-0804-41c4-84f4-49ad145acaf3
title: IPrintOemUniDriverDMS method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemUni::DriverDMS method

The `IPrintOemUni::DriverDMS` method allows a rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) to indicate that it uses a device-managed drawing surface.

## Syntax


```C++
HRESULT DriverDMS(
   PVOID  pDevObj,
   PVOID  pBuffer,
   DWORD  cbSize,
   PDWORD pcbNeeded
);
```



## Parameters

<dl> <dt>

*pDevObj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Caller-supplied pointer to a buffer to receive method-specified flags. (See the following Remarks section.)

</dd> <dt>

*cbSize* 
</dt> <dd>

Caller-supplied size, in bytes, of the buffer pointed to by *pBuffer*.

</dd> <dt>

*pcbNeeded* 
</dt> <dd>

Caller-supplied pointer to a location to receive the required minimum *pBuffer* size.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                            | Description                         |
|----------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | The operation succeeded.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | The operation failed<br/>     |



 

## Remarks

A rendering plug-in for Unidrv must implement the `IPrintOemUni::DriverDMS` method. The method will be called only if Unidrv finds a valid interface pointer to the OEM's rendering plug-in.

The `IPrintOemUni::DriverDMS` method allows a rendering plug-in to indicate that it will be using a device-managed drawing surface instead of the default GDI-managed surface.

The method must specify HOOK\_-prefixed flags in the buffer pointed to by *pBuffer*, indicating which of the plug-in's graphics DDI hooking functions are to be called for the drawing surface. The HOOK\_-prefixed flags are defined in winddi.h and described in the [**EngAssociateSurface**](display.engassociatesurface) function's description. Flags specified by `IPrintOemUni::DriverDMS` are passed by Unidrv to **EngAssociateSurface**. (Note that to support a device-managed surface, the rendering plug-in must hook out all drawing functions.) For more information, see [Handling Device-Managed Surfaces](print.handling_device_managed_surfaces).

If `IPrintOemUni::DriverDMS` sets flags in the buffer pointed to by *pBuffer*, Unidrv creates a device-managed surface by calling [**EngCreateDeviceSurface**](display.engcreatedevicesurface). If `IPrintOemUni::DriverDMS` does not set any flags, Unidrv creates a GDI-managed surface by calling [**EngCreateBitmap**](display.engcreatebitmap). In either of these cases, `IPrintOemUni::DriverDMS` should return S\_OK.

If the output buffer size specified by *cbSize* is too small, the method should specify the required size in the location pointed to by *pcbNeeded*, call **SetLastError**(ERROR\_INSUFFICIENT\_BUFFER), and return E\_FAIL.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::DriverDMS%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




