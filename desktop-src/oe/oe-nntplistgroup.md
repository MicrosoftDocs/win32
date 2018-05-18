---
title: NNTPLISTGROUP structure
description: This structure is sent in response to a CommandLISTGROUP call.
ms.assetid: 'd8006bc2-726d-473f-ba32-16f26e98d9b5'
keywords: ["NNTPLISTGROUP structure Windows Mail (formerly Outlook Express)", "LPNNTPLISTGROUP structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- NNTPLISTGROUP
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# NNTPLISTGROUP structure

\[**NNTPLISTGROUP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This structure is sent in response to a [**CommandLISTGROUP**](oe-inntptransport-commandlistgroup.md) call.**rgArticles** is an array of article numbers that are contained in the newsgroup. Since there can be quite a few articles, [**OnResponse**](oe-inntpcallback-onresponse.md) may be called multiple times with the data as it arrives. **rgArticles** is not accumulated between calls to **OnResponse** so it is up to the client to store this information as it arrives.

## Syntax


```C++
typedef struct tagNNTPLISTGROUP {
  DWORD cArticles;
  DWORD *rgArticles;
} NNTPLISTGROUP, *LPNNTPLISTGROUP;
```



## Members

<dl> <dt>

**cArticles**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Number of article numbers in **rgArticles**

</dd> <dt>

**rgArticles**
</dt> <dd>

Type: **DWORD\***

</dd> <dd>

Array of article numbers available in the group

</dd> </dl>

## Remarks

fDone will be **TRUE** when all the information has been returned.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





