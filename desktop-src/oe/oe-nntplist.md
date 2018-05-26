---
title: NNTPLIST structure
description: This structure is the data returned from the CommandLIST function.
ms.assetid: ec225f79-b826-4f5f-b90c-168fb53bded3
keywords:
- NNTPLIST structure Windows Mail (formerly Outlook Express)
- LPNNTPLIST structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- NNTPLIST
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

# NNTPLIST structure

\[**NNTPLIST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This structure is the data returned from the [**CommandLIST**](oe-inntptransport-commandlist.md) function. Because the NNTP LIST command can have multiple extensions, the data returned is relatively unparsed to provide greater flexibility to the client. The data is returned in array of **NULL** terminated strings that contain the lines returned from the server. When fDone is **TRUE**, then all of the data has been retrieved. rgszLines is not accumulated by the transport between calls to OnResponse(). It is the client's responsibility to store this information as it comes in.

## Syntax


```C++
typedef struct tagNNTPLIST {
  DWORD cLines;
  LPSTR *rgszLines;
} NNTPLIST, *LPNNTPLIST;
```



## Members

<dl> <dt>

**cLines**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Number of lines returned

</dd> <dt>

**rgszLines**
</dt> <dd>

Type: **LPSTR\***

</dd> <dd>

Array of lines returned by the LIST command. The number of lines in **rgszLines** is **cLines**. The recipient must call [**ReleaseResponse**](oe-inntptransport-releaseresponse.md) to free this structure.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





