---
title: Interfaces
description: Settings Management Infrastructure (SMI) uses the public interfaces, listed in the following table, to create and access a namespace and to read and write settings.
ms.assetid: a721e78f-ed3a-44e6-8f17-6bca1001f284
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces

Settings Management Infrastructure (SMI) uses the public interfaces, listed in the following table, to create and access a namespace and to read and write settings.



| Interface          | Description                                                                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IItemEnumerator    | Enumerates the items of a collection.                                                                                                                                |
| ISettingsContext   | Interfaces with a backing store used to store setting changes made through the other SMI APIs. It provides operations to serialize and deserialize a representation. |
| ISettingsEngine    | Opens namespaces and controls how they are opened.                                                                                                                   |
| ISettingsIdentity  | Identifies a namespace to open or use.                                                                                                                               |
| ISettingsItem      | Navigates the settings tree, retrieves the metadata for a particular setting, and retrieves or modifies its value.                                                   |
| ISettingsNamespace | Sets, retrieves, and validates the namespace settings, and saves changes made to the namespace.                                                                      |
| ISettingsResult    | Retrieves the error code and description of an error.                                                                                                                |
| ITargetInfo        | Identifies an offline image of a namespace for a target computer.                                                                                                    |



 

 

 




