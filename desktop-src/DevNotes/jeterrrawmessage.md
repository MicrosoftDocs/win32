---
description: Retrieves an error code identifier (IDA) and an unformatted message string when a Jet error is provided.
ms.assetid: f90b6986-a8d5-430e-94b3-176012c7e282
title: JetErrRawMessage function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- JetErrRawMessage
api_type: 
- DllExport
api_location: 
- Msjter40.dll
---

# JetErrRawMessage function

Retrieves an error code identifier (IDA) and an unformatted message string when a Jet error is provided.

## Syntax


```C++
JET_ERR JetErrRawMessage(
   JET_ERR              err,
   JETERR_IDA           *pIda,
   WCHAR                *pMessage,
   unsigned long        cbMessage,
   unsigned long        *pcbActual,
   JETERR_HELPCONTEXTID *pContextId,
   WCHAR                **pwszHelp/file
);
```



## Parameters

<dl> <dt>

*err* 
</dt> <dd>

The Jet error that corresponds to the information being obtained.

</dd> <dt>

*pIda* 
</dt> <dd>

A pointer to the IDA.

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

Points to a pointer to the file that explains the error.

</dd> </dl>

## Return value

If the function succeeds, it returns **JET\_errSuccess**; otherwise, it returns an unformatted error message that indicates the specific reason for failure.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msjter40.dll</dt> </dl> |



 

 
