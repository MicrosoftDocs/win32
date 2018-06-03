---
Description: The IPrinterScriptableStream interface builds on IPrinterScriptableSequentialStream and adds IStream-like semantics.
ms.assetid: AD3CDF90-76ED-498B-8DE1-B191504EB415
title: IPrinterScriptableStream interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrinterScriptableStream interface

The IPrinterScriptableStream interface builds on [**IPrinterScriptableSequentialStream**](iprinterscriptablesequentialstream-interface.md) and adds IStream-like semantics.

## Members

The **IPrinterScriptableStream** interface inherits from [**IPrinterScriptableSequentialStream**](iprinterscriptablesequentialstream-interface.md). **IPrinterScriptableStream** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrinterScriptableStream** interface has these methods.



| Method                                               | Description                                                  |
|:-----------------------------------------------------|:-------------------------------------------------------------|
| [**Commit**](iprinterscriptablestream--commit.md)   | Commits the operation.<br/>                            |
| [**Seek**](iprinterscriptablestream--seek.md)       | Sets the seek pointer.<br/>                            |
| [**SetSize**](iprinterscriptablestream--setsize.md) | Sets the size of the scriptable stream, in bytes.<br/> |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterScriptableSequentialStream**](iprinterscriptablesequentialstream-interface.md)
</dt> <dt>

[**IPrinterScriptablePropertyBag**](iprinterscriptablepropertybag.md)
</dt> <dt>

[**IPrinterScriptablePropertyBag::GetReadStream**](iprinterscriptablepropertybag-getreadstream.md)
</dt> <dt>

[**IPrinterScriptablePropertyBag::GetWriteStream**](iprinterscriptablepropertybag-getwritestream.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptableStream%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





