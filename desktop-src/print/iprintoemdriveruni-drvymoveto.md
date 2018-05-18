---
Description: 'The IPrintOemDriverUni::DrvYMoveTo method is provided by the Unidrv driver so that a rendering plug-in can notify the driver of cursor y-position changes.'
ms.assetid: 'ce9b1622-4c02-4496-82ca-cefa49d531da'
title: 'IPrintOemDriverUni::DrvYMoveTo method'
---

# IPrintOemDriverUni::DrvYMoveTo method

The `IPrintOemDriverUni::DrvYMoveTo` method is provided by the Unidrv driver so that a [rendering plug-in](print.rendering_plug_ins) can notify the driver of cursor y-position changes.

## Syntax


```C++
HRESULT DrvYMoveTo(
        PDEVOBJ pdevobj,
        INT     y,
        DWORD   dwFlags,
  [out] INT     *piResult
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*y* 
</dt> <dd>

Caller-supplied value representing the number of units the cursor should be moved. The unit is defined by the MV\_GRAPHICS flags in *dwFlags*.

</dd> <dt>

*dwFlags* 
</dt> <dd>

One or more of the following caller-supplied bit flags:



| Flag                    | Definition                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MV\_GRAPHICS<br/> | If set, the *y* parameter's value is expressed in dots, based on the printer's current resolution. For example, if the y resolution is 150 DPI and *y* is 75, the movement is ?? inch.<br/> If not set, the *y* parameter's value is expressed in master units. For example, if the y master unit is 600 and *y* is 300, the movement is ?? inch.<br/>                           |
| MV\_PHYSICAL<br/> | If set, the *y* parameter's value is relative to the cursor origin.<br/> If not set, the *y* parameter's value is relative to the printable area's origin.<br/> Cannot be set if MV\_RELATIVE is set.<br/>                                                                                                                                                                 |
| MV\_RELATIVE<br/> | If set, specifies that the cursor should be moved *y* units from its current position.<br/> If not set, specifies that the cursor should be moved *y* units from its origin.<br/>                                                                                                                                                                                                |
| MV\_UPDATE<br/>   | If set, specifies that Unidrv should update its current calculation of the cursor position without actually moving the cursor. (Should be set if [**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md) has moved the cursor.)<br/> If not set, specifies that Unidrv should update its current calculation of the cursor position and also move the cursor.<br/> |



 

</dd> <dt>

*piResult* \[out\]
</dt> <dd>

Receives the method-supplied result of subtracting the actual new cursor position from the requested new cursor position. This value might be zero, but it is always nonnegative.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The [**IPrintOemDriverUni::DrvXMoveTo**](iprintoemdriveruni-drvxmoveto.md) and `IPrintOemDriverUni::DrvYMoveTo` methods allow a rendering plug-in to send image data to the printer spooler without causing the printer driver to lose track of the printer's cursor position. If you provide an [**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md) method that sends image data directly to the print spooler instead of returning it to the printer driver, the method should call `IPrintOemDriverUni::DrvXMoveTo` and `IPrintOemDriverUni::DrvYMoveTo`.

Either of two techniques can be used for updating the cursor position:

-   Whenever an **IPrintOemUni::ImageProcessing** method needs to update the cursor position, it can call `IPrintOemDriverUni::DrvXMoveTo` or `IPrintOemDriverUni::DrvYMoveTo` with the MV\_UPDATE flag cleared. This causes Unidrv to send cursor commands to the print spooler and to update its internal calculation of the current cursor position.

-   The **IPrintOemUni::ImageProcessing** method can update the cursor by sending cursor commands directly to the print spooler. When the method has finished its spooling operation, it can call `IPrintOemDriverUni::DrvXMoveTo` or `IPrintOemDriverUni::DrvYMoveTo` with the MV\_UPDATE flag set. This causes Unidrv to update its internal calculation of the current cursor position without sending cursor commands to the print spooler.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUni::DrvYMoveTo%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




