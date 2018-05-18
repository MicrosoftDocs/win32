---
title: ResultSnippet Save method
description: Saves this ResultSnippet object to a file.
ms.assetid: '8DF37238-41B9-4F86-A3D1-553329FC4474'
keywords: ["Save method Access Execution Engine", "Save method Access Execution Engine , ResultSnippet interface", "ResultSnippet interface Access Execution Engine , Save method"]
topic_type:
- apiref
api_name:
- ResultSnippet.Save
api_location:
- AxeCore.dll
api_type:
- COM
---

# ResultSnippet::Save method

Saves this [**ResultSnippet**](resultsnippet.md) object to a file.

## Syntax


```C++
virtual HRESULT Save(
   LPCWSTR filePath
) = 0;
```



## Parameters

<dl> <dt>

*filePath* 
</dt> <dd>

The file path.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ResultSnippet**](resultsnippet.md)
</dt> </dl>

 

 





