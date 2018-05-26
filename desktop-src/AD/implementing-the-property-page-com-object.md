---
title: Implementing the Property Page COM Object
description: A property sheet extension is a COM object implemented as an in-proc server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 77a71086-1949-4828-801e-073ea5a6838b
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Implementing the Property Page COM Object
- Property Page COM Object, Implementing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing the Property Page COM Object

A property sheet extension is a COM object implemented as an in-proc server. The property sheet extension must implement the [**IShellExtInit**](_win32_ishellextinit_cpp) and [**IShellPropSheetExt**](_win32_ishellpropsheetext_cpp) interfaces. A property sheet extension is instantiated when the user displays the property sheet for an object of a class for which the property sheet extension has been registered in the display specifier of the class.

-   [Implementing IShellExtInit](#implementing-ishellextinit)
-   [Implementing IShellPropSheetExt](#implementing-ishellpropsheetext)
-   [Passing the Extension Object to the Property Page](#passing-the-extension-object-to-the-property-page)
-   [Working With the Notification Object](#working-with-the-notification-object)
-   [Miscellaneous](#miscellaneous)
-   [Multiple-Selection Property Sheets](#multiple-selection-property-sheets)
-   [New with Windows Server 2003](#new-with-windows-server-2003)
-   [Related topics](#related-topics)

## Implementing IShellExtInit

After the property sheet extension COM object is instantiated, the [**IShellExtInit::Initialize**](_win32_ishellextinit_win32_ishellextinit_initialize_cpp) method is called. **IShellExtInit::Initialize** supplies the property sheet extension with an [**IDataObject**](_ole_idataobject) object that contains data that pertains to the directory object that the property sheet applies.

The [**IDataObject**](_ole_idataobject) contains data in the [**CFSTR\_DSOBJECTNAMES**](https://msdn.microsoft.com/library/aa814586) format. The **CFSTR\_DSOBJECTNAMES** data format is an **HGLOBAL** that contains a [**DSOBJECTNAMES**](/windows/win32/Dsclient/ns-dsclient-dsobjectnames?branch=master) structure. The **DSOBJECTNAMES** structure contains directory object data that the property sheet extension applies.

The [**IDataObject**](_ole_idataobject) also contains data in the [**CFSTR\_DS\_DISPLAY\_SPEC\_OPTIONS**](cfstr-ds-display-spec-options.md) format. The **CFSTR\_DS\_DISPLAY\_SPEC\_OPTIONS** data format is an **HGLOBAL** that contains a [**DSDISPLAYSPECOPTIONS**](/windows/win32/Dsclient/ns-dsclient-_dsdisplayspecoptions?branch=master) structure. The **DSDISPLAYSPECOPTIONS** contains configuration data for use by the extension.

If any value other than **S\_OK** is returned from [**IShellExtInit::Initialize**](_win32_ishellextinit_win32_ishellextinit_initialize_cpp), the property sheet is not displayed.

The *pidlFolder* and *hkeyProgID* parameters of the [**IShellExtInit::Initialize**](_win32_ishellextinit_win32_ishellextinit_initialize_cpp) method are not used.

The [**IDataObject**](_ole_idataobject) pointer can be saved by the extension by incrementing the reference count of the **IDataObject**. This interface must be released when no longer required.

## Implementing IShellPropSheetExt

After [**IShellExtInit::Initialize**](_win32_ishellextinit_win32_ishellextinit_initialize_cpp) returns, the [**IShellPropSheetExt::AddPages**](_win32_ishellpropsheetext_win32_ishellpropsheetext_addpages_cpp) method is called. The property sheet extension must add the page or pages during this method. A property page is created by filling a [**PROPSHEETPAGE**](_win32_propsheetpage_str_cpp) structure and then passing this structure to the [**CreatePropertySheetPage**](_win32_createpropertysheetpage_cpp) function. The property page is then added to the property sheet by calling the callback function passed to **IShellPropSheetExt::AddPages** in the *lpfnAddPage* parameter.

If any value other than **S\_OK** is returned from [**IShellPropSheetExt::AddPages**](_win32_ishellpropsheetext_win32_ishellpropsheetext_addpages_cpp), the property sheet is not displayed.

If the property sheet extension is not required to add any pages to the property sheet, it should not call the callback function passed to [**IShellPropSheetExt::AddPages**](_win32_ishellpropsheetext_win32_ishellpropsheetext_addpages_cpp) in the *lpfnAddPage* parameter.

The [**IShellPropSheetExt::ReplacePage**](_win32_ishellpropsheetext_win32_ishellpropsheetext_replacepage_cpp) method is not used.

## Passing the Extension Object to the Property Page

The property sheet extension object is independent from the property page. In many cases, it is desirable to be able to use the extension object, or some other object, from the property page. To do this, set the **lParam** member of [**PROPSHEETPAGE**](_win32_propsheetpage_str_cpp) structure to the object pointer. The property page can then retrieve this value when it processes the [**WM\_INITDIALOG**](_win32_wm_initdialog_cpp) message. For a property page, the *lParam* parameter of the **WM\_INITDIALOG** message is a pointer to the **PROPSHEETPAGE** structure. Retrieve the object pointer by casting the *lParam* of the **WM\_INITDIALOG** message to a **PROPSHEETPAGE** pointer and then retrieving the **lParam** member of the **PROPSHEETPAGE** structure.

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



Be aware that after [**IShellPropSheetExt::AddPages**](_win32_ishellpropsheetext_win32_ishellpropsheetext_addpages_cpp) is called, the property sheet will release the property sheet extension object and never use it again. This means that the extension object would be deleted before the property page is displayed. When the page attempts to access the object pointer, the memory will have been freed and the pointer will not be valid. To correct this, increment the reference count for the extension object when the page is added and then release the object when the property page dialog is destroyed. This creates another issue because the property page dialog box is not created until the first time the page is displayed. If the user never selects the extension page, the page never gets created and destroyed. This results in the extension object never getting released, so a memory leak occurs. To avoid this, implement a property page callback function. To do this, add the **PSP\_USECALLBACK** flag to the **dwFlags** member of the [**PROPSHEETPAGE**](_win32_propsheetpage_str_cpp) structure and set the **pfnCallback** member of the **PROPSHEETPAGE** structure to the address of the [**PropSheetPageProc**](_win32_propsheetpageproc_cpp) function implemented. When the **PropSheetPageProc** function receives the **PSPCB\_RELEASE** notification, the *ppsp* parameter of the **PropSheetPageProc** contains a pointer to the **PROPSHEETPAGE** structure. The **lParam** member of the **PROPSHEETPAGE** structure contains the extension pointer which can be used to release the object.

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

When the property sheet extension object is initialized, the extension must create a notification object by calling [**ADsPropCreateNotifyObj**](/windows/win32/Adsprop/nf-adsprop-adspropcreatenotifyobj?branch=master), passing the [**IDataObject**](_ole_idataobject) obtained from [**IShellExtInit::Initialize**](_win32_ishellextinit_win32_ishellextinit_initialize_cpp) and the directory object name. It is not necessary to increment the reference count of the **IDataObject** interface, because the notification object created by **ADsPropCreateNotifyObj** function will do this. The notification object handle provided by **ADsPropCreateNotifyObj** should be saved for later use. **ADsPropCreateNotifyObj** can be either called during **IShellExtInit::Initialize** or [**IShellPropSheetExt::AddPages**](_win32_ishellpropsheetext_win32_ishellpropsheetext_addpages_cpp). When the property sheet extension is shut down, it must send a [**WM\_ADSPROP\_NOTIFY\_EXIT**](wm-adsprop-notify-exit.md) message to the notification object. This causes the notification object to destroy itself. This is best done when the [**PropSheetPageProc**](_win32_propsheetpageproc_cpp) function receives the **PSPCB\_RELEASE** notification.

The property sheet extension can obtain data in addition to that provided by the [**CFSTR\_DSOBJECTNAMES**](https://msdn.microsoft.com/library/aa814586) clipboard format by calling [**ADsPropGetInitInfo**](/windows/win32/Adsprop/nf-adsprop-adspropgetinitinfo?branch=master). One of the advantages of using **ADsPropGetInitInfo** is that it provides an [**IDirectoryObject**](https://msdn.microsoft.com/library/aa746355) object used to programmatically work with the directory object.

> [!Note]  
> Unlike most COM methods and functions, [**ADsPropGetInitInfo**](/windows/win32/Adsprop/nf-adsprop-adspropgetinitinfo?branch=master) does not increment the reference count for the [**IDirectoryObject**](https://msdn.microsoft.com/library/aa746355) object. The **IDirectoryObject** must not be released unless the reference count is manually incremented first.

 

When the property page is first created, the extension should register the page with the notification object by calling [**ADsPropSetHwnd**](/windows/win32/Adsprop/nf-adsprop-adspropsethwnd?branch=master) with the window handle of the page.

[**ADsPropCheckIfWritable**](/windows/win32/Adsprop/nf-adsprop-adspropcheckifwritable?branch=master) is a utility function that the property sheet extension can use to determine if a property can be written.

## Miscellaneous

The handle of the property page is passed to the page dialog box procedure. The property sheet is the direct parent of the property page, so the handle of the property sheet can be obtained by calling the [**GetParent**](_win32_getparent_cpp) function with the property page handle.

When the contents of the extension page changes, the extension should use the [**PropSheet\_Changed**](_win32_propsheet_changed_cpp) macro to notify the property sheet of changes. The property sheet will then enable the Apply button.

## Multiple-Selection Property Sheets

With Windows Server 2003 and later operating systems, the Active Directory administrative MMC snap-ins support property sheet extensions for multiple directory objects. These property sheets are displayed when the properties are viewed for more than one item at a time. The primary difference between a single-selection property sheet extension and a multiple-selection property sheet extension is that the [**DSOBJECTNAMES**](/windows/win32/Dsclient/ns-dsclient-dsobjectnames?branch=master) structure supplied by the [**CFSTR\_DSOBJECTNAMES**](https://msdn.microsoft.com/library/aa814586) clipboard format in [**IShellExtInit::Initialize**](_win32_ishellextinit_win32_ishellextinit_initialize_cpp) will contain more than one [**DSOBJECT**](/windows/win32/Dsclient/ns-dsclient-dsobject?branch=master) structure.

When the notification object is created, a multi-selection property sheet extension must pass a unique name that is provided by the snap-in rather than a name created by the extension. To obtain the unique name, request the [**CFSTR\_DS\_MULTISELECTPROPPAGE**](cfstr-ds-multiselectproppage.md) clipboard format from the [**IDataObject**](_ole_idataobject) obtained from [**IShellExtInit::Initialize**](_win32_ishellextinit_win32_ishellextinit_initialize_cpp). This data is an **HGLOBAL** that contains a null-terminated Unicode string that is the unique name. This unique name is then passed to the [**ADsPropCreateNotifyObj**](/windows/win32/Adsprop/nf-adsprop-adspropcreatenotifyobj?branch=master) function to create the notification object. The **CreateADsNotificationObject** example function in [Example Code for Implementation of the Property Sheet COM Object](example-code-for-implementation-of-the-property-sheet-com-object.md) demonstrates how to do this correctly, as well as being compatible with earlier versions of the snap-in that do not support multi-selection property sheets.

For multiple-selection property sheets, the system only binds to the first object in the [**DSOBJECT**](/windows/win32/Dsclient/ns-dsclient-dsobject?branch=master) array. Because of this, [**ADsPropGetInitInfo**](/windows/win32/Adsprop/nf-adsprop-adspropgetinitinfo?branch=master) only supplies the [**IDirectoryObject**](https://msdn.microsoft.com/library/aa746355) and write-able attributes for the first object in the array. The other objects in the array are not bound to.

A multiple-selection property sheet extension is registered under the [**adminMultiselectPropertyPages**](https://msdn.microsoft.com/library/ms675215) attribute.

## New with Windows Server 2003

The following features are new with Windows Server 2003.

If the property page encounters an error, [**ADsPropSendErrorMessage**](/windows/win32/Adsprop/nf-adsprop-adspropsenderrormessage?branch=master) can be called with the appropriate error data. **ADsPropSendErrorMessage** will store all error messages in a queue. These messages will be displayed the next time [**ADsPropShowErrorDialog**](/windows/win32/Adsprop/nf-adsprop-adspropshowerrordialog?branch=master) is called. When **ADsPropShowErrorDialog** returns, the queued messages are deleted.

Windows Server 2003 introduces the [**ADsPropSetHwndWithTitle**](/windows/win32/Adsprop/nf-adsprop-adspropsethwndwithtitle?branch=master) function. This function is similar to [**ADsPropSetHwnd**](/windows/win32/Adsprop/nf-adsprop-adspropsethwnd?branch=master), but includes the page title. This enables the error dialog box displayed by [**ADsPropShowErrorDialog**](/windows/win32/Adsprop/nf-adsprop-adspropshowerrordialog?branch=master) to provide more useful data to the user. If the property sheet extension uses the **ADsPropShowErrorDialog** function, the extension should use **ADsPropSetHwndWithTitle** rather than **ADsPropSetHwnd**.

## Related topics

<dl> <dt>

[Example Code for Implementation of the Property Sheet COM Object](example-code-for-implementation-of-the-property-sheet-com-object.md)
</dt> </dl>

 

 




