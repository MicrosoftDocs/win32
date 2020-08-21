---
title: Active Directory Users and Computers Property Sheets
description: The Active Directory Users and Computers MMC snap-in is designed to display a property sheet for various objects in an Active Directory server.
ms.assetid: 38032d89-9549-475c-90aa-dac5cfe11084
ms.tgt_platform: multiple
keywords:
- Active Directory Users and Computers Property Sheets AD
ms.topic: article
ms.date: 05/31/2018
---

# Active Directory Users and Computers Property Sheets

The Active Directory Users and Computers MMC snap-in is designed to display a property sheet for various objects in an Active Directory server. The property sheet contains one or more pages that are used to view and modify object data. Different object types have different sets of pages displayed for them. The Active Directory Users and Computers MMC snap-in also enables third party vendors to add custom pages to the property sheet for a specific type of object. For more information, see [Property Pages for Use with Display Specifiers](property-pages-for-use-with-display-specifiers.md).

Some applications, other than the Active Directory Users and Computers MMC snap-in, must provide the user with the ability view and edit attributes for an object in an Active Directory server. The application could implement its own property sheets, but it is better to offer a consistent user interface to reduce confusion and learning time. Fortunately, the Active Directory Users and Computers MMC snap-in allows any OLE COM application to display a property sheet for an object that is identical to the property sheet that would be displayed by the Active Directory Users and Computers MMC snap-in for the same object.

For more information and a code example that hosts an Active Directory Users and Computers property sheet, see the PropSheetHost sample in the Platform Software Development Kit (SDK).

## Developer Audience

This documentation assumes that the reader is familiar with COM operation and component development using C++. Currently, it is not possible to create an Active Directory property sheet extension using Visual Basic.

## Hosting an Active Directory Users and Computers Property Sheet

**To display a property sheet for an object in an Active Directory server**

1.  Create a window that can be used to process messages. This can be an existing window or a special purpose window. This is known as the *hidden window*.
2.  Create an OLE COM object that is derived from [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject). This data object must support the following data formats:

    -   [**CFSTR\_DSOBJECTNAMES**](cfstr-dsobjectnames.md) This data format contains a [**DSOBJECTNAMES**](/windows/desktop/api/Dsclient/ns-dsclient-dsobjectnames) that identifies the object that the property sheet applies to. When hosting a property sheet, the more significant members of the **DSOBJECTNAMES** structure are shown in the following list.

        **clsidNamespace** Reserved. Set this to a GUID for your application here in case that it is used in the future.
        
        **aObjects** Contains an array of [**DSBOJECT**](/windows/desktop/api/Dsclient/ns-dsclient-dsobject) structures. Each **DSBOJECT** structure represents a single directory object. The **cItems** member contains the number of elements in the array. Only the first object in this array is used. Other objects are ignored.

    -   [**CFSTR\_DSDISPLAYSPECOPTIONS**](cfstr-ds-display-spec-options.md) This data format contains a [**DSDISPLAYSPECOPTIONS**](/windows/desktop/api/Dsclient/ns-dsclient-dsdisplayspecoptions) structure that contains data that will be used by the property pages, such as where to load the property pages from, the server and credentials to use, and so on. The more significant members of the **DSDISPLAYSPECOPTIONS** are shown in the following list.

        **offsetAttribPrefix** The attribute prefix string determines where the list of property pages is obtained. This must contain one of the following strings.

        

        | Attribute prefix string | Description                                              |
        |-------------------------|----------------------------------------------------------------------------------------------------------------------|
        | "admin"<br/>      | The property pages are loaded from the [**adminPropertyPages**](/windows/desktop/ADSchema/a-adminpropertypages) attribute.<br/> |
        | "shell"<br/>      | The property pages are loaded from the [**shellPropertyPages**](/windows/desktop/ADSchema/a-shellpropertypages) attribute.<br/> |

        


    -   [**CFSTR\_DS\_PROPSHEETCONFIG**](cfstr-ds-propsheetconfig.md) This data format contains a [**PROPSHEETCFG**](propsheetcfg.md) structure that contains property sheet host data. When hosting a property sheet, the more significant members of the **PROPSHEETCFG** structure contain the data shown in the following list.

        **lNotifyHandle** Must be zero.
        **hwndParentSheet**  Contains the handle of the window to receive [**WM\_ADSPROP\_NOTIFY\_CHANGE**](wm-adsprop-notify-change.md) messages when something in one of the pages changes and is applied. Can be **NULL** if this message is not desired.

        **hwndHidden** Contains the handle of the window to receive [**WM\_DSA\_SHEET\_CREATE\_NOTIFY**](wm-dsa-sheet-create-notify.md) and [**WM\_DSA\_SHEET\_CLOSE\_NOTIFY**](wm-dsa-sheet-close-notify.md) messages. Set this to the handle of your hidden window.

        **wParamSheetClose** Contains an application-defined identifier that is returned in the *wParam* in the [**WM\_DSA\_SHEET\_CLOSE\_NOTIFY**](wm-dsa-sheet-close-notify.md) message. If this member is zero, the **WM\_DSA\_SHEET\_CLOSE\_NOTIFY** message will not be posted to the hidden window.


3.  Create an instance of the [**CLSID\_DsPropertyPages**](guids-of-user-interface-elements.md) object and obtain the [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit) interface for the object. It is also possible to duplicate the behavior of the **CLSID\_DsPropertyPages** object. For more information, see Duplicating the Behavior of the CLSID\_DsPropertyPages Object.
4.  Initialize the [**CLSID\_DsPropertyPages**](guids-of-user-interface-elements.md) object by calling the [**IShellExtInit::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize) method. The *pidlFolder* and *hkeyProgID* parameters are not used in this method. The *pdtobj* parameter is the pointer to the data object created in Step 2. When the **IShellExtInit::Initialize** method is called, the **CLSID\_DsPropertyPages** object will save a reference to the data object.
5.  Obtain the [**IShellPropSheetExt**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellpropsheetext) interface for the [**CLSID\_DsPropertyPages**](guids-of-user-interface-elements.md) object and call the [**IShellPropSheetExt::AddPages**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-addpages) method. The *lpfnAddPage* parameter is the address of a callback function that you must implement. The format of this function is shown below. If the callback function is declared as a member of a C++ class, the callback function must be declared as **static**. The *lParam* parameter is an application-defined value that can be used to identify the object that implements the callback function. When the **IShellPropSheetExt::AddPages** method is called, the **CLSID\_DsPropertyPages** object will obtain the data from the data object and enumerate the property pages registered for the object display specifiers. The **CLSID\_DsPropertyPages** object will then enumerate the property page objects, calling each object's **IShellPropSheetExt::AddPages** method.

    ```C++
    BOOL CALLBACK AddPagesCallback(HPROPSHEETPAGE, LPARAM)
    ```

    

6.  Each page added by the property page objects will result in your callback function being called with the handle to the property page and the application-defined value. Your callback function must store each property page handle that is passed. When the [**CLSID\_DsPropertyPages**](guids-of-user-interface-elements.md) object's [**IShellPropSheetExt::AddPages**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-addpages) method returns, all pages will have been added via your callback function.
7.  Fill in a [**PROPSHEETHEADER**](/windows/win32/api/prsht/ns-prsht-propsheetheadera_v2) structure to display the property sheet. The **phpage** member receives a pointer to an array of page handles that were collected by your callback function. The **nPages** member receives the number of pages in the page handle array.
8.  Display the property sheet by calling the [**PropertySheet**](/windows/win32/api/prsht/nf-prsht-propertysheeta) function.

If the data in any page is changed and the **OK** or **Apply** buttons are clicked, the window identified by the **hwndParentSheet** member of the [**PROPSHEETCFG**](propsheetcfg.md) structure will receive a [**WM\_ADSPROP\_NOTIFY\_CHANGE**](wm-adsprop-notify-change.md) message. This message is strictly a notification and requires no specific action.

When the page is closed, the window identified by the **hwndHidden** member of the [**PROPSHEETCFG**](propsheetcfg.md) structure will receive a [**WM\_DSA\_SHEET\_CLOSE\_NOTIFY**](wm-dsa-sheet-close-notify.md) message. This message is strictly a notification and requires no specific action to be performed.

In some cases, the existing property sheets will need to display a secondary property sheet. For example, if you display the property sheet for a user object and select the **Member Of** page, a list of groups that the user is a member of will be displayed. If you double-click one of these groups in the list, the property sheet for that group will be displayed. The primary property sheet does not display the secondary sheet by itself. It requests that the host display the secondary sheet by sending a [**WM\_DSA\_SHEET\_CREATE\_NOTIFY**](wm-dsa-sheet-create-notify.md) message to the window identified by the **hwndHidden** member of the [**PROPSHEETCFG**](propsheetcfg.md) structure. The *wParam* of the **WM\_DSA\_SHEET\_CREATE\_NOTIFY** message is a pointer to a [**DSA\_SEC\_PAGE\_INFO**](dsa-sec-page-info.md) structure that contains information about the secondary property sheet and the object that it represents. In response to this message, the property sheet host must display the secondary property sheet in the same manner as shown above. After processing the **WM\_DSA\_SHEET\_CREATE\_NOTIFY** message, the message receiver must free the **DSA\_SEC\_PAGE\_INFO** structure by passing the *wParam* value to the [**LocalFree**](/windows/desktop/api/winbase/nf-winbase-localfree) function.

## Duplicating the Behavior of the CLSID\_DsPropertyPages Object

**To duplicate the behavior of the CLSID\_DsPropertyPages object**

1.  Enumerate the values in the [**adminPropertyPages**](/windows/desktop/ADSchema/a-adminpropertypages) or [**shellPropertyPages**](/windows/desktop/ADSchema/a-shellpropertypages) attribute for the display specifier for the object class. Each value is a string that contains a number, followed by a comma, followed by the string representation of the class identifier of the property page extension. For more information about the format of the property pages display specifier values, see [Registering the Property Page COM Object in a Display Specifier](registering-the-property-page-com-object-in-a-display-specifier.md).
2.  Convert each class identifier string into a **CLSID** using the [**CLSIDFromString**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) function.
3.  Sort the extension class identifiers by the number that precedes each class identifier string in the attribute value. If two numbers are identical, sort the class identifiers in the order that the attribute values are obtained from the Active Directory server.
4.  Enumerate the extension class identifiers, creating an instance of each extension.
5.  For each extension, in the order sorted above, call the extension's [**IShellExtInit::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize) with the same information described in Step 4 of the Hosting an Active Directory Users and Computers Property Sheet procedure.
6.  For each extension, in the order sorted above, call the extension's [**IShellPropSheetExt::AddPages**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-addpages) with the same information described in Step 5 of the Hosting an Active Directory Users and Computers Property Sheet procedure.

If possible, use the [**CLSID\_DsPropertyPages**](guids-of-user-interface-elements.md) object to create the pages rather than do this manually. The **CLSID\_DsPropertyPages** has been optimized and will correctly handle failure cases, such as when no display specifier is available for the current locale. Also, the **CLSID\_DsPropertyPages** object may change in the future, which means your property sheets may not exactly match those displayed by the Active Directory Users and Computers MMC snap-in.

## Special Programming Elements

Currently, the following programming elements are not defined in a published header file. To use these elements, you must define them yourself in the exact format shown in the particular reference page.

-   [**CFSTR\_DS\_PROPSHEETCONFIG**](cfstr-ds-propsheetconfig.md)
-   [**PROPSHEETCFG**](propsheetcfg.md)
-   [**WM\_DSA\_SHEET\_CLOSE\_NOTIFY**](wm-dsa-sheet-close-notify.md)
-   [**WM\_DSA\_SHEET\_CREATE\_NOTIFY**](wm-dsa-sheet-create-notify.md)
-   [**DSA\_SEC\_PAGE\_INFO**](dsa-sec-page-info.md)

## Example Code

The following C++ code example shows a safe way to define these elements that will continue to work even if these elements are defined in a published header file in the future.


```C++
#ifndef CFSTR_DS_PROPSHEETCONFIG
    #define CFSTR_DS_PROPSHEETCONFIG_W L"DsPropSheetCfgClipFormat"
    #define CFSTR_DS_PROPSHEETCONFIG_A "DsPropSheetCfgClipFormat"

    #ifdef UNICODE
        #define CFSTR_DS_PROPSHEETCONFIG CFSTR_DS_PROPSHEETCONFIG_W
    #else
        #define CFSTR_DS_PROPSHEETCONFIG CFSTR_DS_PROPSHEETCONFIG_A
    #endif //UNICODE
#endif //CFSTR_DS_PROPSHEETCONFIG


#ifndef WM_ADSPROP_SHEET_CREATE
    #define WM_ADSPROP_SHEET_CREATE (WM_USER + 1108)
#endif


#ifndef WM_DSA_SHEET_CREATE_NOTIFY
    #define WM_DSA_SHEET_CREATE_NOTIFY (WM_USER + 6)
#endif


#ifndef WM_DSA_SHEET_CLOSE_NOTIFY
    #define WM_DSA_SHEET_CLOSE_NOTIFY (WM_USER + 5) 
#endif


#ifndef DSA_SEC_PAGE_INFO
    typedef struct _DSA_SEC_PAGE_INFO
    {
        HWND    hwndParentSheet;
        DWORD   offsetTitle;
        DSOBJECTNAMES dsObjectNames;
    } DSA_SEC_PAGE_INFO, *PDSA_SEC_PAGE_INFO;
#endif //DSA_SEC_PAGE_INFO

#ifndef PROPSHEETCFG
    typedef struct _PROPSHEETCFG
    {  
        LONG_PTR lNotifyHandle;  
        HWND hwndParentSheet;  
        HWND hwndHidden;  
        WPARAM wParamSheetClose;
    } PROPSHEETCFG, *PPROPSHEETCFG;
#endif //PROPSHEETCFG
```



 

