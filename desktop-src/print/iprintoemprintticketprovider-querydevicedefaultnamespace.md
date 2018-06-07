---
Description: The IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace method queries the device for its default namespace uniform resource identifier (URI).
ms.assetid: 1af15e59-8796-48e2-ab18-a450db3086d3
title: IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace method

The `IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace` method queries the device for its default namespace uniform resource identifier (URI).

## Syntax


```C++
HRESULT QueryDeviceDefaultNamespace(
  [out] BSTR *pbstrNamespaceUri
);
```



## Parameters

<dl> <dt>

*pbstrNamespaceUri* \[out\]
</dt> <dd>

A pointer to a BSTR that receives the namespace URI. The plug-in places the namespace URI in the buffer that is pointed to by *pbstrNamespaceUri*. `IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace` is responsible for allocating the string by means of a call to **SysAllocString** (described in the Microsoft Windows SDK documentation), but the caller is responsible for freeing the string.

</dd> </dl>

## Return value

`IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace` should return one of the following values.



| Return code                                                                               | Description                                                                                                                          |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>                                                                                                  |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The plug-in does not intend to override the default namespace that the core driver generated from the plug-in's provider.<br/> |



 

## Remarks

The plug-in should specify the name of the private namespace URI that the core driver should use to handle any features that are defined in the GPD file or PPD file that the core driver does not recognize. The plug-in might specify a set of namespaces as a result of the call to the [**IPrintOemPrintTicketProvider::BindPrinter**](iprintoemprintticketprovider-bindprinter.md) method. The purpose of the `IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace` is to inform the core driver about which of these namespaces is to be used as the default namespace. The core driver associates all of the features that it does not recognize with this default namespace, and places any such features in the print ticket.

> [!Note]  
> When `IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace` returns, the core driver is responsible for adding the private namespace URI that the plug-in has specified (in \**pbstrNamespaceUri*) to the root node of the DOM document. The core driver also must define a prefix for the private namespace that the plug-in should use when the plug-in adds a new node to the print ticket under the plug-in's private namespace. The plug-in should not define its own prefix for this default private namespace URI.

 

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemPrintTicketProvider**](iprintoemprintticketprovider-interface.md)
</dt> <dt>

[**IPrintOemPrintTicketProvider::BindPrinter**](iprintoemprintticketprovider-bindprinter.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





