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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding Dynamic Extensions: Interfaces

Dynamic namespace extensions require the use of the following interface and method:

-   [**IConsoleNameSpace2**](iconsolenamespace2.md)
    -   [**IConsoleNameSpace2::AddExtension**](iconsolenamespace2-addextension.md)

Non-namespace dynamic extensions (context menu, property sheet, toolbar, taskpad) must support the following clipboard format in their [**IDataObject**](_ole_idataobject) implementation:

-   [**CCF\_MMC\_DYNAMIC\_EXTENSIONS**](ccf-mmc-dynamic-extensions.md)

The clipboard format uses the following structure:

-   [**SMMCDynamicExtensions**](smmcdynamicextensions.md)

## Related topics

<dl> <dt>

[Dynamic Namespace Extensions](dynamic-namespace-extensions.md)
</dt> <dt>

[Dynamic Non-Namespace Extensions](dynamic-non-namespace-extensions.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




