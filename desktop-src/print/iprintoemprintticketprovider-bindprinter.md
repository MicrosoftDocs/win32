---
Description: The IPrintOemPrintTicketProviderBindPrinter method enables the core driver to associate a set of private namespace uniform resource identifiers (URIs) with a device.
ms.assetid: 6b31b340-de94-4e6c-a48a-7c1b874eb7cd
title: IPrintOemPrintTicketProviderBindPrinter method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemPrintTicketProvider::BindPrinter method

The `IPrintOemPrintTicketProvider::BindPrinter` method enables the core driver to associate a set of private namespace uniform resource identifiers (URIs) with a device. This method also allows the plug-in to cache information (such as the printer handle) that can be used at a later time.

## Syntax


```C++
HRESULT BindPrinter(
  [in]  HANDLE     hPrinter,
  [in]  INT        version,
  [out] POEMPTOPTS pOptions,
  [out] INT        *cNamespaces,
  [out] BSTR       **ppNamespaces
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

The spooler's print handle, which is supplied by Unidrv. The provider should not close this handle at any time, because the client of the provider is responsible for managing the lifetime of this handle. The provider can cache the print handle; all future calls on this object are relative to the printer that is associated with this handle.

</dd> <dt>

*version* \[in\]
</dt> <dd>

The major version number of the print schema. Windows Vista supports only version 1.

</dd> <dt>

*pOptions* \[out\]
</dt> <dd>

A pointer to a variable that receives one of the following enumerated values:

<dl> <dt>

<span id="OEMPT_DEFAULT"></span><span id="oempt_default"></span>OEMPT\_DEFAULT
</dt> <dd>

The system places a binary encoding (a binary large object \[BLOB\]) of the private [**DEVMODEW**](display.devmodew) structure into the print ticket in a conversion of a DEVMODEW to a print ticket.

</dd> <dt>

<span id="OEMPT_NOSNAPSHOT"></span><span id="oempt_nosnapshot"></span>OEMPT\_NOSNAPSHOT
</dt> <dd>

The system will not place a binary encoding (a BLOB) of the private DEVMODEW structure into the print ticket in a conversion of a DEVMODEW to a print ticket. Use this value if all of the public and private DEVMODEW members are fully represented in the print ticket.

</dd> </dl>

The OEM object that is being called should set the value pointed to by this parameter.

</dd> <dt>

*cNamespaces* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of private namespace URIs that are used in the plug-in. This number represents the count of strings in the array that is pointed to by \**ppNamespaces*.

</dd> <dt>

*ppNamespaces* \[out\]
</dt> <dd>

A pointer to a variable that receives the address of the first element of a BSTR array. The plug-in fills each array position with a namespace URI. For more information about this parameter, see the following Remarks section.

</dd> </dl>

## Return value

`IPrintOemPrintTicketProvider::BindPrinter` should return one of the following values.



| Return code                                                                                               | Description                                                                                                           |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | The operation succeeded.<br/>                                                                                   |
| <dl> <dt>**E\_VERSION\_NOT\_SUPPORTED**</dt> </dl> | The plug-in does not support the version of the print schema that is specified in the *version* parameter.<br/> |



 

## Remarks

The plug-in is responsible for allocating memory for the array that is pointed to by the *ppNamespaces* parameter and for the namespace URI strings. The array should be allocated by using the **CoTaskMemAlloc** function; the namespace strings should be allocated by using the **SysAllocString** function. Both of these functions are described in the Microsoft Windows SDK documentation. The array that is pointed to by the *ppNamespaces* parameter is not required to contain the namespaces for the Print Schema Keywords or the Print Schema Framework.

Binding to a device enables the provider to cache certain objects and handles that it will need for future print ticket or print capabilities services on that device. For example, the printer handle in *hPrinter* can be cached. `IPrintOemPrintTicketProvider::BindPrinter` is guaranteed to be called only once.

An **IPrintTicketProvider** object does not have to be able to bind more than once. The print ticket manager always uses different **IPrintTicketProvider** object instances for binding to different devices. All resources that are acquired in a successful call to `IPrintTicketProvider::BindPrinter` should be released when the reference count of an **IPrintTicketProvider** object is zero. (Note that the provider should not close the handle that was passed into the call to **BindPrinter**). The print ticket manager might create multiple providers for the same device, in different versions, if multiple versions are supported.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemPrintTicketProvider**](iprintoemprintticketprovider-interface.md)
</dt> <dt>

[**IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket**](iprintoemprintticketprovider-convertdevmodetoprintticket.md)
</dt> <dt>

[**IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode**](iprintoemprintticketprovider-convertprinttickettodevmode.md)
</dt> <dt>

[**IPrintOemPrintTicketProvider::GetSupportedVersions**](iprintoemprintticketprovider-getsupportedversions.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPrintTicketProvider::BindPrinter%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





