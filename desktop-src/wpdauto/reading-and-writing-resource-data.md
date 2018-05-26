---
title: Reading and Writing Resource Data
description: In WPD Automation, a device can read resource data by using a Resource object that is accessed through the Resource property of a WPDObject.
ms.assetid: 8f1d1a54-bb0d-4746-b44a-98b8b1e85cda
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reading and Writing Resource Data

In WPD Automation, a device can read resource data by using a [**Resource**](resource-object.md) object that is accessed through the [**Resource**](wpdobject-resource.md) property of a [**WPDObject**](wpdobject.md). The **Resource** object has a [**Resource.Stream**](resource-stream.md) property that is an **IStream**, which can be used with the **IXMLHttpRequest.send** method to transmit and receive data via [XML HTTP Requests](http://go.microsoft.com/fwlink/p/?linkid=130621).

Writing resource data is supported only when the object is first created. This is done by assigning the [**Data**](createcontainerobject-data.md) property of the [**Creation Container**](creation-container-object.md) object before calling the [**AddChild**](wpdobject-addchild.md) method on the parent object.

The following sections include examples of reading and writing resource data synchronously and asynchronously.



| Section                                                                | Description                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Synchronous Reading and Writing](synchronous-reading-and-writing.md) | Describes reading resource data synchronously by upgrading the firmware of a device with new firmware obtained from a web service, and describes writing resource data synchronously by uploading diagnostic data from a device to a web service. |
| [Asynchronous Functions](asynchronous-functions.md)                   | Describes how to enable asynchronous behavior for certain functions, and demonstrates reading resource data asynchronously by using a completion event, and writing resource data asynchronously by using an XMLHTTPRequest in asynchronous mode. |



 

## Related topics

<dl> <dt>

[**Creation Container Object**](creation-container-object.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Resource Object**](resource-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> <dt>

[WPD Automation Programming Guide](wpd-automation-programming-guide.md)
</dt> </dl>

 

 




