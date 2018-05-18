---
Description: 'The IPrintOemUni::EnableDriver method allows a rendering plug-in for Unidrv to hook out some graphics DDI functions.'
ms.assetid: '7d7cd1de-569a-4083-8d4c-e073645941e6'
title: 'IPrintOemUni::EnableDriver method'
---

# IPrintOemUni::EnableDriver method

The `IPrintOemUni::EnableDriver` method allows a rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) to hook out some graphics DDI functions.

## Syntax


```C++
STDMETHOD EnableDriver(
   DWORD          DriverVersion,
   DWORD          cbSize,
   PDRVENABLEDATA pded
);
```



## Parameters

<dl> <dt>

*DriverVersion* 
</dt> <dd>

Caller-supplied interface version number. This value is defined by PRINTER\_OEMINTF\_VERSION, in printoem.h.

</dd> <dt>

*cbSize* 
</dt> <dd>

Caller-supplied size, in bytes, of the structure pointed to by *pded*.

</dd> <dt>

*pded* 
</dt> <dd>

Caller-supplied pointer to a [**DRVENABLEDATA**](display.drvenabledata) structure.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                            | Description                         |
|----------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | The operation succeeded.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | The operation failed<br/>     |



 

## Remarks

A rendering plug-in for Unidrv must implement the `IPrintOemUni::EnableDriver` method.

The `IPrintOemUni::EnableDriver` method allows a rendering plug-in to perform the same types of operations as the [**DrvEnableDriver**](display.drvenabledriver) function that is exported by printer graphics DLLs.

Like the **DrvEnableDriver** function, the `IPrintOemUni::EnableDriver` method is responsible for providing addresses of internally supported graphics DDI functions, known as hooking functions. It can also perform other one-time initialization operations. Unlike the **DrvEnableDriver** function, implementation of `IPrintOemUni::EnableDriver` is optional.

> [!Note]  
> If you implement `IPrintOemUni::EnableDriver`, you must also implement [**IPrintOemUni::DisableDriver**](iprintoemuni-disabledriver.md). Actions begun in the former method might need to be completed in the latter method. For example, if a large buffer is allocated in `IPrintOemUni::EnableDriver`, but not deallocated in **IPrintOemUni::DisableDriver**, a memory leak can occur.

 

The method should fill the supplied [**DRVENABLEDATA**](display.drvenabledata) structure and allocate an array of [**DRVFN**](display.drvfn) structures. It should fill the array with pointers to hooking functions, along with winddi.h-defined index values that identify the hooked out graphics DDI functions.

A rendering plug-in for Unidrv can hook out a graphics DDI function only if the Unidrv driver defines the function. The following graphics DDI functions are defined in Unidrv and/or Pscript5 and can therefore be hooked out:

<dl>

[**DrvAlphaBlend**](display.drvalphablend)  
[**DrvBitBlt**](display.drvbitblt)  
[**DrvCopyBits**](display.drvcopybits)  
[**DrvDitherColor**](display.drvdithercolor) (Unidrv only)  
[**DrvEndDoc**](display.drvenddoc)  
[**DrvEscape**](display.drvescape)  
[**DrvFillPath**](display.drvfillpath)  
[**DrvFontManagement**](display.drvfontmanagement)  
[**DrvGetGlyphMode**](display.drvgetglyphmode)  
[**DrvGradientFill**](display.drvgradientfill)  
[**DrvIcmCreateColorTransform**](display.drvicmcreatecolortransform) (Pscript only)  
[**DrvIcmDeleteColorTransform**](display.drvicmdeletecolortransform) (Pscript only)  
[**DrvLineTo**](display.drvlineto) (Unidrv only)  
[**DrvNextBand**](display.drvnextband) (Unidrv only)  
[**DrvPlgBlt**](display.drvplgblt)  
[**DrvQueryAdvanceWidths**](display.drvqueryadvancewidths)  
[**DrvQueryDeviceSupport**](display.drvquerydevicesupport) (Pscript only)  
[**DrvQueryFont**](display.drvqueryfont)  
[**DrvQueryFontData**](display.drvqueryfontdata)  
[**DrvQueryFontTree**](display.drvqueryfonttree)  
[**DrvRealizeBrush**](display.drvrealizebrush)  
[*DrvSendPage*](display.drvsendpage)  
[**DrvStartBanding**](display.drvstartbanding) (Unidrv only)  
[**DrvStartDoc**](display.drvstartdoc)  
[**DrvStartPage**](display.drvstartpage)  
[**DrvStretchBlt**](display.drvstretchblt)  
[**DrvStretchBltROP**](display.drvstretchbltrop)  
[**DrvStrokeAndFillPath**](display.drvstrokeandfillpath)  
[**DrvStrokePath**](display.drvstrokepath)  
[**DrvTextOut**](display.drvtextout)  
[**DrvTransparentBlt**](display.drvtransparentblt)  
</dl>

If you provide a customized hooking function, it preempts the driver's equivalent graphics DDI function. Hooking functions can also call back into the driver's graphics DDI functions. For more information see [Customized Graphics DDI Functions](print.customized_graphics_ddi_functions).

Customized hooking functions have the same input and output parameters as the equivalent graphics DDI function, with one exception - where graphics DDI functions receive PDEV pointers, customized hooking functions receive [**DEVOBJ**](devobj.md) pointers. There are two ways for graphics DDI functions to receive PDEV pointers:

-   As the contents of the **dhpdev** member of a [**SURFOBJ**](display.surfobj) structure for the destination surface.

    For the equivalent customized hooking function, the destination SURFOBJ structure's **dhpdev** member points to a DEVOBJ structure, and must be cast to type PDEVOBJ when referenced. An example graphics DDI function is **DrvBitBlt**.

-   As an input argument for a *dhpdev* parameter.

    The equivalent customized hooking function must cast this input parameter to type PDEVOBJ when referencing it. An example graphics DDI function is **DrvDitherColor**.

Note that while a [printer graphics DLL](print.printer_graphics_dll) includes the addresses of its [**DrvEnablePDEV**](display.drvenablepdev), [**DrvDisablePDEV**](display.drvdisablepdev), and [**DrvResetPDEV**](display.drvresetpdev) functions in the DRVENABLEDATA structure, a rendering plug-in explicitly exports **EnablePDEV**, **DisablePDEV**, and **ResetPDEV** as methods of the **IPrintOemUni** interface and does not place their addresses in the DRVENABLEDATA structure.

If `IPrintOemUni::EnableDriver` methods are exported by multiple rendering plug-ins, the methods are called in the order that the plug-ins are specified for installation.

> [!Note]  
> Each graphics DDI function can be hooked out by only one rendering plug-in. If multiple plug-ins attempt to hook out the same graphics DDI function, all hook-outs after the first one are ignored.

 

For more information about creating and installing rendering plug-ins, see [Customizing Microsoft's Printer Drivers](print.customizing_microsoft_s_printer_drivers).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::EnableDriver%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




