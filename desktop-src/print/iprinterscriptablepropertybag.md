---
Description: The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients.
ms.assetid: E6F48895-7ED6-479B-BF16-42192461C56D
title: IPrinterScriptablePropertyBag interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrinterScriptablePropertyBag interface

The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients.

This interface is the same as [**IPrinterPropertyBag**](iprinterpropertybag-interface.md), except that the GetBytes and SetBytes methods operate on JavaScript arrays and the GetReadStream and GetWriteStream methods operate on [**IPrinterScriptableStream**](iprinterscriptablestream.md) objects.

## Members

The **IPrinterScriptablePropertyBag** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrinterScriptablePropertyBag** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrinterScriptablePropertyBag** interface has these methods.



| Method                                                                 | Description                                                         |
|:-----------------------------------------------------------------------|:--------------------------------------------------------------------|
| [**GetBool**](iprinterscriptablepropertybag-getbool.md)               | Gets a specified boolean property.<br/>                       |
| [**GetBytes**](iprinterscriptablepropertybag-getbytes.md)             | Gets a byte array property.<br/>                              |
| [**GetInt32**](iprinterscriptablepropertybag-getint32.md)             | Gets an integer property.<br/>                                |
| [**GetReadStream**](iprinterscriptablepropertybag-getreadstream.md)   | Gets a read stream and uses it to read from a property.<br/>  |
| [**GetString**](iprinterscriptablepropertybag-getstring.md)           | Gets a string property.<br/>                                  |
| [**GetWriteStream**](iprinterscriptablepropertybag-getwritestream.md) | Gets a stream and uses it to write to a stream property.<br/> |
| [**SetBool**](iprinterscriptablepropertybag-setbool.md)               | Writes a specified boolean property value.<br/>               |
| [**SetBytes**](iprinterscriptablepropertybag-setbytes.md)             | Writes a byte array property.<br/>                            |
| [**SetInt32**](iprinterscriptablepropertybag-setint32.md)             | Writes an integer property.<br/>                              |
| [**SetString**](iprinterscriptablepropertybag-setstring.md)           | Writes a string property.<br/>                                |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterPropertyBag**](iprinterpropertybag-interface.md)
</dt> <dt>

[**IPrinterScriptableStream**](iprinterscriptablestream.md)
</dt> <dt>

[**IPrinterScriptContext::DriverProperties**](iprinterscriptcontext-driverproperties.md)
</dt> <dt>

[**IPrinterScriptContext::QueueProperties**](iprinterscriptcontext-queueproperties.md)
</dt> <dt>

[**IPrinterScriptContext::UserProperties**](iprinterscriptcontext-userproperties.md)
</dt> <dt>

[V4 Printer Driver Property Bags](https://www.bing.com/search?q=V4 Printer Driver Property Bags)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptablePropertyBag%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





