---
title: CRIT\_LOGIC enumeration
description: CRIT\_LOGIC is no longer available for use as of Windows Vista.
ms.assetid: 'd4c8728f-f6c0-4c24-902b-77a6be9b9787'
keywords: ["CRIT_LOGIC enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Oerules.h
api_type:
- HeaderDef
---

# CRIT\_LOGIC enumeration

\[**CRIT\_LOGIC** is no longer available for use as of Windows Vista.\]

Specifies criteria logic.

## Syntax


```C++
typedef enum tagCRIT_LOGIC { 
  CRIT_LOGIC_NULL  = 0,
  CRIT_LOGIC_OR    = 1,
  CRIT_LOGIC_AND   = 2,
  CRIT_LOGIC_MAX   = 3
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="CRIT_LOGIC_NULL"></span><span id="crit_logic_null"></span>**CRIT\_LOGIC\_NULL**
</dt> <dd></dd> <dt>

<span id="CRIT_LOGIC_OR"></span><span id="crit_logic_or"></span>**CRIT\_LOGIC\_OR**
</dt> <dd></dd> <dt>

<span id="CRIT_LOGIC_AND"></span><span id="crit_logic_and"></span>**CRIT\_LOGIC\_AND**
</dt> <dd></dd> <dt>

<span id="CRIT_LOGIC_MAX"></span><span id="crit_logic_max"></span>**CRIT\_LOGIC\_MAX**
</dt> <dd></dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Oerules.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl> |



 

 





