---
Description: This reference section describes the Windows serial I/O request interface that is used by drivers and applications to send I/O requests to serial ports.
ms.assetid: 48808806-be9d-48fb-8178-a19a88bdb2f8
title: Serial Controller Driver Reference
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Serial Controller Driver Reference

This reference section describes the Windows [serial I/O request interface](https://www.bing.com/search?q=serial+I/O+request+interface) that is used by drivers and applications to send I/O requests to serial ports. Also described is the device driver interface (DDI) that an extension-based serial controller driver uses to communicate with version 1 or 2 of the serial framework extension (SerCx or SerCx2). The serial I/O request interface is supported by SerCx and SerCx2, and by the inbox serial driver, Serial.sys. Serial.sys is augmented by the [Serenum service](https://www.bing.com/search?q=Serenum+service) and the [COM port database](https://www.bing.com/search?q=COM+port+database).

For more information, see [Serial Controller Drivers Overview](https://www.bing.com/search?q=Serial+Controller+Drivers+Overview).

## 

## In this section

-   [Extension-Based Serial Controller Driver Reference](https://www.bing.com/search?q=Extension-Based+Serial+Controller+Driver+Reference)
-   [Serial I/O Request Reference](https://www.bing.com/search?q=Serial+I/O+Request+Reference)
-   [Serial Controller Driver reference in SDK header files](serial-controller-driver-reference-in-sdk-header-files.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Serial%20Controller%20Driver%20Reference%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



