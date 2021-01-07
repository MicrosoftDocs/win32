---
description: The expert must implement the Register expert function. Network Monitor calls the Register expert function to obtain information about the expert.
ms.assetid: 58cfe525-99b1-40ce-b8d8-fa1c62a20c40
title: Register Expert callback function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Register
api_type: 
- UserDefined
api_location: 
- Netmon.h
---

# Register Expert callback function

The expert must implement the **Register** expert function. Network Monitor calls the **Register** expert function to obtain information about the expert.

## Syntax


```C++
BOOL WINAPI Register(
  _Inout_ PEXPERTENUMINFO pExpertInfo
);
```



## Parameters

<dl> <dt>

*pExpertInfo* \[in, out\]
</dt> <dd>

Pointer to an [**EXPERTENUMINFO**](expertenuminfo.md) structure that Network Monitor allocates. The expert fills in the structure with all requested information.

</dd> </dl>

## Return value

If the function is successful, the return value is **TRUE**, and the function returns the requested information.

If the function is unsuccessful, the return value is **FALSE**.

## Remarks

The **Version** member of the [**EXPERTENUMINFO**](expertenuminfo.md) structure must be zero.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




