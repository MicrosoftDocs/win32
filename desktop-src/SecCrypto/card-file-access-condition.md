---
Description: Specifies access control permissions for a file on a smart card.
ms.assetid: 995d959f-30dc-4e5c-be2d-6b447499415a
title: CARD\_FILE\_ACCESS\_CONDITION enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# CARD\_FILE\_ACCESS\_CONDITION enumeration

The **CARD\_FILE\_ACCESS\_CONDITION** enumeration specifies access control permissions for a file on a [*smart card*](security.s_gly#-security-smart-card-gly).

## Syntax


```C++
typedef enum  { 
  InvalidAc                 = 0,
  EveryoneReadUserWriteAc   = 1,
  UserWriteExecuteAc        = 2,
  EveryoneReadAdminWriteAc  = 3,
  UnknownAc                 = 4
} CARD_FILE_ACCESS_CONDITION;
```



## Constants

<dl> <dt>

<span id="InvalidAc"></span><span id="invalidac"></span><span id="INVALIDAC"></span>**InvalidAc**
</dt> <dd>

This value is not valid.

</dd> <dt>

<span id="EveryoneReadUserWriteAc"></span><span id="everyonereaduserwriteac"></span><span id="EVERYONEREADUSERWRITEAC"></span>**EveryoneReadUserWriteAc**
</dt> <dd>

Everyone can read the file. Specific users can write to the file.

</dd> <dt>

<span id="UserWriteExecuteAc"></span><span id="userwriteexecuteac"></span><span id="USERWRITEEXECUTEAC"></span>**UserWriteExecuteAc**
</dt> <dd>

Only specific users can read or write to the file.

</dd> <dt>

<span id="EveryoneReadAdminWriteAc"></span><span id="everyonereadadminwriteac"></span><span id="EVERYONEREADADMINWRITEAC"></span>**EveryoneReadAdminWriteAc**
</dt> <dd>

Everyone can read the file. Administrators can write to the file.

</dd> <dt>

<span id="UnknownAc"></span><span id="unknownac"></span><span id="UNKNOWNAC"></span>**UnknownAc**
</dt> <dd>

Access permissions for the file are unknown.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows XP \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2003, Windows Server 2003 \[desktop apps only\]<br/>            |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](https://msdn.microsoft.com/8d71e365-c581-4ec8-977b-0725a8c7d9ad)
</dt> <dt>

[**CARD\_FILE\_INFO**](https://msdn.microsoft.com/9acabc20-1de5-44ee-827f-08a8042e6f75)
</dt> <dt>

[**CardCreateFile**](https://msdn.microsoft.com/030a7102-0e5c-43c8-a0ef-3688655dc75d)
</dt> </dl>

 

 




