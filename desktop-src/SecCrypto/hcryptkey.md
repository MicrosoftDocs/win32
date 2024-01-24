---
description: The HCRYPTKEY data type is used to represent handles to cryptographic keys.
ms.assetid: d62f1d40-4f42-4684-96d7-de88db67dceb
title: HCRYPTKEY (Wincrypt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# HCRYPTKEY

The **HCRYPTKEY** data type is used to represent handles to [*cryptographic keys*](../secgloss/c-gly.md). These handles are used to indicate to the CSP module which key is being used in a specific operation. The CSP module does not enable direct access to the key values. Instead, the user performs functions by using the key value through the key handle.


```C++
typedef ULONG_PTR HCRYPTKEY;
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



 

 
