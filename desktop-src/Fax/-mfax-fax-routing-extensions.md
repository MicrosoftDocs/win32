---
Description: A fax routing extension is a DLL that adds routing functionality to the fax service.
ms.assetid: abf031c2-d206-40eb-9ad5-74eedb1a8423
title: Fax Routing Extensions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Routing Extensions

A fax routing extension is a DLL that adds routing functionality to the fax service. Multiple fax routing extensions can reside on one server. When the fax server receives a fax transmission, it routes the received document through each of the fax routing extensions in order of priority. A user sets the routing priority using the fax service administration application, a Microsoft Management Console (MMC) snap-in component.

Each fax routing extension must register with the fax service to inform the fax service about the extension and its fax routing methods. If the correct entries exist in the registry, the fax service loads the fax routing extension when the service initializes. For more information, see [Fax Routing Extension Registration](-mfax-fax-routing-extension-registration.md).

 

 



