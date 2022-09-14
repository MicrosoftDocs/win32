---
description: 'The LSA\_ENUMERATION\_HANDLE data type is used by the LSA function that enumerates TrustedDomain objects: LsaEnumerateTrustedDomainsEx.'
ms.assetid: 99dad3aa-cb92-4b7e-8a18-2c977cb2737c
title: LSA_ENUMERATION_HANDLE (Ntsecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LSA\_ENUMERATION\_HANDLE

The **LSA\_ENUMERATION\_HANDLE** data type is used by the LSA function that enumerates [**TrustedDomain**](trusteddomain-object.md) objects: [**LsaEnumerateTrustedDomainsEx**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaenumeratetrusteddomainsex). This function is designed so that you can make multiple calls to enumerate all the objects of a given type in the database.

On the initial enumeration function call, you pass in a pointer to an **LSA\_ENUMERATION\_HANDLE** variable that is initialized to zero. The function updates this value. If the function returns a value that indicates there are more objects to enumerate, call the function again and pass in the updated **LSA\_ENUMERATION\_HANDLE** value to obtain an enumeration continuing from the point where the previous enumeration left off.


```C++
typedef ULONG LSA_ENUMERATION_HANDLE, *PLSA_ENUMERATION_HANDLE;
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Ntsecapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LsaEnumerateTrustedDomainsEx**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaenumeratetrusteddomainsex)
</dt> </dl>

 

 




