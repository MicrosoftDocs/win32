---
Description: 'The IPrintTicketProvider::GetSupportedVersions method retrieves major version numbers of the print schemas that are supported by the plug-in provider.'
ms.assetid: 'ea22cc52-f47b-4a54-b507-5963faa41c2d'
title: 'IPrintTicketProvider::GetSupportedVersions method'
---

# IPrintTicketProvider::GetSupportedVersions method

The `IPrintTicketProvider::GetSupportedVersions` method retrieves major version numbers of the print schemas that are supported by the plug-in provider.

## Syntax


```C++
STDMETHOD GetSupportedVersions(
  [in]  HANDLE hPrinter,
  [out] INT    *ppVersions[],
  [out] INT    *cVersions
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the print device.

</dd> <dt>

*ppVersions\[\]* \[out\]
</dt> <dd>

A pointer to a variable that receives the address of the first element of an array of version numbers. Version numbers in the array can appear in any order. For more information about this parameter, see the following Remarks section.

</dd> <dt>

*cVersions* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of elements in the array that is pointed to by \**ppVersions*.

</dd> </dl>

## Return value

`IPrintTicketProvider::GetSupportedVersions` should return S\_OK if the operation succeeds. If this method fails because of lack of memory or other resources, it should return a standard COM error code.

## Remarks

`IPrintTicketProvider::GetSupportedVersions` returns the major version numbers of the print schemas that are supported by the provider interface. (The only currently defined version number is 1.) Providers can omit intermediate versions

The plug-in is responsible for allocating the array memory that is pointed to by the *ppVersions* parameter. The plug-in should allocate this memory by using the **CoTaskMemAlloc** function (described in the Microsoft Windows SDK documentation), but the plug-in is not responsible for freeing this memory.

Because `IPrintTicketProvider::GetSupportedVersions` can be called before the [**IPrintTicketProvider::BindPrinter**](iprintticketprovider-bindprinter.md) method is called, the OEM plug-in provider must check version support based on the handle that is passed in the *hPrinter* parameter. As a result, the OEM plug-in provider should not close the printer handle that is associated with *hPrinter*.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prdrvcom.h (include Prdrvcom.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintTicketProvider**](iprintticketprovider-interface.md)
</dt> <dt>

[**IPrintTicketProvider::BindPrinter**](iprintticketprovider-bindprinter.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintTicketProvider::GetSupportedVersions%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





