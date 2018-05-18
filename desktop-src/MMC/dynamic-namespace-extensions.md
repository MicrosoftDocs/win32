---
title: Dynamic Namespace Extensions
description: This feature is introduced in MMC 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3dc9b2db-1fc0-495b-9acc-3366a24a18a7'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["dynamic namespace extensions MMC"]
---

# Dynamic Namespace Extensions

This feature is introduced in MMC 1.1.

A snap-in can dynamically add namespace extensions to any of its own scope items. To dynamically extend one of your snap-in's scope items, the snap-in simply calls the [**IConsoleNameSpace2::AddExtension**](iconsolenamespace2-addextension.md) method. Be aware that the **AddExtension** method only works for items that are directly owned by the snap-in making the **AddExtension** call.

In addition, [**AddExtension**](iconsolenamespace2-addextension.md) adds the extension (specified by the CLSID specified in the *lpClsid* parameter) to a particular instance of a scope item (which is specified by *hItem* parameter). It does not affect other scope items of that node type.

A common place to add dynamic namespace extensions is in the [**MMCN\_EXPAND**](mmcn-expand.md) notification handler of the snap-in's [**IComponentData**](icomponentdata.md) object.

Be aware that the extension snap-in must be a namespace extension. In addition, the MMC registry entries for the primary snap-in and the extension snap-in must be set correctly. For details on setting MMC registry entries for namespace extensions, see [Extending a Primary Snap-in's Namespace](extending-a-primary-snap-ins-namespace.md).

As with all namespace extensions, the extension snap-in must be able to handle the data object of the scope item extended in the primary snap-in. To interact with a primary snap-in, an extension snap-in must understand the primary snap-in's clipboard formats.

## Related topics

<dl> <dt>

[Adding Dynamic Extensions: Interfaces](adding-dynamic-extensions-interfaces.md)
</dt> <dt>

[Dynamic Non-Namespace Extensions](dynamic-non-namespace-extensions.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> <dt>

[MMC Registry Entries](mmc-registry-entries.md)
</dt> </dl>

 

 




