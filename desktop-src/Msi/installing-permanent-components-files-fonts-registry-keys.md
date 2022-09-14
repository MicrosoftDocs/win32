---
description: To install a file, font, or registry key so that it is not removed when the product is uninstalled, the entire component containing the file, font, or registry key must be made permanent.
ms.assetid: 99db6485-2e85-47c3-a449-ef85b7efc865
title: Installing Permanent Components, Files, Fonts, Registry Keys
ms.topic: article
ms.date: 05/31/2018
---

# Installing Permanent Components, Files, Fonts, Registry Keys

To install a file, font, or registry key so that it is not removed when the product is uninstalled, the entire component containing the file, font, or registry key must be made permanent. To make a component permanent, set **msidbComponentAttributesPermanent** in the Attributes column of the [Component table](component-table.md).

Note that the installer removes a registry key after removing the last value or subkey under the key. To prevent an empty registry key from being removed on uninstall, write a dummy value under the key you need keep, and enter + in the Name column of the [Registry table](registry-table.md).

 

 



