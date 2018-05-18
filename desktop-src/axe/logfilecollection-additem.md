---
title: LogFileCollection AddItem method
description: Adds a log file to the collection.
ms.assetid: 'A594A530-4E17-4D40-A1A9-27708E9F3506'
keywords: ["AddItem method Access Execution Engine", "AddItem method Access Execution Engine , LogFileCollection interface", "LogFileCollection interface Access Execution Engine , AddItem method"]
topic_type:
- apiref
api_name:
- LogFileCollection.AddItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# LogFileCollection::AddItem method

Adds a log file to the collection.

## Syntax


```C++
virtual HRESULT AddItem(
  [in] LPCWSTR filePath
) = 0;
```



## Parameters

<dl> <dt>

*filePath* \[in\]
</dt> <dd>

The file path of the log file to add.

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

[**LogFileCollection**](logfilecollection.md)
</dt> </dl>

 

 





