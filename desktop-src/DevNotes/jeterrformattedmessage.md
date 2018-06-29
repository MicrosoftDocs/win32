---
Description: Retrieves an error code identifier (IDA) and creates the final display string when a Jet error and extended error information is provided.
ms.assetid: 961da4fb-cb70-4f3d-a4a4-1774be7a05f4
title: JetErrFormattedMessage function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- JetErrFormattedMessage
api_type: 
- DllExport
api_location: 
- Msjter40.dll
---

# JetErrFormattedMessage function

Retrieves an error code identifier (IDA) and creates the final display string when a Jet error and extended error information is provided.

## Syntax


```C++
JET_ERR JetErrFormattedMessage(
   JET_ERR              err,
   JETERR_EXTERR        *pExtendedErrorInfo,
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

The Jet error number that is used to look up and format the displayable error message.

</dd> <dt>

*pExtendedErrorInfo* 
</dt> <dd>

All Jet error information including the database name, the table name, and any minor error information.

</dd> <dt>

*pIda* 
</dt> <dd>

A pointer to the IDA that is associated with the specific error code.

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

If the function succeeds, it returns **JET\_errSuccess**; otherwise, it returns a formatted error message that indicates the specific reason for failure.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msjter40.dll</dt> </dl> |



 

 




