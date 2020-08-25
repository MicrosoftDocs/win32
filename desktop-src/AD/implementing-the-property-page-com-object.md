---
title: Implementing the Property Page COM Object
description: A property sheet extension is a COM object implemented as an in-proc server.
ms.assetid: 77a71086-1949-4828-801e-073ea5a6838b
ms.tgt_platform: multiple
keywords:
- Implementing the Property Page COM Object
- Property Page COM Object, Implementing
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Property Page COM Object

A property sheet extension is a COM object implemented as an in-proc server. The property sheet extension must implement the [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit) and [**IShellPropSheetExt**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellpropsheetext) interfaces. A property sheet extension is instantiated when the user displays the property sheet for an object of a class for which the property sheet extension has been registered in the display specifier of the class.

-   [Implementing IShellExtInit](#implementing-ishellextinit)
-   [Implementing IShellPropSheetExt](#implementing-ishellpropsheetext)
-   [Passing the Extension Object to the Property Page](#passing-the-extension-object-to-the-property-page)
-   [Working With the Notification Object](#working-with-the-notification-object)
-   [Miscellaneous](#miscellaneous)
-   [Multiple-Selection Property Sheets](#multiple-selection-property-sheets)
-   [New with Windows Server 2003](#new-with-windows-server-2003)
-   [Related topics](#related-topics)

## Implementing IShellExtInit

After the property sheet extension COM object is instantiated, the [**IShellExtInit::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize) method is called. **IShellExtInit::Initialize** supplies the property sheet extension with an [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) object that contains data that pertains to the directory object that the property sheet applies.

The [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) contains data in the [**CFSTR\_DSOBJECTNAMES**](/previous-versions/windows/desktop/mmc/cfstr-dsobjectnames-clipboard-format) format. The **CFSTR\_DSOBJECTNAMES** data format is an **HGLOBAL** that contains a [**DSOBJECTNAMES**](/windows/desktop/api/Dsclient/ns-dsclient-dsobjectnames) structure. The **DSOBJECTNAMES** structure contains directory object data that the property sheet extension applies.

The [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) also contains data in the [**CFSTR\_DS\_DISPLAY\_SPEC\_OPTIONS**](cfstr-ds-display-spec-options.md) format. The **CFSTR\_DS\_DISPLAY\_SPEC\_OPTIONS** data format is an **HGLOBAL** that contains a [**DSDISPLAYSPECOPTIONS**](/windows/desktop/api/Dsclient/ns-dsclient-dsdisplayspecoptions) structure. The **DSDISPLAYSPECOPTIONS** contains configuration data for use by the extension.

If any value other than **S\_OK** is returned from [**IShellExtInit::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize), the property sheet is not displayed.

The *pidlFolder* and *hkeyProgID* parameters of the [**IShellExtInit::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize) method are not used.

The [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) pointer can be saved by the extension by incrementing the reference count of the **IDataObject**. This interface must be released when no longer required.

## Implementing IShellPropSheetExt

After [**IShellExtInit::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize) returns, the [**IShellPropSheetExt::AddPages**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-addpages) method is called. The property sheet extension must add the page or pages during this method. A property page is created by filling a [**PROPSHEETPAGE**](/windows/win32/api/prsht/ns-prsht-propsheetpagea_v2) structure and then passing this structure to the [**CreatePropertySheetPage**](/windows/win32/api/prsht/nf-prsht-createpropertysheetpagea) function. The property page is then added to the property sheet by calling the callback function passed to **IShellPropSheetExt::AddPages** in the *lpfnAddPage* parameter.

If any value other than **S\_OK** is returned from [**IShellPropSheetExt::AddPages**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-addpages), the property sheet is not displayed.

If the property sheet extension is not required to add any pages to the property sheet, it should not call the callback function passed to [**IShellPropSheetExt::AddPages**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-addpages) in the *lpfnAddPage* parameter.

The [**IShellPropSheetExt::ReplacePage**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-replacepage) method is not used.

## Passing the Extension Object to the Property Page

The property sheet extension object is independent from the property page. In many cases, it is desirable to be able to use the extension object, or some other object, from the property page. To do this, set the **lParam** member of [**PROPSHEETPAGE**](/windows/win32/api/prsht/ns-prsht-propsheetpagea_v2) structure to the object pointer. The property page can then retrieve this value when it processes the [**WM\_INITDIALOG**](../dlgbox/wm-initdialog.md) message. For a property page, the *lParam* parameter of the **WM\_INITDIALOG** message is a pointer to the **PROPSHEETPAGE** structure. Retrieve the object pointer by casting the *lParam* of the **WM\_INITDIALOG** message to a **PROPSHEETPAGE** pointer and then retrieving the **lParam** member of the **PROPSHEETPAGE** structure.

The following C++ code example shows how to pass an object to a property page.


```C++
case WM_INITDIALOG:
    {
        LPPROPSHEETPAGE pPage = (LPPROPSHEETPAGE)lParam;

        if(NULL != pPage)
        {
            CPropSheetExt *pPropSheetExt;
            pPropSheetExt = (CPropSheetExt*)pPage->lParam;

            if(pPropSheetExt)
            {
                return pPropSheetExt>OnInitDialog(wParam, lParam);
            }
        }
    }
    break;
```



Be aware that after [**IShellPropSheetExt::AddPages**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-addpages) is called, the property sheet will release the property sheet extension object and never use it again. This means that the extension object would be deleted before the property page is displayed. When the page attempts to access the object pointer, the memory will have been freed and the pointer will not be valid. To correct this, increment the reference count for the extension object when the page is added and then release the object when the property page dialog is destroyed. This creates another issue because the property page dialog box is not created until the first time the page is displayed. If the user never selects the extension page, the page never gets created and destroyed. This results in the extension object never getting released, so a memory leak occurs. To avoid this, implement a property page callback function. To do this, add the **PSP\_USECALLBACK** flag to the **dwFlags** member of the [**PROPSHEETPAGE**](/windows/win32/api/prsht/ns-prsht-propsheetpagea_v2) structure and set the **pfnCallback** member of the **PROPSHEETPAGE** structure to the address of the [**PropSheetPageProc**](/windows/win32/api/prsht/nc-prsht-lpfnpspcallbacka) function implemented. When the **PropSheetPageProc** function receives the **PSPCB\_RELEASE** notification, the *ppsp* parameter of the **PropSheetPageProc** contains a pointer to the **PROPSHEETPAGE** structure. The **lParam** member of the **PROPSHEETPAGE** structure contains the extension pointer which can be used to release the object.

The following C++ code example shows how to release an extension object.


```C++
UINT CALLBACK CPropSheetExt::PageCallbackProc(  HWND hWnd,
                                                UINT uMsg,
                                                LPPROPSHEETPAGE ppsp)
{
    switch(uMsg)
    {
    case PSPCB_CREATE:
        // Must return TRUE to enable the page to be created.
        return TRUE;

    case PSPCB_RELEASE:
        {
            /*
            Release the object. This is called even if the page dialog box was 
            never actually created.
            */
            CPropSheetExt *pPropSheetExt = (CPropSheetExt*)ppsp->lParam;

            if(pPropSheetExt)
            {
                pPropSheetExt->Release();
            }
        }
        break;
    }

    return FALSE;
}
```



## Working With the Notification Object

Because the property sheet extension pages are displayed within a property sheet created by a component unknown to the extension, it is necessary to use a "manager" to handle the data transfer between the extension pages and the property sheet. This "manager" is called the notification object. The notification object operates as a moderator between the individual pages and the property sheet.

When the property sheet extension object is initialized, the extension must create a notification object by calling [**ADsPropCreateNotifyObj**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcreatenotifyobj), passing the [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) obtained from [**IShellExtInit::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize) and the directory object name. It is not necessary to increment the reference count of the **IDataObject** interface, because the notification object created by **ADsPropCreateNotifyObj** function will do this. The notification object handle provided by **ADsPropCreateNotifyObj** should be saved for later use. **ADsPropCreateNotifyObj** can be either called during **IShellExtInit::Initialize** or [**IShellPropSheetExt::AddPages**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-addpages). When the property sheet extension is shut down, it must send a [**WM\_ADSPROP\_NOTIFY\_EXIT**](wm-adsprop-notify-exit.md) message to the notification object. This causes the notification object to destroy itself. This is best done when the [**PropSheetPageProc**](/windows/win32/api/prsht/nc-prsht-lpfnpspcallbacka) function receives the **PSPCB\_RELEASE** notification.

The property sheet extension can obtain data in addition to that provided by the [**CFSTR\_DSOBJECTNAMES**](/previous-versions/windows/desktop/mmc/cfstr-dsobjectnames-clipboard-format) clipboard format by calling [**ADsPropGetInitInfo**](/windows/desktop/api/Adsprop/nf-adsprop-adspropgetinitinfo). One of the advantages of using **ADsPropGetInitInfo** is that it provides an [**IDirectoryObject**](/windows/desktop/api/iads/nn-iads-idirectoryobject) object used to programmatically work with the directory object.

> [!Note]  
> Unlike most COM methods and functions, [**ADsPropGetInitInfo**](/windows/desktop/api/Adsprop/nf-adsprop-adspropgetinitinfo) does not increment the reference count for the [**IDirectoryObject**](/windows/desktop/api/iads/nn-iads-idirectoryobject) object. The **IDirectoryObject** must not be released unless the reference count is manually incremented first.

 

When the property page is first created, the extension should register the page with the notification object by calling [**ADsPropSetHwnd**](/windows/desktop/api/Adsprop/nf-adsprop-adspropsethwnd) with the window handle of the page.

[**ADsPropCheckIfWritable**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcheckifwritable) is a utility function that the property sheet extension can use to determine if a property can be written.

## Miscellaneous

The handle of the property page is passed to the page dialog box procedure. The property sheet is the direct parent of the property page, so the handle of the property sheet can be obtained by calling the [**GetParent**](/windows/win32/api/winuser/nf-winuser-getparent) function with the property page handle.

When the contents of the extension page changes, the extension should use the [**PropSheet\_Changed**](/windows/win32/api/prsht/nf-prsht-propsheet_changed) macro to notify the property sheet of changes. The property sheet will then enable the Apply button.

## Multiple-Selection Property Sheets

With Windows Server 2003 and later operating systems, the Active Directory administrative MMC snap-ins support property sheet extensions for multiple directory objects. These property sheets are displayed when the properties are viewed for more than one item at a time. The primary difference between a single-selection property sheet extension and a multiple-selection property sheet extension is that the [**DSOBJECTNAMES**](/windows/desktop/api/Dsclient/ns-dsclient-dsobjectnames) structure supplied by the [**CFSTR\_DSOBJECTNAMES**](/previous-versions/windows/desktop/mmc/cfstr-dsobjectnames-clipboard-format) clipboard format in [**IShellExtInit::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize) will contain more than one [**DSOBJECT**](/windows/desktop/api/Dsclient/ns-dsclient-dsobject) structure.

When the notification object is created, a multi-selection property sheet extension must pass a unique name that is provided by the snap-in rather than a name created by the extension. To obtain the unique name, request the [**CFSTR\_DS\_MULTISELECTPROPPAGE**](cfstr-ds-multiselectproppage.md) clipboard format from the [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) obtained from [**IShellExtInit::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize). This data is an **HGLOBAL** that contains a null-terminated Unicode string that is the unique name. This unique name is then passed to the [**ADsPropCreateNotifyObj**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcreatenotifyobj) function to create the notification object. The **CreateADsNotificationObject** example function in [Example Code for Implementation of the Property Sheet COM Object](example-code-for-implementation-of-the-property-sheet-com-object.md) demonstrates how to do this correctly, as well as being compatible with earlier versions of the snap-in that do not support multi-selection property sheets.

For multiple-selection property sheets, the system only binds to the first object in the [**DSOBJECT**](/windows/desktop/api/Dsclient/ns-dsclient-dsobject) array. Because of this, [**ADsPropGetInitInfo**](/windows/desktop/api/Adsprop/nf-adsprop-adspropgetinitinfo) only supplies the [**IDirectoryObject**](/windows/desktop/api/iads/nn-iads-idirectoryobject) and write-able attributes for the first object in the array. The other objects in the array are not bound to.

A multiple-selection property sheet extension is registered under the [**adminMultiselectPropertyPages**](/windows/desktop/ADSchema/a-adminmultiselectpropertypages) attribute.

## New with Windows Server 2003

The following features are new with Windows Server 2003.

If the property page encounters an error, [**ADsPropSendErrorMessage**](/windows/desktop/api/Adsprop/nf-adsprop-adspropsenderrormessage) can be called with the appropriate error data. **ADsPropSendErrorMessage** will store all error messages in a queue. These messages will be displayed the next time [**ADsPropShowErrorDialog**](/windows/desktop/api/Adsprop/nf-adsprop-adspropshowerrordialog) is called. When **ADsPropShowErrorDialog** returns, the queued messages are deleted.

Windows Server 2003 introduces the [**ADsPropSetHwndWithTitle**](/windows/desktop/api/Adsprop/nf-adsprop-adspropsethwndwithtitle) function. This function is similar to [**ADsPropSetHwnd**](/windows/desktop/api/Adsprop/nf-adsprop-adspropsethwnd), but includes the page title. This enables the error dialog box displayed by [**ADsPropShowErrorDialog**](/windows/desktop/api/Adsprop/nf-adsprop-adspropshowerrordialog) to provide more useful data to the user. If the property sheet extension uses the **ADsPropShowErrorDialog** function, the extension should use **ADsPropSetHwndWithTitle** rather than **ADsPropSetHwnd**.

## Related topics

<dl> <dt>

[Example Code for Implementation of the Property Sheet COM Object](example-code-for-implementation-of-the-property-sheet-com-object.md)
</dt> </dl>

 

 