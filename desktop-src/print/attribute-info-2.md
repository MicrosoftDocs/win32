---
Description: The ATTRIBUTE\_INFO\_2 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. All member values are function-supplied.
ms.assetid: c5bb9943-ee5b-4128-9e5f-438971119e3a
title: ATTRIBUTE\_INFO\_2 structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ATTRIBUTE\_INFO\_2 structure

The ATTRIBUTE\_INFO\_2 structure is used as a parameter for a printer interface DLL's [**DrvQueryJobAttributes**](drvqueryjobattributes.md) function. All member values are function-supplied.

## Syntax


```C++
typedef struct _ATTRIBUTE_INFO_2 {
  DWORD dwJobNumberOfPagesPerSide;
  DWORD dwDrvNumberOfPagesPerSide;
  DWORD dwNupBorderFlags;
  DWORD dwJobPageOrderFlags;
  DWORD dwDrvPageOrderFlags;
  DWORD dwJobNumberOfCopies;
  DWORD dwDrvNumberOfCopies;
  DWORD dwColorOptimization;
} ATTRIBUTE_INFO_2, *PATTRIBUTE_INFO_2;
```



## Members

<dl> <dt>

**dwJobNumberOfPagesPerSide**
</dt> <dd>

Number of document pages to be placed on one side of a physical page, as requested by the user. Allowable values are 1, 2, 4, 6, 9, or 16.

</dd> <dt>

**dwDrvNumberOfPagesPerSide**
</dt> <dd>

Number of document pages that the printer and driver can place on one side of a physical page. This value must be 1 or the value specified for **dwJobNumberOfPagesPerSide**.

</dd> <dt>

**dwNupBorderFlags**
</dt> <dd>

One of the following bit flag values:



| Flag                         | Definition                                                               |
|------------------------------|--------------------------------------------------------------------------|
| BORDER\_PRINT<br/>     | The print processor should draw a border around the page.<br/>     |
| NO\_BORDER\_PRINT<br/> | The print processor should not draw a border around the page.<br/> |



 

</dd> <dt>

**dwJobPageOrderFlags**
</dt> <dd>

One of the following bit flag values:



| Flag                      | Definition                                                                                                                                                                                                                                                                |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BOOKLET\_PRINT<br/> | Pages should be printed in booklet form, with two document pages printed on one side of a physical page. In landscape mode, the two document pages are printed side-by-side on the paper. In portrait mode, the two document pages are printed top-and-bottom.<br/> |
| NORMAL\_PRINT<br/>  | Pages should be printed in normal order: page 1, page 2, and so on.<br/>                                                                                                                                                                                            |
| REVERSE\_PRINT<br/> | Pages should be printed in reverse order: last page, next-to-last page, and so on.<br/>                                                                                                                                                                             |



 

</dd> <dt>

**dwDrvPageOrderFlags**
</dt> <dd>

Bit flags indicating which page ordering options are supported by the printer and driver. Uses the same flags as **dwJobPageOrderFlags**.

</dd> <dt>

**dwJobNumberOfCopies**
</dt> <dd>

Number of copies of the print job, as requested by the user.

</dd> <dt>

**dwDrvNumberOfCopies**
</dt> <dd>

Maximum number of copies the printer and driver can handle at once, taking into account such job attributes as collating and stapling.

</dd> <dt>

**dwColorOptimization**
</dt> <dd>

One of the following bit flag values:



| Flag                               | Definition                                                                   |
|------------------------------------|------------------------------------------------------------------------------|
| COLOR\_OPTIMIZATION<br/>     | The print processor should use monochrome color optimization.<br/>     |
| NO\_COLOR\_OPTIMIZATION<br/> | The print processor should not use monochrome color optimization.<br/> |



 

</dd> </dl>

## Remarks

The EMF print processor uses the flag specified for **dwColorOptimization** to determine whether to request GDI to perform monochrome color optimization. If monochrome color optimization is enabled, the print job can be switched between monochrome and color rendering as appropriate.

If you are creating a Unidrv rendering plug-in to generate color watermarks, note that when the **dwColorOptimization** member is set to COLOR\_OPTIMIZATION, color watermarks are printed in black and white when they are printed on black-and-white documents. To ensure that color watermarks print correctly with color and black-and-white documents, disable color optimization. Color optimization also can be controlled by the Unidrv \***ChangeColorModeOnDoc?** color attribute (see [Color Attributes](https://www.bing.com/search?q=Color Attributes)), and by the [**GdiEndPageEMF**](gdiendpageemf.md) function.

For more information about other structure members, see [**ATTRIBUTE\_INFO\_1**](attribute-info-1.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvQueryJobAttributes**](drvqueryjobattributes.md)
</dt> <dt>

[**ATTRIBUTE\_INFO\_1**](attribute-info-1.md)
</dt> <dt>

[**GdiEndPageEMF**](gdiendpageemf.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ATTRIBUTE_INFO_2%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





