---
title: About the Resource Object
description: The Resource object has additional properties to facilitate reading data on the device and transferring it to a web service.
ms.assetid: 219c7958-1683-4cd5-aaa4-65ebc0bb3a1b
keywords:
- WPD Automation,IStream
- WPD Automation,IXMLHttpRequest
- WPD Automation,Resource object
- Resource object
- IStream
- IXMLHttpRequest
- resources,Resource object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About the Resource Object

The [**Resource**](resource-object.md) object has additional properties to facilitate reading data on the device and transferring it to a web service. It provides a [**Stream**](resource-stream.md) property (an **IStream**) that can be used with the [IXMLHttpRequest](http://msdn.microsoft.com/library/ms763706(VS.85).aspx) method to send or receive data. The **Resource** object also provides [**Format**](resource-format.md), [**Size**](resource-size.md), and [**IsReadOnly**](resource-isreadonly.md) properties for determining the data format of the resource, its size (in bytes), and whether the resource is read-only.

For examples of using the **Resource** object while reading and writing resource data synchronously and asynchronously, see [Reading and Writing Resource Data](reading-and-writing-resource-data.md).

## Related topics

<dl> <dt>

[About the WPD Automation Object Model](about-the-wpd-automation-object-model.md)
</dt> <dt>

[Creating and Deleting Objects](creating-and-deleting-objects.md)
</dt> <dt>

[**Creation Container Object**](creation-container-object.md)
</dt> <dt>

[**Resource Object**](resource-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 




