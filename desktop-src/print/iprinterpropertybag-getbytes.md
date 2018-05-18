---
Description: 'Reads a byte array property.'
ms.assetid: 'F75E182D-90FA-4597-95E0-60A6326CF68D'
title: 'IPrinterPropertyBag::GetBytes method'
---

# IPrinterPropertyBag::GetBytes method

Reads a byte array property.

The [**IPrinterPropertyBag**](iprinterpropertybag-interface.md) interface is used by all the printer property bags, including driver property bag, user property bag, queue property bag, and DEVMODE property bag.

## Syntax


```C++
HRESULT GetBytes(
  [in]  BSTR  bstrName,
  [out] DWORD *pcbValue,
  [out] BYTE  *rgbValue
);
```



## Parameters

<dl> <dt>

*bstrName* \[in\]
</dt> <dd>

The property to read.

</dd> <dt>

*pcbValue* \[out\]
</dt> <dd>

The number of bytes read.

</dd> <dt>

*rgbValue* \[out\]
</dt> <dd>

The returned array. This array must be freed by using CoTaskFree.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

## Requirements



|                            |                                                                                                                            |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                         |
| Header<br/>          | <dl> <dt>Printerextension.h (include Printerextension.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterPropertyBag**](iprinterpropertybag-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterPropertyBag::GetBytes%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





