---
title: Adding Dynamic Extensions Interfaces
description: Dynamic namespace extensions require the use of the following interface and method
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 40a55628-5e49-4086-ac48-506708d606e0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- dynamic extensions MMC , interfaces
- adding dynamic extensions interfaces MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Dynamic Extensions: Interfaces

Dynamic namespace extensions require the use of the following interface and method:

-   [**IConsoleNameSpace2**](/windows/desktop/api/Mmc/nn-mmc-iconsolenamespace2)
    -   [**IConsoleNameSpace2::AddExtension**](/windows/desktop/api/Mmc/nf-mmc-iconsolenamespace2-addextension)

Non-namespace dynamic extensions (context menu, property sheet, toolbar, taskpad) must support the following clipboard format in their [**IDataObject**](https://www.bing.com/search?q=**IDataObject**) implementation:

-   [**CCF\_MMC\_DYNAMIC\_EXTENSIONS**](ccf-mmc-dynamic-extensions.md)

The clipboard format uses the following structure:

-   [**SMMCDynamicExtensions**](https://www.bing.com/search?q=**SMMCDynamicExtensions**)

## Related topics

<dl> <dt>

[Dynamic Namespace Extensions](dynamic-namespace-extensions.md)
</dt> <dt>

[Dynamic Non-Namespace Extensions](dynamic-non-namespace-extensions.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




