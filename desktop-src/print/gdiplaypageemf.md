---
Description: The GdiPlayPageEMF function plays the EMF records within a specified rectangle for one document page of a spooled print job.
ms.assetid: e0122858-0c9d-4aa8-a394-89d65fb98fda
title: GdiPlayPageEMF function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GdiPlayPageEMF function

The **GdiPlayPageEMF** function plays the EMF records within a specified rectangle for one document page of a spooled print job.

## Syntax


```C++
BOOL GdiPlayPageEMF(
   HANDLE SpoolFileHandle,
   HANDLE hemf,
   RECT   *prectDocument,
   RECT   *prectBorder,
   RECT   *prectClip
);
```



## Parameters

<dl> <dt>

*SpoolFileHandle* 
</dt> <dd>

Caller-supplied spool file handle, obtained by a previous call to [**GdiGetSpoolFileHandle**](gdigetspoolfilehandle.md).

</dd> <dt>

*hemf* 
</dt> <dd>

Caller-supplied page handle, obtained by calling [**GdiGetPageHandle**](gdigetpagehandle.md), identifying the page for which records are to be played.

</dd> <dt>

*prectDocument* 
</dt> <dd>

Caller-supplied pointer to a [**RECT**](https://msdn.microsoft.com/a44f33f4-49b2-4a36-a7bd-fc4a9d3a3943) structure specifying the rectangle into which the page is to be drawn.

</dd> <dt>

*prectBorder* 
</dt> <dd>

Caller-supplied pointer to a RECT structure specifying the page's border rectangle (if any). Can be **NULL**.

</dd> <dt>

*prectClip* 
</dt> <dd>

Caller-supplied pointer to a RECT structure specifying the coordinates of the page's clip region (if any). Can be **NULL**.

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise the function returns **FALSE**, and an error code can be obtained by calling **GetLastError**.

## Remarks

The **GdiPlayPageEMF** function is exported by gdi32.dll for use within a print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function.

The **GdiPlayPageEMF** function is the means by which a print processor positions a document page or a specified rectangular region of a document page on a physical page. Note that **GdiPlayPageEMF** does not actually print on the device context, but instead prepares a data structure that describes the text and graphics that are to be printed on the physical page(s). The text and graphics are printed to the device context when [**GdiEndPageEMF**](gdiendpageemf.md) is called.

The print processor uses *prectClip* to describe the rectangular region to be printed, and *prectDocument* to describe a rectangle into which the document page (or clipped region) must fit. If *prectClip* is **NULL**, the entire document page will be printed. For non-**NULL** values of *prectClip*, only the portion of the document page within the clip region will be printed. The **GdiPlayPageEMF** function then performs the scaling and translation operations required to make the document page (or selected portion) fit into the rectangle.

The *prectBorder* parameter, if it is non-**NULL**, describes a solid-line border rectangle to be drawn around the document page. If *prectBorder* is **NULL**, no such border will be drawn.

For additional information, see [Using GDI Functions in Print Processors](https://www.bing.com/search?q=Using+GDI+Functions+in+Print+Processors).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Winppi.h (include Winppi.h)</dt> </dl>                                  |
| Library<br/>         | <dl> <dt>Gdi32.Lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Gdi32.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**GdiEndPageEMF**](gdiendpageemf.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GdiPlayPageEMF%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





