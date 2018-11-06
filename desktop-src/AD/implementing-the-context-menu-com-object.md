---
title: Implementing the Context Menu COM Object
description: A context menu extension is a COM object implemented as an in-proc server.
ms.assetid: 362dd8e5-1518-4bf4-ac53-115263cd6c62
ms.tgt_platform: multiple
keywords:
- context menu COM object AD
- context menu COM object AD ,implementing
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Context Menu COM Object

A context menu extension is a COM object implemented as an in-proc server. The context menu extension must implement the [**IShellExtInit**](https://msdn.microsoft.com/library/Bb775096(v=VS.85).aspx) and [**IContextMenu**](https://msdn.microsoft.com/library/Bb776095(v=VS.85).aspx) interfaces. A context menu extension is instantiated when the user displays the context menu for an object of a class for which the context menu extension has been registered.

## Implementing IShellExtInit

After the context menu extension COM object is instantiated, the [**IShellExtInit::Initialize**](https://msdn.microsoft.com/library/Bb775094(v=VS.85).aspx) method is called. **IShellExtInit::Initialize** supplies the context menu extension with an [**IDataObject**](https://msdn.microsoft.com/en-us/library/ms688421(v=VS.85).aspx) object that contains data pertinent to the directory object that the context menu applies to.

The [**IDataObject**](https://msdn.microsoft.com/en-us/library/ms688421(v=VS.85).aspx) contains data in the [**CFSTR\_DSOBJECTNAMES**](https://msdn.microsoft.com/library/aa814586) format. The **CFSTR\_DSOBJECTNAMES** data format is an **HGLOBAL** that contains a [**DSOBJECTNAMES**](/windows/desktop/api/Dsclient/ns-dsclient-dsobjectnames) structure. The **DSOBJECTNAMES** structure contains data about the directory object that the property sheet extension applies to.

The [**IDataObject**](https://msdn.microsoft.com/en-us/library/ms688421(v=VS.85).aspx) also contains data in the [**CFSTR\_DS\_DISPLAY\_SPEC\_OPTIONS**](cfstr-ds-display-spec-options.md) format. The **CFSTR\_DS\_DISPLAY\_SPEC\_OPTIONS** data format is an **HGLOBAL** that contains a [**DSDISPLAYSPECOPTIONS**](/windows/desktop/api/Dsclient/ns-dsclient-_dsdisplayspecoptions) structure. The **DSDISPLAYSPECOPTIONS** contains configuration data for use by the extension.

If any value other than **S\_OK** is returned from [**IShellExtInit::Initialize**](https://msdn.microsoft.com/library/Bb775094(v=VS.85).aspx), the context menu extension will not be used.

The *pidlFolder* and *hkeyProgID* parameters of the [**IShellExtInit::Initialize**](https://msdn.microsoft.com/library/Bb775094(v=VS.85).aspx) method are not used.

## Implementing IContextMenu

After [**IShellExtInit::Initialize**](https://msdn.microsoft.com/library/Bb775094(v=VS.85).aspx) returns, the [**IContextMenu::QueryContextMenu**](https://msdn.microsoft.com/library/Bb776097(v=VS.85).aspx) method is called to obtain the menu item or items that the context menu extension will add. The **QueryContextMenu** implementation is fairly straightforward. The context menu extension adds its menu items using the [**InsertMenuItem**](https://msdn.microsoft.com/library/ms647988(v=VS.85).aspx) or similar function. The menu command identifiers must be greater than or equal to *idCmdFirst* and must be less than *idCmdLast*. **QueryContextMenu** must return the greatest numeric identifier added to the menu plus one. The best way to assign menu command identifiers is to start at zero and work up in sequence. If the context menu extension does not need to any menu items, it should simply not add any items to the menu and return zero from **QueryContextMenu**.

[**IContextMenu::GetCommandString**](https://msdn.microsoft.com/library/Bb776094(v=VS.85).aspx) is called to retrieve textual data for the menu item, such as help text to be displayed for the menu item. It is possible that the context menu host will use Unicode strings while the extension uses ANSI strings. Because of this, the **GCS\_HELPTEXTA**, **GCS\_HELPTEXTW**, **GCS\_VERBA** and **GCS\_VERBW** cases must be handled individually. Implementation of this method is optional.

[**IContextMenu::InvokeCommand**](https://msdn.microsoft.com/library/Bb776096(v=VS.85).aspx) is called when one of the menu items installed by the context menu extension is selected. The context menu performs or initiates the desired actions in response to this method.

 

 




