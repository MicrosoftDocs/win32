---
title: MEMBERINFOFLAGS
description: DWORD that classifies resource properties.
ms.assetid: 94b6cf23-bd4a-447c-afbb-a3cb80f19bc6
topic_type:
- apiref
api_name:
- HTTP_MEMBERINFO_COMMONPROPS
- HTTP_MEMBERINFO_FOLDERPROPS
- HTTP_MEMBERINFO_MESSAGEPROPS
- HTTP_MEMBERINFO_ALLPROPS
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEMBERINFOFLAGS

\[**MEMBERINFOFLAGS** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

**DWORD** that classifies resource properties.



| Constant/value                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                        |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="HTTP_MEMBERINFO_COMMONPROPS"></span><span id="http_memberinfo_commonprops"></span><dl> <dt>**HTTP\_MEMBERINFO\_COMMONPROPS**</dt> <dt>0x00000000</dt> </dl>                                             | Properties common to all resources. Combines the **pszHref** and **fIsFolder** members of the [**HTTPMEMBERINFO**](oe-httpmemberinfo.md) structure. <br/>                                                                                   |
| <span id="HTTP_MEMBERINFO_FOLDERPROPS"></span><span id="http_memberinfo_folderprops"></span><dl> <dt>**HTTP\_MEMBERINFO\_FOLDERPROPS**</dt> <dt>0x00000001</dt> </dl>                                             | Properties common to collection resources. Combines the **pszDisplayName**, **fHasSubs**, **fNoSubs**, **dwUnreadCount**, **dwVisibleCount**, and **tySpecial** members of the [**HTTPMEMBERINFO**](oe-httpmemberinfo.md) structure. <br/>  |
| <span id="HTTP_MEMBERINFO_MESSAGEPROPS"></span><span id="http_memberinfo_messageprops"></span><dl> <dt>**HTTP\_MEMBERINFO\_MESSAGEPROPS**</dt> <dt>0x00000002</dt> </dl>                                          | Properties common to message resources. Combines the **fRead**, **fHasAttachment**, **pszTo**, **pszFrom**, **pszSubject**, **pszDate**, and **dwContentLength** members of the [**HTTPMEMBERINFO**](oe-httpmemberinfo.md) structure. <br/> |
| <span id="HTTP_MEMBERINFO_ALLPROPS"></span><span id="http_memberinfo_allprops"></span><dl> <dt>**HTTP\_MEMBERINFO\_ALLPROPS**</dt> <dt>HTTP\_MEMBERINFO\_FOLDERPROPS \| HTTP\_MEMBERINFO\_MESSAGEPROPS</dt> </dl> | All the properties of resources. <br/>                                                                                                                                                                                                       |



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





