---
Description: The ATTRIBUTE\_INFO\_1 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. All member values are function-supplied.
ms.assetid: 7902877c-4991-48ae-9285-82949f898af2
title: ATTRIBUTE\_INFO\_1 structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ATTRIBUTE\_INFO\_1 structure

The ATTRIBUTE\_INFO\_1 structure is used as a parameter for a printer interface DLL's [**DrvQueryJobAttributes**](drvqueryjobattributes.md) function. All member values are function-supplied.

## Syntax


```C++
typedef struct _ATTRIBUTE_INFO_1 {
  DWORD dwJobNumberOfPagesPerSide;
  DWORD dwDrvNumberOfPagesPerSide;
  DWORD dwNupBorderFlags;
  DWORD dwJobPageOrderFlags;
  DWORD dwDrvPageOrderFlags;
  DWORD dwJobNumberOfCopies;
  DWORD dwDrvNumberOfCopies;
} ATTRIBUTE_INFO_1, *PATTRIBUTE_INFO_1;
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

</dd> </dl>

## Remarks

The caller (the EMF print processor) uses the **dwJobNumberOfPagesPerSide** and **dwDrvNumberOfPagesPerSide** members to determine whether the driver or the print processor handles "N-up" printing.

If the print processor handles "N-up" printing, it checks **dwNupBorderFlags** to determine if it should draw a page border.

The print processor checks **dwJobPageOrderFlags** and **dwDrvPageOrderFlags** to determine the order in which pages should be sent to the printer.

The print processor uses **dwJobNumberOfCopies** and **dwDrvNumberOfCopies** to determine the number of times the print job must be sent to the printer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvQueryJobAttributes**](drvqueryjobattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ATTRIBUTE_INFO_1%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





