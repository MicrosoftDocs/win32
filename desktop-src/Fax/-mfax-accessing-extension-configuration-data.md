---
Description: A fax extension DLL can access its global and device-specific extension configuration data from within the fax server process (internal access).
ms.assetid: 1226a4be-94ef-4a35-af28-8ff65bb8bcec
title: Accessing Extension Configuration Data
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Extension Configuration Data

A fax extension DLL can access its global and device-specific extension configuration data from within the fax server process (internal access). Processes that execute outside of the fax server process can also access configuration data (external access).

-   **Internal access**. Fax routing extension DLLs and fax service providers (FSPs) can access their configuration data by calling the fax service callback functions [**FaxExtGetData**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextgetdata) and [**FaxExtSetData**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextsetdata) to retrieve and set configuration data. Note that the extension DLL must export the [**FaxExtInitializeConfig**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextinitializeconfig) function. For more information, see [Fax Service and Configuration Extension Interaction](-mfax-fax-service-and-configuration-extension-interaction.md).

 

 



