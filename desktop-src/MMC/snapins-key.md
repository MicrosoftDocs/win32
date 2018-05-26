---
title: SnapIns Key
description: All snap-ins must have their own key in the SnapIns key.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dbaa70f0-685d-42c9-bc33-aad8e616ecc5
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- SnapIns Key
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SnapIns Key

All snap-ins must have their own key in the **SnapIns** key. A snap-in's key contains values and subkeys that MMC uses to display the snap-in in the "Add/Remove Snap-ins" dialog box, to identify the snap-in's type (stand-alone and/or extension), and to get a list of its node types.

> [!Note]  
> Use of symbols (such as %systemroot% for example) are not supported in registry key properties.

 

The **SnapIns** key has the following form:


```C++
HKEY_LOCAL_MACHINE\Software\Microsoft\MMC\SnapIns\
  {snapinCLSID}
    NameString REG_SZ "SnapinDisplayName"
    NameStringIndirect REG_SZ "@[path\]<dllname>,-<strId>"
    About REG_SZ "{SnapinAboutCLSID}"
    StandAlone
    NodeTypes
      {nodetypeGUID}
```



<dl> <dt>

<span id="_snapinCLSID_"></span><span id="_snapinclsid_"></span><span id="_SNAPINCLSID_"></span>{snapinCLSID}
</dt> <dd>

Key. The name for a snap-in's key is the string representation of the snap-in's CLSID. The string must begin with an open curly brace ({) and end with a close curly brace (}).

</dd> <dt>

<span id="NameString"></span><span id="namestring"></span><span id="NAMESTRING"></span>NameString
</dt> <dd>

REG\_SZ value. The name of the snap-in displayed in the Add/Remove Snap-ins dialog box. If this value is not set, the snap-in appears in the Add/Remove Snap-ins dialog box with no name.

</dd> <dt>

<span id="NameStringIndirect"></span><span id="namestringindirect"></span><span id="NAMESTRINGINDIRECT"></span>NameStringIndirect
</dt> <dd>

REG\_SZ value. The string representation of the resource DLL name and string identifier used to indirectly retrieve the snap-in's name. Multilanguage User Interface (MUI) support requires a value for NameStringIndirect.

The string is represented by the following format:


```C++
"@[path\]<dllname>,-<strId>"
```



path is an optional path to the DLL. If no path is provided, MMC uses the search strategy employed by [LoadLibrary](https://msdn.microsoft.com/library/windows/desktop/ms684175) to locate the DLL.

dllname is the name of the DLL that contains the string resource.

strId is the string identifier (an integer).

The NameStringIndirect value is not used prior to MMC 2.0. If NameStringIndirect does not exist in the registry, or if its value data does not lead to a successful string load, then MMC uses the NameString value data as the name string.

</dd> <dt>

<span id="About"></span><span id="about"></span><span id="ABOUT"></span>About
</dt> <dd>

REG\_SZ value. The string representation of the CLSID of the object that is created using the CoCreateInstance COM function to get an interface pointer to [**ISnapInAbout**](/windows/win32/Mmc/nn-mmc-isnapinabout?branch=master). The string must begin with an open curly brace ({) and end with a close curly brace (}).

The ISnapInAbout object is created when MMC must display the icon and/or description for the snap-in in the Add/Remove Snap-ins dialog box.

If your snap-in does not implement **ISnapinAbout** or if the About value is not set, no description is displayed and a generic folder icon is displayed in the Add/Remove Snap-ins dialog box.

</dd> <dt>

<span id="StandAlone"></span><span id="standalone"></span><span id="STANDALONE"></span>StandAlone
</dt> <dd>

Key. The presence of this key specifies that the snap-in is a stand-alone snap-in.

If the snap-in is a stand-alone snap-in, add the StandAlone key. The snap-in can then be added to the namespace as a stand-alone snap-in in the Standalone tab of the Add/Remove Snap-ins dialog box. Be aware that a stand-alone snap-in can also be an extension snap-in (that is, it can extend other snap-ins). If the snap-in is also an extension snap-in, it must be registered for the particular node types it extends. For more information, see [NodeTypes Key](nodetypes-key.md).

If the snap-in is an extension snap-in only, do not add the StandAlone key. If the StandAlone key is not present, the snap-in cannot be added in the Standalone tab. An extension snap-in can extend other snap-ins in the Extensions tab. Be aware that the extension snap-in must be registered as an extension for the particular node type that it extends in order for it to appear as an available extension for a stand-alone snap-in. For more information, see [NodeTypes Key](nodetypes-key.md).

</dd> <dt>

<span id="NodeTypes"></span><span id="nodetypes"></span><span id="NODETYPES"></span>NodeTypes
</dt> <dd>

Key. This key contains values that represent the snap-in's own node types. Each node type is represented as a value that is the GUID of the node type. All node types (that is, all node types for the snap-in specified by {snapinCLSID}) that can be extended should be added as subkeys of this key. If the snap-in is stand-alone, the node type for the snap-in's static node can also be added if you want other snap-ins to extend the static node.

MMC uses the values in this key to find the node types for the snap-in and then uses that list of node types to get the extensions for those node types. That set of extension snap-ins is displayed as the available extensions for the snap-in in the Extensions tab of the Add/Remove Snap-ins dialog box.

</dd> <dt>

<span id="_nodetypeGUID_"></span><span id="_nodetypeguid_"></span><span id="_NODETYPEGUID_"></span>{nodetypeGUID}
</dt> <dd>

Key. The string representation of the GUID of the node type. The string must begin with an open curly brace ({) and end with a close curly brace (}).

</dd> </dl>

## Example

The following example shows the **SnapIns** key for a stand-alone snap-in with the display name of My Snap-in, an **ISnapinAbout** object, and four node types that can be extended.

Incidentally, do not use these GUIDs for your own applications. They are examples only.


```C++
HKEY_LOCAL_MACHINE\Software\Microsoft\MMC\Snapins\
  {04ebc1e6-a16c-11d0-a799-00c04fd8d565} 
    NameString = REG_SZ "My Snap-in"
    NameStringIndirect = REG_SZ "@MyApp.dll,-42"
    About = REG_SZ "{128ac4e6-a16c-11d0-a799-00c04fd8d565}"
    NodeTypes
      {c713e06c-a16e-11d0-a799-00c04fd8d565}
      {c713e06d-a16e-11d0-a799-00c04fd8d565}
      {c713e06e-a16e-11d0-a799-00c04fd8d565}
      {c713e06f-a16e-11d0-a799-00c04fd8d565}
    StandAlone
```



 

 




