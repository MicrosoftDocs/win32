---
Description: Provides strongly-typed get and set methods.
ms.assetid: 421397FF-4956-4052-B63D-32F8E79A22D0
title: IPrinterPropertyBag interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrinterPropertyBag interface

Provides strongly-typed **get** and **set** methods.

Note that the driver property bag uses the following GUID for its property store format ID: <dl> DEFINE\_GUID(FMTID\_PrinterPropertyBag, 0x75f9adca, 0x097d, 0x45c3, 0xa6, 0xe4, 0xba, 0xb2, 0x9e, 0x27, 0x6f, 0x3e);  
</dl>

The **IPrinterPropertyBag** interface is used by all the printer property bags, including driver property bag, user property bag, queue property bag, and DEVMODE property bag.

## Members

The **IPrinterPropertyBag** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IPrinterPropertyBag** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrinterPropertyBag** interface has these methods.



| Method                                                       | Description                                                       |
|:-------------------------------------------------------------|:------------------------------------------------------------------|
| [**GetBool**](iprinterpropertybag-getbool.md)               | Reads a specified boolean property.<br/>                    |
| [**GetBytes**](iprinterpropertybag-getbytes.md)             | Reads a byte array property.<br/>                           |
| [**GetInt32**](iprinterpropertybag-getint32.md)             | Reads an integer property.<br/>                             |
| [**GetReadStream**](iprinterpropertybag-getreadstream.md)   | Gets a stream in order to read from a stream property.<br/> |
| [**GetString**](iprinterpropertybag-getstring.md)           | Reads a string property.<br/>                               |
| [**GetWriteStream**](iprinterpropertybag-getwritestream.md) | Gets a stream in order to write a stream property.<br/>     |
| [**SetBool**](iprinterpropertybag-setbool.md)               | Writes a specified boolean property value.<br/>             |
| [**SetBytes**](iprinterpropertybag-setbytes.md)             | Writes a byte array property.<br/>                          |
| [**SetInt32**](iprinterpropertybag-setint32.md)             | Writes an integer property.<br/>                            |
| [**SetString**](iprinterpropertybag-setstring.md)           | Writes a string property.<br/>                              |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[**IPrinterExtensionContext::DriverProperties**](iprinterextensioncontext-driverproperties.md)
</dt> <dt>

[**IPrinterExtensionContext::UserProperties**](iprinterextensioncontext-userproperties.md)
</dt> <dt>

[**IPrinterQueue::GetProperties**](iprinterqueue-getproperties.md)
</dt> <dt>

[**IPrinterScriptablePropertyBag**](iprinterscriptablepropertybag.md)
</dt> <dt>

[V4 Printer Driver Property Bags](https://www.bing.com/search?q=V4+Printer+Driver+Property+Bags)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterPropertyBag%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





