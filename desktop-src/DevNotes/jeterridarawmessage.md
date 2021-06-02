---
description: Retrieves an unformatted message string when an error code identifier (IDA) is provided.
ms.assetid: 3869e0c0-b3ec-4409-b071-04fd793ebf93
title: JetErrIDARawMessage function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- JetErrIDARawMessage
api_type: 
- DllExport
api_location: 
- Msjter40.dll
---

# JetErrIDARawMessage function

Retrieves an unformatted message string when an error code identifier (IDA) is provided.

## Syntax


```C++
JET_ERR JetErrIDARawMessage(
   JETERR_IDA           Ida,
   WCHAR                *pMessage,
   unsigned long        cbMessage,
   unsigned long        *pcbActual,
   JETERR_HELPCONTEXTID *pContextId,
   WCHAR                **pwszHelp/file
);
```



## Parameters

<dl> <dt>

*Ida* 
</dt> <dd>

A number that maps to a specific error code and is displayed to the user.

</dd> <dt>

*pMessage* 
</dt> <dd>

A pointer to the error message.

</dd> <dt>

*cbMessage* 
</dt> <dd>

A count of the number of bytes in the error message.

</dd> <dt>

*pcbActual* 
</dt> <dd>

A pointer to the actual number of bytes read.

</dd> <dt>

*pContextId* 
</dt> <dd>

A pointer to the context identifier that is associated with the help file.

</dd> <dt>

*pwszHelp/file* 
</dt> <dd>

A pointer to a pointer to the file that explains the error.

</dd> </dl>

## Return value

If the function succeeds, it returns **JET\_errSuccess**; otherwise, it returns an unformatted message that indicates the specific reason for failure.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msjter40.dll</dt> </dl> |



 

 
