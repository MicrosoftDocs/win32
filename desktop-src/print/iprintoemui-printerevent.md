---
Description: The IPrintOemUI::PrinterEvent method allows a user interface plug-in to process printer events.
ms.assetid: 214ea4d8-3bf9-4248-8bfa-7180635769be
title: IPrintOemUI::PrinterEvent method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUI::PrinterEvent method

The `IPrintOemUI::PrinterEvent` method allows a user interface plug-in to process printer events.

## Syntax


```C++
HRESULT PrinterEvent(
   PWSTR  pPrinterName,
   INT    iDriverEvent,
   DWORD  dwFlags,
   LPARAM lParam
);
```



## Parameters

<dl> <dt>

*pPrinterName* 
</dt> <dd>

Caller-supplied pointer to a NULL-terminated printer name string. The string can identify a local printer ("*PrinterName*") or remote printer ("\\\\*Machine*\\*PrinterName*").

</dd> <dt>

*iDriverEvent* 
</dt> <dd>

Caller-supplied value identifying the event that has occurred. For a list of valid values, see [**DrvPrinterEvent**](drvprinterevent.md).

</dd> <dt>

*dwFlags* 
</dt> <dd>

Caller-supplied flags. For a list of valid flags, see **DrvPrinterEvent**.

</dd> <dt>

*lParam* 
</dt> <dd>

Caller-supplied event-specific parameter. For more information, see **DrvPrinterEvent**.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

A user interface plug-in's `IPrintOemUI::PrinterEvent` method performs the same types of operations as the **DrvPrinterEvent** function that is exported by user-mode printer interface DLLs. For information about printer events and how they should be processed, see the description of the [**DrvPrinterEvent**](drvprinterevent.md) function.

If you provide a user interface plug-in, the printer driver's **DrvPrinterEvent** function calls the `IPrintOemUI::PrinterEvent` method. The **DrvPrinterEvent** function performs its own processing for the specified event, and then calls the `IPrintOemUI::PrinterEvent` method to handle additional processing of the event.

If `IPrintOemUI::PrinterEvent` methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.

For more information about creating and installing user interface plug-ins, see [Customizing Microsoft's Printer Drivers](https://www.bing.com/search?q=Customizing Microsoft's Printer Drivers).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUI**](iprintoemui-interface.md)
</dt> <dt>

[**DrvPrinterEvent**](drvprinterevent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::PrinterEvent%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





