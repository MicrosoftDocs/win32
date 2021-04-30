---
description: WpdServicesApiSample Application
ms.assetid: 857753f7-bca1-4f4a-a8f9-0b2232e2f0dc
title: WpdServicesApiSample Application
ms.topic: article
ms.date: 05/31/2018
---

# WpdServicesApiSample Application

A device service is an extension of a functional object: In addition to logically grouping device capabilities, a device service provides applications with the ability to programmatically discover those capabilities.

The WpdServicesApiSample sample application is a command-line desktop application that you can use to explore Contacts services on devices attached to your computer. You can explore these services by listing supported: formats, events, methods, and abstract services. You can also use this application retrieve the properties on a given Contact service and to invoke methods supported by that service.

If you don't yet have a device that supports Contacts services, you can still run the WpdServicesApiSample if you first install the WpdServiceSampleDriver that is included in the Windows Driver Kit.

The WpdServicesApiSample sample application includes the following files:



| **File**                | **Description**                                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ContentEnumeration.cpp  | Contains methods that enumerate the content on a given Contacts service.                                                                                                                                  |
| ContentProperties.cpp   | Contains methods that read and write properties on a given Contacts service.                                                                                                                              |
| ServiceCapabilities.cpp | Contains the methods that retrieve the supported formats, events, and abstract services that are supported by a given Contacts service.                                                                   |
| ServiceEnumeration.cpp  | Contains the helper functions that retrieve device information such as the device-friendly name or the supported Contacts services.                                                                       |
| ServiceMethods.cpp      | Contains the methods that retrieve and invoke methods supported by a given Contacts service.                                                                                                              |
| Stdafx.cpp              | Includes the standard files.                                                                                                                                                                              |
| WpdServiceApiSample.cpp | Hosts the **\_tmain** startup function, which calls the local **DoMenu** function, which displays a list of available devices and tasks and calls the function appropriate for the user's menu selection. |



 


## Related topics

<dl> <dt>

[Samples](sample.md)
</dt> </dl>

 

 



