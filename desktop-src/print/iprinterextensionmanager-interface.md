---
Description: The IPrinterExtensionManager interface is retrieved by CoCreating the PrinterExtensionManager class.
ms.assetid: 918AE3F6-2AC4-42AD-9581-E87AD7E79BAD
title: IPrinterExtensionManager interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrinterExtensionManager interface

The **IPrinterExtensionManager** interface is retrieved by CoCreating the **PrinterExtensionManager** class.

## Members

The **IPrinterExtensionManager** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrinterExtensionManager** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrinterExtensionManager** interface has these methods.



| Method                                                          | Description                                                                                                                                                                         |
|:----------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DisableEvents**](iprinterextensionmanager-disableevents.md) | Disallows events to be generated.<br/>                                                                                                                                        |
| [**EnableEvents**](iprinterextensionmanager-enableevents.md)   | The EnableEvents method allows events to be generated for the specified printer driver until [**DisableEvents**](iprinterextensionmanager-disableevents.md) is called. <br/> |



 

## Remarks

Any event sink that implements [**IPrinterExtensionEvent**](iprinterextensionevent-interface.md) is connected to the associated event source, **IPrinterExtensionManager**, via the **IConnectionPoint** mechanism. You must retrieve a pointer to the **IConnectionPoint** interface by invoking **QueryInterface** on the **IPrinterExtensionManager** object.

> [!Note]  
> It is mandatory to implement **IDispatch::Invoke** on the event sink that implements **IPrinterExtensionEvent**, since that is the mechanism via which events are raised. It is sufficient to provide stub implementations of the other methods on the **IDispatch** interface.

 

## Requirements



|                   |                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printerextension.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterExtensionManager%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




