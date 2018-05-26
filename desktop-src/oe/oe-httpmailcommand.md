---
title: HTTPMAILCOMMAND enumeration
description: Identifies the various HTTP commands.
ms.assetid: d12b5119-f760-4997-9dd2-616e383ac1e4
keywords:
- HTTPMAILCOMMAND enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HTTPMAILCOMMAND enumeration

\[**HTTPMAILCOMMAND** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Identifies the various HTTP commands.

## Syntax


```C++
typedef enum tagHTTPMAILCOMMAND { 
  HTTPMAIL_NONE          = 0,
  HTTPMAIL_GETPROP       = 1,
  HTTPMAIL_GET           = 2,
  HTTPMAIL_PUT           = 3,
  HTTPMAIL_POST          = 4,
  HTTPMAIL_DELETE        = 5,
  HTTPMAIL_BDELETE       = 6,
  HTTPMAIL_PROPFIND      = 7,
  HTTPMAIL_PROPPATCH     = 8,
  HTTPMAIL_MKCOL         = 9,
  HTTPMAIL_COPY          = 10,
  HTTPMAIL_BCOPY         = 11,
  HTTPMAIL_MOVE          = 12,
  HTTPMAIL_BMOVE         = 13,
  HTTPMAIL_MEMBERINFO    = 14,
  HTTPMAIL_FINDFOLDERS   = 15,
  HTTPMAIL_MARKREAD      = 16,
  HTTPMAIL_SENDMESSAGE   = 17,
  HTTPMAIL_LISTCONTACTS  = 18,
  HTTPMAIL_CONTACTINFO   = 19,
  HTTPMAIL_POSTCONTACT   = 20,
  HTTPMAIL_PATCHCONTACT  = 21
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="HTTPMAIL_NONE"></span><span id="httpmail_none"></span>**HTTPMAIL\_NONE**
</dt> <dd>

No command.

</dd> <dt>

<span id="HTTPMAIL_GETPROP"></span><span id="httpmail_getprop"></span>**HTTPMAIL\_GETPROP**
</dt> <dd>

The PROPFIND command. See the [**GetProperty**](oe-ihttpmailtransport-getproperty.md) and [**GetPropertyDw**](oe-ihttpmailtransport-getpropertydw.md) methods.

</dd> <dt>

<span id="HTTPMAIL_GET"></span><span id="httpmail_get"></span>**HTTPMAIL\_GET**
</dt> <dd>

The GET command. See the [**CommandGET**](oe-ihttpmailtransport-commandget.md) method.

</dd> <dt>

<span id="HTTPMAIL_PUT"></span><span id="httpmail_put"></span>**HTTPMAIL\_PUT**
</dt> <dd>

The PUT command. See the [**CommandPUT**](oe-ihttpmailtransport-commandput.md) method.

</dd> <dt>

<span id="HTTPMAIL_POST"></span><span id="httpmail_post"></span>**HTTPMAIL\_POST**
</dt> <dd>

The POST command. See the [**CommandPOST**](oe-ihttpmailtransport-commandpost.md) method.

</dd> <dt>

<span id="HTTPMAIL_DELETE"></span><span id="httpmail_delete"></span>**HTTPMAIL\_DELETE**
</dt> <dd>

The DELETE command. See the [**CommandDELETE**](oe-ihttpmailtransport-commanddelete.md) method.

</dd> <dt>

<span id="HTTPMAIL_BDELETE"></span><span id="httpmail_bdelete"></span>**HTTPMAIL\_BDELETE**
</dt> <dd>

The BDELETE command. See the [**CommandBDELETE**](oe-ihttpmailtransport-commandbdelete.md) method.

</dd> <dt>

<span id="HTTPMAIL_PROPFIND"></span><span id="httpmail_propfind"></span>**HTTPMAIL\_PROPFIND**
</dt> <dd>

The PROPFIND command.

</dd> <dt>

<span id="HTTPMAIL_PROPPATCH"></span><span id="httpmail_proppatch"></span>**HTTPMAIL\_PROPPATCH**
</dt> <dd>

The PROPPATCH command. See the [**CommandPROPPATCH**](oe-ihttpmailtransport-commandproppatch.md) method.

</dd> <dt>

<span id="HTTPMAIL_MKCOL"></span><span id="httpmail_mkcol"></span>**HTTPMAIL\_MKCOL**
</dt> <dd>

The MKCOL command. See the [**CommandMKCOL**](oe-ihttpmailtransport-commandmkcol.md) method.

</dd> <dt>

<span id="HTTPMAIL_COPY"></span><span id="httpmail_copy"></span>**HTTPMAIL\_COPY**
</dt> <dd>

The COPY command. See the [**CommandCOPY**](oe-ihttpmailtransport-commandcopy.md) method.

</dd> <dt>

<span id="HTTPMAIL_BCOPY"></span><span id="httpmail_bcopy"></span>**HTTPMAIL\_BCOPY**
</dt> <dd>

The BCOPY command. See the [**CommandBCOPY**](oe-ihttpmailtransport-commandbcopy.md) method.

</dd> <dt>

<span id="HTTPMAIL_MOVE"></span><span id="httpmail_move"></span>**HTTPMAIL\_MOVE**
</dt> <dd>

The MOVE command. See the [**CommandMOVE**](oe-ihttpmailtransport-commandmove.md) method.

</dd> <dt>

<span id="HTTPMAIL_BMOVE"></span><span id="httpmail_bmove"></span>**HTTPMAIL\_BMOVE**
</dt> <dd>

The BMOVE command. See the [**CommandBMOVE**](oe-ihttpmailtransport-commandbmove.md) method.

</dd> <dt>

<span id="HTTPMAIL_MEMBERINFO"></span><span id="httpmail_memberinfo"></span>**HTTPMAIL\_MEMBERINFO**
</dt> <dd>

See the [**MemberInfo**](oe-ihttpmailtransport-memberinfo.md) method.

</dd> <dt>

<span id="HTTPMAIL_FINDFOLDERS"></span><span id="httpmail_findfolders"></span>**HTTPMAIL\_FINDFOLDERS**
</dt> <dd>

Unused.

</dd> <dt>

<span id="HTTPMAIL_MARKREAD"></span><span id="httpmail_markread"></span>**HTTPMAIL\_MARKREAD**
</dt> <dd>

See the [**MarkRead**](oe-ihttpmailtransport-markread.md) method.

</dd> <dt>

<span id="HTTPMAIL_SENDMESSAGE"></span><span id="httpmail_sendmessage"></span>**HTTPMAIL\_SENDMESSAGE**
</dt> <dd>

See the [**SendMessage**](oe-ihttpmailtransport-sendmessage.md) method.

</dd> <dt>

<span id="HTTPMAIL_LISTCONTACTS"></span><span id="httpmail_listcontacts"></span>**HTTPMAIL\_LISTCONTACTS**
</dt> <dd>

See the [**ListContacts**](oe-ihttpmailtransport-listcontacts.md) method.

</dd> <dt>

<span id="HTTPMAIL_CONTACTINFO"></span><span id="httpmail_contactinfo"></span>**HTTPMAIL\_CONTACTINFO**
</dt> <dd>

See the [**ContactInfo**](oe-ihttpmailtransport-contactinfo.md) and [**ListContactInfos**](oe-ihttpmailtransport-listcontactinfos.md) methods.

</dd> <dt>

<span id="HTTPMAIL_POSTCONTACT"></span><span id="httpmail_postcontact"></span>**HTTPMAIL\_POSTCONTACT**
</dt> <dd>

See the [**PostContact**](oe-ihttpmailtransport-postcontact.md) method.

</dd> <dt>

<span id="HTTPMAIL_PATCHCONTACT"></span><span id="httpmail_patchcontact"></span>**HTTPMAIL\_PATCHCONTACT**
</dt> <dd>

See the [**PatchContact**](oe-ihttpmailtransport-patchcontact.md) method.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





