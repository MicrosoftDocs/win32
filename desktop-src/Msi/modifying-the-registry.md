---
description: Registry keys can be written to the system registry once all selected components and their related files have been installed.
ms.assetid: b3b39471-85b1-4361-94fd-19d0f0ee2b78
title: Modifying the Registry
ms.topic: article
ms.date: 05/31/2018
---

# Modifying the Registry

Registry keys can be written to the system registry once all selected components and their related files have been installed. The standard actions related to modifying the registry must be sequenced after the file installation standard actions because registry keys cannot be written unless the corresponding component and file have been successfully installed.

The [RegisterClassInfo action](registerclassinfo-action.md) accesses the [Class table](class-table.md) to register the COM class information of the installed components.

The [RegisterExtensionInfo action](registerextensioninfo-action.md) queries the [Extension table](extension-table.md) and [Verb table](verb-table.md) and registers the corresponding extensions and command-verb information with the operating system.

The [RegisterProgIdInfo action](registerprogidinfo-action.md) manages the registration of OLE ProgId information with the operating system.

The [RegisterMIMEInfo action](registermimeinfo-action.md) processes the [MIME table](mime-table.md) to register the association between a MIME context type, the file name extension, and the CLSID.

The [WriteRegistryValues action](writeregistryvalues-action.md) processes the [Registry table](registry-table.md) and writes the keys for all components that have been either installed locally or to run from source. The Registry table allows keys to be written to the **HKEY\_CLASSES\_ROOT**, **HKEY\_CURRENT\_USER**, **HKEY\_LOCAL\_MACHINE**, and **HKEY\_USERS** registry hives.

The [RemoveRegistryValues action](removeregistryvalues-action.md) removes the keys that have been marked to be deleted in the Name column of the [Registry table](registry-table.md) or the [RemoveRegistry Table](removeregistry-table.md).

The [RegisterTypeLibraries action](registertypelibraries-action.md) processes the [TypeLib table](typelib-table.md) and registers the installed type libraries with the system.

 

 



