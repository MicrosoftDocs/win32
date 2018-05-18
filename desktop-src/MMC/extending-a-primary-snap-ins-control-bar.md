---
title: Extending the Control Bar of a Primary Snap-in
description: This section discusses the specific Steps necessary for an extension snap-in to extend the control bar of an extendable node type owned by a primary snap-in. For more information about working with extension snap-ins, see Working with Extension Snap-ins.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a3e05023-0209-4deb-accc-c0aac97d6b9c'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["extending a primary snap-in's control bar MMC", "primary snap-in's, extending a control bar"]
---

# Extending the Control Bar of a Primary Snap-in

This section discusses the specific Steps necessary for an extension snap-in to extend the control bar of an extendable node type owned by a primary snap-in. For more information about working with extension snap-ins, see [Working with Extension Snap-ins](working-with-extension-snap-ins.md).

A primary snap-in registers the extendable node types that it adds to its namespace. An extension snap-in can extend the control bar of a primary snap-in node type by adding the appropriate registration code and then implementing the [**IExtendControlBar**](iextendcontrolbar.md) interface. The snap-in can then associate either a toolbar or menu button with the control bar and add items accordingly.

In the following procedure, be aware that {CLSID}, {snapinCLSID}, and {nodetypeGUID} all denote string representations of the specified CLSIDs and GUIDs. The strings must begin with an open brace ({) and end with a close brace (}).

**To extend the control bar of a primary snap-in**

1.  The CLSID of each snap-in (extension or stand-alone) must be registered under the HKEY\_CLASSES\_ROOT\\CLSID key in the {CLSID} subkey as an in-process server DLL. The snap-in must also register a threading model for the snap-in CLSID. An apartment threading model is recommended.

    For more information about the HKEY\_CLASSES\_ROOT\\CLSID key, see the [CLSID Key](_com_CLSID_Key). For more information and a code example, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

2.  All snap-ins must be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns key in the {snapinCLSID} key. For more information about the SnapIns key, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).
3.  Register the CLSID of the extension snap-in under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{nodetypeGUID}\\Extensions\\ToolBar subkey, where nodetypeGUID is the node type GUID of the node type whose control bar is extended. For more information about the NodeTypes key, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).
4.  Implement the [**IExtendControlBar**](iextendcontrolbar.md) interface as you would for adding a toolbar or menu button to the control bar of a primary snap-in. For more information and specific instructions, see [Working with Toolbars: Implementation Details](working-with-toolbars-implementation-details.md) or [Working with Menu Buttons: Implementation Details](working-with-menu-buttons-implementation-details.md).

## Related topics

<dl> <dt>

[Working with Toolbars and Menu Buttons](working-with-toolbars-and-menu-buttons.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




