---
title: Extending Views
description: View extensions, introduced in MMC 2.0, enable a snap-in to add user interface elements to an existing view or to create new views.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3c626853-a9f1-4961-97d0-a12d0bf8b9ed
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extending Views

View extensions, introduced in MMC 2.0, enable a snap-in to add user interface elements to an existing view or to create new views. View extensions use HTML to provide the user interface elements. The HTML can include script to use the [MMC 2.0 Automation Object Model](mmc-2-0-automation-object-model.md).

A snap-in developer can create new view extensions or use the Extended View extension to add view extensions to a snap-in. MMC 2.0 includes the Extended View as an extension that snap-in developers can use to provide a web-folder look and feel to their snap-ins.

A primary snap-in registers a view extension for any node type that is to contain view extensions. Be aware that this is different from the registration that takes place by other (non-view) extensions, which register themselves for the node types extended. Register the view extension entry in the following form:

HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\ {nodetypeGUID} Extensions View {viewextensionsnapinCLSID}

-   The {nodetypeGUID} key specifies the string representation of the globally unique identifier (GUID) of the node type that is extended. The string must begin with an open brace ({) and end with a close brace (}). There must also be a corresponding {nodetypeGUID} value in the primary snap-in HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns\\{snapinCLSID}\\NodeTypes key, where {snapinCLSID} is the string representation of the snap-in class identifier (CLSID).
-   The View key contains values that represent the CLSIDs of snap-ins that can extend the view of items with this node type.
-   The {viewextensionsnapinCLSID} key specifies the string representation of the CLSID of a view extension snap-in. The string must begin with an open brace ({) and end with a close brace (}).

For more information about extension registration, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).

The following list contains topics that provide more information about view extensions and the Extended View extension:

-   [View Extension Mechanism](view-extension-mechanism.md)
-   [Using the Extended View Extension](using-the-extended-view-extension.md)
-   [Using the Extended View Extension - Implementation Details](using-the-extended-view-extension-implementation-details.md)
-   [Extending a Primary Snap-in's View](extending-a-primary-snap-ins-view.md)

## Related topics

<dl> <dt>

[**View object**](view-object.md)
</dt> </dl>

 

 




