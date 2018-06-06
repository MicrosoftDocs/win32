---
Description: Describes the signature of the callback object that receives the Bidi response.
ms.assetid: C85690D0-3CA7-46C7-B597-E36555879F08
title: IPrinterBidiSetRequestCallback interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrinterBidiSetRequestCallback interface

Describes the signature of the callback object that receives the Bidi response.

## Members

The **IPrinterBidiSetRequestCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrinterBidiSetRequestCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrinterBidiSetRequestCallback** interface has these methods.



| Method                                                        | Description                                                     |
|:--------------------------------------------------------------|:----------------------------------------------------------------|
| [**Completed**](iprinterbidisetrequestcallback-completed.md) | Invoked when the Bidi “Set”” operation is completed.<br/> |



 

## Remarks

**IPrinterBidiSetRequestCallback** provides the Bidi response string, and **HRESULT** value returned from the [IBidiSpl2::SendRecvXmlString](http://msdn.microsoft.com/en-us/library/windows/desktop/dd144984.aspx) method. In other words, this interface provides the results of the attempt to send data to the device.

**IPrinterBidiSetRequestCallback** helps to make it possible to perform device maintenance from a UWP device app or from a printer extension. For more information, see [Device Maintenance](https://www.bing.com/search?q=Device+Maintenance).

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[Device Maintenance](https://www.bing.com/search?q=Device+Maintenance)
</dt> <dt>

[IBidiSpl2::SendRecvXmlString](http://msdn.microsoft.com/en-us/library/windows/desktop/dd144984.aspx)
</dt> <dt>

[**SendBidiSetRequestAsync**](iprinterqueue2-sendbidisetrequestasync.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterBidiSetRequestCallback%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





