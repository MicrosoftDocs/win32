---
Description: 'The IPrintOemPS::EnablePDEV method allows a rendering plug-in for Pscript5 to create its own PDEV structure.'
ms.assetid: 'f284e89f-463e-4d04-8018-5ce02786d921'
title: 'IPrintOemPS::EnablePDEV method'
---

# IPrintOemPS::EnablePDEV method

The `IPrintOemPS::EnablePDEV` method allows a rendering plug-in for Pscript5 to create its own PDEV structure.

## Syntax


```C++
STDMETHOD EnablePDEV(
        PDEVOBJ       pdevobj,
        PWSTR         pPrinterName,
        ULONG         cPatterns,
        HSURF         *phsurfPatterns,
        ULONG         cjGdiInfo,
        GDIINFO       *pGdiInfo,
        ULONG         cjDevInfo,
        DEVINFO       *pDevInfo,
        DRVENABLEDATA *pded,
  [out] PDEVOEM       *pDevOem
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*pPrinterName* 
</dt> <dd>

Caller-supplied pointer to a text string representing the logical address of the printer.

</dd> <dt>

*cPatterns* 
</dt> <dd>

Caller-supplied value representing the number of HSURF-typed surface handles contained in the buffer pointed to by *phsurfPatterns*.

</dd> <dt>

*phsurfPatterns* 
</dt> <dd>

Caller-supplied pointer to a buffer that is large enough to contain *cPatterns* number of HSURF-typed surface handles. The handles represent surface fill patterns.

</dd> <dt>

*cjGdiInfo* 
</dt> <dd>

Caller-supplied value representing the size of the structure pointed to by *pGdiInfo*.

</dd> <dt>

*pGdiInfo* 
</dt> <dd>

Caller-supplied pointer to a [**GDIINFO**](display.gdiinfo) structure.

</dd> <dt>

*cjDevInfo* 
</dt> <dd>

Caller-supplied value representing the size of the structure pointed to by *pDevInfo*.

</dd> <dt>

*pDevInfo* 
</dt> <dd>

Caller-supplied pointer to a [**DEVINFO**](display.devinfo) structure.

</dd> <dt>

*pded* 
</dt> <dd>

Caller-supplied pointer to a [**DRVENABLEDATA**](display.drvenabledata) structure containing the addresses of the printer driver's graphics DDI hooking functions. For more information, see the following Remarks section.

</dd> <dt>

*pDevOem* \[out\]
</dt> <dd>

Receives a method-supplied pointer to a private PDEV structure. (For more information, see the following Remarks section.)

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

If the operation fails, the method should call **SetLastError** to set an error code.

## Remarks

The `IPrintOemPS::EnablePDEV` method performs the same types of operations as the [**DrvEnablePDEV**](display.drvenablepdev) function that is exported by a printer graphics DLL. Its purpose is to allow a rendering plug-in to create its own PDEV structure. (For more information about PDEV structures, see [Customized PDEV Structures](print.customized_pdev_structures).)

If you provide a rendering plug-in that exports the `IPrintOemPS::EnablePDEV` method, Pscript5's printer graphics DLL calls the method from within its [**DrvEnablePDEV**](display.drvenablepdev) function.

The `IPrintOemPS::EnablePDEV` method should allocate an instance of its private PDEV structure, initialize it, and return its address as the method's *pDevOem* parameter. Other plug-in methods receive the address as the **pdevOEM** member of the [**DEVOBJ**](devobj.md) structure.

The **pdevOEM** member of the DEVOBJ structure is not used with the `IPrintOemPS::EnablePDEV` method.

The structures pointed to by the *phsurfPatterns*, *pGdiInfo*, and *pDevInfo* parameter values are the same ones that Pscript5's **DrvEnablePDEV** function receives. The rendering plug-in can modify the structure contents as necessary. It can supply surface fill patterns by obtaining HSURF-typed surface handles and placing them in the buffer pointed to by *phsurfPatterns*. Fill pattern types and handle order are listed in the description of [**DrvEnablePDEV**](display.drvenablepdev).

The [**DRVENABLEDATA**](display.drvenabledata) structure pointed to by *pded* contains the addresses of graphics DDI functions provided by Pscript5's printer graphics DLL. You are allowed to provide customized hooking functions in your plug-in for these graphics DDI functions. The DRVENABLEDATA structure's contents enable your customized hooking functions to call back to the driver's graphics DDI functions. For more information, see [Customized Graphics DDI Functions](print.customized_graphics_ddi_functions).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPS::EnablePDEV%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




