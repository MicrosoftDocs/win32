---
title: MESSAGEPROPS structure
description: Do not use. Defines message properties.
ms.assetid: 5c41bdac-89e6-45db-b18c-a7bb46f7de2e
keywords:
- MESSAGEPROPS structure Windows Mail (formerly Outlook Express)
- LPMESSAGEPROPS structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MESSAGEPROPS
api_location:
- Msoeapi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MESSAGEPROPS structure

Do not use. Defines message properties.

## Syntax


```C++
typedef struct tagMESSAGEPROPS {
  DWORD        cbSize;
  DWORD        dwReserved;
  MESSAGEID    dwMessageId;
  DWORD        dwLanguage;
  DWORD        dwState;
  DWORD        cbMessage;
  IMSGPRIORITY priority;
  FILETIME     ftReceived;
  FILETIME     ftSent;
  LPSTR        pszSubject;
  LPSTR        pszDisplayTo;
  LPSTR        pszDisplayFrom;
  LPSTR        pszNormalSubject;
  DWORD        dwFlags;
  IStream      *pStmOffsetTable;
} MESSAGEPROPS, *LPMESSAGEPROPS;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Size of the structure in bytes.

</dd> <dt>

**dwReserved**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Reserved value.

</dd> <dt>

**dwMessageId**
</dt> <dd>

Type: **MESSAGEID**

</dd> <dd>

ID value of the message.

</dd> <dt>

**dwLanguage**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The language codepage of this message. For a list of acceptable values, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

**dwState**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Message state flags. For a list of acceptable values, see [**Message State Flags**](oe-message-state-flags.md).

</dd> <dt>

**cbMessage**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Size of the message in bytes.

</dd> <dt>

**priority**
</dt> <dd>

Type: **[**IMSGPRIORITY**](oe-imsgpriority.md)**

</dd> <dd>

The priority level of the message. May be IMSG\_PRI\_LOW, IMSG\_PRI\_NORMAL, or IMSG\_PRI\_HIGH.

</dd> <dt>

**ftReceived**
</dt> <dd>

Type: **[FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp)**

</dd> <dd>

The time at which this message was received.

</dd> <dt>

**ftSent**
</dt> <dd>

Type: **[FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp)**

</dd> <dd>

The time at which this message was sent.

</dd> <dt>

**pszSubject**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

The subject line of the message.

</dd> <dt>

**pszDisplayTo**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

The displayed names on the To: line of the message.

</dd> <dt>

**pszDisplayFrom**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

The displayed names on the From: line of the message.

</dd> <dt>

**pszNormalSubject**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

The normalized form of the subject line of the message.

</dd> <dt>

**dwFlags**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

MIME flags that specify the state of the message. For a list of acceptable values, see [**IMSGFLAGS**](oe-imsgflags.md).

</dd> <dt>

**pStmOffsetTable**
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

</dd> <dd>

An offset table to facilitate quicker message loading. See [**LoadOffsetTable**](oe-imimemessagetree-loadoffsettable.md).

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl> |



 

 





