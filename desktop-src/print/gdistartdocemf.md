---
Description: The GdiStartDocEMF function performs initialization operations for an EMF-formatted print job.
ms.assetid: aca4534a-871e-4d86-b329-cb4f84611a29
title: GdiStartDocEMF function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GdiStartDocEMF function

The **GdiStartDocEMF** function performs initialization operations for an EMF-formatted print job.

## Syntax


```C++
BOOL GdiStartDocEMF(
   HANDLE   SpoolFileHandle,
   DOCINFOW *pDocInfo
);
```



## Parameters

<dl> <dt>

*SpoolFileHandle* 
</dt> <dd>

Caller-supplied spool file handle, obtained by a previous call to [**GdiGetSpoolFileHandle**](gdigetspoolfilehandle.md).

</dd> <dt>

*pDocInfo* 
</dt> <dd>

Caller-supplied pointer to a DOCINFOW structure (described in the Microsoft Window SDK documentation).

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise the function returns **FALSE**, and an error code can be obtained by calling **GetLastError**.

## Remarks

The **GdiStartDocEMF** function is exported by gdi32.dll for use within a print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function.

The function performs initializations that must take place before a print job's EMF records can be played. The function calls the spooler's **StartDoc** function (described in the Window SDK documentation), which in turn calls the printer driver's [**DrvStartDoc**](https://msdn.microsoft.com/f73adc24-2e61-4b62-9d38-12a23b62ed01) function.

The print processor must set the **lpszOutput** member of the DOCINFOW structure to the output file name contained in the [**PRINTPROCESSOROPENDATA**](printprocessoropendata.md) structure, previously received by the [**OpenPrintProcessor**](openprintprocessor.md) function.

The print processor must set the **lpszDocName** member of the DOCINFOW structure to the document name pointer, previously received by the [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function.

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

[**GdiEndDocEMF**](gdienddocemf.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GdiStartDocEMF%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





