---
Description: The IPrintOemPrintTicketProvider::ExpandIntentOptions method enables the plug-in to expand printer options (such as photo printing) into individual feature settings in the print ticket.
ms.assetid: c0499a9b-8f02-4a88-bffa-e088e9098a6c
title: IPrintOemPrintTicketProvider::ExpandIntentOptions method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemPrintTicketProvider::ExpandIntentOptions method

The `IPrintOemPrintTicketProvider::ExpandIntentOptions` method enables the plug-in to expand printer options (such as photo printing) into individual feature settings in the print ticket.

## Syntax


```C++
HRESULT ExpandIntentOptions(
  [in, out] IXMLDOMDocument2 *pPrintTicket
);
```



## Parameters

<dl> <dt>

*pPrintTicket* \[in, out\]
</dt> <dd>

A pointer to a print ticket.

</dd> </dl>

## Return value

`IPrintOemPrintTicketProvider::ExpandIntentOptions` should return S\_OK if the operation succeeds or when the plug-in does not support intent features. Otherwise, this method should return a standard COM error code.

## Remarks

The Unidrv or Pscript5 driver calls `IPrintOemPrintTicketProvider::ExpandIntentOptions` to enable the plug-in to expand options that represent intent into their individual settings in other features in the print ticket before print ticket validation. Such option expansion has two important effects: the client receives information about the results of the intent expansion, and the core driver resolves constraints against the individual features that are affected by the intent.

We recommend that the driver preserve the state of the intent option in the driver's private [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure when it converts a print ticket to a DEVMODEW, and then from a DEVMODEW back to a print ticket.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPrintTicketProvider::ExpandIntentOptions%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




