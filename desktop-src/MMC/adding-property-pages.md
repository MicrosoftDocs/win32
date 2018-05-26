---
title: Adding Property Pages
description: This topic discusses adding property pages to a snap-in using the interfaces and other constructs provided in the MMC SDK.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 66039fc0-8992-4154-9f69-52f4ca9475bb
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- property pages MMC
- property pages MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding Property Pages

This topic discusses adding property pages to a snap-in using the interfaces and other constructs provided in the MMC SDK.

The MMC SDK defines three main interfaces for working with property pages. Two of these interfaces —[**IPropertySheetProvider**](ipropertysheetprovider.md) and [**IPropertySheetCallback**](ipropertysheetcallback.md)— are implemented by MMC and are used to create and maintain property sheet objects. The third interface, [**IExtendPropertySheet2**](iextendpropertysheet2.md), is implemented by the snap-in.

The [**IPropertySheetProvider**](ipropertysheetprovider.md) interface implements property sheets as COM objects.

The following list contains methods included in this interface:

-   [**CreatePropertySheet**](ipropertysheetprovider-createpropertysheet.md) creates a property sheet frame.
-   [**FindPropertySheet**](ipropertysheetprovider-findpropertysheet.md) determines whether a property sheet already exists.
-   [**AddPrimaryPages**](ipropertysheetprovider-addprimarypages.md) collects pages from a primary snap-in.
-   [**AddExtensionPages**](ipropertysheetprovider-addextensionpages.md) collects pages from extension snap-ins.
-   [**Show**](ipropertysheetprovider-show.md) displays a specific property sheet frame.

MMC uses its own [**IPropertySheetProvider**](ipropertysheetprovider.md) implementation when it initiates the display of the property sheet — for example, when the user activates the properties verb on an item. If the snap-in wishes to display property sheets at other times, it should call directly into MMC's **IPropertySheetProvider**. In both cases, the **IPropertySheetProvider** methods call into the snap-in's IExtendPropertySheet implementation and supply an [**IPropertySheetCallback**](ipropertysheetcallback.md) interface pointer so that the snap-in can add property pages.

Be aware that MMC owns all property sheets created by its [**IPropertySheetProvider**](ipropertysheetprovider.md) implementation. Snap-ins own property pages that they add to property sheets, but the property sheet objects themselves are created, maintained, and destroyed by MMC.

The [**IPropertySheetCallback**](ipropertysheetcallback.md) interface contains two methods. [**AddPage**](ipropertysheetcallback-addpage.md) enables a snap-in to add a single page to the MMC-owned property sheet of a scope or result item. [**RemovePage**](ipropertysheetcallback-removepage.md) enables a snap-in to remove a page.

Generally, if a primary snap-in wants its extendable node types to be extended by property sheet extensions, it should enable the MMC\_VERB\_PROPERTIES verb for the extendable items, even if it does not add property pages of its own. In addition, the primary snap-in must implement [**IExtendPropertySheet2**](iextendpropertysheet2.md) and return S\_OK in its implementation of the **IExtendPropertySheet2** methods. This allows all property sheet extensions to the selected node type to add their own pages when the user activates the properties verb.

As previously stated, snap-ins can choose to display a property sheet independent of the properties verb. In this case, they must use the [**IPropertySheetProvider**](ipropertysheetprovider.md) interface. A situation where this can occur is if an extension snap-in wants to display properties for an extendable node type that does not display its own property sheet (via the properties verb). Although this is not recommended (see previous paragraph), it may occur. Now, extension snap-ins cannot enable verbs (such as the properties verb) on the context menus owned by other snap-ins. Extension snap-ins must therefore use the **IPropertySheetProvider** interface to display a property sheet. See [Using IPropertySheetProvider Directly](using-ipropertysheetprovider-directly.md) for details.

Similarly, snap-ins must use [**IPropertySheetProvider**](ipropertysheetprovider.md) to add a feature that has a property sheet as a user interface, but identifies the sheet as something else. An example of this is the Select Computer dialog box. This dialog box appears in the Event Viewer snap-in when the user selects the Event Viewer node and clicks the Connect to another computer context menu item.

Finally, snap-ins (primary and extension) must also use the [**IPropertySheetProvider**](ipropertysheetprovider.md) interface to display wizards and add pages to them. For more information about adding wizard pages, see [Adding Wizard Pages: Implementation Details](adding-wizard-pages-implementation-details.md).

Be aware that each property sheet is modeless and is created in its own thread. MMC does not support marshaling of its published interfaces, so snap-ins cannot call MMC interfaces from within their property page dialog procedure (which executes in the property sheet thread). However, snap-ins can use other techniques, such as posting messages to hidden windows.

## Related topics

<dl> <dt>

[Adding Property Pages: Interfaces](adding-property-pages-interfaces.md)
</dt> <dt>

[Adding Property Pages: Implementation Details](adding-property-pages-implementation-details.md)
</dt> <dt>

[Using IPropertySheetProvider Directly](using-ipropertysheetprovider-directly.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> <dt>

[Adding Wizard Pages](adding-wizard-pages.md)
</dt> </dl>

 

 




