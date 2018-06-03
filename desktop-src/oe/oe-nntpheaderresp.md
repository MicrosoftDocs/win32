---
title: NNTPHEADERRESP structure
description: This structure will be returned in response to the GetHeaders command.
ms.assetid: 0ce996f6-0409-49df-929d-6ed29fcf39f3
keywords:
- NNTPHEADERRESP structure Windows Mail (formerly Outlook Express)
- LPNNTPHEADERRESP structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- NNTPHEADERRESP
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

# NNTPHEADERRESP structure

\[**NNTPHEADERRESP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This structure will be returned in response to the [**GetHeaders**](oe-inntptransport-getheaders.md) command. Because the number of headers requested may be large, [**OnResponse**](oe-inntpcallback-onresponse.md) may be called multiple times in response to this command. **rgHeaders** is not accumulated by the transport between calls to **OnResponse** therefore it is the responsibility of the caller to store this information as it is retrieved. When all the data is retrieved, then fDone will be set to **TRUE**. Since not all servers provide the XREF: header in their XOVER records, **fSupportsXRef** will be set to **TRUE** if the **pszXref** field in [**NNTPHEADER**](oe-nntpheader.md) is valid. If this is **FALSE**, the client can retrieve this header with a call to [**CommandXHDR**](oe-inntptransport-commandxhdr.md).

## Syntax


```C++
typedef struct tagNNTPHEADERRESP {
  DWORD        cHeaders;
  LPNNTPHEADER rgHeaders;
  BOOL         fSupportsXRef;
  DWORD_PTR    dwReserved;
} NNTPHEADERRESP, *LPNNTPHEADERRESP;
```



## Members

<dl> <dt>

**cHeaders**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Number of headers in **rgHeaders**

</dd> <dt>

**rgHeaders**
</dt> <dd>

Type: **LPNNTPHEADER**

</dd> <dd>

Array of header structures

</dd> <dt>

**fSupportsXRef**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

**TRUE** if the headers have a valid pszXref value. Otherwise, the client needs to issue an XHdr to retrieve that value if they're interested.

</dd> <dt>

**dwReserved**
</dt> <dd>

Type: **DWORD\_PTR**

</dd> <dd>

Reserved for system use

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





