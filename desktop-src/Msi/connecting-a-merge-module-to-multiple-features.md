---
description: The Connect method of the Merge Object can be used to connect a module to an additional feature that has been merged into the database or that will be merged into the database. The feature must exist before calling this method.
ms.assetid: 8b59de42-bc3f-468b-a410-8f935ff73345
title: Connecting a Merge Module to Multiple Features
ms.topic: article
ms.date: 05/31/2018
---

# Connecting a Merge Module to Multiple Features

The [**Connect**](merge-connect.md) method of the [Merge Object](merge-object.md) can be used to connect a module to an additional feature that has been merged into the database or that will be merged into the database. The feature must exist before calling this method.

A merge module should never deliver a component containing system files to the main feature of an application, because this may cause the Installer to validate and repair the application each time the system file is used. A .msi file that is intended to accept components from a merge module should be authored so that any components that contain system files only belong to features that are separate from the main feature of the application.

If your package uses a merge module containing system files that link all the components from the merge module to the main feature of the application, an attempt to use the system file may trigger the Installer to try and repair the main feature of the application. If the main feature cannot be repaired, the installation may fail.

 

 



