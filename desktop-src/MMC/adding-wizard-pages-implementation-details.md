---
title: Adding Wizard Pages Implementation Details
description: The procedures in this topic describe how to create and add wizard pages to your snap-in. To add standard property pages, see Adding Property Pages Implementation Details.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d00e0e6d-3416-47c0-8d70-dcdacba220d0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- wizard pages MMC , implementation details
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Wizard Pages: Implementation Details

The procedures in this topic describe how to create and add wizard pages to your snap-in. To add standard property pages, see [Adding Property Pages: Implementation Details](adding-property-pages-implementation-details.md).

**To add Wizard pages**

1.  Implement a procedure, for example a function called InvokeWizardSheet, that is called when the user performs an action that causes the snap-in to invoke the wizard.
2.  In InvokeWizardSheet, call the [**IPropertySheetProvider::CreatePropertySheet**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-createpropertysheet) method to create a wizard. Ensure that the type parameter passed in the call is set to **FALSE** (for wizard).
3.  In InvokeWizardSheet, call the [**IPropertySheetProvider::AddPrimaryPages**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-addprimarypages) method. In the call to **AddPrimaryPages**:

    -   If the wizard sheet is for a scope item, set bScopePane to **TRUE**. Otherwise, set this parameter to **FALSE**.
    -   If the snap-in should receive notifications via the [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification when the user changes any wizard properties, set the bCreateHandle parameter to **TRUE**.
    -   If bCreateHandle is set to **TRUE**, the snap-in must implement either [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) (if bScopePane == **FALSE**) or [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) (if bScopePane == **TRUE**) and handle the [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification in its [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) (or [**IComponentData::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify)) implementation. The lpUnknown parameter should be a pointer to the **IComponent** (or **IComponentData**) object that receives the **MMCN\_PROPERTY\_CHANGE** notification.

    In the MMC [**AddPrimaryPages**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-addprimarypages) implementation, MMC calls back to the snap-in [**IExtendPropertySheet2::CreatePropertyPages**](https://www.bing.com/search?q=**IExtendPropertySheet2::CreatePropertyPages**) method.

4.  In InvokeWizardSheet, call [**IPropertySheetProvider::Show**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-show) to display the wizard.
5.  Implement the [**IExtendPropertySheet2::CreatePropertyPages**](https://www.bing.com/search?q=**IExtendPropertySheet2::CreatePropertyPages**) method in the appropriate [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) or [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation to add pages to the wizard.

    In the implementation of [**CreatePropertyPages**](https://www.bing.com/search?q=**CreatePropertyPages**):

    -   If you set bCreateA handle to **TRUE** in the call to [**IPropertySheetProvider::AddPrimaryPages**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-addprimarypages) in Step 3, the handle parameter holds the handle value that the snap-in requires to specify in any future calls to [**MMCPropertyChangeNotify**](/windows/desktop/api/Mmc/nf-mmc-mmcpropertychangenotify). The snap-in should cache this value for future use.
    -   Define one or more wizard pages by filling the [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage) structure for each of the pages with information about the page. Be aware that the standard size for a property page in an MMC console is 252 dialog units horizontally and 218 dialog units vertically.
    -   For each [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage) structure, call the API function [**CreatePropertySheetPage**](https://www.bing.com/search?q=**CreatePropertySheetPage**) to create a page. The function returns a handle to the HPROPSHEETPAGE type that uniquely identifies the page.
    -   Using the pointer to the [**IPropertySheetCallback**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetcallback) interface passed to the snap-in in the call to the [**CreatePropertyPages**](https://www.bing.com/search?q=**CreatePropertyPages**) method, call the [**IPropertySheetCallback::AddPage**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetcallback-addpage) method to add each page to the wizard.

6.  Implement a dialog box procedure for each page. The pfnDlgProc member of each page's [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage) structure should be set to the address of this procedure.
7.  The snap-in should call the [**MMCPropertyChangeNotify**](/windows/desktop/api/Mmc/nf-mmc-mmcpropertychangenotify) function if the user has changed any wizard properties. As a result of this method call, an [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification is sent to the appropriate [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) or [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) object. The snap-in should be prepared to handle this notification.

To add wizard pages with the Wizard 97 style, follow the previous procedure for adding wizard pages. In addition to the Steps in that procedure:

**To add wizard pages with the Wizard 97 style**

1.  In the call to the [**IPropertySheetProvider::CreatePropertySheet**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-createpropertysheet) method, set the dwOptions parameter to MMC\_PSO\_NEWWIZARDTYPE. This specifies the Wizard 97 style.
2.  Implement the [**IExtendPropertySheet2::GetWatermarks**](/windows/desktop/api/Mmc/nf-mmc-iextendpropertysheet2-getwatermarks) method to specify the watermark and header bitmaps for the wizard.
3.  By setting the pszHeaderTitle and pszHeaderSubTitle members of the [**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage) structure, you can specify the header title and subtitle text for interior Wizard 97 pages.

To add Wizard 97 style pages without watermarks and header bitmaps, follow the instructions in "To add wizard pages with the Wizard 97 style". In the snap-in's implementation of [**IExtendPropertySheet2::GetWatermarks**](/windows/desktop/api/Mmc/nf-mmc-iextendpropertysheet2-getwatermarks), return a success code (for example, S\_OK or S\_FALSE) without providing any bitmaps.

Be aware that if [**GetWatermarks**](/windows/desktop/api/Mmc/nf-mmc-iextendpropertysheet2-getwatermarks) is not implemented or returns a failure code, MMC reverts the wizard requested by the snap-in in the call to [**IPropertySheetProvider::CreatePropertySheet**](/windows/desktop/api/Mmc/nf-mmc-ipropertysheetprovider-createpropertysheet) to the non-Wizard 97 style. This is to maintain compatibility with MMC 1.1.

## Related topics

<dl> <dt>

[Adding Wizard Pages: Interfaces](adding-wizard-pages-interfaces.md)
</dt> <dt>

[Adding Watermarks to Wizard 97 Pages](adding-watermarks-to-wizard-97-pages.md)
</dt> <dt>

[Adding Wizard Pages](adding-wizard-pages.md)
</dt> </dl>

 

 




