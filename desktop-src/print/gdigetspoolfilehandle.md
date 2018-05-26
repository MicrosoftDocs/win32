---
Description: The GdiGetSpoolFileHandle function returns a handle to a print jobs EMF file.
ms.assetid: c820ee94-29c2-4478-884c-49dd68cd713a
title: GdiGetSpoolFileHandle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GdiGetSpoolFileHandle function

The **GdiGetSpoolFileHandle** function returns a handle to a print job's EMF file.

## Syntax


```C++
HANDLE GdiGetSpoolFileHandle(
   LPWSTR     pwszPrinterName,
   LPDEVMODEW pDevmode,
   LPWSTR     pwszDocName
);
```



## Parameters

<dl> <dt>

*pwszPrinterName* 
</dt> <dd>

Caller-supplied pointer to a string representing the name of the target printer. See the following Remarks section.

</dd> <dt>

*pDevmode* 
</dt> <dd>

Caller-supplied pointer to a [**DEVMODEW**](display.devmodew) structure. See the following Remarks section.

</dd> <dt>

*pwszDocName* 
</dt> <dd>

Caller-supplied pointer to the print job's document name. See the following Remarks section.

</dd> </dl>

## Return value

If the operation succeeds, the function returns a spool file handle. Otherwise the function returns **NULL**.

## Remarks

The **GdiGetSpoolFileHandle** function is exported by gdi32.dll for use within a print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function.

When a print processor calls **GdiGetSpoolFileHandle**, it should supply arguments as illustrated in the following table.



| Parameter                    | Argument                                                                                                                                                                                                                                               |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *pwszPrinterName*<br/> | Pointer to the printer name received by the print processor's [**OpenPrintProcessor**](openprintprocessor.md) function.<br/>                                                                                                                    |
| *pDevmode*<br/>        | Pointer to the [**DEVMODEW**](display.devmodew) structure contained in the [**PRINTPROCESSOROPENDATA**](printprocessoropendata.md) structure, received by the print processor's [**OpenPrintProcessor**](openprintprocessor.md) function.<br/> |
| *pwszDocName*<br/>     | Document name pointer received by the print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function.<br/>                                                                                                    |



 

A print processor must call the **GdiGetSpoolFileHandle** function before calling any other GDI printing functions, because the returned handle must be passed to the other functions. The function calls OpenPrinter to open a connection to the printer, and CreateDC to create a device context for drawing. The print processor can obtain the device context's handle by calling [**GdiGetDC**](gdigetdc.md).

For additional information, see [Using GDI Functions in Print Processors](print.using_gdi_functions_in_print_processors).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Winppi.h (include Winppi.h)</dt> </dl>                                  |
| Library<br/>         | <dl> <dt>Gdi32.Lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Gdi32.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**GdiDeleteSpoolFileHandle**](gdideletespoolfilehandle.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GdiGetSpoolFileHandle%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





