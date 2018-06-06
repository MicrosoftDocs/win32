---
Description: The GdiGetPageCount function returns the number of pages in a print job.
ms.assetid: 0a101b59-c610-4158-97a8-002222a94309
title: GdiGetPageCount function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GdiGetPageCount function

The **GdiGetPageCount** function returns the number of pages in a print job.

## Syntax


```C++
DWORD GdiGetPageCount(
   HANDLE SpoolFileHandle
);
```



## Parameters

<dl> <dt>

*SpoolFileHandle* 
</dt> <dd>

Caller-supplied spool file handle, obtained by a previous call to [**GdiGetSpoolFileHandle**](gdigetspoolfilehandle.md).

</dd> </dl>

## Return value

If the operation succeeds, the function returns the number of pages in the current print job. Otherwise the function returns zero.

## Remarks

The **GdiGetPageCount** function is exported by gdi32.dll for use within a print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function.

> [!Note]The **GdiGetPageCount** function does not return until all pages have been spooled, even if the print server administrator has specified that print jobs should be printed during spooling. Therefore, this function should not be used unless it is necessary to obtain the total page count before document processing can begin, such as for printing pages in reverse order.
>
> Usually, a better method for determining the page count is to count the number of calls made to [**GdiGetPageHandle**](gdigetpagehandle.md).

 

For additional information about this set of functions, see [Using GDI Functions in Print Processors](https://www.bing.com/search?q=Using+GDI+Functions+in+Print+Processors).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Winppi.h (include Winppi.h)</dt> </dl>                                  |
| Library<br/>         | <dl> <dt>Gdi32.Lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Gdi32.dll</dt> </dl>                                                    |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GdiGetPageCount%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




