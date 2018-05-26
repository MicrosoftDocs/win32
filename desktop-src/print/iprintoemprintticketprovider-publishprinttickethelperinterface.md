---
Description: The IPrintOemPrintTicketProviderPublishPrintTicketHelperInterface method publishes the print ticket helper interface for either Unidrv or Pscript5 user interface (UI) plug-ins.
ms.assetid: d7512da3-eb47-4e22-9df8-b152b39cbcad
title: IPrintOemPrintTicketProviderPublishPrintTicketHelperInterface method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemPrintTicketProvider::PublishPrintTicketHelperInterface method

The `IPrintOemPrintTicketProvider::PublishPrintTicketHelperInterface` method publishes the print ticket helper interface for either Unidrv or Pscript5 user interface (UI) plug-ins.

## Syntax


```C++
HRESULT PublishPrintTicketHelperInterface(
  [in] IUnknown *pHelper
);
```



## Parameters

<dl> <dt>

*pHelper* \[in\]
</dt> <dd>

A pointer to an **IUnknown** interface, which should be cast to one of the following interfaces: For Unidrv plug-ins, the print ticket helper interface is **IPrintCoreHelperUni**; for Pscript5 plug-ins, the print ticket helper interface is **IPrintCoreHelperPS**.

</dd> </dl>

## Return value

`IPrintOemPrintTicketProvider::PublishPrintTicketHelperInterface` should return S\_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

## Remarks

If the plug-in maintains a handle to the helper object, the plug-in is responsible for later releasing that handle when it is no longer needed.

If `IPrintOemPrintTicketProvider::PublishPrintTicketHelperInterface` uses the helper interface, it should cache a pointer to the interface, and increment the reference count (by means of a call to the interface's **AddRef** method). If this method successfully increments the reference count, it should return S\_OK.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPrintTicketProvider::PublishPrintTicketHelperInterface%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




