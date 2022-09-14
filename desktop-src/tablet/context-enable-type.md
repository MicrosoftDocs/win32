---
description: Indicates whether context messages should be sent to the owning window's window procedure.
ms.assetid: 57ecf10a-8a02-4353-b916-9080ebc0b270
title: CONTEXT_ENABLE_TYPE enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CONTEXT_ENABLE_TYPE
api_type: 
- NA
api_location: 
---

# CONTEXT\_ENABLE\_TYPE enumeration

Indicates whether context messages should be sent to the owning window's window procedure.

## Syntax


```C++
typedef enum _CONTEXT_ENABLE_TYPE { 
  CONTEXT_ENABLE   = 1,
  CONTEXT_DISABLE  = 2
} CONTEXT_ENABLE_TYPE;
```



## Constants

<dl> <dt>

<span id="CONTEXT_ENABLE"></span><span id="context_enable"></span>**CONTEXT\_ENABLE**
</dt> <dd>

The tablet context should be enabled, resulting in context messages being sent to the owning window's window procedure.

</dd> <dt>

<span id="CONTEXT_DISABLE"></span><span id="context_disable"></span>**CONTEXT\_DISABLE**
</dt> <dd>

The tablet context should be disabled, preventing any further context messages from being sent to the owning window's window procedure or event sink.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                     |



## See also

<dl> <dt>

[**ITablet::CreateContext Method**](itablet-createcontext.md)
</dt> </dl>

 

 




