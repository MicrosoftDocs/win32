---
Description: Represents a single printer queue.
ms.assetid: 06459A1F-A14B-43BA-9771-47205CC3F388
title: IPrinterQueue2 interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrinterQueue2 interface

Represents a single printer queue.

This interface extends [**IPrinterQueue**](iprinterqueue-interface.md) and allows a user to manage print jobs and device maintenance from within a UWP device app for printers, or from a printer extension.

## Members

The **IPrinterQueue2** interface inherits from [**IPrinterQueue**](iprinterqueue-interface.md). **IPrinterQueue2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrinterQueue2** interface has these methods.



| Method                                                                    | Description                                                                                                                                       |
|:--------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetPrinterQueueView**](iprinterqueue2-getprinterqueueview.md)         | Retrieves an [**IPrinterQueueView**](iprinterqueueview.md) object, and initializes the object with the range of jobs to be monitored.<br/> |
| [**SendBidiSetRequestAsync**](iprinterqueue2-sendbidisetrequestasync.md) | Uses an XML string value to send a Bidi Set request as an asynchronous operation.<br/>                                                      |



 

## Remarks

**IPrinterQueue2** also helps to make it possible to perform device maintenance and job management from a UWP device app or from a printer extension. For more information, see [Device Maintenance](print.device_maintenance) and [Job Management](print.job_management).

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[Device Maintenance](print.device_maintenance)
</dt> <dt>

[**IPrinterQueue**](iprinterqueue-interface.md)
</dt> <dt>

[Job Management](print.job_management)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterQueue2%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





