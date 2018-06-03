---
title: NodeTypes Key
description: All node types that can be extended have their own subkey in the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes key.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0745c385-dff7-41cb-ba74-a635a8cb77b2
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- NodeTypes Key
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NodeTypes Key

All node types that can be extended have their own subkey in the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes key. A node type key contains an Extensions subkey. The Extensions key contains subkeys that represent the types of extensions (such as NameSpace for namespace extensions, and so on). Each extension type subkey contains values that represent the CLSIDs of the snap-ins that extend that node type with that type of extension. For example, you would add the CLSID of a snap-in that extended the namespace of the node type in the MMC\\NodeTypes\\{nodetypeGUID}\\Extensions\\NameSpace subkey.

MMC uses the NodeTypes key to determine the extension snap-ins that can extend the node types for each snap-in. An extension snap-in must register itself for each node type that it extends as well as register what type of extensions it provides. Be aware that an extension snap-in does not extend a snap-in until the user enables the extension from the Extensions tab of the Add/Remove Snap-ins dialog box or until the extended snap-in adds the extension as a dynamic extension. For more information, see [Adding Dynamic Extensions](adding-dynamic-extensions.md).

A snap-in with node types that can be extended must add those node types as node type keys in the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes key. A node type key is represented as a key whose name is the GUID of the node type. The node type must also be added as a value in the snap-in's HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns\\{snapinCLSID}\\NodeTypes key.

An extension snap-in must add its CLSID as a value to the extension type key for each type of extension it provides for a particular node type.

The NodeTypes key has the following form:


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



<dl> <dt>

<span id="_nodetypeGUID_"></span><span id="_nodetypeguid_"></span><span id="_NODETYPEGUID_"></span>{nodetypeGUID}
</dt> <dd>

Key. The string representation of the GUID of the node type. The string must begin with an open curly brace ({) and end with a close curly brace (}).

There must also be a corresponding {nodetypeGUID} value in the snap-in's HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns\\{snapinCLSID}\\NodeTypes key.

</dd> <dt>

<span id="Extensions"></span><span id="extensions"></span><span id="EXTENSIONS"></span>Extensions
</dt> <dd>

Key. This key contains subkeys and values that list the snap-ins that are registered to extend the node type. The extensions are grouped by extension type. There are six types: NameSpace, ContextMenu, ToolBar, PropertySheet, Task, and View (in MMC 2.0 only).

The extension snap-in must add its CLSID as a value in the extension type key for each type of extension it adds.

</dd> <dt>

<span id="NameSpace"></span><span id="namespace"></span><span id="NAMESPACE"></span>NameSpace
</dt> <dd>

Key. This key contains values that represent the CLSIDs of snap-ins that can extend the namespace of items with this node type.

</dd> <dt>

<span id="ContextMenu"></span><span id="contextmenu"></span><span id="CONTEXTMENU"></span>**ContextMenu**
</dt> <dd>

Key. This key contains values that represent the CLSIDs of snap-ins that can extend the context menu of items with this node type.

</dd> <dt>

<span id="ToolBar"></span><span id="toolbar"></span><span id="TOOLBAR"></span>ToolBar
</dt> <dd>

Key. This key contains values that represent the CLSIDs of snap-ins that can extend the toolbar of items with this node type.

</dd> <dt>

<span id="PropertySheet"></span><span id="propertysheet"></span><span id="PROPERTYSHEET"></span>PropertySheet
</dt> <dd>

Key. This key contains values that represent the CLSIDs of snap-ins that can extend the property sheet of items with this node type.

</dd> <dt>

<span id="Task"></span><span id="task"></span><span id="TASK"></span>**Task**
</dt> <dd>

Key. This key contains values that represent the CLSIDs of snap-ins that can extend the taskpad of items with this node type.

</dd> <dt>

<span id="View"></span><span id="view"></span><span id="VIEW"></span>View
</dt> <dd>

Key. This key contains values that represent the CLSIDs of snap-ins that can extend the view of items with this node type.

</dd> <dt>

<span id="_extensionsnapinCLSID_"></span><span id="_extensionsnapinclsid_"></span><span id="_EXTENSIONSNAPINCLSID_"></span>{extensionsnapinCLSID}
</dt> <dd>

Key. The string representation of the CLSID of an extension snap-in. The string must begin with an open curly brace ({) and end with a close curly brace (}).

</dd> <dt>

<span id="Dynamic_Extensions"></span><span id="dynamic_extensions"></span><span id="DYNAMIC_EXTENSIONS"></span>Dynamic Extensions
</dt> <dd>

Key. This key contains values that represent the CLSIDs of snap-ins that should act only as dynamic extensions to this node type. Snap-ins listed in this key are not displayed in the Extensions tab of the Add/Remove Snap-ins dialog box. Dynamic extensions are extension snap-ins that are added to a scope or result item programmatically at run time.

</dd> </dl>

## Example

The following example shows the NodeTypes key for a node type with NameSpace, ContextMenu, ToolBar, and PropertySheet extensions. There is also one dynamic extension.

Incidentally, do not use these GUIDs for your own applications. They are examples only.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         MMC
            NodeTypes
               {12345601-EA27-11CF-ADCF-00AA00A80033} = Log object<dl>
<dt>

               Data type
</dt>
<dd>               REG_SZ</dd>
</dl>
               Extensions
                  NameSpace
                     {19876201-EA27-11CF-ADCF-00AA00A80033} = Alert Snap-In<dl>
<dt>

                     Data type
</dt>
<dd>                     REG_SZ</dd>
</dl>
                     {34346202-EA27-11CF-ADCF-00AA00A80033} = Viewer Snap-In<dl>
<dt>

                     Data type
</dt>
<dd>                     REG_SZ</dd>
</dl>
                  ContextMenu
                     {19876202-EA27-11CF-ADCF-00AA00A80033} = Alert Snap-In<dl>
<dt>

                     Data type
</dt>
<dd>                     REG_SZ</dd>
</dl>
                     {34346202-EA27-11CF-ADCF-00AA00A80033} = Viewer Snap-In<dl>
<dt>

                     Data type
</dt>
<dd>                     REG_SZ</dd>
</dl>
                     {4c8811b4-aa1a-11d1-95b5-0000f875b660} = My Dynamic Snap-In<dl>
<dt>

                     Data type
</dt>
<dd>                     REG_SZ</dd>
</dl>
                  ToolBar
                     {19876202-EA27-11CF-ADCF-00AA00A80033} = Alert Snap-In<dl>
<dt>

                     Data type
</dt>
<dd>                     REG_SZ</dd>
</dl>
                     {45091ca8-EA27-11CF-ADCF-00AA00A80033} = Crystal Report<dl>
<dt>

                     Data type
</dt>
<dd>                     REG_SZ</dd>
</dl>
                  PropertySheet
                     {19876202-EA27-11CF-ADCF-00AA00A80033} = Alert Snap-In<dl>
<dt>

                     Data type
</dt>
<dd>                     REG_SZ</dd>
</dl>
                     {4c8811b4-aa1a-11d1-95b5-0000f875b660} = My Dynamic Snap-In<dl>
<dt>

                     Data type
</dt>
<dd>                     REG_SZ</dd>
</dl>
               Dynamic Extensions
                  {4c8811b4-aa1a-11d1-95b5-0000f875b660} = My Dynamic Snap-In<dl>
<dt>

                  Data type
</dt>
<dd>                  REG_SZ</dd>
</dl>
```

For more information about the registry, see [Registry](mmc-registry-entries.md).

 

 




