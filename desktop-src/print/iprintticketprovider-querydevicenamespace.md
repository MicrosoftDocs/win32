---
Description: 'The IPrintTicketProvider::QueryDeviceNamespace method queries the device for its default namespace uniform resource identifier (URI).'
ms.assetid: 'd4a36a33-f8b8-4b8c-8ff7-918cb8ba79cb'
title: 'IPrintTicketProvider::QueryDeviceNamespace method'
---

# IPrintTicketProvider::QueryDeviceNamespace method

The `IPrintTicketProvider::QueryDeviceNamespace` method queries the device for its default namespace uniform resource identifier (URI).

## Syntax


```C++
HRESULT QueryDeviceNamespace(
  [out] BSTR *pDefaultNamespace
);
```



## Parameters

<dl> <dt>

*pDefaultNamespace* \[out\]
</dt> <dd>

A pointer to a BSTR that receives the namespace URI. The driver places the namespace URI in the buffer that is pointed to by *pDefaultNamespace*.

`IPrintTicketProvider::QueryDeviceNamespace` is responsible for allocating the string by means of a call to **SysAllocString** (described in the Microsoft Windows SDK documentation), but the caller is responsible for freeing the string.

</dd> </dl>

## Return value

`IPrintTicketProvider::QueryDeviceNamespace` should return S\_OK if the operation succeeds and E\_FAIL otherwise.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prdrvcom.h (include Prdrvcom.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintTicketProvider::QueryDeviceNamespace%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




