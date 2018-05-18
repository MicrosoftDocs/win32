---
title: Extending the Context Menu of a Primary Snap-in
description: This topic discusses the specific Steps necessary for an extension snap-in to extend the context menu of a node type owned by a primary snap-in. For more information about working with extension snap-ins, see Working with Extension Snap-ins.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6953ca1f-25db-402d-824b-3fc9436c9fbd'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["extending a primary snap-in's context menu MMC", "primary snap-in's, extending a context menu"]
---

# Extending the Context Menu of a Primary Snap-in

This topic discusses the specific Steps necessary for an extension snap-in to extend the context menu of a node type owned by a primary snap-in. For more information about working with extension snap-ins, see [Working with Extension Snap-ins](working-with-extension-snap-ins.md).

A primary snap-in registers the extendable node types that it adds to its namespace. An extension snap-in can extend the context menu of a primary snap-in node type by adding the appropriate registration code and then implementing the [**IExtendContextMenu**](iextendcontextmenu.md) interface.

In the following procedure, be aware that {CLSID}, {snapinCLSID} and {nodetypeGUID} all denote string representations of the specified CLSIDs and GUIDs. The strings must begin with an open brace ({) and end with a close brace (}).

**To extend a primary snap-in context menu**

1.  The CLSID of each snap-in (extension or stand-alone) must be registered under the HKEY\_CLASSES\_ROOT\\CLSID key in the {CLSID} subkey as an in-process server DLL. The snap-in must also register a threading model for the snap-in CLSID. An apartment threading model is recommended.

    For more information about the HKEY\_CLASSES\_ROOT\\CLSID key, see the [CLSID Key](_com_CLSID_Key). For more informationa nd a code example, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

2.  All snap-ins must be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns key in the {snapinCLSID} key. For more information about the SnapIns key, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).
3.  Register the CLSID of the extension snap-in under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{nodetypeGUID}\\Extensions\\ContextMenu subkey, where nodetypeGUID is the node type GUID of the node type whose context menu is extended. For more information about the NodeTypes key, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).
4.  Implement the [**IExtendContextMenu**](iextendcontextmenu.md) interface as you would for adding items to the context menu of a primary snap-in. For more information, see [Working with Context Menus: Implementation Details](working-with-context-menus-implementation-details.md).

## Related topics

<dl> <dt>

[Working with Context Menus](working-with-context-menus.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




