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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding Property Pages: Implementation Details

The procedures in this section assume that you want to create and add property pages to property sheets that are owned by MMC.

**To add a property page**

1.  Determine whether you want to implement the property page for a scope item or for a result item. Then, depending on your choice, ensure that the snap-in's [**IComponentData**](icomponentdata.md) or correct [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation implements the [**IExtendPropertySheet2**](iextendpropertysheet2.md) interface.
2.  Implement the [**IExtendPropertySheet2::CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method in the appropriate [**IComponentData**](icomponentdata.md) or [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation to add property pages.

    In the implementation of [**CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md):

    -   Define one or more property pages by filling the [**PROPSHEETPAGE**](/windows/win32/Prsht/nc-prsht-lpfnaddpropsheetpage?branch=master) structure for each of the property pages with information about the page. Be aware that the standard size for a property page in an MMC console is 252 dialog units horizontally and 218 dialog units vertically.
    -   For each [**PROPSHEETPAGE**](/windows/win32/Prsht/nc-prsht-lpfnaddpropsheetpage?branch=master) structure, call the API function [**CreatePropertySheetPage**](_win32_createpropertysheetpage_cpp) to create a property sheet page. The function returns a handle to the HPROPSHEETPAGE type that uniquely identifies the page.
    -   Using the pointer to the [**IPropertySheetCallback**](ipropertysheetcallback.md) interface passed to the snap-in in the call to the [**CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method, call the [**IPropertySheetCallback::AddPage**](ipropertysheetcallback-addpage.md) method to add each property page to the MMC-provided property sheet.

3.  Implement a dialog box procedure for each property page. The pfnDlgProc member of each property page's [**PROPSHEETPAGE**](/windows/win32/Prsht/nc-prsht-lpfnaddpropsheetpage?branch=master) structure should be set to the address of this procedure.
4.  Implement the [**IExtendPropertySheet2::QueryPagesFor**](iextendpropertysheet2-querypagesfor.md) method. MMC calls this method when the user selects a scope or result item and clicks the **Properties** context menu item. If this method returns **S\_OK**, MMC then calls the snap-in implementation of the [**IExtendPropertySheet2::CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method.
5.  Use the [**IConsoleVerb::SetVerbState**](iconsoleverb-setverbstate.md) method to enable the MMC\_VERB\_PROPERTIES enumerator value of the [**MMC\_CONSOLE\_VERB**](mmc-console-verb.md) enumeration. The snap-in should call SetVerbState in the handler for the [**MMCN\_SELECT**](mmcn-select.md) notification sent to the corresponding [**IComponentData**](icomponentdata.md) or [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) object. This notification is sent to the snap-in when the user selects the scope item or result item for which you are implementing the property page.
6.  The snap-in should call the [**MMCPropertyChangeNotify**](mmcpropertychangenotify.md) function if the user can change any page properties. As a result of this method call, an [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification is sent to the corresponding [**IComponentData**](icomponentdata.md) or [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) object. The snap-in should be prepared to handle this notification.

## Related topics

<dl> <dt>

[Adding Property Pages: Interfaces](adding-property-pages-interfaces.md)
</dt> </dl>

 

 




