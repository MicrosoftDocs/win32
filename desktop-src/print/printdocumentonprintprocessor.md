---
Description: A print processor's PrintDocumentOnPrintProcessor function converts a print job from a spooled format into raw data that can be sent to a print monitor.
ms.assetid: 1360a699-e312-40be-bf2f-b73b1419cfc5
title: PrintDocumentOnPrintProcessor function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PrintDocumentOnPrintProcessor function

A print processor's `PrintDocumentOnPrintProcessor` function converts a print job from a spooled format into raw data that can be sent to a print monitor.

## Syntax


```C++
BOOL PrintDocumentOnPrintProcessor(
  _In_ HANDLE hPrintProcessor,
  _In_ LPWSTR pDocumentName
);
```



## Parameters

<dl> <dt>

*hPrintProcessor* \[in\]
</dt> <dd>

Caller-supplied print processor handle. This is the handle returned by a previous call to [**OpenPrintProcessor**](openprintprocessor.md).

</dd> <dt>

*pDocumentName* \[in\]
</dt> <dd>

Caller-supplied pointer to the document name.

</dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**. If the operation fails, the function should call **SetLastError** to set an error code, and then return **FALSE**.

## Remarks

Print processors are required to export a `PrintDocumentOnPrintProcessor` function. The spooler calls the function after calling [**OpenPrintProcessor**](openprintprocessor.md). The function's purpose is to read the contents of the file named by *pDocumentName*, convert (if necessary) the file's data to a data stream that can be read by printer hardware, and to send the data stream back to the spooler. The spooler can then send the data stream to the appropriate [*print monitor*](wdkgloss.p#wdkgloss-print-monitor).

If the input format is NT-based operating system EMF, the `PrintDocumentOnPrintProcessor` function can call [GDI functions for print processors](gdi-functions-for-print-processors.md). For more information, see [Processing a Print Job](https://www.bing.com/search?q=Processing+a+Print+Job).

The converted data stream must be sent back to the spooler by calling **WritePrinter**, which is described in the Microsoft Windows SDK documentation. For more information, see [Processing a Print Job](https://www.bing.com/search?q=Processing+a+Print+Job).

The `PrintDocumentOnPrintProcessor` function must be written to handle requests to pause, resume, or cancel the print job. For more information, see [**ControlPrintProcessor**](controlprintprocessor.md).

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Nwprint.lib</dt> </dl>                   |



## See also

<dl> <dt>

[**OpenPrintProcessor**](openprintprocessor.md)
</dt> <dt>

[**ControlPrintProcessor**](controlprintprocessor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PrintDocumentOnPrintProcessor%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





