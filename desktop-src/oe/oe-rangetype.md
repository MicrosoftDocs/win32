---
title: RANGETYPE enumeration
description: The range structure allows the caller to provide arguments for commands that allow a range of headers to be retrieved.
ms.assetid: 'bbd36012-19f6-45ca-ae65-b950e5c59ae0'
keywords: ["RANGETYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# RANGETYPE enumeration

\[**RANGETYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The range structure allows the caller to provide arguments for commands that allow a range of headers to be retrieved. The range structure can be used to specify a single number (ie XOVER 2010), or bounded range (ie XOVER 2000-2010) to request all of the headers within that range \[inclusive\].

## Syntax


```C++
typedef enum tagRANGETYPE { 
  RT_SINGLE  = 0,
  RT_RANGE   = 1
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="RT_SINGLE"></span><span id="rt_single"></span>**RT\_SINGLE**
</dt> <dd>

Single number

</dd> <dt>

<span id="RT_RANGE"></span><span id="rt_range"></span>**RT\_RANGE**
</dt> <dd>

Bounded range

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





