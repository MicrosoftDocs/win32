---
Description: 'A print processor''s OpenPrintProcessor function prepares the print processor for printing a job and returns a handle.'
ms.assetid: 'bab79fb6-1bb0-48ec-9d60-fcb6e679b758'
title: OpenPrintProcessor function
---

# OpenPrintProcessor function

A print processor's `OpenPrintProcessor` function prepares the print processor for printing a job and returns a handle.

## Syntax


```C++
HANDLE OpenPrintProcessor(
  _In_ LPWSTR                  pPrinterName,
  _In_ PPRINTPROCESSOROPENDATA pPrintProcessorOpenData
);
```



## Parameters

<dl> <dt>

*pPrinterName* \[in\]
</dt> <dd>

Caller-supplied pointer to the name of the printer for which the print processor is being opened.

</dd> <dt>

*pPrintProcessorOpenData* \[in\]
</dt> <dd>

Caller-supplied pointer to a [**PRINTPROCESSOROPENDATA**](printprocessoropendata.md) structure.

</dd> </dl>

## Return value

If the operation succeeds, the function should return a handle that can be used as an input argument for subsequent calls to [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md), [**ControlPrintProcessor**](controlprintprocessor.md), and [**ClosePrintProcessor**](closeprintprocessor.md). If the operation fails, the function should call **SetLastError** to set an error code, and then return **NULL**.

## Remarks

Print processors are required to export an `OpenPrintProcessor` function. The spooler calls the function when a print job is available. The function should perform initialization operations that are required before a job can be processed, based on the job's data type.

The function must return a handle. Typically, the handle is a pointer to an internal structure. The structure must contain a pointer to the printer's name and a pointer to the printer's [**DEVMODEW**](display.devmodew) structure, both of which are received in the [**PRINTPROCESSOROPENDATA**](printprocessoropendata.md) structure. These two pointers are required by the print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function, and this latter function receives the handle as input when the spooler calls it.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Nwprint.lib</dt> </dl>                   |



## See also

<dl> <dt>

[**PRINTPROCESSOROPENDATA**](printprocessoropendata.md)
</dt> <dt>

[**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md)
</dt> <dt>

[**ControlPrintProcessor**](controlprintprocessor.md)
</dt> <dt>

[**ClosePrintProcessor**](closeprintprocessor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OpenPrintProcessor%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





