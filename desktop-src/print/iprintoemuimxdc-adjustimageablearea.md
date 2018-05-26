---
Description: The IPrintOemUIMXDCAdjustImageableArea method enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of the printable area, including orientation and direction of rotation.
ms.assetid: a698fcb9-1285-4201-9b49-e79dcda66043
title: IPrintOemUIMXDCAdjustImageableArea method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemUIMXDC::AdjustImageableArea method

The `IPrintOemUIMXDC::AdjustImageableArea` method enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of the printable area, including orientation and direction of rotation.

## Syntax


```C++
HRESULT AdjustImageableArea(
         HANDLE   hPrinter,
         DWORD    cbDevMode,
   const PDEVMODE pDevMode,
         DWORD    cbOEMDM,
   const PVOID    pOEMDM,
         PRECTL   prclImageableArea
);
```



## Parameters

<dl> <dt>

*hPrinter* 
</dt> <dd>

A handle to the printer that is currently being queried.

</dd> <dt>

*cbDevMode* 
</dt> <dd>

The size of the [**DEVMODE**](display.devmodew) structure, in bytes, including appended data.

</dd> <dt>

*pDevMode* 
</dt> <dd>

A pointer to the DEVMODE structure that contains the current device settings.

</dd> <dt>

*cbOEMDM* 
</dt> <dd>

The number of bytes in the vendor-provided section of the DEVMODE structure.

</dd> <dt>

*pOEMDM* 
</dt> <dd>

A pointer to the data that is contained in the vendor portion of the DEVMODE structure that *pDevMode* points to.

</dd> <dt>

*prclImageableArea* 
</dt> <dd>

A pointer to a [**RECTL**](display.rectl) structure that contains the printable area. This parameter is populated by UnidrvUI.dll or PS5UI.dll with data from the corresponding GPD or PPD, before the parameter is passed to the plug-in. The plug-in can then update this data before returning.

</dd> </dl>

## Return value

`AdjustImageableArea` returns S\_OK if this method succeeds. Otherwise, this method should return E\_NOTIMPL if the plug-in does not support the method, or any appropriate failure value if the plug-in cannot complete the operation. For more information, see the following Remarks section.

## Remarks

The *prclImageableArea* parameter is IN OUT. All other parameters for this method are input only.

If the plug-in cannot complete the operation, it should return an appropriate failure HRESULT value, which willcause the current print job to fail.

## Requirements



|                            |                                                                                                                                                                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                                                                                                           |
| Version<br/>         | Available with Windows Vista and later versions of Unidrvui.dll and Ps5ui.dll, which are redistributable. This method is also available for XPSDrv drivers in Microsoft Windows XP if you have installed the XPS Essentials Pack.<br/> |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl>                                                                                                                                   |



## See also

<dl> <dt>

[**IPrintOemUIMXDC**](iprintoemuimxdc-interface.md)
</dt> <dt>

[**RECTL**](display.rectl)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUIMXDC::AdjustImageableArea%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





