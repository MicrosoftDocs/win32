---
Description: This topic describes the components required to support the functionality of the Fax Service Client API.
ms.assetid: 30755339-d4c4-4c4c-a0d7-bb44005784e4
title: Fax Service Client API Software Requirements
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Service Client API Software Requirements

The following components are required to support the functionality of the Fax Service Client API.

-   The fax service. This support-service application manages fax devices and configuration data, provides print services, and sends and receives fax documents. The fax service also initiates and retries fax routing methods exported by fax routing extensions.
-   WinFax.lib. The static-link library that contains the Fax Service Client API functionality.
-   The DLL that contains the Fax Service Client API functionality.

In addition, you must include the WinFax.h header file in your source code files. To use the fax client Component Object Model (COM) implementation that Microsoft supplies, you must include FaxCom.h.

The fax service communicates with networked client machines using remote procedure call (RPC). Although it is not necessary to install the fax service on each client computer, the service must be accessible to the client through RPC.

 

 



