---
Description: The ATTRIBUTE\_INFO\_4 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function.
ms.assetid: 09071fff-834b-452b-ae1e-b75c9f191b15
title: ATTRIBUTE\_INFO\_4 structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ATTRIBUTE\_INFO\_4 structure

The ATTRIBUTE\_INFO\_4 structure is used as a parameter for a printer interface DLL's [**DrvQueryJobAttributes**](drvqueryjobattributes.md) function. All member values are function-supplied. This structure is similar to [**ATTRIBUTE\_INFO\_3**](attribute-info-3.md), but it includes additional members to control N-up, duplex and booklet printing, and scaling.

## Syntax


```C++
typedef struct _ATTRIBUTE_INFO_4 {
  DWORD dwJobNumberOfPagesPerSide;
  DWORD dwDrvNumberOfPagesPerSide;
  DWORD dwNupBorderFlags;
  DWORD dwJobPageOrderFlags;
  DWORD dwDrvPageOrderFlags;
  DWORD dwJobNumberOfCopies;
  DWORD dwDrvNumberOfCopies;
  DWORD dwColorOptimization;
  short dmPrintQuality;
  short dmYResolution;
  DWORD dwDuplexFlags;
  DWORD dwNupDirection;
  DWORD dwBookletFlags;
  DWORD dwScalingPercentX;
  DWORD dwScalingPercentY;
} ATTRIBUTE_INFO_4, *PATTRIBUTE_INFO_4;
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



 

</dd> <dt>

**dmPrintQuality**
</dt> <dd>

Value to be used instead of the **dmPrintQuality** member of the print job's [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure, if the COLOR\_OPTIMIZATION flag is set in **dwColorOptimization**.

</dd> <dt>

**dmYResolution**
</dt> <dd>

Value to be used instead of the **dmYResolution** member of the print job's DEVMODEW structure, if the COLOR\_OPTIMIZATION flag is set in **dwColorOptimization**.

</dd> <dt>

**dwDuplexFlags**
</dt> <dd>

One of the following bit flag values used in duplex printing:



| Flag                                             | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DONT\_SEND\_EXTRA\_PAGES\_FOR\_DUPLEX<br/> | The print processor should not send extra blank pages when duplex printing.<br/> For example, if you send a three-page job for duplex printing, some printers expect to receive four pages. If you print this job on Microsoft Windows XP or Windows Server 2003, the print processor sends four pages to the printer by default (the fourth page is a blank page). If you print this job on Windows Vista with this flag set, the print processor sends only the three pages of the print job and does not send the extra blank page.<br/> |
| REVERSE\_PAGES\_FOR\_REVERSE\_DUPLEX<br/>  | The print processor should reverse the order of page pairs when printing in reverse duplex mode. For example, when this flag is set, the print processor should print pages in order 7, 8, 5, 6, 3, 4, 1, 2 instead of 8, 7, 6, 5, 4, 3, 2, 1.<br/>                                                                                                                                                                                                                                                                                               |



 

Set to 0 if your driver does not require any of these options.

</dd> <dt>

**dwNupDirection**
</dt> <dd>

One of the following bit flag values used in N-up printing:



| Flag                         | Definition                                                                                                                                                                         |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RIGHT\_THEN\_DOWN<br/> | The print processor should provide page images in sequence from left to right, then down the final printed page. Also set to this value if N-up printing is not needed.<br/> |
| DOWN\_THEN\_RIGHT<br/> | The print processor should provide page images in sequence from top to bottom, then left to right on the final printed page.<br/>                                            |
| LEFT\_THEN\_DOWN<br/>  | The print processor should provide page images in sequence from right to left, then down the final printed page.<br/>                                                        |
| DOWN\_THEN\_LEFT<br/>  | The print processor should provide page images in sequence from top to bottom, then right to left on the final printed page.<br/>                                            |



 

This flag is considered only if **dwJobNumberOfPagesPerSide** and/or **dwDrvNumberOfPagesPerSide** indicate that N-up printing is active. For more information, see the descriptions above for **dwJobNumberOfPagesPerSide** and **dwDrvNumberOfPagesPerSide**.

</dd> <dt>

**dwBookletFlags**
</dt> <dd>

If **dwJobPageOrderFlags** is set to BOOKLET\_PRINT, one of the following values.



| Flag                            | Definition                                                                                                                                                              |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BOOKLET\_EDGE\_LEFT<br/>  | The print processor should print pages in a left-to-right booklet layout, where the bound edge of the final folded booklet is on the left edge of page one.<br/>  |
| BOOKLET\_EDGE\_RIGHT<br/> | The print processor should print pages in a right-to-left booklet layout, where the bound edge of the final folded booklet is on the right edge of page one.<br/> |



 

If **dwJobPageOrderFlags** is not set to BOOKLET\_PRINT, **dwBookletFlags** is set to 0.

This flag is considered only if the **dwJobPageOrderFlags** member is set to BOOKLET\_PRINT.

</dd> <dt>

**dwScalingPercentX**
</dt> <dd>

Scaling percentage in the horizontal (x) direction with respect to the normal paper size. Must be in the range of 1 to 1000. Set to 100 if scaling will not be done.

> [!Note]  
> To ensure predictable printing results, **dwScalingPercentX** and **dwScalingPercentY** must have the same value.

 

</dd> <dt>

**dwScalingPercentY**
</dt> <dd>

Scaling percentage in the vertical (y) direction with respect to the normal paper size. Must be in the range of 1 to 1000. Set to 100 if scaling will not be done.

> [!Note]  
> To ensure predictable printing results, **dwScalingPercentX** and **dwScalingPercentY** must have the same value.

 

</dd> </dl>

## Remarks

If the **dmPrintQuality** member of a print job's DEVMODEW structure is a negative value, such as DMRES\_HIGH, and if monochrome color optimization is enabled, then switching between color and monochrome could result in different resolutions being used. This is because DMRES\_HIGH might be assigned to different DPI values for color and monochrome rendering. (For Unidrv-supported devices, this assignment occurs in the printer's [*GPD*](wdkgloss.g#wdkgloss-generic-printer-description--gpd-) file.) To ensure a consistent resolution throughout the print job, the driver can specify positive **dmPrintQuality** and **dmYResolution** values (representing a specific DPI resolution) to override the equivalent [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) values.

The EMF print processor uses the flag specified for **dwColorOptimization** to determine whether to request GDI to perform monochrome color optimization. If monochrome color optimization is enabled, the print job can be switched between monochrome and color rendering as appropriate.

If you are creating a Unidrv rendering plug-in to generate color watermarks, note that when the **dwColorOptimization** member is set to COLOR\_OPTIMIZATION, color watermarks are printed in black and white when they are printed on black-and-white documents. To ensure that color watermarks print correctly with color and black-and-white documents, disable color optimization. Color optimization also can be controlled by the Unidrv \***ChangeColorModeOnDoc?** color attribute (see [Color Attributes](https://www.bing.com/search?q=Color+Attributes)), and by the [**GdiEndPageEMF**](gdiendpageemf.md) function.

For a list of default values for ATTRIBUTE\_INFO\_4 members, see [**GetJobAttributesEx**](getjobattributesex.md).

This structure is available in Windows Vista.

## Requirements



|                   |                                                                                                                         |
|-------------------|-------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h or Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**ATTRIBUTE\_INFO\_2**](attribute-info-2.md)
</dt> <dt>

[**ATTRIBUTE\_INFO\_3**](attribute-info-3.md)
</dt> <dt>

[**DrvQueryJobAttributes**](drvqueryjobattributes.md)
</dt> <dt>

[**GetJobAttributesEx**](getjobattributesex.md)
</dt> <dt>

[**GdiEndPageEMF**](gdiendpageemf.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ATTRIBUTE_INFO_4%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





