---
title: Adding Required Extensions
description: Required extensions are extension snap-ins that are automatically added to the primary snap-in when the primary snap-in is loaded.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e43209ad-3155-4841-8948-cc9b008068e9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- adding required extensions MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Required Extensions

Required extensions are extension snap-ins that are automatically added to the primary snap-in when the primary snap-in is loaded. By implementing the [**IRequiredExtensions**](/windows/desktop/api/Mmc/nn-mmc-irequiredextensions) interface, a snap-in specifies the list of required extensions that MMC should load when that snap-in is loaded.

Required extensions are added to all instances of the primary snap-in. In addition, required extensions cannot be removed programmatically or through the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md).

Required extensions are persisted in the console file, but at each session the snap-in is queried for the list. Only required extensions specified by the latest query are used.

The snap-in can specify that all registered extension snap-ins should be added by implementing the [**IRequiredExtensions::EnableAllExtensions**](/windows/desktop/api/Mmc/nf-mmc-irequiredextensions-enableallextensions) method. The snap-in can specify a specific list of registered extension snap-ins to be added by implementing the [**IRequiredExtensions::GetFirstExtension**](/windows/desktop/api/Mmc/nf-mmc-irequiredextensions-getfirstextension) and [**IRequiredExtensions::GetNextExtension**](/windows/desktop/api/Mmc/nf-mmc-irequiredextensions-getnextextension) methods.

## Related topics

<dl> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




