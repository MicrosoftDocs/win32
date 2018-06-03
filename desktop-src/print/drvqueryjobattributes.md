---
Description: The DrvQueryJobAttributes function allows a printer interface DLL to specify support for such capabilities as printing multiple document pages on a physical page (&\#0034;N-up&\#0034; printing), printing multiple copies of each page, collating pages, and printing pages in reverse order.
ms.assetid: 71e07572-bb15-4838-94d1-e07a3305ab82
title: DrvQueryJobAttributes function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DrvQueryJobAttributes function

The **DrvQueryJobAttributes** function allows a printer interface DLL to specify support for such capabilities as printing multiple document pages on a physical page ("N-up" printing), printing multiple copies of each page, collating pages, and printing pages in reverse order.

## Syntax


```C++
BOOL DrvQueryJobAttributes(
  _In_  HANDLE   hPrinter,
  _In_  PDEVMODE pDevMode,
  _In_  DWORD    dwLevel,
  _Out_ LPBYTE   lpAttributeInfo
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

Caller-supplied printer handle.

</dd> <dt>

*pDevMode* \[in\]
</dt> <dd>

Caller-supplied pointer to a [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure.

</dd> <dt>

*dwLevel* \[in\]
</dt> <dd>

Caller-supplied value indicating the type of structure pointed to by *lpAttributeInfo*, as indicated in the following table.



| *dwLevel* Value | Structure pointed to by *lpAttributeInfo*                 |
|-----------------|-----------------------------------------------------------|
| 1<br/>    | [**ATTRIBUTE\_INFO\_1**](attribute-info-1.md)<br/> |
| 2<br/>    | [**ATTRIBUTE\_INFO\_2**](attribute-info-2.md)<br/> |
| 3<br/>    | [**ATTRIBUTE\_INFO\_3**](attribute-info-3.md)<br/> |
| 4<br/>    | [**ATTRIBUTE\_INFO\_4**](attribute-info-4.md)<br/> |



 

</dd> <dt>

*lpAttributeInfo* \[out\]
</dt> <dd>

Caller-supplied pointer to a structure identified by *dwLevel*.

</dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**. Otherwise, it should return **FALSE**. Returning **FALSE** causes the current print job to be canceled.

## Remarks

A [printer interface DLL](https://www.bing.com/search?q=printer interface DLL) can optionally provide a **DrvQueryJobAttributes** function. If the function is provided, it should fill in the supplied structure, described by *dwLevel* and *plAttributeInfo*, to indicate the current print job's user-requested attributes (such as N-up parameters and the number of copies) and the driver's ability to support those attributes. The function is typically called by the EMF print processor, so it can determine which job attributes can be handled by the driver (or printer), and which must be handled by the print processor.

For descriptions of the job attributes that the function can specify, see the descriptions of [**ATTRIBUTE\_INFO\_1**](attribute-info-1.md), [**ATTRIBUTE\_INFO\_2**](attribute-info-2.md), [**ATTRIBUTE\_INFO\_3**](attribute-info-3.md), and [**ATTRIBUTE\_INFO\_4**](attribute-info-4.md).

The ATTRIBUTE\_INFO\_4 structure is defined for Windows Vista.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**ATTRIBUTE\_INFO\_1**](attribute-info-1.md)
</dt> <dt>

[**ATTRIBUTE\_INFO\_2**](attribute-info-2.md)
</dt> <dt>

[**ATTRIBUTE\_INFO\_3**](attribute-info-3.md)
</dt> <dt>

[**ATTRIBUTE\_INFO\_4**](attribute-info-4.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvQueryJobAttributes%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





