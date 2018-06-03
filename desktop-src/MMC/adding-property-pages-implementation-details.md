---
title: Adding Property Pages Implementation Details
description: The procedures in this section assume that you want to create and add property pages to property sheets that are owned by MMC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2d384e97-d0f5-4c5e-beec-7d260b5f4d9d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- property pages MMC , implementation details
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Property Pages: Implementation Details

The procedures in this section assume that you want to create and add property pages to property sheets that are owned by MMC.

**To add a property page**

1.  Determine whether you want to implement the property page for a scope item or for a result item. Then, depending on your choice, ensure that the snap-in's [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) or correct [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation implements the [**IExtendPropertySheet2**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet2) interface.
2.  Implement the [**IExtendPropertySheet2::CreatePropertyPages**](https://www.bing.com/search?q=**IExtendPropertySheet2::CreatePropertyPages**) method in the appropriate [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) or [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation to add property pages.

    In the implementation of [**CreatePropertyPages**](https://www.bing.com/search?q=**CreatePropertyPages**):

    -   Define one or more property pages by filling the [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage) structure for each of the property pages with information about the page. Be aware that the standard size for a property page in an MMC console is 252 dialog units horizontally and 218 dialog units vertically.
    -   For each [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage) structure, call the API function [**CreatePropertySheetPage**](https://www.bing.com/search?q=**CreatePropertySheetPage**) to create a property sheet page. The function returns a handle to the HPROPSHEETPAGE type that uniquely identifies the page.
    -   Using the pointer to the [**IPropertySheetCallback**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetcallback) interface passed to the snap-in in the call to the [**CreatePropertyPages**](https://www.bing.com/search?q=**CreatePropertyPages**) method, call the [**IPropertySheetCallback::AddPage**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetcallback-addpage) method to add each property page to the MMC-provided property sheet.

3.  Implement a dialog box procedure for each property page. The pfnDlgProc member of each property page's [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage) structure should be set to the address of this procedure.
4.  Implement the [**IExtendPropertySheet2::QueryPagesFor**](https://www.bing.com/search?q=**IExtendPropertySheet2::QueryPagesFor**) method. MMC calls this method when the user selects a scope or result item and clicks the **Properties** context menu item. If this method returns **S\_OK**, MMC then calls the snap-in implementation of the [**IExtendPropertySheet2::CreatePropertyPages**](https://www.bing.com/search?q=**IExtendPropertySheet2::CreatePropertyPages**) method.
5.  Use the [**IConsoleVerb::SetVerbState**](/windows/desktop/api/Mmc/nf-mmc-iconsoleverb-setverbstate) method to enable the MMC\_VERB\_PROPERTIES enumerator value of the [**MMC\_CONSOLE\_VERB**](/windows/desktop/api/Mmc/ne-mmc-_mmc_console_verb) enumeration. The snap-in should call SetVerbState in the handler for the [**MMCN\_SELECT**](mmcn-select.md) notification sent to the corresponding [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) or [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) object. This notification is sent to the snap-in when the user selects the scope item or result item for which you are implementing the property page.
6.  The snap-in should call the [**MMCPropertyChangeNotify**](/windows/desktop/api/Mmc/nf-mmc-mmcpropertychangenotify) function if the user can change any page properties. As a result of this method call, an [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification is sent to the corresponding [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) or [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) object. The snap-in should be prepared to handle this notification.

## Related topics

<dl> <dt>

[Adding Property Pages: Interfaces](adding-property-pages-interfaces.md)
</dt> </dl>

 

 




