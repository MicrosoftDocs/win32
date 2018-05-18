---
Description: 'The following components are required to support the functionality of the Fax Routing Extension API.'
ms.assetid: '0100f885-28c6-4d30-9d2e-9bdb3241c105'
title: Fax Routing Extension Software Requirements
---

# Fax Routing Extension Software Requirements

The following components are required to support the functionality of the Fax Routing Extension API.

-   A fax routing extension DLL. This DLL exposes a well-defined interface that connects the fax routing software of third-party vendors to the fax service.
-   The fax service. This support-service application provides an execution context for the fax routing extension. The fax service manages fax devices and configuration data, provides print services, and sends and receives fax documents. The fax service also initiates and retries fax routing methods for the fax routing extension.

In addition, you must include the appropriate fax routing extension header in your source code files, FaxRoute.h (Windows 2000 or later versions).

 

 



