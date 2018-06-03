---
Description: Provides the event delegate for printer queue events.
ms.assetid: AA4B2578-61C9-47C3-A114-4B873B475124
title: IPrinterQueueEvent interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrinterQueueEvent interface

Provides the event delegate for printer queue events.

## Members

The **IPrinterQueueEvent** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IPrinterQueueEvent** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrinterQueueEvent** interface has these methods.



| Method                                                                      | Description                                         |
|:----------------------------------------------------------------------------|:----------------------------------------------------|
| [**OnBidiResponseReceived**](iprinterqueueevent-onbidiresponsereceived.md) | Called when a bidi response is received.<br/> |



 

## Remarks

An event sink that implements **IPrinterQueueEvent** and the event source, [**IPrinterQueue**](iprinterqueue-interface.md) are connected via the [IConnectionPoint](http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318.aspx) mechanism. You must retrieve a pointer to the **IConnectionPoint** interface by invoking **QueryInterface** on the **IPrinterQueue** object.

> [!Note]  
> It is mandatory to implement **IDispatch::Invoke** on the event sink that implements **IPrinterQueueEvent**, since that is the mechanism via which events are raised. It is sufficient to provide stub implementations of the other methods on the **IDispatch** interface.

 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[IConnectionPoint](http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318.aspx)
</dt> <dt>

[**IPrinterQueue**](iprinterqueue-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterQueueEvent%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





