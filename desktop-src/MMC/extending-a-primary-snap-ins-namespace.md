---
title: Extending the Namespace of a Primary Snap-in
description: This section discusses the steps necessary for an extension snap-in to extend the namespace of a primary snap-in. For more information about working with extension snap-ins, see Working with Extension Snap-ins.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12c499ce-291d-4599-aca6-48f7538ba3ce
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- extending a primary snap-ins namespace MMC
- primary snap-ins, extending a namespace
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Extending the Namespace of a Primary Snap-in

This section discusses the steps necessary for an extension snap-in to extend the namespace of a primary snap-in. For more information about working with extension snap-ins, see [Working with Extension Snap-ins](working-with-extension-snap-ins.md).

A primary snap-in registers the extendable node types it adds to its namespace. An extension snap-in can extend the namespace of a primary snap-in's node type by adding the appropriate registration code and then implementing the [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master) interface.

When the user selects a scope item in a primary snap-in that is extended by a namespace extension, MMC requests the extension's [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master) interface and calls [**IComponentData::Initialize**](/windows/win32/Mmc/nf-mmc-icomponentdata-initialize?branch=master) to initialize the extension's **IComponentData** object (unless it is already initialized). Like a primary snap-in, a namespace extension can add scope items and enumerate the result pane of any items it adds. When the user selects a scope or result item that a namespace extension has added, MMC uses the extension's **IComponentData** or [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation to notify the extension of notification messages and to request data objects.

A namespace extension owns any scope or result items that it adds. Therefore, it can extend its own items by adding context menu items, property pages, toolbars, and other features, just like any other snap-in.

Also, any scope or result items added by a namespace extension can also be extended by other extension snap-ins. The namespace extension then behaves like a primary snap-in, so it must register the node type GUIDs of its extendable node types and publish any clipboard formats that other extension snap-ins require for extracting context information.

Be aware that MMC creates one instance of a namespace extension for each primary snap-in instance that it extends. This namespace extension instance extends all nodes of the appropriate node type that appear under that instance of the primary snap-in.

In the following procedure, be aware that {CLSID}, {snapinCLSID}, and {nodetypeGUID} all denote string representations of the specified CLSIDs and GUIDs. The strings must begin with an open brace ({) and end with a close brace (}).

**To extend the namespace of a primary snap-in**

1.  The CLSID of each snap-in (extension or stand-alone) must be registered under the HKEY\_CLASSES\_ROOT\\CLSID key in the {CLSID} subkey as an in-process server DLL. The snap-in must also register a threading model for the snap-in CLSID. An apartment threading model is recommended.

    For more information about the HKEY\_CLASSES\_ROOT\\CLSID key, see the [CLSID Key](_com_CLSID_Key). For more information and a code example, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

2.  All snap-ins must be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns key in the {snapinCLSID} key. Also, if the namespace extension adds scope or result items that can be extended by other extension snap-ins, add the node type GUIDs of the extendable node types under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns\\{snapinCLSID}\\NodeTypes key.

    For more information about the **SnapIns** key, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

3.  Register the CLSID of the extension snap-in under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{nodetypeGUID}\\Extensions\\Namespace subkey, where nodetypeGUID is the GUID of the node type whose namespace is extended. For more information about the NodeTypes key, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).
4.  Implement the [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master) interface as you would for adding scope items to the scope pane of a primary snap-in. For more information and detailed instructions, see [Working with the Scope Pane: Implementation Details](working-with-the-scope-pane-implementation-details.md).
5.  The namespace extension [**IComponentData::Notify**](/windows/win32/Mmc/nf-mmc-icomponentdata-notify?branch=master) method will receive an [**MMCN\_EXPAND**](mmcn-expand.md) notification message the first time the user selects a primary snap-in's scope item that is extended by the namespace extension. For the namespace extension to recognize that it is being instructed to add its own items under the primary snap-in scope item, you must implement a mechanism to verify that the currently selected scope item belongs to the primary snap-in or the namespace extension.
6.  If any of the scope items added by the namespace extension also have result pane views, you will need to implement the [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) interface as well. For more information about the view types available, see [Using Different Result Pane View Types](using-different-result-pane-view-types.md).
7.  Also implement the [**IDataObject**](_ole_idataobject) interface. MMC will request data objects from the extension snap-in when one of the scope or result items it adds is selected by the user.
8.  If the namespace extension extends its own items by adding context menu items, toolbars, menu buttons, or property pages, implement the required interfaces. For more information, see [Working with Toolbars and Menu Buttons](working-with-toolbars-and-menu-buttons.md) and [Adding Property Pages and Wizard Pages](adding-property-pages-and-wizard-pages.md).

## Related topics

<dl> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




