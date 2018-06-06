---
Description: The IPrintOemUni::EnablePDEV method allows a rendering plug-in for Unidrv to create its own PDEV structure.
ms.assetid: 93028b21-7995-42cd-af14-97e74ae75092
title: IPrintOemUni::EnablePDEV method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::EnablePDEV method

The `IPrintOemUni::EnablePDEV` method allows a rendering plug-in for [*Unidrv*](https://msdn.microsoft.com/0a51fa2b-3d09-4a5f-9fff-40604877a414) to create its own PDEV structure.

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

Caller-supplied pointer to a [**GDIINFO**](https://msdn.microsoft.com/f75f599f-43ea-4da6-a6e3-6591cf6d69f1) structure.

</dd> <dt>

*cjDevInfo* 
</dt> <dd>

Caller-supplied value representing the size of the structure pointed to by *pDevInfo*.

</dd> <dt>

*pDevInfo* 
</dt> <dd>

Caller-supplied pointer to a [**DEVINFO**](https://msdn.microsoft.com/5ba3e521-2e70-4a5b-979d-30a061275d42) structure.

</dd> <dt>

*pded* 
</dt> <dd>

Caller-supplied pointer to a [**DRVENABLEDATA**](https://msdn.microsoft.com/dbeaecf8-dea1-4412-babb-6e40bf5dc7b0) structure containing the addresses of the printer driver's graphics DDI hooking functions. For more information, see the following Remarks section.

</dd> <dt>

*pDevOem* \[out\]
</dt> <dd>

Receives a method-supplied pointer to a private PDEV structure. (For more information, see the following Remarks section.)

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                            | Description                         |
|----------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | The operation succeeded.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | The operation failed<br/>     |



 

If the operation fails, the method should call **SetLastError** to set an error code.

## Remarks

A rendering plug-in for Unidrv must implement the `IPrintOemUni::EnablePDEV` method.

The `IPrintOemUni::EnablePDEV` method performs the same types of operations as the [**DrvEnablePDEV**](https://msdn.microsoft.com/9a7ed18a-f21c-486b-9261-59a3fe5aef9e) function that is exported by a printer graphics DLL. Its purpose is to allow a rendering plug-in to create its own PDEV structure. (For more information about PDEV structures, see [Customized PDEV Structures](https://www.bing.com/search?q=Customized+PDEV+Structures).)

If you provide a rendering plug-in that exports the `IPrintOemUni::EnablePDEV` method, Undrv's printer graphics DLL calls the method from within its [**DrvEnablePDEV**](https://msdn.microsoft.com/9a7ed18a-f21c-486b-9261-59a3fe5aef9e) function.

The `IPrintOemUni::EnablePDEV` method should allocate an instance of its private PDEV structure, initialize it, and return its address as the method's *pDevOem* parameter. Other plug-in methods receive the address as the *pdevOEM* member of the [**DEVOBJ**](devobj.md) structure.

The **pdevOEM** member of the DEVOBJ structure is not used with the `IPrintOemUni::EnablePDEV` method.

The structures pointed to by the *phsurfPatterns*, *pGdiInfo*, and *pDevInfo* parameter values are the same ones that Unidrv's **DrvEnablePDEV** function receives. The rendering plug-in can modify the structure contents as necessary. It can supply surface fill patterns by obtaining HSURF-typed surface handles and placing them in the buffer pointed to by *phsurfPatterns*. Fill pattern types and handle order are listed in the description of [**DrvEnablePDEV**](https://msdn.microsoft.com/9a7ed18a-f21c-486b-9261-59a3fe5aef9e).

The [**DRVENABLEDATA**](https://msdn.microsoft.com/dbeaecf8-dea1-4412-babb-6e40bf5dc7b0) structure pointed to by *pded* contains the addresses of graphics DDI functions provided Unidrv's printer graphics DLL. You are allowed to provide customized hooking functions in your plug-in for these graphics DDI functions. The DRVENABLEDATA structure's contents enable your customized hooking functions to call back to the driver's graphics DDI functions. For more information, see [Customized Graphics DDI Functions](https://www.bing.com/search?q=Customized+Graphics+DDI+Functions).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::EnablePDEV%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




