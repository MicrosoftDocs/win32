---
Description: Gets an enumerator object that can be used in turn to enumerate the protected storage providers that are currently installed on the system.
ms.assetid: df162086-caeb-427f-9db8-9722855cfbbf
title: PStoreEnumProviders function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PStoreEnumProviders function

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/windows/desktop/765a68fd-f105-49fc-a738-4a8129eb0770) and [**CryptUnprotectData**](https://msdn.microsoft.com/windows/desktop/54eab3b0-d341-47c6-9c32-79328d7a7155) functions.\]

Gets an enumerator object that can be used in turn to enumerate the protected storage providers that are currently installed on the system.

## Syntax


```C++
HRESULT PStoreEnumProviders(
   DWORD                dwFlags,
   IEnumPStoreProviders **ppenum
);
```



## Parameters

<dl> <dt>

*dwFlags* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> <dt>

*ppenum* 
</dt> <dd>

A pointer to a pointer to an [**IEnumPStoreProviders**](ienumpstoreproviders.md) interface that can be used to enumerate installed providers.

</dd> </dl>

## Return value

This function returns an **HRESULT**.

## Remarks

The protected storage component has a provider-based architecture. Applications that make use of protected storage can specify which of the installed providers to use when storing and retrieving their data.

The **PStoreEnumProviders** function is used to enumerate the installed protected storage providers. Each provider is identified by a globally unique identifier (GUID).

Up to this time, only one protected storage provider has ever been written. Given that the protected storage service is currently deprecated, it is very unlikely that any additional providers will ever be produced. As a result, this function should not be used for any purpose.

This function has no associated import library; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumPStoreProviders**](ienumpstoreproviders.md)
</dt> </dl>

 

 




