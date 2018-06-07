---
Description: The GdiGetDevmodeForPage function returns DEVMODEW structures for the specified and previous pages of a print job.
ms.assetid: 3410e8b1-820f-4892-8d26-d803e3f943da
title: GdiGetDevmodeForPage function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GdiGetDevmodeForPage function

The **GdiGetDevmodeForPage** function returns [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structures for the specified and previous pages of a print job.

## Syntax


```C++
BOOL GdiGetDevmodeForPage(
   HANDLE    SpoolFileHandle,
   DWORD     dwPageNumber,
   PDEVMODEW *pCurrDM,
   PDEVMODEW *pLastDM
);
```



## Parameters

<dl> <dt>

*SpoolFileHandle* 
</dt> <dd>

Caller-supplied spool file handle, obtained by a previous call to [**GdiGetSpoolFileHandle**](gdigetspoolfilehandle.md).

</dd> <dt>

*dwPageNumber* 
</dt> <dd>

Caller-supplied number of the page for which [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) contents are to be returned.

</dd> <dt>

*pCurrDM* 
</dt> <dd>

Caller-supplied location to receive a pointer to a DEVMODE structure for the page specified by *dwPageNumber*.

</dd> <dt>

*pLastDM* 
</dt> <dd>

Caller-supplied location to receive a pointer to a DEVMODE structure for the page previous to the one specified by *dwPageNumber*.

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise it returns **FALSE**.

## Remarks

The **GdiGetDevmodeForPage** function is exported by gdi32.dll for use within a print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function.

Before calling [**GdiPlayPageEMF**](gdiplaypageemf.md) to execute a page's EMF instructions, a print processor must call **GdiGetDevmodeForPage** to determine if the DEVMODE structure associated with the page to be printed is the same as that of the last page printed. If the two returned DEVMODE structures are not identical, the print processor must perform the following steps, in order, before calling **GdiPlayPageEMF** for the page:

1.  Call [**GdiEndPageEMF**](gdiendpageemf.md).

2.  Call [**GdiResetDCEMF**](gdiresetdcemf.md), specifying the DEVMODE pointed to by *pCurrDM*.

3.  Call [**GdiStartPageEMF**](gdistartpageemf.md).

For additional information, see [Using GDI Functions in Print Processors](https://www.bing.com/search?q=Using+GDI+Functions+in+Print+Processors).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Winppi.h (include Winppi.h)</dt> </dl>                                  |
| Library<br/>         | <dl> <dt>Gdi32.Lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Gdi32.dll</dt> </dl>                                                    |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GdiGetDevmodeForPage%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




