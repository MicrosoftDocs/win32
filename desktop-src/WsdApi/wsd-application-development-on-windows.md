---
Description: The Microsoft Web Services on Devices API (WSDAPI) supports the implementation of client-controlled devices and services, and device hosts conforming to the Devices Profile for Web Services (DPWS).
ms.assetid: 88de8dea-56d5-4bfc-8837-03da81b7d0f9
title: WSD Application Development on Windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WSD Application Development on Windows

The Microsoft Web Services on Devices API (WSDAPI) supports the implementation of client-controlled devices and services, and device hosts conforming to the [Devices Profile for Web Services](http://go.microsoft.com/fwlink/p/?linkid=59069) (DPWS). WSDAPI may be used for the development of both client and server (device) implementations.

Quite often, WSDAPI code for these applications is generated using [WsdCodeGen](web-services-for-devices-code-generator.md). Some WSDAPI functions and methods are intended to be called only by generated code. The API reference documentation indicates when a function or method should be used or implemented only by generated code.

The Windows SDK includes some sample WSDL files, WsdCodeGen configuration files, and generated code. For more information, see [WSDAPI Samples](wsdapi-samples.md).

If you want to enumerate devices using the WSD protocol and query WSD device metadata, you can use the [Function Discovery](https://msdn.microsoft.com/library/windows/desktop/aa814070) API instead.

If you want to implement a WSD device that does not run Windows, see [WSD Device Development](wsd-device-development.md).
