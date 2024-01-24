---
description: Creates a user profile for a specified user.
ms.assetid: e4ea4032-d8d3-45c1-b2e5-7fef52a8a869
title: CreateUserProfileEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreateUserProfileEx
- CreateUserProfileExA
- CreateUserProfileExW
api_type: 
- DllExport
api_location: 
- Userenv.dll
---

# CreateUserProfileEx function

\[This function is not available as of Windows Vista.\]

Creates a user profile for a specified user.

## Syntax


```C++
BOOL WINAPI CreateUserProfileEx(
  _In_      PSID    pSid,
  _In_      LPCTSTR lpUserName,
  _In_opt_  LPCTSTR lpUserHive,
  _Out_opt_ LPTSTR  lpProfileDir,
  _In_      DWORD   dwDirSize,
  _In_      BOOL    bWin9xUpg
);
```



## Parameters

<dl> <dt>

*pSid* \[in\]
</dt> <dd>

Type: **PSID**

The SID of the new user.

</dd> <dt>

*lpUserName* \[in\]
</dt> <dd>

Type: **LPCTSTR**

Pointer to a buffer that contains the user name of the new user.

</dd> <dt>

*lpUserHive* \[in, optional\]
</dt> <dd>

Type: **LPCTSTR**

Pointer to a buffer that contains the [registry hive](../sysinfo/registry-hives.md) to use. This parameter can be **NULL**.

</dd> <dt>

*lpProfileDir* \[out, optional\]
</dt> <dd>

Type: **LPTSTR**

Pointer to a buffer that, when this function returns, receives the user's profile directory path. This parameter can be **NULL**.

</dd> <dt>

*dwDirSize* \[in\]
</dt> <dd>

Type: **DWORD**

Size of the buffer specified by *lpProfileDir*, in TCHARs.

</dd> <dt>

*bWin9xUpg* \[in\]
</dt> <dd>

Type: **BOOL**

**TRUE** if the user profile is being created as part of a profile migration from Windows 9x; otherwise, **FALSE**.

When **TRUE**, the user profile is set up in the default profile directory—normally C:\\Documents and Settings\\*UserName*. If that directory already exists, it is used. If it does not, it is created.

If **FALSE**, the default profile directory is created if it does not exist. If the default profile directory already exists, a new directory is created for this user profile.

</dd> </dl>

## Return value

Type: **BOOL**

Returns **TRUE** if the new user profile was created successfully; otherwise, **FALSE**.

## Remarks

This function is not declared in the software development kit (SDK) headers and has no associated import library. You must use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to link to Userenv.dll. The ANSI version of the function, **CreateUserProfileExA** is referenced from Userenv.dll as ordinal 153. The Unicode version, **CreateUserProfileExW** is referenced as ordinal 154.

## Requirements



| Requirement | Value |
|-----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/>  | Windows XP<br/>                                                                  |
| DLL<br/>                    | <dl> <dt>Userenv.dll</dt> </dl> |
| Unicode and ANSI names<br/> | **CreateUserProfileExW** (Unicode) and **CreateUserProfileExA** (ANSI)<br/>      |



 

 
