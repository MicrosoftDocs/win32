---
description: An attachment engine is a DLL that handles service-specific configuration and analysis requests.
ms.assetid: bbca486a-9eec-4510-b5fd-435972182a69
title: Attachment Engines
ms.topic: article
ms.date: 05/31/2018
---

# Attachment Engines

An attachment engine is a DLL that handles service-specific configuration and analysis requests.

The user makes a service-specific configuration and analysis request using the attachment snap-in extension. This request is then passed through the Security Configuration snap-ins to the general Security Configuration Engine, which in turn passes the service-specific processing to the appropriate attachment engine. The attachment engine then connects to the service and changes its configuration. In other words, the attachment engine provides the back-end processing that supports the attachment snap-in extension.

An attachment engine must implement the following three functions:

-   [**SceSvcAttachmentAnalyze**](scesvcattachmentanalyze.md), which computes the difference between the service's configuration and the configuration stored in the security database. The differences are written to the security database.
-   [**SceSvcAttachmentConfig**](scesvcattachmentconfig.md), which configures the service as specified in the snap-in user interface.
-   [**SceSvcAttachmentUpdate**](scesvcattachmentupdate.md), which updates the base configuration and configuration analysis for the service in the security database.

To simplify implementation of the preceding functions, the Security Configuration tool set provides support functions and structures that your application can use to query and set information in the security database. For more information, see [Attachment Callback Functions](management-functions.md).

When you create an attachment engine DLL, you must install it and then register it with the Security Configuration Engine. To register the DLL, you add a specific key to the registry. When the Security Configuration Engine starts, it checks the registry and loads all registered attachment engine DLLs. It then passes service-specific configuration and analysis requests to the appropriate attachment engine. Standard configuration and analysis requests, those that are not service-specific, are handled by the Security Configuration Engine.

 

 



