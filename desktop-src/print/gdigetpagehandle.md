---
Description: 'The GdiGetPageHandle function returns a handle to the specified page within a print job.'
ms.assetid: '7eaed9d2-20fa-4cf1-b924-fbe1443535e9'
title: GdiGetPageHandle function
---

# GdiGetPageHandle function

The **GdiGetPageHandle** function returns a handle to the specified page within a print job.

## Syntax


```C++
HANDLE GdiGetPageHandle(
   HANDLE  SpoolFileHandle,
   DWORD   Page,
   LPDWORD pdwPageType
);
```



## Parameters

<dl> <dt>

*SpoolFileHandle* 
</dt> <dd>

Caller-supplied spool file handle, obtained by a previous call to [**GdiGetSpoolFileHandle**](gdigetspoolfilehandle.md).

</dd> <dt>

*Page* 
</dt> <dd>

Caller-supplied page number.

</dd> <dt>

*pdwPageType* 
</dt> <dd>

Caller-supplied pointer to a location that receives the page type. The possible page types are shown in the following table:



| Page Type                  | Meaning                                                                      |
|----------------------------|------------------------------------------------------------------------------|
| EMF\_PP\_FORM<br/>   | The page is a form or has a watermark. (Not currently supported.)<br/> |
| EMF\_PP\_NORMAL<br/> | The page is a normal page.<br/>                                        |



 

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise the function returns **FALSE**, and an error code can be obtained by calling **GetLastError**.

## Remarks

The **GdiGetPageHandle** function is exported by gdi32.dll for use within a print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function.

Print processors must obtain a page handle before calling [**GdiPlayPageEMF**](gdiplaypageemf.md) to draw a page. If a Page value is specified that is too large, the function returns ERROR\_NO\_MORE\_ITEMS.

For additional information, see [Using GDI Functions in Print Processors](print.using_gdi_functions_in_print_processors).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Winppi.h (include Winppi.h)</dt> </dl>                                  |
| Library<br/>         | <dl> <dt>Gdi32.Lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Gdi32.dll</dt> </dl>                                                    |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GdiGetPageHandle%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




