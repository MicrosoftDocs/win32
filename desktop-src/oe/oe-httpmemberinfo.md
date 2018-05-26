---
title: HTTPMEMBERINFO structure
description: Contains resource properties returned in a server response for the MemberInfo method.
ms.assetid: de511ac9-2ab8-42eb-a7e0-4b69c05d09dd
keywords:
- HTTPMEMBERINFO structure Windows Mail (formerly Outlook Express)
- LPHTTPMEMBERINFO structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPMEMBERINFO
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HTTPMEMBERINFO structure

\[**HTTPMEMBERINFO** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains resource properties returned in a server response for the [**MemberInfo**](oe-ihttpmailtransport-memberinfo.md) method.

## Syntax


```C++
typedef struct tagHTTPMEMBERINFO {
  LPSTR                 pszHref;
  BOOL                  fIsFolder;
  LPSTR                 pszDisplayName;
  BOOL                  fHasSubs;
  BOOL                  fNoSubs;
  DWORD                 dwUnreadCount;
  DWORD                 dwVisibleCount;
  HTTPMAILSPECIALFOLDER tySpecial;
  BOOL                  fRead;
  BOOL                  fHasAttachment;
  LPSTR                 pszTo;
  LPSTR                 pszFrom;
  LPSTR                 pszSubject;
  LPSTR                 pszDate;
  DWORD                 dwContentLength;
} HTTPMEMBERINFO, *LPHTTPMEMBERINFO;
```



## Members

<dl> <dt>

**pszHref**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the URL of the resource.

</dd> <dt>

**fIsFolder**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the resource is a collection.

</dd> <dt>

**pszDisplayName**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the name of the resource used for UI. This is a folder property.

</dd> <dt>

**fHasSubs**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the collection resource has subtrees. This is a folder property.

</dd> <dt>

**fNoSubs**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the collection resource has no subtrees. This is a folder property.

</dd> <dt>

**dwUnreadCount**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the number of unread messages contained in the collection. This is a folder property.

</dd> <dt>

**dwVisibleCount**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the number of visible messages in the collection. This is a folder property.

</dd> <dt>

**tySpecial**
</dt> <dd>

Type: **[**HTTPMAILSPECIALFOLDER**](oe-httpmailspecialfolder.md)**

</dd> <dd>

Contains a value from the [**HTTPMAILSPECIALFOLDER**](oe-httpmailspecialfolder.md) enumeration that indicates the special folder type. This is a folder property.

</dd> <dt>

**fRead**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the resource is marked read. This is a message property.

</dd> <dt>

**fHasAttachment**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the resource has an attachment. This is a message property.

</dd> <dt>

**pszTo**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the contents of the To: field in the header. This is a message property.

</dd> <dt>

**pszFrom**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the contents of the From: field in the header. This is a message property.

</dd> <dt>

**pszSubject**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the contents of the Subject: field in the header. This is a message property.

</dd> <dt>

**pszDate**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the contents of the Date: field in the header. This is a message property.

</dd> <dt>

**dwContentLength**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the size of the content of the resource. This is a message property.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





