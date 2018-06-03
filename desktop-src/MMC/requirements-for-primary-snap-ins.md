---
title: Requirements for Primary Snap-ins
description: Primary snap-ins have the following requirements
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 09412bc3-0e39-49c5-8943-c2948f01a139
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- requirements for primary snap-ins MMC
- requirements MMC
- requirements MMC , primary snap-ins
- primary snap-in's
- primary snap-in's, requirements
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Requirements for Primary Snap-ins

Primary snap-ins have the following requirements:

-   Primary snap-ins must register the node type GUIDs of their extendable node types under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns\\{snapinCLSID}\\[NodeTypes Key](nodetypes-key.md). The {snapinCLSID} key is the name for a snap-in's key and is the string representation of the snap-in's CLSID. For more information about the [SnapIns Key](snapins-key.md), see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

    MMC uses the values in the [NodeTypes Key](nodetypes-key.md) to find the node types for the snap-in and then uses that list of node types to get the extensions for those node types. That set of extension snap-ins is displayed as the available extensions for the snap-in on the Extensions tab of the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md).

-   Primary snap-ins must publish any clipboard formats that extension snap-ins need to be able to exchange data with them. Primary snap-in developers should also make information available about the data structures that must be used with the published clipboard formats.
-   Primary snap-ins with node types that are extended by property page extensions must implement the [**IExtendPropertySheet2**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet2) interface and enable the properties verb, even if they do not add any property pages themselves. For more information, see [Extending a Primary Snap-in's Property Sheet](extending-a-primary-snap-ins-property-sheet.md).

Primary snap-ins that also support required or dynamic extensions have additional requirements. For more information about required extensions, see [Adding Required Extensions](adding-required-extensions.md). For more information about adding support for dynamic extensions, see [Adding Dynamic Extensions](adding-dynamic-extensions.md).

## Related topics

<dl> <dt>

[Requirements for Extension Snap-ins](requirements-for-extension-snap-ins.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




