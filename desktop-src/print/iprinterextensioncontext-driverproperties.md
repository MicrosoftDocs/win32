---
Description: Gets the driver property bag.
ms.assetid: 52EC01D5-43C7-4CE0-ABEC-1604A4198316
title: IPrinterExtensionContextDriverProperties property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrinterExtensionContext::DriverProperties property

Gets the driver property bag.

This property is read-only.

## Syntax


```C++
HRESULT get_DriverProperties(
  [out, retval] IPrinterPropertyBag **ppPropertyBag
);
```



## Property value

The driver property bag.

## Error codes

Returns an **HRESULT** value. If the property call was not successful, it returns the appropriate **HRESULT** error code.

## Remarks

The driver property bag uses the following GUID for its property store format ID:

`DEFINE_GUID(FMTID_PrinterPropertyBag, 0x75f9adca, 0x097d, 0x45c3, 0xa6, 0xe4, 0xba, 0xb2, 0x9e, 0x27, 0x6f, 0x3e);`

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterExtensionContext**](iprinterextensioncontext-interface.md)
</dt> <dt>

[**IPrinterPropertyBag**](iprinterpropertybag-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterExtensionContext::DriverProperties%20property%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





