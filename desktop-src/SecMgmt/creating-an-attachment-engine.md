---
description: An attachment engine is a DLL that processes service-specific configuration and analysis requests. In other words, it handles the processing that cannot be handled by the standard Security Configuration tool set.
ms.assetid: c04779f4-f1e9-40b0-9f00-0176afb1b839
title: Creating an Attachment Engine
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Attachment Engine

An attachment engine is a DLL that processes service-specific configuration and analysis requests. In other words, it handles the processing that cannot be handled by the standard Security Configuration tool set.

To create an attachment engine, you must implement the following three functions:

-   [**SceSvcAttachmentAnalyze**](scesvcattachmentanalyze.md), which computes the difference between the service's configuration and the configuration stored in the security database. These differences are written to the security database. For more information, see [Implementing SceSvcAttachmentAnalyze](implementing-scesvcattachmentanalyze.md).
-   [**SceSvcAttachmentConfig**](scesvcattachmentconfig.md), which configures the service as specified in the snap-in user interface. For more information, see [Implementing SceSvcAttachmentConfig](implementing-scesvcattachmentconfig.md).
-   [**SceSvcAttachmentUpdate**](scesvcattachmentupdate.md), which updates the base configuration and configuration analysis for the service in the security database. For more information, see [Implementing SceSvcAttachmentUpdate](implementing-scesvcattachmentupdate.md).

The Security Configuration tool set implements a set of support functions that your application can call to query and set information in the security database. For more information, see [Attachment Callback Functions](management-functions.md).

After you create an attachment engine DLL, you must register it with the Security Configuration tool set. This process is described in [Registering an Attachment Engine](registering-an-attachment-engine.md).

In addition to creating an attachment engine, you must also create an attachment snap-in extension. The snap-in extension provides a user interface for service-specific tasks. When the user specifies a new configuration using a snap-in extension, the request is passed to the appropriate attachment engine. The engine then connects to the service and changes its configuration. If you do not implement a snap-in extension, users will have no way to change the service configuration or analysis. For more information on how to create an attachment snap-in extension, see [Creating an Attachment Snap-in Extension](creating-an-attachment-snap-in-extension.md).

 

 



