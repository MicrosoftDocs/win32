---
description: Retrieves basic attributes for the specified file object.
ms.assetid: 19f9a2ac-4db6-4c67-9f85-c107063e11b8
title: NtQueryAttributesFile function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtQueryAttributesFile
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# NtQueryAttributesFile function

\[This function may be changed or removed from Windows without further notice.\]

Retrieves basic attributes for the specified file object.

## Syntax


```C++
NTSTATUS NtQueryAttributesFile(
  _In_  POBJECT_ATTRIBUTES      ObjectAttributes,
  _Out_ PFILE_BASIC_INFORMATION FileInformation
);
```



## Parameters

<dl> <dt>

*ObjectAttributes* \[in\]
</dt> <dd>

A pointer to an [OBJECT\_ATTRIBUTES](https://msdn.microsoft.com/library/aa491657.aspx) structure that supplies the attributes to be used for the file object.

</dd> <dt>

*FileInformation* \[out\]
</dt> <dd>

A pointer to a [FILE\_BASIC\_INFORMATION](https://msdn.microsoft.com/library/aa491634.aspx) structure to receive the returned file attribute information.

</dd> </dl>

## Return value

Returns an NTSTATUS or error code.

The forms and significance of NTSTATUS error codes are listed in the Ntstatus.h header file available in the WDK, and are described in the WDK documentation.

## Remarks

This function has no associated header file. The associated import library, Ntdll.lib, is available in the WDK. You can also use the [**LoadLibrary**](-loadlibrary.md) and [**GetProcAddress**](-getprocaddress-.md) functions to dynamically link to Ntdll.dll.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 




