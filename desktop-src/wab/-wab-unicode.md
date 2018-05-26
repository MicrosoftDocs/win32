---
title: UNICODE Support in WAB
description: Versions 5.0 and later of the WAB support UNICODE.
ms.assetid: bafc1884-8961-40a4-b189-902d751e3386
keywords:
- address books
- Windows Address Book (WAB),UNICODE support
- WAB (Windows Address Book),UNICODE support
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UNICODE Support in WAB

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](_wincontacts_entry_point).

 

Versions 5.0 and later of the WAB support UNICODE.

## Methods that Support UNICODE Strings

The following methods and structures exhibit some level of support for UNICODE:



| Method/Structure                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LDAPUrl**](/windows/previous-versions/Wabapi/?branch=master)                                                                                | The *lpszURL* parameter of this method is of type **LPSTR**. You can pass a **LPWSTR**URL into this method by casting it to an **LPSTR** and setting the *ulFlags* parameter to MAPI\_UNICODE. Upon seeing the flag, the WAB casts the URL to an **LPWSTR** prior to using it.                                                                                                                           |
| ContextMenu and Property Sheet Extensions                                                                                 | The *lpsz* member of the [**WABEXTDISPLAY**](/windows/previous-versions/Wabapi/ns-wabapi-_wabextdisplay?branch=master) structure is defined to be type **LPTSTR**. If this member contains a wide string, *ulFlags* in the structure contains MAPI\_UNICODE. If *ulFlags* does not contain MAPI\_UNICODE then this string is a **LPSTR** and must be cast as such before using.                                                                            |
| IPropObject::GetProps                                                                                                     | If caller specifies MAPI\_UNICODE as the flag, the returned property array contains all wide strings. Corresponding property tags are of type PT\_UNICODE and PT\_MV\_UNICODE.                                                                                                                                                                                                                           |
| IPropObject::GetPropList                                                                                                  | If caller specifies MAPI\_UNICODE, the returned prop list shows strings of type PT\_UNICODE and PT\_MV\_UNICODE instead of PT\_STRING8 and PT\_MV\_STRING8.                                                                                                                                                                                                                                              |
| [**Address**](/windows/previous-versions/Wabiab/?branch=master)                                                                                 | If the caller sets the **ulFlags** member to contain MAPI\_UNICODE, then all the strings in the [**ADRPARM**](/windows/previous-versions/Wabdefs/ns-wabdefs-_adrparm?branch=master) structure are assumed to be of type **LPWSTR**. Otherwise, they are assumed to be of type **LPSTR**. If MAPI\_UNICODE is specified, then all strings passed in and returned by the [**ADRLIST**](/windows/previous-versions/Wabdefs/ns-wabdefs-_adrlist?branch=master) are in UNICODE; otherwise, the strings are ANSI/DBCS. |
| [**Details**](/windows/previous-versions/Wabiab/?branch=master)                                                                                 | Specifying MAPI\_UNICODE has no effect on this method, since the *lpszButtonText* parameter is the only parameter affected by the UNICODE flag and this parameter is ignored within the WAB.                                                                                                                                                                                                             |
| [**CreateOneOff**](/windows/previous-versions/Wabiab/?branch=master)                                                                       | Specify MAPI\_UNICODE if the strings being passed in are in UNICODE. Absence of the flag means that the strings are ANSI/DBCS.                                                                                                                                                                                                                                                                           |
| [**ResolveName**](/windows/previous-versions/Wabiab/?branch=master)                                                                         | Specify WAB\_RESOLVE\_UNICODE (not MAPI\_UNICODE) if all strings in the [**ADRLIST**](/windows/previous-versions/Wabdefs/ns-wabdefs-_adrlist?branch=master) are in UNICODE. The returned strings are in UNICODE. Otherwise, all in and out strings are ANSI/DBCS.                                                                                                                                                                                            |
| [**ResolveNames**](-wab-iabcontainer-resolvenames.md)                                                                    | Specify MAPI\_UNICODE for UNICODE strings; specify 0 for ANSI/DBCS strings.                                                                                                                                                                                                                                                                                                                              |
| [**GetContentsTable**](-wab-idistlist-getcontentstable.md)[**GetContentsTable**](-wab-iabcontainer-getcontentstable.md) | Specify MAPI\_UNICODE to ensure that all strings in the table are UNICODE; otherwise, all strings will be ANSI/DBCS.                                                                                                                                                                                                                                                                                     |
| [**GetSearchPath**](/windows/previous-versions/Wabiab/?branch=master)                                                                     | Specify MAPI\_UNICODE for UNICODE strings, 0 for ANSI/DBCS.                                                                                                                                                                                                                                                                                                                                              |



 

 

 




