---
Description: The IPrintOemPS::ResetPDEV method allows a rendering plug-in for Pscript5 to reset its PDEV structure.
ms.assetid: 10248026-471a-4419-9c96-3502c24a6e96
title: IPrintOemPS::ResetPDEV method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemPS::ResetPDEV method

The `IPrintOemPS::ResetPDEV` method allows a rendering plug-in for Pscript5 to reset its PDEV structure.

## Syntax


```C++
STDMETHOD ResetPDEV(
   PDEVOBJ pdevobjOld,
   PDEVOBJ pdevobjNew
);
```



## Parameters

<dl> <dt>

*pdevobjOld* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure containing current PDEV information.

</dd> <dt>

*pdevobjNew* 
</dt> <dd>

Caller-supplied pointer to a DEVOBJ structure into which the method should place new PDEV information.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

If the operation fails it should call **SetLastError**.

## Remarks

A rendering plug-in's `IPrintOemPS::ResetPDEV` method performs the same types of operations as the [**DrvResetPDEV**](https://www.bing.com/search?q=**DrvResetPDEV**) function that is exported by a printer graphics DLL. During the processing of an application's call to the Microsoft Windows SDK **ResetDC** function, the `IPrintOemPS::ResetPDEV` method is called by the **DrvResetPDEV** function in Pscript5's printer graphics DLL. For more information about when **DrvResetPDEV** is called, see its description.

The rendering plug-in's private PDEV structure's address is contained in the **pdevOEM** member of the DEVOBJ structure pointed to by *pdevobjOld*. The `IPrintOemPS::ResetPDEV` method should use relevant members of this old structure to fill in the new structure, which is referenced through *pdevobjNew*.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPS::ResetPDEV%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




