---
title: Defining Custom Properties
description: Defining Custom Properties
ms.assetid: ccf2fdd4-7986-4f3a-995d-27e30297cc90
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Defining Custom Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following data types are for custom properties:

-   String: **DBTYPE\_LPSTR\|DBTYPE\_BYREF**, **DBTYPE\_WSTR\|DBTYPE\_BYREF**, **DBTYPE\_STR\|DBTYPE\_BYREF**
-   Date: **VT\_FILETIME**
-   Number: **DBTYPE\_I4**
-   Yes or No (TRUE or FALSE): **DBTYPE\_BOOL**

Office document properties take the following GUIDs:

-   Custom properties: D5CDD505-2E9C-101B-9397-08002B2CF9AE
-   Properties such as company name: D5CDD502-2E9C-101B-9397-08002B2CF9AE
-   Built-in properties, like **DocTitle**: F29F85E0-4FF9-1068-AB91-08002B27B3D9
-   **A\_HRef** (and **HTMLHRef**): c82bf597-b831-11d0-b733-00aa00a1ebd2\\A.HREF
-   **Img\_Alt**: 70eb7a10-55d9-11cf-b75b-00aa0051fe20\\IMG.ALT

The following example shows you how to name a custom property for Office by adding a GUID to the Names section of the .idq file:

``` syntax
Custom_Text ( DBTYPE_STR|DBTYPE_BYREF ) = D5CDD505-2E9C-101B-9397-08002B2CF9AE "Custom_Text"
```

In this example, *Custom\_Text* can be any string. The value of *Custom\_Text* does not have to be the same at the beginning and end of the line. The one at the beginning is the friendly name, and the one at the end (in quotation marks) is the Office property name.

If defining a custom date, you must use the **VT\_FILETIME** data type. For example:

``` syntax
DocDateCompleted( VT_FILETIME,20 ) = D5CDD505-2E9C-101B-9397-08002B2CF9AE "Date completed"
```

For other Office properties, see the Microsoft Office Software Developer’s Kit (SDK). For properties available with other products, see the documentation for each independent software vendor that supplies an [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) implementation.

 

 




