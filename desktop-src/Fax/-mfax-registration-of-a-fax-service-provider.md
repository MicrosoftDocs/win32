---
Description: This topic describes how to register with the fax service.
ms.assetid: 13bfb897-11f5-4fce-ac6e-8fbec7413e13
title: Registration of a Fax Service Provider
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registration of a Fax Service Provider

A fax service provider (FSP) should register with the fax service by performing the following steps.

## To install a service provider and register

1.  Install a telephony service provider (TSP) for device abstraction. The TSP identifies all the fax devices that the FSP controls, and enables the fax service to use the exposed fax devices.
2.  Copy the FSP DLL to the location specified by the *ImageName* parameter to the [**FaxRegisterServiceProvider**](/previous-versions/windows/desktop/api/Winfax/) function.
3.  Call the [**FaxRegisterServiceProvider**](/previous-versions/windows/desktop/api/Winfax/) function to configure the new devices for use by the fax service. The function registers the FSP DLL with the fax service.

For information about developing a FSP DLL, see [About the Fax Service Provider API](-mfax-about-the-fax-service-provider-api.md).

 

 



