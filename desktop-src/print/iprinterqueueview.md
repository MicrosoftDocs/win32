---
Description: 'Provides a way to change the range of print jobs being monitored.'
ms.assetid: '81B3D4A3-7176-4656-B23D-04F0F84D9000'
title: IPrinterQueueView interface
---

# IPrinterQueueView interface

Provides a way to change the range of print jobs being monitored.

## Members

The **IPrinterQueueView** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IPrinterQueueView** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrinterQueueView** interface has these methods.



| Method                                                 | Description                                              |
|:-------------------------------------------------------|:---------------------------------------------------------|
| [**SetViewRange**](iprinterqueueview-setviewrange.md) | Sets the range of print jobs being monitored.<br/> |



 

## Remarks

An event is raised whenever the status of the print queue changes. So when a client uses [**SetViewRange**](iprinterqueueview-setviewrange.md) to specify the range of print jobs (the view) to be monitored, the [**IPrinterQueueViewEvent::OnChanged**](iprinterqueueviewevent-onchanged.md) event method fires, and the live queue is returned in response.

And also, note that job enumeration starts when the first event handler is added and stops when the last event handler is removed.

**IPrinterQueueView** also helps to make it possible to perform job management from a UWP device app or from a printer extension. For more information, see [Job Management](print.job_management).

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterQueueViewEvent::OnChanged**](iprinterqueueviewevent-onchanged.md)
</dt> <dt>

[Job Management](print.job_management)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterQueueView%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





