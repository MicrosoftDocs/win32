---
Description: Initializes a string table.
ms.assetid: 184df85a-6d59-42c5-8ec1-f0c046091645
title: pSetupStringTableInitializeEx function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pSetupStringTableInitializeEx
api_type: 
- DllExport
api_location: 
- Setupapi.dll
---

# pSetupStringTableInitializeEx function

\[This function is not available in Windows Vista or Windows Server 2008.\]

Initializes a string table.

## Syntax


```C++
PVOID pSetupStringTableInitializeEx(
  _In_ UINT ExtraDataSize,
  _In_ UINT Reserved
);
```



## Parameters

<dl> <dt>

*ExtraDataSize* \[in\]
</dt> <dd>

Size of extra data object.

</dd> <dt>

*Reserved* \[in\]
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 




