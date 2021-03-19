---
description: Opens a handle to a thread object with the access specified.
ms.assetid: 85148f27-cfb4-4a33-8bcc-e48d2c2e3c51
title: NtOpenThread function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtOpenThread
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# NtOpenThread function

\[This function may be changed or removed from Windows without further notice. Use the [**OpenThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthread) function instead.\]

Opens a handle to a thread object with the access specified.

## Syntax


```C++
NTSTATUS NtOpenThread(
  _Out_ PHANDLE            ThreadHandle,
  _In_  ACCESS_MASK        DesiredAccess,
  _In_  POBJECT_ATTRIBUTES ObjectAttributes,
  _In_  PCLIENT_ID         ClientId
);
```



## Parameters

<dl> <dt>

*ThreadHandle* \[out\]
</dt> <dd>

A pointer to a variable that receives the thread object handle.

</dd> <dt>

*DesiredAccess* \[in\]
</dt> <dd>

An [**ACCESS\_MASK**](../secauthz/access-mask-format.md) data type that provides the desired types of access for the thread object.

</dd> <dt>

*ObjectAttributes* \[in\]
</dt> <dd>

A pointer to an [OBJECT\_ATTRIBUTES](https://msdn.microsoft.com/library/aa491657.aspx) structure. The **ObjectName** member of this structure must be NULL.

**Windows Server 2003 and Windows XP:** The **ObjectName** member of this structure can point to an object name. If **ObjectName** is not NULL, the *ClientId* parameter must be NULL.

</dd> <dt>

*ClientId* \[in\]
</dt> <dd>

A pointer to a **CLIENT\_ID** structure that identifies the thread whose thread is to be opened.

**Windows Server 2003 and Windows XP:** A pointer to a **CLIENT\_ID** structure that identifies the thread whose thread is to be opened. This parameter can be NULL. If this parameter is not NULL, the **ObjectName** member of the structure pointed to by the *ObjectAttributes* parameter must be NULL.

</dd> </dl>

## Return value

Returns an **NTSTATUS** or error code.

The forms and significance of **NTSTATUS** error codes are listed in the Ntstatus.h header file available in the WDK, and are described in the WDK documentation.

## Remarks

This function has no associated header file. The associated import library, Ntdll.lib is available in the WDK. You can also use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Ntdll.dll.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 
