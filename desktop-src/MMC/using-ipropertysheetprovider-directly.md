---
title: Using IPropertySheetProvider Directly
description: Allows snap-ins to display property sheets and wizards.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5371b7ab-a298-44d1-99f1-1cd8f188cb91
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using IPropertySheetProvider Directly

The [**IPropertySheetProvider**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetprovider) interface allows snap-ins to display property sheets and wizards. Usually, snap-ins need not directly use **IPropertySheetProvider** to display a property sheet. Instead, snap-ins use the [**IPropertySheetCallback**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetcallback) interface, which MMC supplies to them so that they can add their own property pages to the property sheet for a particular scope or result item.

The situations in which snap-ins must directly use the [**IPropertySheetProvider**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetprovider) interface include:

-   Snap-ins that display wizards must directly use the [**IPropertySheetProvider**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetprovider) interface to specify wizard sheets. For more information, see [Adding Wizard Pages: Implementation Details](adding-wizard-pages-implementation-details.md).
-   Snap-ins that display property sheets in response to user actions other than the activation of the properties verb must directly use the [**IPropertySheetProvider**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetprovider) interface.

For more information about that displays property sheets in response to the user activating the properties verb, see [Adding Property Pages: Implementation Details](adding-property-pages-implementation-details.md). The rest of this section discusses how to use [**IPropertySheetProvider**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetprovider) to display a property sheet independent of the properties verb.

Be aware that, regardless of whether or not a snap-in directly uses MMC's [**IPropertySheetProvider**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetprovider) implementation, the **IPropertySheetProvider** methods call into the snap-in's [**IExtendPropertySheet**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet) implementation and supply an [**IPropertySheetCallback**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetcallback) interface pointer so that the snap-in can add pages.

**To use IPropertySheetProvider to display a property sheet**

1.  Implement a procedure, say a function called `InvokePropSheet`, that is called when the user performs an action that causes the snap-in to invoke the wizard.
2.  Obtain an [**IPropertySheetProvider**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetprovider) interface pointer by creating an instance of the MMC Node Manager. In the call to [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615), set the rclsid parameter to **CLSID\_NodeManager**, and the riid parameter to **IID\_IPropertySheetProvider**.
3.  In `InvokePropSheet`, call the [**IPropertySheetProvider::CreatePropertySheet**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-createpropertysheet) method to create a property sheet.
4.  In `InvokePropSheet`, call the [**IPropertySheetProvider::AddPrimaryPages**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-addprimarypages) method. The *lpUnknown* parameter in the method call specifies the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) of the snap-in's [**IExtendPropertySheet**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet) implementation that is responsible for adding the property pages.

    -   If the wizard sheet is for a scope item, set *bScopePane* to **TRUE**. Otherwise, set this parameter to **FALSE**.
    -   If the snap-in should receive notifications via the [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification when the user changes any wizard properties, set the *bCreateHandle* parameter to **TRUE**.
    -   If *bCreateHandle* is set to **TRUE**, the snap-in object that exposes [**IExtendPropertySheet**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet) to MMC must also expose either [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) (if *bScopePane* == **FALSE**) or [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) (if *bScopePane* == **TRUE**) and handle the [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification in its [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) (or [**IComponentData::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify)) implementation. The *lpUnknown* parameter should be a pointer to the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) of this object. Be aware that non-namespace extension snap-ins need only implement **IComponent::Notify** (or **IComponentData::Notify**). The implementations of all other **IComponent** (or **IComponentData**) methods can return **E\_NOTIMPL**.

    In MMC's [**AddPrimaryPages**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-addprimarypages) implementation, MMC calls back to the snap-in's [**IExtendPropertySheet2::CreatePropertyPages**](https://www.bing.com/search?q=**IExtendPropertySheet2::CreatePropertyPages**) method.

5.  In `InvokePropSheet`, call the [**IPropertySheetProvider::AddExtensionPages**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-addextensionpages) method to allow extensions to add their own property pages to the property sheet.
6.  In `InvokePropSheet`, call [**IPropertySheetProvider::Show**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-show) to display the wizard.
7.  Implement the [**IExtendPropertySheet2::CreatePropertyPages**](https://www.bing.com/search?q=**IExtendPropertySheet2::CreatePropertyPages**) method.

    In the implementation of [**CreatePropertyPages**](https://www.bing.com/search?q=**CreatePropertyPages**):

    -   If you set *bCreateHandle* to **TRUE** in the call to [**IPropertySheetProvider::AddPrimaryPages**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-addprimarypages) in Step 4., the handle parameter holds the handle value that the snap-in must specify in any future calls to [**MMCPropertyChangeNotify**](/windows/desktop/api/Mmc/nf-mmc-mmcpropertychangenotify). The snap-in should cache this value for future use.
    -   Define one or more wizard pages by filling the [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage) structure for each of the pages with information about the page. Be aware that the standard size for a property page in an MMC console is 252 dialog units horizontally and 218 dialog units vertically.
    -   For each [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage) structure, call the API function [**CreatePropertySheetPage**](https://www.bing.com/search?q=**CreatePropertySheetPage**) to create a page. The function returns a handle to the **HPROPSHEETPAGE** type that uniquely identifies the page.
    -   Using the pointer to the [**IPropertySheetCallback**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetcallback) interface passed to the snap-in in the call to the [**CreatePropertyPages**](https://www.bing.com/search?q=**CreatePropertyPages**) method, call the [**IPropertySheetCallback::AddPage**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetcallback-addpage) method to add each page to the wizard.

8.  Implement a dialog box procedure for each page. The **pfnDlgProc** member of each page's [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage) structure should be set to the address of this procedure.
9.  The snap-in should call the [**MMCPropertyChangeNotify**](/windows/desktop/api/Mmc/nf-mmc-mmcpropertychangenotify) function if the user has changed any properties. As a result of this method call, an [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification is sent to the appropriate [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) or [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) object. The snap-in should be prepared to handle this notification.

## Related topics

<dl> <dt>

[**IPropertySheetProvider**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetprovider)
</dt> <dt>

[Adding Wizard Pages](adding-wizard-pages.md)
</dt> <dt>

[Adding Property Pages](adding-property-pages.md)
</dt> </dl>

 

 




