---
title: NNTPRESPONSE structure
description: Do not use.
ms.assetid: 35675f0f-d8df-4653-86aa-9f8be6327786
keywords:
- NNTPRESPONSE structure Windows Mail (formerly Outlook Express)
- LPNNTPRESPONSE structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- NNTPRESPONSE
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# NNTPRESPONSE structure

Do not use. This structure is the general holder for all of the data returned from the [**INNTPTransport**](oe-inntptransport.md) commands. The state member tells the receiver which command this data is in response to. If **fMustRelease** is **TRUE**, then when the client is done with this data, it should call [**ReleaseResponse**](oe-inntptransport-releaseresponse.md) to free that memory. See the explanation of the various structures to see the details on each type of response.

## Syntax


```C++
typedef struct tagNNTPRESPONSE {
  NNTPSTATE      state;
  BOOL           fMustRelease;
  BOOL           fDone;
  IXPRESULT      rIxpResult;
  INNTPTransport *pTransport;
} NNTPRESPONSE, *LPNNTPRESPONSE;
```



## Members

<dl> <dt>

**state**
</dt> <dd>

Type: **[**NNTPSTATE**](oe-nntpstate.md)**

</dd> <dd>

Command in which the response was generated for

</dd> <dt>

**fMustRelease**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

**TRUE** if the data contained within this struct must be freed with a call to [**ReleaseResponse**](oe-inntptransport-releaseresponse.md)

</dd> <dt>

**fDone**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

**TRUE** when there is no more data that will arrive for this command

</dd> <dt>

**rIxpResult**
</dt> <dd>

Type: **[**IXPRESULT**](oe-ixpresult.md)**

</dd> <dd>

Result Information

</dd> <dt>

**pTransport**
</dt> <dd>

Type: **[**INNTPTransport**](oe-inntptransport.md)\***

</dd> <dd>

Pointer to the NNTP transport that generated the response

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





