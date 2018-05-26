---
title: Adding Wizard Pages
description: This feature is introduced in MMC 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3100f43b-36ec-4627-ab55-fac3c6bb44c6
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- wizard pages MMC
- wizard pages MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding Wizard Pages

This feature is introduced in MMC 1.1.

A wizard is a special type of property sheet. Wizards are designed to present pages one at a time in a sequence that is controlled by the application. Instead of selecting from a group of pages by clicking a tab, users move forward and backward through the sequence, one page at a time, by clicking the **Next** or **Back** button located at the bottom of the wizard.

MMC enables a snap-in to add either standard wizard pages or Wizard 97 pages. Wizard 97 pages have a different style than standard wizard pages. Be aware that snap-ins are strongly encouraged to use the Wizard 97 style for all wizards they create in order to have a consistent style throughout MMC.

For more information about wizard pages, see the Windows SDK on MSDN. The rest of the discussion focuses on adding wizard pages to a snap-in using the interfaces and other constructs provided in the MMC SDK.

The MMC interfaces used for adding wizard pages are the same as those used for [adding property pages](adding-property-pages.md). The [**IPropertySheetProvider**](/windows/win32/Mmc/nn-mmc-ipropertysheetprovider?branch=master) and [**IPropertySheetCallback**](/windows/win32/Mmc/nn-mmc-ipropertysheetcallback?branch=master) interfaces are implemented by MMC and are used to create and maintain property sheet objects. The [**IExtendPropertySheet2**](/windows/win32/Mmc/nn-mmc-iextendpropertysheet2?branch=master) interface is implemented by the snap-in.

In order for MMC to create the property sheet with wizard controls (a wizard), the snap-in must directly call the [**IPropertySheetProvider**](/windows/win32/Mmc/nn-mmc-ipropertysheetprovider?branch=master) interface and its [**CreatePropertySheet**](/windows/win32/Mmc/nf-mmc-ipropertysheetprovider-createpropertysheet?branch=master) method. The snap-in can also specify in the method call that the wizard use the Wizard 97 style.

In addition to the [**CreatePropertySheet**](/windows/win32/Mmc/nf-mmc-ipropertysheetprovider-createpropertysheet?branch=master) method, the [**IPropertySheetProvider**](/windows/win32/Mmc/nn-mmc-ipropertysheetprovider?branch=master) interface includes the following methods:

-   [**FindPropertySheet**](/windows/win32/Mmc/nf-mmc-ipropertysheetprovider-findpropertysheet?branch=master) determines whether a property sheet already exists for a particular scope or result item.
-   [**AddPrimaryPages**](/windows/win32/Mmc/nf-mmc-ipropertysheetprovider-addprimarypages?branch=master) collects pages from a primary snap-in.
-   [**AddExtensionPages**](/windows/win32/Mmc/nf-mmc-ipropertysheetprovider-addextensionpages?branch=master) collects pages from extension snap-ins.
-   [**Show**](/windows/win32/Mmc/nf-mmc-ipropertysheetprovider-show?branch=master) displays a specific property sheet frame.

To define wizard pages with watermarks and header bitmaps, snap-ins must implement the [**IExtendPropertySheet2**](/windows/win32/Mmc/nn-mmc-iextendpropertysheet2?branch=master) interface. The [**CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method defines the properties of one or more wizard pages using the [**PROPSHEETPAGE**](/windows/win32/Prsht/nc-prsht-lpfnaddpropsheetpage?branch=master) structure. The [**GetWatermarks**](/windows/win32/Mmc/nf-mmc-iextendpropertysheet2-getwatermarks?branch=master) method is used to specify the watermark and header bitmaps for the wizard. MMC calls the [**QueryPagesFor**](iextendpropertysheet2-querypagesfor.md) method to verify that a wizard page exists for a particular scope or result item when the user clicks the **Properties** context menu item.

## Related topics

<dl> <dt>

[Adding Wizard Pages: Interfaces](adding-wizard-pages-interfaces.md)
</dt> <dt>

[Adding Wizard Pages: Implementation Details](adding-wizard-pages-implementation-details.md)
</dt> <dt>

[Adding Watermarks to Wizard 97 Pages](adding-watermarks-to-wizard-97-pages.md)
</dt> <dt>

[Using IPropertySheetProvider Directly](using-ipropertysheetprovider-directly.md)
</dt> <dt>

[Adding Property Pages and Wizard Pages](adding-property-pages-and-wizard-pages.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




