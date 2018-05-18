---
title: NNTPXHDRRESP structure
description: This will be returned in response to a CommandXHDR call.
ms.assetid: 'cd14854b-a9d3-4285-8fc8-ac978d988c50'
keywords: ["NNTPXHDRRESP structure Windows Mail (formerly Outlook Express)", "LPNNTPXHDRRESP structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- NNTPXHDRRESP
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# NNTPXHDRRESP structure

\[**NNTPXHDRRESP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This will be returned in response to a [**CommandXHDR**](oe-inntptransport-commandxhdr.md) call. Since the number of headers returned is potentially large, [**OnResponse**](oe-inntpcallback-onresponse.md) may be called multiple times in response to this command. **rgHeaders** is not accumulated between calls to **OnResponse**, therefore it is up to the client to store this data as it arrives.

## Syntax


```C++
typedef struct tagNNTPXHDRRESP {
  DWORD      cHeaders;
  LPNNTPXHDR rgHeaders;
  DWORD_PTR  dwReserved;
} NNTPXHDRRESP, *LPNNTPXHDRRESP;
```



## Members

<dl> <dt>

**cHeaders**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Number of header values in **rgHeaders**

</dd> <dt>

**rgHeaders**
</dt> <dd>

Type: **LPNNTPXHDR**

</dd> <dd>

Array of [**NNTPXHDR**](oe-nntpxhdr.md) structs containing the requested headers

</dd> <dt>

**dwReserved**
</dt> <dd>

Type: **DWORD\_PTR**

</dd> <dd>

Reserved for system use

</dd> </dl>

## Remarks

fDone will be set to **TRUE** when all of the headers have been returned.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





