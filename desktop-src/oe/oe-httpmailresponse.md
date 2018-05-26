---
title: HTTPMAILRESPONSE structure
description: Contains information about an HTTPMail response.
ms.assetid: 885374a7-42a6-42b9-b5a9-27f2092024bc
keywords:
- HTTPMAILRESPONSE structure Windows Mail (formerly Outlook Express)
- LPHTTPMAILRESPONSE structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPMAILRESPONSE
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

# HTTPMAILRESPONSE structure

\[**HTTPMAILRESPONSE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains information about an HTTPMail response.

## Syntax


```C++
typedef struct tagHTTPMAILRESPONSE {
  HTTPMAILCOMMAND       command;
  DWORD                 dwContext;
  BOOL                  fDone;
  IXPRESULT             rIxpResult;
  IHTTPMailTransport    *pTransport;
  HTTPMAILGETPROP       rGetPropInfo;
  HTTPMAILGET           rGetInfo;
  HTTPMAILPOST          rPutInfo;
  HTTPMAILPOST          rPostInfo;
  HTTPMAILPROPFIND      rPropFindInfo;
  HTTPMAILLOCATION      rMkColInfo;
  HTTPMAILLOCATION      rCopyMoveInfo;
  HTTPMAILBCOPYMOVELIST rBCopyMoveList;
  HTTPMEMBERINFOLIST    rMemberInfoList;
  HTTPMEMBERERRORLIST   rMemberErrorList;
  HTTPMAILPOST          rSendMessageInfo;
  HTTPCONTACTIDLIST     rContactIdList;
  HTTPCONTACTINFOLIST   rContactInfoList;
  HTTPCONTACTID         rPostContactInfo;
  HTTPCONTACTID         rPatchContactInfo;
} HTTPMAILRESPONSE, *LPHTTPMAILRESPONSE;
```



## Members

<dl> <dt>

**command**
</dt> <dd>

Type: **[**HTTPMAILCOMMAND**](oe-httpmailcommand.md)**

</dd> <dd>

Contains the [**HTTPMAILCOMMAND**](oe-httpmailcommand.md) for which the response was generated.

</dd> <dt>

**dwContext**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Currently unused. Should be set to zero.

</dd> <dt>

**fDone**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether this is the last response for the command.

</dd> <dt>

**rIxpResult**
</dt> <dd>

Type: **[**IXPRESULT**](oe-ixpresult.md)**

</dd> <dd>

Contains an [**IXPRESULT**](oe-ixpresult.md) structure that contains the information about the server response. If **rIxpResult**.**hrResult** specifies a FAILED result, the structure contains other information.

</dd> <dt>

**pTransport**
</dt> <dd>

Type: **[**IHTTPMailTransport**](oe-ihttpmailtransport.md)\***

</dd> <dd>

Contains a pointer to the [**IHTTPMailTransport**](oe-ihttpmailtransport.md) object that generated the [**OnResponse**](oe-ihttpmailcallback-onresponse.md) call.

</dd> <dt>

**rGetPropInfo**
</dt> <dd>

Type: **[**HTTPMAILGETPROP**](oe-httpmailgetprop.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_GETPROP**](oe-httpmailcommand.md). Contains the [**HTTPMAILGETPROP**](oe-httpmailgetprop.md) structure that holds the response data for the [**GetProperty**](oe-ihttpmailtransport-getproperty.md) and [**GetPropertyDw**](oe-ihttpmailtransport-getpropertydw.md) methods.

</dd> <dt>

**rGetInfo**
</dt> <dd>

Type: **[**HTTPMAILGET**](oe-httpmailget.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_GET**](oe-httpmailcommand.md). Contains the [**HTTPMAILGET**](oe-httpmailget.md) structure that holds the response data for the [**CommandGET**](oe-ihttpmailtransport-commandget.md) method.

</dd> <dt>

**rPutInfo**
</dt> <dd>

Type: **[**HTTPMAILPOST**](oe-httpmailpost.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_PUT**](oe-httpmailcommand.md). Contains the [**HTTPMAILPOST**](oe-httpmailpost.md) structure that holds the response data for the [**CommandPUT**](oe-ihttpmailtransport-commandput.md) method.

</dd> <dt>

**rPostInfo**
</dt> <dd>

Type: **[**HTTPMAILPOST**](oe-httpmailpost.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_POST**](oe-httpmailcommand.md). Contains the [**HTTPMAILPOST**](oe-httpmailpost.md) structure that holds the response data for the [**CommandPOST**](oe-ihttpmailtransport-commandpost.md) method.

</dd> <dt>

**rPropFindInfo**
</dt> <dd>

Type: **[**HTTPMAILPROPFIND**](oe-httpmailpropfind.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_PROPFIND**](oe-httpmailcommand.md). Contains the [**HTTPMAILPROPFIND**](oe-httpmailpropfind.md) structure that holds the response data.

</dd> <dt>

**rMkColInfo**
</dt> <dd>

Type: **[**HTTPMAILLOCATION**](oe-httpmaillocation.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_MKCOL**](oe-httpmailcommand.md). Contains the [**HTTPMAILLOCATION**](oe-httpmaillocation.md) structure that holds the response data for the [**CommandMKCOL**](oe-ihttpmailtransport-commandmkcol.md) method.

</dd> <dt>

**rCopyMoveInfo**
</dt> <dd>

Type: **[**HTTPMAILLOCATION**](oe-httpmaillocation.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_COPY**](oe-httpmailcommand.md). Contains the [**HTTPMAILLOCATION**](oe-httpmaillocation.md) structure that holds the response data for the [**CommandCOPY**](oe-ihttpmailtransport-commandcopy.md) and [**CommandMOVE**](oe-ihttpmailtransport-commandmove.md) methods.

</dd> <dt>

**rBCopyMoveList**
</dt> <dd>

Type: **[**HTTPMAILBCOPYMOVELIST**](oe-httpmailbcopymovelist.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_BCOPY**](oe-httpmailcommand.md). Contains the [**HTTPMAILBCOPYMOVELIST**](oe-httpmailbcopymovelist.md) structure that holds the response data for the [**CommandBCOPY**](oe-ihttpmailtransport-commandbcopy.md) and [**CommandBMOVE**](oe-ihttpmailtransport-commandbmove.md) methods.

</dd> <dt>

**rMemberInfoList**
</dt> <dd>

Type: **[**HTTPMEMBERINFOLIST**](oe-httpmemberinfolist.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_MEMBERINFO**](oe-httpmailcommand.md). Contains the [**HTTPMEMBERINFOLIST**](oe-httpmemberinfolist.md) structure that holds the response data for the [**MemberInfo**](oe-ihttpmailtransport-memberinfo.md) method.

</dd> <dt>

**rMemberErrorList**
</dt> <dd>

Type: **[**HTTPMEMBERERRORLIST**](oe-httpmembererrorlist.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_MARKREAD**](oe-httpmailcommand.md). Contains the [**HTTPMEMBERERRORLIST**](oe-httpmembererrorlist.md) structure that holds the response data for the [**MarkRead**](oe-ihttpmailtransport-markread.md) method.

</dd> <dt>

**rSendMessageInfo**
</dt> <dd>

Type: **[**HTTPMAILPOST**](oe-httpmailpost.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_SENDMESSAGE**](oe-httpmailcommand.md). Contains the [**HTTPMAILPOST**](oe-httpmailpost.md) structure that holds the response data for the [**SendMessage**](oe-ihttpmailtransport-sendmessage.md) method.

</dd> <dt>

**rContactIdList**
</dt> <dd>

Type: **[**HTTPCONTACTIDLIST**](oe-httpcontactidlist.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_LISTCONTACTS**](oe-httpmailcommand.md). Contains the [**HTTPCONTACTIDLIST**](oe-httpcontactidlist.md) structure that holds the response data for the [**ContactInfo**](oe-ihttpmailtransport-contactinfo.md) method.

</dd> <dt>

**rContactInfoList**
</dt> <dd>

Type: **[**HTTPCONTACTINFOLIST**](oe-httpcontactinfolist.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_CONTACTINFO**](oe-httpmailcommand.md). Contains the [**HTTPCONTACTINFOLIST**](oe-httpcontactinfolist.md) structure that holds the response data for the [**ListContactInfos**](oe-ihttpmailtransport-listcontactinfos.md) method.

</dd> <dt>

**rPostContactInfo**
</dt> <dd>

Type: **[**HTTPCONTACTID**](oe-httpcontactid.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_POSTCONTACT**](oe-httpmailcommand.md). Contains the [**HTTPCONTACTID**](oe-httpcontactid.md) structure that holds the response data for the [**ListContacts**](oe-ihttpmailtransport-listcontacts.md) method.

</dd> <dt>

**rPatchContactInfo**
</dt> <dd>

Type: **[**HTTPCONTACTID**](oe-httpcontactid.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**HTTPMAIL\_PATCHCONTACT**](oe-httpmailcommand.md). Contains the [**HTTPCONTACTID**](oe-httpcontactid.md) structure that holds the response data for the [**PatchContact**](oe-ihttpmailtransport-patchcontact.md) method.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





