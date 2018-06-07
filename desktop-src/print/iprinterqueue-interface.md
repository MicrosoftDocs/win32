---
Description: Represents a single printer queue.
ms.assetid: 2DB57234-E783-4C6B-A743-F1E9F7D34D97
title: IPrinterQueue interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrinterQueue interface

Represents a single printer queue.

## Members

The **IPrinterQueue** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IPrinterQueue** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IPrinterQueue** interface has these methods.



| Method                                               | Description                                                                                                                                                                                             |
|:-----------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetProperties**](iprinterqueue-getproperties.md) | Gets the properties in the property bag for the queue.<br/>                                                                                                                                       |
| [**SendBidiQuery**](iprinterqueue-sendbidiquery.md) | Performs an asynchronous refresh operation with the specified query, and invokes the [**IPrinterQueueEvent::OnBidiResponseReceived**](iprinterqueueevent-onbidiresponsereceived.md) method.<br/> |



 

### Properties

The **IPrinterQueue** interface has these properties.



| Property                                          | Access type          | Description                                                        |
|:--------------------------------------------------|:---------------------|:-------------------------------------------------------------------|
| [**Handle**](iprinterqueue-handle.md)<br/> | Read-only<br/> | Gets the underlying native handle for this print queue.<br/> |
| [**Name**](iprinterqueue-name.md)<br/>     | Read-only<br/> | Gets the name of the printer for this print queue.<br/>      |



 

## Remarks

Any event sink that implements [**IPrinterQueueEvent**](iprinterqueueevent-interface.md) is connected to the associated event source, **IPrinterQueue**, via the [IConnectionPoint](http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318.aspx) mechanism. You must retrieve a pointer to the **IConnectionPoint** interface by invoking **QueryInterface** on the **IPrinterQueue** object.

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

[**IPrinterQueueEvent**](iprinterqueueevent-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterQueue%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





