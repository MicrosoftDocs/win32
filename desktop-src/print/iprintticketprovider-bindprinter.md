---
Description: 'The IPrintTicketProvider::BindPrinter method binds a printer or print queue to a specific version of the print ticket schema, which enables the core driver to associate a set of private namespace uniform resource identifiers (URIs) with a device.'
ms.assetid: '6176b80c-0e99-4c37-94fc-25ed1d55b66c'
title: 'IPrintTicketProvider::BindPrinter method'
---

# IPrintTicketProvider::BindPrinter method

The `IPrintTicketProvider::BindPrinter` method binds a printer or print queue to a specific version of the print ticket schema, which enables the core driver to associate a set of private namespace uniform resource identifiers (URIs) with a device.

## Syntax


```C++
HRESULT BindPrinter(
  [in]  HANDLE    hPrinter,
  [in]  INT       version,
  [out] PSHIMOPTS pOptions,
  [out] DWORD     *pDevModeFlags,
  [out] INT       *cNamespaces,
  [out] BSTR      **ppNamespaces
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

The spooler's print handle, which is supplied by the core driver. The provider should not close this handle at any time because the client of the provider is responsible for managing the lifetime of this handle. The provider can cache the print handle; all future calls are relative to the printer that is associated with this handle.

</dd> <dt>

*version* \[in\]
</dt> <dd>

The major version number of the print ticket or print ticket schema that the print ticket manager requests the OEM plug-in provider to support. Windows Vista supports only version 1. The provider should fail any attempt to bind to a version that it does not support or recognize.

</dd> <dt>

*pOptions* \[out\]
</dt> <dd>

A pointer to a variable that receives one of the following enumerated values:

<dl> <dt>

<span id="PTSHIM_DEFAULT"></span><span id="ptshim_default"></span>PTSHIM\_DEFAULT
</dt> <dd>

The system places a binary encoding (a binary large object \[BLOB\]) of the private portion of the [**DEVMODEW**](display.devmodew) structure into the print ticket in a conversion of a DEVMODEW to a print ticket.

</dd> <dt>

<span id="PTSHIM_NOSNAPSHOT"></span><span id="ptshim_nosnapshot"></span>PTSHIM\_NOSNAPSHOT
</dt> <dd>

The system will not place a binary encoding (a BLOB) of the private portion of the DEVMODEW structure into the print ticket in a conversion of a DEVMODEW to a print ticket. Use this value if all of the public and private DEVMODEW members are fully represented in the print ticket.

</dd> </dl>

The object that is being called should set the value pointed to by this parameter.

</dd> <dt>

*pDevModeFlags* \[out\]
</dt> <dd>

A pointer to a DWORD-typed variable that receives a set of bit flags that indicate which public [**DEVMODEW**](display.devmodew) members should not be processed by the print ticket shim in DEVMODEW-to-print ticket or print ticket-to-DEVMODEW conversions. A bit flag that is present in this parameter indicates either that the printer does not support the associated DEVMODEW member or that the provider handles that DEVMODEW characteristic. For example, if DM\_MEDIATYPE is set in \**pDevModeFlags*, either the printer does not support multiple media types, or the provider is responsible for supporting multiple media types. (All of the DM\_*XXX* bit flags are defined in wingdi.h and described in the Microsoft Windows SDK.) By default, the print ticket shim handles all of the members that are represented in the **dmFlags** member of the default DEVMODEW structure.

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

`IPrintTicketProvider::BindPrinter` should return one of the following values.



| Return code                                                                                               | Description                                                                                                           |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | The operation succeeded.<br/>                                                                                   |
| <dl> <dt>**E\_VERSION\_NOT\_SUPPORTED**</dt> </dl> | The plug-in does not support the version of the print schema that is specified in the *version* parameter.<br/> |



 

## Remarks

Binding to a device enables the provider to cache certain objects and handles that it will need for future print ticket or device capabilities services on that device. For example, the printer handle in the *hPrinter* parameter can be cached. The `IPrintTicketProvider::BindPrinter` method is guaranteed to be called only once.

The driver is responsible for allocating memory for the array that is pointed to by the *ppNamespaces* parameter and for the namespace URI strings. The array should be allocated by using the **CoTaskMemAlloc** function; the namespace strings should be allocated by using the **SysAllocString** function. Both functions are described in the Windows SDK documentation. The array that is pointed to by the *ppNamespaces* parameter is not required to contain the namespaces for the Print Schema Keywords or the Print Schema Framework.

An **IPrintTicketProvider** object does not have to be able to bind more than once. The print ticket manager always uses different **IPrintTicketProvider** object instances for binding to different devices. All resources that are acquired in a successful call to `IPrintTicketProvider::BindPrinter` should be released when the reference count of an **IPrintTicketProvider** object is zero. (Note that the provider should not close the handle that was passed into the call to `BindPrinter`). The print ticket manager might create multiple providers for the same device, in different versions, if multiple versions are supported.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintTicketProvider**](iprintticketprovider-interface.md)
</dt> <dt>

[**IPrintTicketProvider::ConvertDevModeToPrintTicket**](iprintticketprovider-convertdevmodetoprintticket.md)
</dt> <dt>

[**IPrintTicketProvider::ConvertPrintTicketToDevMode**](iprintticketprovider-convertprinttickettodevmode.md)
</dt> <dt>

[**IPrintTicketProvider::GetSupportedVersions**](iprintticketprovider-getsupportedversions.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintTicketProvider::BindPrinter%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





