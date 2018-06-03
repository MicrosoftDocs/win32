---
title: Adding Dynamic Extensions
description: This feature is introduced in MMC 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d1ea37df-82d7-428d-b708-77719fe88d1b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- dynamic extensions MMC
- dynamic extensions MMC , adding
- adding dynamic extensions MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Dynamic Extensions

This feature is introduced in MMC 1.1.

Dynamic extensions are extension snap-ins that are added to a scope or result item programmatically at run time. A snap-in can dynamically add any type of extension to any of its own items.

A primary snap-in can add known extension snap-ins on a per-item basis to items that it (the primary snap-in) owns. For example, if a primary snap-in has a namespace extension that adds an item to its namespace, the primary snap-in cannot dynamically extend the item provided by the namespace extension because the snap-in does not own that item.

When a primary snap-in dynamically extends one of its items, the extension snap-in extends only the specific instance of the item. Other items of that node type are not affected. Dynamically adding an extension is not the same as using the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md) to add an extension to a snap-in. By using the dialog box to add an extension to a primary snap-in, the extension is added to all instances of snap-ins of that type. If you want all instances of your snap-in to be automatically extended by one or more extension snap-ins, the snap-in should implement required extensions. For more information about required extensions, see [Adding Required Extensions](adding-required-extensions.md).

When adding a dynamic extension, the primary snap-in must know the CLSID of the extension snap-ins that can extend it. To prevent extension snap-ins from indiscriminately extending all snap-ins or extending snap-ins inappropriately, MMC forces primary snap-ins to specify the extension snap-ins by their CLSIDs.

In addition to registering its class ID (CLSID) under the HKEY\_CLASSES\_ROOT\\CLSID key as an in-process server DLL, a dynamic extension snap-in also must register its CLSID in three additional places in the registry:

-   All extension snap-ins, including dynamic extensions, must be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns key in the {snapinCLSID} key. The {snapinCLSID} key is the name for a snap-in's key and is the string representation of the snap-in's CLSID. For more information see [SnapIns Key](snapins-key.md) and [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).
-   All extension snap-ins, including dynamic extensions, must also be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{nodetypeGUID}\\Extensions key, where the {nodetypeGUID} key specifies the string representation of the GUID of the node type that is extended, and the Extensions key contains subkeys and values that list the snap-ins that are registered to extend the node type specified by {nodetypeGUID}.
-   Extension snap-ins that can only be loaded as dynamic extensions must be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{nodetypeGUID}\\Dynamic Extensions key. The Dynamic Extensions key contains values that represent the CLSIDs of snap-ins that should act only as dynamic extensions to the node type specified by {nodetypeGUID}.

    Snap-ins listed under the Dynamic Extensions key are not displayed on the Extensions tab of the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md).

    > [!Note]  
    > When grouping dynamic extensions as qualified components in a Windows Installer package, do not use the extended snap-in's GUID as the category GUID. That is, you can still group dynamic extensions by sharing a category GUID (which is the ComponentId value in the PublishComponent table), but the category GUID must not be the extended snap-in's GUID. If the packaged extensions use the extended snap-in's GUID as the category GUID, then MMC will not consider the extensions to be dynamic.

     

For more information about the NodeTypes key, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).

To dynamically extend the namespace of a primary snap-in, use [**IConsoleNameSpace2::AddExtension**](/windows/desktop/api/Mmc/nf-mmc-iconsolenamespace2-addextension). For other types of extensions (context menus, toolbars, property sheets, taskpads), add the [**CCF\_MMC\_DYNAMIC\_EXTENSIONS**](ccf-mmc-dynamic-extensions.md) clipboard format to the [**IDataObject**](https://www.bing.com/search?q=**IDataObject**) implementation for the items you want to extend. The CCF\_MMC\_DYNAMIC\_EXTENSIONS format uses the [**SMMCDynamicExtensions**](https://www.bing.com/search?q=**SMMCDynamicExtensions**) structure, which contains the CLSIDs of the snap-ins that you want to add to an item.

Dynamic extensions apply only to the current session and are not persisted in the console file. For namespace extensions, dynamic extensions persist only for the lifetime of the scope item specified by the hItem parameter of [**IConsoleNameSpace2::AddExtension**](/windows/desktop/api/Mmc/nf-mmc-iconsolenamespace2-addextension). Non-namespace dynamic extensions are not persisted beyond a single use. Each time a context menu, property sheet, or snap-in toolbar is displayed, MMC looks at the [**IDataObject**](https://www.bing.com/search?q=**IDataObject**) for the selected item to get the active dynamic extensions.

To allow future extension snap-ins to dynamically extend your snap-in, you can do one of the following:

-   To enable your own dynamic extensions to the snap-in, you can reserve CLSIDs that can be used by your extensions in the future. Be aware that MMC will ignore non-namespace extension snap-ins that are not properly registered. For namespace extensions, [**IConsoleNameSpace2::AddExtension**](/windows/desktop/api/Mmc/nf-mmc-iconsolenamespace2-addextension) returns **E\_INVALIDARG** if the CLSID is not registered as a namespace extension.
-   To enable other snap-in developers to create extensions that can be dynamically added to your snap-in, your snap-in can read the list of extensions to add dynamically from the registry or from an initialization file and extension snap-ins can add themselves there.

For more information about registering extension snap-ins, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).

## Related topics

<dl> <dt>

[Adding Dynamic Extensions: Interfaces](adding-dynamic-extensions-interfaces.md)
</dt> <dt>

[Dynamic Namespace Extensions](dynamic-namespace-extensions.md)
</dt> <dt>

[Dynamic Non-Namespace Extensions](dynamic-non-namespace-extensions.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> <dt>

[MMC Registry Entries](mmc-registry-entries.md)
</dt> </dl>

 

 




