---
title: Registration Requirements for Extension Snap-ins
description: Registration Requirements for Extension Snap-ins
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6edbd21d-2ec8-4142-97ec-be089d810b7e'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["registration requirements for extension snap-ins MMC"]
---

# Registration Requirements for Extension Snap-ins

In addition to registering its class ID (CLSID) under the HKEY\_CLASSES\_ROOT\\CLSID key as in-process server DLL, an extension snap-in also must register its CLSID in two additional places in the registry:

-   All snap-ins, including extensions, must be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns key in the {snapinCLSID} key. The {snapinCLSID} key is the name for a snap-in's key and is the string representation of the snap-in's CLSID.

    Be aware that when registering an extension snap-in under the [**SnapIns**](document-snapins.md) key, the StandAlone key must not be added. The presence of the StandAlone key is used only to indicate that a snap-in is a stand-alone snap-in.

    For more information about the [**SnapIns**](document-snapins.md) key, see [SnapIns Key](snapins-key.md). For more information about registering snap-ins, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

-   The CLSID of the extension snap-in must also be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes key.

The NodeTypes key has the following form.


```C++
HKEY_LOCAL_MACHINE\Software\Microsoft\MMC\NodeTypes\
   {nodetypeGUID}
      Extensions
         NameSpace
            {extensionsnapinCLSID}
         ContextMenu
            {extensionsnapinCLSID}
         ToolBar
            {extensionsnapinCLSID}
         PropertySheet
            {extensionsnapinCLSID}
         Task
            {extensionsnapinCLSID}
         View
            {extensionsnapinCLSID}
      Dynamic Extensions
         {extensionsnapinCLSID}
```



-   The {nodetypeGUID} key specifies the string representation of the GUID of the node type that is extended. The string must begin with an open brace ({) and end with a close brace (}). There must also be a corresponding {nodetypeGUID} value in the primary snap-in's HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns\\{snapinCLSID}\\NodeTypes key, where {snapinCLSID} is the string representation of the snap-in's CLSID.
-   The Extensions key contains subkeys and values that list the snap-ins registered to extend the node type specified by {nodetypeGUID}. The extensions are grouped by extension type. There are six types: NameSpace, ContextMenu, ToolBar, PropertySheet, Task, and View. An extension snap-in must add its CLSID as a value in the appropriate extension type key for each type of extension it adds. View extensions, however, are an exception. The primary snap-in registers the view extension's CLSID for each node type extended.

    -   The NameSpace key contains values that represent the CLSIDs of snap-ins that can extend the namespace of items with this node type.
    -   The **ContextMenu** key contains values that represent the CLSIDs of snap-ins that can extend the context menu of items with this node type.
    -   The ToolBar key contains values that represent the CLSIDs of snap-ins that can extend the toolbar of items with this node type.
    -   The PropertySheet key contains values that represent the CLSIDs of snap-ins that can extend the property sheet of items with this node type.
    -   The **Task** key contains values that represent the CLSIDs of snap-ins that can extend the taskpad of items with this node type.
    -   The View key contains values that represent the CLSIDs of snap-ins that can extend the result view of items with this node type. View extensions require MMC 2.0. For more information about view extensions, see [Extending Views](extending-views.md) and [Extending a Primary Snap-in's View](extending-a-primary-snap-ins-view.md).

-   The {extensionsnapinCLSID} key specifies the string representation of the CLSID of an extension snap-in. The string must begin with an open brace ({) and end with a close brace (}).
-   The Dynamic Extensions key contains values that represent the CLSIDs of snap-ins that should act only as dynamic extensions to this node type. Snap-ins listed in this key are not displayed on the Extensions tab of the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md). Dynamic extensions are extension snap-ins that are added to a scope or result item programmatically at run time.

    Be aware that dynamic extensions must be registered under the Dynamic Extensions key and under the particular subkey of the Extensions key. MMC needs the registration under the Extensions key to determine the extension type of a particular dynamic extension.

MMC uses the CLSID of an extension snap-in to create an instance of the snap-in object and to request the snap-in interface that implements a specific extension type. An extension snap-in can support a number of different extension types, and it is recommended that you register different CLSIDs for the snap-in under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{nodetypeGUID}\\Extensions\\{extensionType} subkey—one for each extension type that the snap-in supports. This enables the snap-in to detect the correct context when its DllGetClassObject method is called. The rclsid parameter in the function call is the same CLSID that MMC finds under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{nodetypeGUID}\\Extensions\\{extensionType} subkey. The riid parameter specifies the requested interface (usually IClassFactory). If the rclsid parameter is different for each extension type, snap-ins can detect which interface is requested during a call to DllGetClassObject.

If you register a different CLSID for each extension type the snap-in supports, verify that you also register each CLSID as an in-process server DLL under the HKEY\_CLASSES\_ROOT\\CLSID key.

## Related topics

<dl> <dt>

[Requirements for Extension Snap-ins](requirements-for-extension-snap-ins.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




