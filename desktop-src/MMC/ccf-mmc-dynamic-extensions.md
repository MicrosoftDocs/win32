---
title: CCF\_MMC\_DYNAMIC\_EXTENSIONS clipboard format
description: For MMC 1.1 and later, the CCF\_MMC\_DYNAMIC\_EXTENSIONS clipboard format enables a snap-in to add any of the following types of extensions to its own scope or result items context menu, toolbar, property sheet, or taskpad.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 48d55143-7873-4c66-a4c9-bde5663cb7f1
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_MMC_DYNAMIC_EXTENSIONS clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_MMC_DYNAMIC_EXTENSIONS
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CCF\_MMC\_DYNAMIC\_EXTENSIONS clipboard format

For MMC 1.1 and later, the CCF\_MMC\_DYNAMIC\_EXTENSIONS clipboard format enables a snap-in to add any of the following types of extensions to its own scope or result items: context menu, toolbar, property sheet, or taskpad.

## Data Format

SMMCDynamicExtensions structure.

## Remarks

For a snap-in to support dynamic extension of its scope or result items with non-namespace extensions (that is, context menu, toolbar, property sheet, or taskpad extensions), the clipboard format CCF\_MMC\_DYNAMIC\_EXTENSIONS must be handled in the snap-in [**IDataObject**](https://www.bing.com/search?q=**IDataObject**) implementation. For more information, see [Dynamic Non-Namespace Extensions](dynamic-non-namespace-extensions.md).

Be aware that the extension snap-in must be a non-namespace extension and the MMC registry entries for the snap-in to be extended as well as the extension snap-in must be set correctly. For more information about how to set an MMC registry entry for extensions, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).

The CCF\_MMC\_DYNAMIC\_EXTENSIONS clipboard format extends only non-namespace extensions. To dynamically add namespace extensions, the snap-in must use the [**IConsoleNameSpace2::AddExtension**](/windows/desktop/api/Mmc/nf-mmc-iconsolenamespace2-addextension) method. For more information, see [Dynamic Namespace Extensions](dynamic-namespace-extensions.md).

Just before MMC must use an extensible feature (that is, just before creating and that displays a context menu, property sheet, toolbar, or taskpad), MMC calls [**IDataObject::GetData**](https://www.bing.com/search?q=**IDataObject::GetData**) on the data object for the selected item and asks for dynamic extensions to add through the CCF\_MMC\_DYNAMIC\_EXTENSIONS clipboard format. Based on CLSIDs passed in the [**SMMCDynamicExtensions**](https://www.bing.com/search?q=**SMMCDynamicExtensions**) structure, MMC attempts to add the specified extensions to the extensible feature. If an extension is unavailable or unregistered, MMC skips that extension and continues to the next CLSID passed in the structure.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





