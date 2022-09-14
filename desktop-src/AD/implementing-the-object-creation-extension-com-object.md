---
title: Implementing the Object Creation Extension COM Object
description: An object creation extension is a COM object implemented as an in-proc server. Both primary and secondary object creation extensions must implement the IDsAdminNewObjExt interface.
ms.assetid: 0a8ed0ed-9dcb-4373-b549-7da3f3d9f641
ms.tgt_platform: multiple
keywords:
- Implementing the Object Creation Extension COM Object AD
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Object Creation Extension COM Object

An object creation extension is a COM object implemented as an in-proc server. Both primary and secondary object creation extensions must implement the [**IDsAdminNewObjExt**](/windows/desktop/api/DSAdmin/nn-dsadmin-idsadminnewobjext) interface.

## Implementing IDsAdminNewObjExt

When the object creation wizard is created, it initializes each object creation extension by calling the extension's [**IDsAdminNewObjExt::Initialize**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjext-initialize) method. The **Initialize** method supplies the extension with information about the container the object is being created in, the class name of the new object and information about the wizard itself. If the object creation wizard is started to create a new object from an existing object, the *pADsCopySource* parameter will not be **NULL**. In this case, the extension should attempt to obtain as much data from the object being copied as is feasible.

After the extension is initialized, the [**IDsAdminNewObjExt::AddPages**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjext-addpages) method is called. The extension must add the page or pages to the wizard during this method. A wizard page is created by filling in a [**PROPSHEETPAGE**](/windows/win32/api/prsht/ns-prsht-propsheetpagea_v2) structure and then passing this structure to the [**CreatePropertySheetPage**](/windows/win32/api/prsht/nf-prsht-createpropertysheetpagea) function. The page is then added to the wizard by calling the callback function that is passed to **AddPages** in the *lpfnAddPage* parameter.

Before the extension page is displayed, [**IDsAdminNewObjExt::SetObject**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjext-setobject) is called. This supplies the extension with an [**IADs**](/windows/desktop/api/iads/nn-iads-iads) interface pointer for the object being created.

While the wizard page is displayed, the page should handle and respond to any necessary wizard notification messages, such as [**PSN\_SETACTIVE**](../controls/psn-setactive.md) and [**PSN\_WIZNEXT**](../controls/psn-wiznext.md).

When the user completes all of the wizard pages, the wizard will display a "Finish" page that provides a summary of the data entered. The wizard obtains this data by calling the [**IDsAdminNewObjExt::GetSummaryInfo**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjext-getsummaryinfo) method for each of the extensions. The **GetSummaryInfo** method provides a **BSTR** that contains the text data displayed in the "Finish" page. An object creation extension does not have to supply summary data. In this case, **GetSummaryInfo** should return **E\_NOTIMPL**. **GetSummaryInfo** is only called one time for each extension, not per page, so if the object creation extension adds more than one page, the extension must combine the summary data into one string.

When the user clicks the **Finish** button in the "Finish" page, the wizard calls each of the extension's [**IDsAdminNewObjExt::WriteData**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjext-writedata) methods with the **DSA\_NEWOBJ\_CTX\_PRECOMMIT** context. When this occurs, the extension should write the gathered data into the appropriate properties using the [**IADs::Put**](/windows/desktop/api/iads/nf-iads-iads-put) or [**IADs::PutEx**](/windows/desktop/api/iads/nf-iads-iads-putex) method. The [**IADs**](/windows/desktop/api/iads/nn-iads-iads) interface is provided to the extension in the [**IDsAdminNewObjExt::SetObject**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjext-setobject) method. The extension should not commit the cached properties by calling [**IADs::SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo). When all of the properties have been written, the primary object creation extension commits the changes by calling **IADs::SetInfo**. This is discussed in more detail below.

If an error occurs, the extension will be notified of the error and during which operation it occurred when the [**IDsAdminNewObjExt::OnError**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjext-onerror) method is called.

## Implementing a Primary Object Creation Wizard

The implementation of a primary object creation wizard is identical to a secondary object creation wizard, except that a primary object creation wizard must perform a few more steps.

Prior to the first page being dismissed, the object creation wizard must create the temporary directory object. To do this, call the [**IDsAdminNewObjPrimarySite::CreateNew**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjprimarysite-createnew) method. A pointer to the [**IDsAdminNewObjPrimarySite**](/windows/desktop/api/DSAdmin/nn-dsadmin-idsadminnewobjprimarysite) interface is obtained by calling [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) with **IID\_IDsAdminNewObjPrimarySite** on the [**IDsAdminNewObj**](/windows/desktop/api/DSAdmin/nn-dsadmin-idsadminnewobj) interface that is passed to [**IDsAdminNewObjExt::Initialize**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjext-initialize). The **CreateNew** method creates a new temporary object and calls [**IDsAdminNewObjExt::SetObject**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjext-setobject) for each extension.

When an object creation wizard contains more than one page, the system implements a "Finish" page that displays a summary of the object information to be saved. When the **Finish** button on the "Finish" page is clicked, the system will call each of the object creation extension's [**IDsAdminNewObjExt::WriteData**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjext-writedata) method and then commit the temporary object to persistent memory. If, however, the object creation wizard only contains one page, the page will have **OK** and **Cancel** buttons instead of the **Back**, **Next** and **Cancel** buttons normally found in a wizard and no "Finish" page is provided. Because of this, a single-page object creation extension wizard must call [**IDsAdminNewObjPrimarySite::Commit**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjprimarysite-commit) to perform the write and save operations. A single-page primary object creation extension should call **Commit** in response to the [**PSN\_WIZFINISH**](../controls/psn-wizfinish.md) notification.

Because other object creation extensions can add pages to the wizard, the primary object creation extension may not know if there is more than one page in the wizard. This is not an issue for two reasons: First, if the system implements the "Finish" page, the primary object creation extension will receive the [**PSN\_WIZNEXT**](../controls/psn-wiznext.md) notification instead of the **PSN\_WIZNEXT** notification. Second, [**Commit**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnewobjprimarysite-commit) will fail harmlessly if the wizard contains more than one page.

 

 