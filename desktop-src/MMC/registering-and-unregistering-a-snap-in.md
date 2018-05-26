---
title: Registering and Unregistering a Snap-in
description: Snap-ins are implemented as COM in-process server DLLs and must be registered appropriately in the MMC registry area.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f46bfe9b-4c4e-49d5-991a-1843b9f99d6c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- registering and unregistering a snap-in MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Registering and Unregistering a Snap-in

Snap-ins are implemented as COM in-process server DLLs and must be registered appropriately in the MMC registry area.

The following list describes all the places in the registry where a snap-in must register itself. Be aware that {CLSID}, {snapinCLSID}, and {nodetypeGUID} all denote string representations of the specified CLSIDs and GUIDs. The strings must begin with an open brace ({) and end with a close brace (}).

-   The CLSID of the snap-in must be registered under the HKEY\_CLASSES\_ROOT\\CLSID key in the {CLSID} subkey as an in-process server DLL. The snap-in must also register a threading model for its CLSID. The snap-in can specify either ThreadingModel = "Apartment" or ThreadingModel = "Both" for the threading model. Be aware that snap-in developers who are unsure of the requirements imposed by specifying ThreadingModel = "Both" should specify an apartment threading model.

    For more information about the HKEY\_CLASSES\_ROOT\\CLSID key, see the [CLSID Key](_com_CLSID_Key) topic.

-   The CLSID of the snap-in must also be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns key. The SnapIns Key has the following form.
    ```C++
    HKEY_LOCAL_MACHINE\Software\Microsoft\MMC\SnapIns\
        {snapinCLSID}
            NameString REG_SZ "SnapinDisplayName"
            About REG_SZ "{SnapinAboutCLSID}"
            StandAlone
            NodeTypes
                {nodetypeGUID}
    ```

    

-   The {snapinCLSID} key specifies the string representation of the snap-in's CLSID. The string must begin with an open brace ({) and end with a close brace (}).
-   The NameString named value specifies the name of the snap-in displayed in the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md). If this value is not set, the snap-in appears in the Add/Remove Snap-in dialog box with no name.
-   The About named value specifies the string representation of the CLSID of the object that is created using the [**CoCreateInstance**](_com_cocreateinstance) COM function to get an interface pointer to [**ISnapInAbout**](/windows/win32/Mmc/nn-mmc-isnapinabout?branch=master). The string must begin with an open brace ({) and end with a close brace (}). The **ISnapInAbout** object is created when MMC displays the icon and description for the snap-in in the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md). If your snap-in does not implement **ISnapInAbout** or if the About value is not set, no description is displayed and a generic folder icon is displayed in the Add/Remove Snap-in dialog box. For more information about implementing the **ISnapInAbout** interface, see [Adding About Information](adding-about-information.md).
-   The presence of the StandAlone key indicates that the snap-in is a stand-alone snap-in. If the snap-in is a stand-alone snap-in, add the StandAlone key. The snap-in can then be added to the namespace as a stand-alone snap-in in the Standalone tab of the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md). Be aware that a stand-alone snap-in can also be an extension snap-in (that is, it can extend other snap-ins). If the snap-in is also an extension snap-in, it must be registered for the node types it extends. For more information, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).

    If the snap-in is an extension snap-in only, do not add the StandAlone key. If the StandAlone key is not present, the snap-in cannot be added in the Standalone tab. An extension snap-in can extend other snap-ins in the Extensions tab. As stated in the previous paragraph, the extension snap-in must be registered as an extension for the node type that it extends in order for it to appear as an available extension for a stand-alone snap-in.

-   The NodeTypes Key contains subkeys that represent the snap-in's own node types. Each node type is represented as a subkey that is the GUID of the node type. All node types (that is, all node types for the snap-in specified by {snapinCLSID}) that can be extended should be added as subkeys in this key. If the snap-in is stand-alone, the node type for the snap-in's static node can also be added if you want other snap-ins to extend the static node.

    MMC uses the subkeys in this key to find the node types for the snap-in and then uses that list of node types to get the extensions for those node types. That set of extension snap-ins is displayed as available extensions for the snap-in in the Extensions tab of the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md).

-   The {nodetypeGUID} named value specifies the string representation of the GUID of the node type. The string must begin with an open brace ({) and end with a close brace (}).

    In addition, all extension snap-ins for a particular node type must be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{nodetypeGUID} key. For more information, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).

For more information about the registry, see the Registry topic.

## Related topics

<dl> <dt>

[Working with IComponentData](working-with-icomponentdata.md)
</dt> <dt>

[Working with IComponent](working-with-icomponent.md)
</dt> <dt>

[Working with IDataObject](working-with-idataobject.md)
</dt> <dt>

[Working with IConsole](working-with-iconsole.md)
</dt> </dl>

 

 




