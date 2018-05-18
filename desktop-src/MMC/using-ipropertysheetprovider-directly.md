---
title: Using IPropertySheetProvider Directly
description: Allows snap-ins to display property sheets and wizards.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5371b7ab-a298-44d1-99f1-1cd8f188cb91'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Using IPropertySheetProvider Directly

The [**IPropertySheetProvider**](ipropertysheetprovider.md) interface allows snap-ins to display property sheets and wizards. Usually, snap-ins need not directly use **IPropertySheetProvider** to display a property sheet. Instead, snap-ins use the [**IPropertySheetCallback**](ipropertysheetcallback.md) interface, which MMC supplies to them so that they can add their own property pages to the property sheet for a particular scope or result item.

The situations in which snap-ins must directly use the [**IPropertySheetProvider**](ipropertysheetprovider.md) interface include:

-   Snap-ins that display wizards must directly use the [**IPropertySheetProvider**](ipropertysheetprovider.md) interface to specify wizard sheets. For more information, see [Adding Wizard Pages: Implementation Details](adding-wizard-pages-implementation-details.md).
-   Snap-ins that display property sheets in response to user actions other than the activation of the properties verb must directly use the [**IPropertySheetProvider**](ipropertysheetprovider.md) interface.

For more information about that displays property sheets in response to the user activating the properties verb, see [Adding Property Pages: Implementation Details](adding-property-pages-implementation-details.md). The rest of this section discusses how to use [**IPropertySheetProvider**](ipropertysheetprovider.md) to display a property sheet independent of the properties verb.

Be aware that, regardless of whether or not a snap-in directly uses MMC's [**IPropertySheetProvider**](ipropertysheetprovider.md) implementation, the **IPropertySheetProvider** methods call into the snap-in's [**IExtendPropertySheet**](iextendpropertysheet.md) implementation and supply an [**IPropertySheetCallback**](ipropertysheetcallback.md) interface pointer so that the snap-in can add pages.

**To use IPropertySheetProvider to display a property sheet**

1.  Implement a procedure, say a function called `InvokePropSheet`, that is called when the user performs an action that causes the snap-in to invoke the wizard.
2.  Obtain an [**IPropertySheetProvider**](ipropertysheetprovider.md) interface pointer by creating an instance of the MMC Node Manager. In the call to [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615), set the rclsid parameter to **CLSID\_NodeManager**, and the riid parameter to **IID\_IPropertySheetProvider**.
3.  In `InvokePropSheet`, call the [**IPropertySheetProvider::CreatePropertySheet**](ipropertysheetprovider-createpropertysheet.md) method to create a property sheet.
4.  In `InvokePropSheet`, call the [**IPropertySheetProvider::AddPrimaryPages**](ipropertysheetprovider-addprimarypages.md) method. The *lpUnknown* parameter in the method call specifies the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) of the snap-in's [**IExtendPropertySheet**](iextendpropertysheet.md) implementation that is responsible for adding the property pages.

    -   If the wizard sheet is for a scope item, set *bScopePane* to **TRUE**. Otherwise, set this parameter to **FALSE**.
    -   If the snap-in should receive notifications via the [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification when the user changes any wizard properties, set the *bCreateHandle* parameter to **TRUE**.
    -   If *bCreateHandle* is set to **TRUE**, the snap-in object that exposes [**IExtendPropertySheet**](iextendpropertysheet.md) to MMC must also expose either [**IComponent**](icomponent.md) (if *bScopePane* == **FALSE**) or [**IComponentData**](icomponentdata.md) (if *bScopePane* == **TRUE**) and handle the [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification in its [**IComponent::Notify**](icomponent-notify.md) (or [**IComponentData::Notify**](icomponentdata-notify.md)) implementation. The *lpUnknown* parameter should be a pointer to the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) of this object. Be aware that non-namespace extension snap-ins need only implement **IComponent::Notify** (or **IComponentData::Notify**). The implementations of all other **IComponent** (or **IComponentData**) methods can return **E\_NOTIMPL**.

    In MMC's [**AddPrimaryPages**](ipropertysheetprovider-addprimarypages.md) implementation, MMC calls back to the snap-in's [**IExtendPropertySheet2::CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method.

5.  In `InvokePropSheet`, call the [**IPropertySheetProvider::AddExtensionPages**](ipropertysheetprovider-addextensionpages.md) method to allow extensions to add their own property pages to the property sheet.
6.  In `InvokePropSheet`, call [**IPropertySheetProvider::Show**](ipropertysheetprovider-show.md) to display the wizard.
7.  Implement the [**IExtendPropertySheet2::CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method.

    In the implementation of [**CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md):

    -   If you set *bCreateHandle* to **TRUE** in the call to [**IPropertySheetProvider::AddPrimaryPages**](ipropertysheetprovider-addprimarypages.md) in Step 4., the handle parameter holds the handle value that the snap-in must specify in any future calls to [**MMCPropertyChangeNotify**](mmcpropertychangenotify.md). The snap-in should cache this value for future use.
    -   Define one or more wizard pages by filling the [**PROPSHEETPAGE**](propsheetpage.md) structure for each of the pages with information about the page. Be aware that the standard size for a property page in an MMC console is 252 dialog units horizontally and 218 dialog units vertically.
    -   For each [**PROPSHEETPAGE**](propsheetpage.md) structure, call the API function [**CreatePropertySheetPage**](_win32_createpropertysheetpage_cpp) to create a page. The function returns a handle to the **HPROPSHEETPAGE** type that uniquely identifies the page.
    -   Using the pointer to the [**IPropertySheetCallback**](ipropertysheetcallback.md) interface passed to the snap-in in the call to the [**CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method, call the [**IPropertySheetCallback::AddPage**](ipropertysheetcallback-addpage.md) method to add each page to the wizard.

8.  Implement a dialog box procedure for each page. The **pfnDlgProc** member of each page's [**PROPSHEETPAGE**](propsheetpage.md) structure should be set to the address of this procedure.
9.  The snap-in should call the [**MMCPropertyChangeNotify**](mmcpropertychangenotify.md) function if the user has changed any properties. As a result of this method call, an [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification is sent to the appropriate [**IComponent**](icomponent.md) or [**IComponentData**](icomponentdata.md) object. The snap-in should be prepared to handle this notification.

## Related topics

<dl> <dt>

[**IPropertySheetProvider**](ipropertysheetprovider.md)
</dt> <dt>

[Adding Wizard Pages](adding-wizard-pages.md)
</dt> <dt>

[Adding Property Pages](adding-property-pages.md)
</dt> </dl>

 

 




