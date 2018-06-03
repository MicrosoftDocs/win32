---
title: Internet Shortcuts
description: The Internet shortcut object is used to create desktop shortcuts to Internet sites.
ms.assetid: 367c003f-2362-408c-81e1-fda1ffc7e15b
keywords:
- Internet shortcut objects
- WebBrowser controls
- IPropertySetStorage
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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

1.  Create an instance of the Internet shortcut object with [CoCreateInstance](http://msdn.microsoft.com/library/ms686615(VS.85).aspx), using a class identifier (CLSID) of CLSID\_InternetShortcut.
2.  Pass the pointer to the WebBrowser's [IUnknown](http://msdn.microsoft.com/library/ms680509(VS.85).aspx) interface to the Internet shortcut object with [IObjectWithSite::SetSite](http://msdn.microsoft.com/library/ms683869(VS.85).aspx).
3.  Call the Internet shortcut object's [IPersistFile::Save](http://msdn.microsoft.com/library/ms693701(VS.85).aspx) method when you want to create a shortcut to the page being viewed by the WebBrowser control.

A shortcut will be created in the location specified in [IPersistFile::Save](http://msdn.microsoft.com/library/ms693701(VS.85).aspx). This location enables the WebBrowser control to restore its state, which includes the task of loading of the correct documents into framesets.

### Creating an Internet Shortcut from a URL

You can also create an Internet shortcut if you have the URL of the page to which you want to link.

1.  Create an instance of the Internet shortcut object with [CoCreateInstance](http://msdn.microsoft.com/library/ms686615(VS.85).aspx), using a CLSID of CLSID\_InternetShortcut.
2.  Use the [IUniformResourceLocator::SetURL](http://msdn.microsoft.com/library/dd565676(VS.85).aspx) method to set the URL in the shortcut.
3.  Use the [IPersistFile::Save](http://msdn.microsoft.com/library/ms693701(VS.85).aspx) method to save the shortcut file to a desired location.

## Accessing Property Storage

The Internet shortcut object contains several properties that you can access through the object's [IPropertySetStorage](http://msdn.microsoft.com/library/Aa379840(VS.85).aspx) interface with the following procedure.

1.  Get the [IPropertySetStorage](http://msdn.microsoft.com/library/Aa379840(VS.85).aspx) interface by calling [QueryInterface](http://msdn.microsoft.com/library/ms682521(VS.85).aspx) with IID\_IPropertySetStorage.
2.  Access the Internet shortcut property storage set by calling [IPropertySetStorage::Open](http://msdn.microsoft.com/library/Aa379965(VS.85).aspx) with FMTID\_Intshcut or FMTID\_InternetSite to obtain the [IPropertyStorage](http://msdn.microsoft.com/library/Aa379968(VS.85).aspx) interface.
3.  Read the property storage information with [IPropertyStorage::ReadMultiple](http://msdn.microsoft.com/library/Aa379975(VS.85).aspx) by passing the appropriate property ID.

With [version 4.70 or higher](https://msdn.microsoft.com/library/windows/desktop/bb776779) of Shell32.dll, you can also retrieve the [IPropertySetStorage](http://msdn.microsoft.com/library/Aa379840(VS.85).aspx) interface by calling [**IShellFolder::BindToStorage**](https://msdn.microsoft.com/library/windows/desktop/bb775061) with the *pidl* parameter set to the .URL file and the *riid* parameter set to IID\_IPropertySetStorage.

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

-   [IDataObject](http://msdn.microsoft.com/library/ms688421(VS.85).aspx)
-   [IPersistFile](http://msdn.microsoft.com/library/ms687223(VS.85).aspx)
-   [IPersistStream](http://msdn.microsoft.com/library/ms690091(VS.85).aspx)
-   [IOleCommandTarget](http://msdn.microsoft.com/library/ms683797(VS.85).aspx)
-   [IPropertySetStorage](http://msdn.microsoft.com/library/Aa379840(VS.85).aspx)
-   [IObjectWithSite](http://msdn.microsoft.com/library/ms693765(VS.85).aspx)

### Shell interfaces

-   [**IContextMenu2**](https://msdn.microsoft.com/library/windows/desktop/bb776091)
-   [**IExtractIcon**](https://msdn.microsoft.com/library/windows/desktop/bb761854)
-   [**INewShortcutHook**](https://msdn.microsoft.com/library/windows/desktop/bb775445)
-   [**IShellExtInit**](https://msdn.microsoft.com/library/windows/desktop/bb775096)
-   [**IShellLink**](https://msdn.microsoft.com/library/windows/desktop/bb774950)
-   [**IShellPropSheetExt**](https://msdn.microsoft.com/library/windows/desktop/bb774880)
-   [**IQueryInfo**](https://msdn.microsoft.com/library/windows/desktop/bb761359)

## Functions

There are several utility functions that can be used with the Internet shortcut object.

### Internet shortcut utility functions

-   [**InetIsOffline**](https://msdn.microsoft.com/library/windows/desktop/bb776460)
-   [**MIMEAssociationDialog**](https://msdn.microsoft.com/library/windows/desktop/bb776466)
-   [**TranslateURL**](https://msdn.microsoft.com/library/windows/desktop/bb762262)
-   [**URLAssociationDialog**](https://msdn.microsoft.com/library/windows/desktop/bb762264)

 

 




