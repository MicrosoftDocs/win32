---
Description: Writes the access rules for the given type.
ms.assetid: d5cfd782-8d87-45ae-a574-0a294a30ca71
title: IPStore::WriteAccessRuleset method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPStore::WriteAccessRuleset method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/765a68fd-f105-49fc-a738-4a8129eb0770) and [**CryptUnprotectData**](https://msdn.microsoft.com/54eab3b0-d341-47c6-9c32-79328d7a7155) functions.\]

\[This method is not implemented.\]

Writes the access rules for the given type.

## Syntax


```C++
HRESULT WriteAccessRuleset(
  [in]       PST_KEY            Key,
  [in] const GUID               *pType,
  [in] const GUID               *pSubtype,
  [in]       PPST_TYPEINFO      pInfo,
  [in]       PPST_ACCESSRULESET pRules,
  [in]       DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*pType* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*pSubtype* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*pInfo* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*pRules* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved.

</dd> </dl>

## Return value

Calls to this method will always fail.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



## See also

<dl> <dt>

[**IPStore**](ipstore.md)
</dt> </dl>

 

 




