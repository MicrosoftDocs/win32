---
title: Internet Shortcuts
description: The Internet shortcut object is used to create desktop shortcuts to Internet sites.
ms.assetid: 367c003f-2362-408c-81e1-fda1ffc7e15b
keywords:
- Internet shortcut objects
- WebBrowser controls
- IPropertySetStorage
ms.topic: article
ms.date: 05/31/2018
---

# Internet Shortcuts

The Internet shortcut object is used to create desktop shortcuts to Internet sites. Like shortcuts to items in the file system, Internet shortcuts take the form of an icon on the desktop. When the user clicks the icon, the browser is launched and displays the site associated with the shortcut.

The following topics are discussed.

-   [Creating Internet Shortcuts](#creating-internet-shortcuts)
    -   [Creating an Internet Shortcut from a WebBrowser Control](#creating-an-internet-shortcut-from-a-webbrowser-control)
    -   [Creating an Internet Shortcut from a URL](#creating-an-internet-shortcut-from-a-url)
-   [Accessing Property Storage](#accessing-property-storage)
-   [Interfaces](#interfaces)
    -   [OLE interfaces](#ole-interfaces)
    -   [Shell interfaces](#shell-interfaces)
-   [Functions](#functions)
    -   [Internet shortcut utility functions](#internet-shortcut-utility-functions)

## Creating Internet Shortcuts

You can create an Internet shortcut by using a WebBrowser control or with the URL of the page.

### Creating an Internet Shortcut from a WebBrowser Control

If your application hosts a WebBrowser control, you can use the Internet shortcut object to create shortcuts in the following way.

1.  Create an instance of the Internet shortcut object with [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance), using a class identifier (CLSID) of CLSID\_InternetShortcut.
2.  Pass the pointer to the WebBrowser's [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface to the Internet shortcut object with [IObjectWithSite::SetSite](/windows/win32/api/ocidl/nf-ocidl-iobjectwithsite-setsite).
3.  Call the Internet shortcut object's [IPersistFile::Save](/windows/win32/api/objidl/nf-objidl-ipersistfile-save) method when you want to create a shortcut to the page being viewed by the WebBrowser control.

A shortcut will be created in the location specified in [IPersistFile::Save](/windows/win32/api/objidl/nf-objidl-ipersistfile-save). This location enables the WebBrowser control to restore its state, which includes the task of loading of the correct documents into framesets.

### Creating an Internet Shortcut from a URL

You can also create an Internet shortcut if you have the URL of the page to which you want to link.

1.  Create an instance of the Internet shortcut object with [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance), using a CLSID of CLSID\_InternetShortcut.
2.  Use the [IUniformResourceLocator::SetURL](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/dd565676(v=vs.85)) method to set the URL in the shortcut.
3.  Use the [IPersistFile::Save](/windows/win32/api/objidl/nf-objidl-ipersistfile-save) method to save the shortcut file to a desired location.

## Accessing Property Storage

The Internet shortcut object contains several properties that you can access through the object's [IPropertySetStorage](/windows/win32/api/propidl/nn-propidl-ipropertysetstorage) interface with the following procedure.

1.  Get the [IPropertySetStorage](/windows/win32/api/propidl/nn-propidl-ipropertysetstorage) interface by calling [QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) with IID\_IPropertySetStorage.
2.  Access the Internet shortcut property storage set by calling [IPropertySetStorage::Open](/windows/win32/api/propidl/nf-propidl-ipropertysetstorage-open) with FMTID\_Intshcut or FMTID\_InternetSite to obtain the [IPropertyStorage](/windows/win32/api/propidlbase/nn-propidlbase-ipropertystorage) interface.
3.  Read the property storage information with [IPropertyStorage::ReadMultiple](/windows/win32/api/propidlbase/nf-propidlbase-ipropertystorage-readmultiple) by passing the appropriate property ID.

With [version 4.70 or higher](/previous-versions/windows/desktop/legacy/bb776779(v=vs.85)) of Shell32.dll, you can also retrieve the [IPropertySetStorage](/windows/win32/api/propidl/nn-propidl-ipropertysetstorage) interface by calling [**IShellFolder::BindToStorage**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtostorage) with the *pidl* parameter set to the .URL file and the *riid* parameter set to IID\_IPropertySetStorage.

The following property IDs can be requested for FMTID\_Intshcut.



| PROPID               | Variant Type | Description                                 |
|----------------------|--------------|---------------------------------------------|
| PID\_IS\_URL         | VT\_LPWSTR   | URL to which the shortcut leads             |
| PID\_IS\_NAME        | VT\_LPWSTR   | Name of the Internet shortcut               |
| PID\_IS\_WORKINGDIR  | VT\_LPWSTR   | Working directory for the shortcut          |
| PID\_IS\_HOTKEY      | VT\_UI2      | Hotkey for the shortcut                     |
| PID\_IS\_SHOWCMD     | VT\_I4       | Show command for shortcut                   |
| PID\_IS\_ICONINDEX   | VT\_I4       | Index of the icon                           |
| PID\_IS\_ICONFILE    | VT\_LPWSTR   | File that contains the icon                 |
| PID\_IS\_WHATSNEW    | VT\_LPWSTR   | What's New text                             |
| PID\_IS\_AUTHOR      | VT\_LPWSTR   | Author                                      |
| PID\_IS\_DESCRIPTION | VT\_LPWSTR   | Description text of site                    |
| PID\_IS\_COMMENT     | VT\_LPWSTR   | User annotated comment                      |
| PID\_IS\_ROAMED      | VT\_BOOL     | True when shortcut is roamed for first time |



 

The following property IDs can be requested for FMTID\_InternetSite.



| PROPID                     | Variant Type | Description                                       |
|----------------------------|--------------|---------------------------------------------------|
| PID\_INTSITE\_WHATSNEW     | VT\_LPWSTR   | What's New text                                   |
| PID\_INTSITE\_AUTHOR       | VT\_LPWSTR   | Author                                            |
| PID\_INTSITE\_LASTVISIT    | VT\_FILETIME | Time site was last visited                        |
| PID\_INTSITE\_LASTMOD      | VT\_FILETIME | Time site was last modified                       |
| PID\_INTSITE\_VISITCOUNT   | VT\_UI4      | Number of times user has visited                  |
| PID\_INTSITE\_DESCRIPTION  | VT\_LPWSTR   | Description text of site                          |
| PID\_INTSITE\_COMMENT      | VT\_LPWSTR   | User annotated comment                            |
| PID\_INTSITE\_FLAGS        | VT\_UI4      | Indicates use of PIDISF\_ flags (see below)       |
| PID\_INTSITE\_CONTENTLEN   | N/A          | Not currently supported                           |
| PID\_INTSITE\_CONTENTCODE  | N/A          | Not currently supported                           |
| PID\_INTSITE\_RECURSE      | N/A          | Not currently supported                           |
| PID\_INTSITE\_WATCH        | N/A          | Not currently supported                           |
| PID\_INTSITE\_SUBSCRIPTION | VT\_UI8      | SUBSCRIPTIONCOOKIE value for subscription manager |
| PID\_INTSITE\_URL          | VT\_LPWSTR   | URL to which the shortcut leads                   |
| PID\_INTSITE\_TITLE        | VT\_LPWSTR   | Title                                             |
| PID\_INTSITE\_CODEPAGE     | VT\_UI4      | Codepage of the document                          |
| PID\_INTSITE\_TRACKING     | N/A          | Not currently supported                           |
| PID\_INTSITE\_ICONINDEX    | VT\_I4       | Index of the icon                                 |
| PID\_INTSITE\_ICONFILE     | VT\_LPWSTR   | File that contains the icon                       |
| PID\_INTSITE\_ROAMED       | VT\_UI4      | The entry was added due to roaming                |



 

The following are the Internet site flags.



| Flag                    | Description                                |
|-------------------------|--------------------------------------------|
| PIDISF\_RECENTLYCHANGED | Indicates that a site was recently changed |
| PIDISF\_CACHEDSTICKY    | Not currently supported                    |
| PIDISF\_CACHEIMAGES     | Not currently supported                    |
| PIDISF\_FOLLOWALLLINKS  | Not currently supported                    |



 

The following values are used for Internet roaming history.



| Value of PID\_INTSITE\_ROAMED         | Description                                                                                                                                                              |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Value not set or PIDISR\_UP\_TO\_DATE | This cache entry has not been modified by roaming.                                                                                                                       |
| PIDISR\_NEEDS\_ADD                    | This cache entry was added to the cache by roaming. Set PIDISR\_UP\_TO\_DATE once processing of the entry is complete.                                                   |
| PIDISR\_NEEDS\_UPDATE                 | This cache entry already existed on the local machine, but it was updated by roaming. Set PIDISR\_UP\_TO\_DATE once processing of the entry is complete.                 |
| PIDISR\_NEEDS\_DELETE                 | Roaming detected that this cache entry should be deleted. For example, the user may have cleared his or her browser history. Delete the entry using DeleteUrlCacheEntry. |



 

## Interfaces

The Internet shortcut object exposes a number of interfaces.

### OLE interfaces

-   [IDataObject](/windows/win32/api/objidl/nn-objidl-idataobject)
-   [IPersistFile](/windows/win32/api/objidl/nn-objidl-ipersistfile)
-   [IPersistStream](/windows/win32/api/objidl/nn-objidl-ipersiststream)
-   [IOleCommandTarget](/windows/win32/api/docobj/nn-docobj-iolecommandtarget)
-   [IPropertySetStorage](/windows/win32/api/propidl/nn-propidl-ipropertysetstorage)
-   [IObjectWithSite](/windows/win32/api/ocidl/nn-ocidl-iobjectwithsite)

### Shell interfaces

-   [**IContextMenu2**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icontextmenu2)
-   [**IExtractIcon**](/windows/desktop/api/shlobj_core/nn-shlobj_core-iextracticona)
-   [**INewShortcutHook**](/windows/desktop/api/shlobj/nn-shlobj-inewshortcuthooka)
-   [**IShellExtInit**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellextinit)
-   [**IShellLink**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllinka)
-   [**IShellPropSheetExt**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellpropsheetext)
-   [**IQueryInfo**](/windows/desktop/api/shlobj_core/nn-shlobj_core-iqueryinfo)

## Functions

There are several utility functions that can be used with the Internet shortcut object.

### Internet shortcut utility functions

-   [**InetIsOffline**](/windows/desktop/api/intshcut/nf-intshcut-inetisoffline)
-   [**MIMEAssociationDialog**](/windows/desktop/api/intshcut/nf-intshcut-mimeassociationdialoga)
-   [**TranslateURL**](/windows/desktop/api/intshcut/nf-intshcut-translateurla)
-   [**URLAssociationDialog**](/windows/desktop/api/intshcut/nf-intshcut-urlassociationdialoga)

 

 