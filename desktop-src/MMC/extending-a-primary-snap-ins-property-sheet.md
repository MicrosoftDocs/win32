---
title: Extending the Property Sheet of a Primary Snap-in
description: This section discusses the specific Steps necessary for an extension snap-in to extend the property sheet of an extendable node type owned by a primary snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bb360bf9-8d8e-402f-af61-b6c9b57852e3'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["extending a primary snap-in's property sheet MMC", "primary snap-in's, extending a property sheet"]
---

# Extending the Property Sheet of a Primary Snap-in

This section discusses the specific Steps necessary for an extension snap-in to extend the property sheet of an extendable node type owned by a primary snap-in. For more information about working with extension snap-ins, see [Working with Extension Snap-ins](working-with-extension-snap-ins.md).

A primary snap-in registers the extendable node types that it adds to its namespace. An extension snap-in can extend the property sheet of a primary snap-in's node type by adding the appropriate registration code and then implementing the [**IExtendPropertySheet2**](iextendpropertysheet2.md) interface.

Primary snap-ins that add node types that can be extended by property page extensions must enable the MMC\_VERB\_PROPERTIES verb for the extendable items. For more information about enabling standard verbs, see [Enabling MMC Standard Verbs](enabling-mmc-standard-verbs.md). Primary snap-ins that do not add property pages of their own must still implement [**IExtendPropertySheet2**](iextendpropertysheet2.md) and return S\_OK in their implementation of the **IExtendPropertySheet2** methods.

A primary snap-in that uses [**IPropertySheetProvider**](ipropertysheetprovider.md) to display a property sheet must explicitly enable extension snap-ins to add extension pages by calling [**IPropertySheetProvider::AddExtensionPages**](ipropertysheetprovider-addextensionpages.md).

In the following procedure, be aware that {CLSID}, {snapinCLSID}, and {nodetypeGUID} all denote string representations of the specified CLSIDs and GUIDs. The strings must begin with an open brace ({) and end with a close brace (}).

**To extend a primary snap-in property sheet**

1.  The CLSID of each snap-in (extension or stand-alone) must be registered under the HKEY\_CLASSES\_ROOT\\CLSID key in the {CLSID} subkey as an in-process server DLL. The snap-in must also register a threading model for the snap-in CLSID. An apartment threading model is recommended.

    For more information about the HKEY\_CLASSES\_ROOT\\CLSID key, see the [CLSID Key](_com_CLSID_Key) . For more information and a code example, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

2.  All snap-ins must be registered under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns key in the {snapinCLSID} key. For more information about the SnapIns key, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).
3.  Register the CLSID of the extension snap-in under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{nodetypeGUID}\\Extensions\\PropertySheet subkey, where nodetypeGUID is the node type GUID of the node type whose property sheet is extended. For more information about the NodeTypes key, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).
4.  Implement the [**IExtendPropertySheet2::CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method to add property pages.

    In the implementation of [**CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md):

    -   Define one or more property pages by filling the [**PROPSHEETPAGE**](propsheetpage.md) structure for each of the property pages with information about the page. Be aware that the standard size for a property page in an MMC console is 252 dialog units horizontally and 218 dialog units vertically.
    -   For each [**PROPSHEETPAGE**](propsheetpage.md) structure, call the API function [**CreatePropertySheetPage**](_win32_createpropertysheetpage_cpp) to create a property sheet page. The function returns a handle to the HPROPSHEETPAGE type that uniquely identifies the page.
    -   Using the pointer to the [**IPropertySheetCallback**](ipropertysheetcallback.md) interface passed to the snap-in in the call to the [**CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method, call the [**IPropertySheetCallback::AddPage**](ipropertysheetcallback-addpage.md) method to add each property page to the MMC-provided property sheet.

5.  Implement a dialog box procedure for each property page. The pfnDlgProc member of each property page's [**PROPSHEETPAGE**](propsheetpage.md) structure should be set to the address of this procedure.
6.  Implement the [**IExtendPropertySheet2::QueryPagesFor**](iextendpropertysheet2-querypagesfor.md) method. MMC calls this method when the user selects a scope or result item and clicks the [**Properties**](snapin-properties.md) context menu item. If this method returns S\_OK, MMC then calls the snap-in's implementation of the [**IExtendPropertySheet2::CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method.

## Related topics

<dl> <dt>

[Adding Property Pages and Wizard Pages](adding-property-pages-and-wizard-pages.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




