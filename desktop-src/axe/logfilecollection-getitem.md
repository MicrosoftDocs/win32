---
title: LogFileCollection GetItem method
description: Returns the file path of a log file in the collection.
ms.assetid: '08E706BA-62EA-4DC3-A09A-B7129712C507'
keywords: ["GetItem method Access Execution Engine", "GetItem method Access Execution Engine , LogFileCollection interface", "LogFileCollection interface Access Execution Engine , GetItem method"]
topic_type:
- apiref
api_name:
- LogFileCollection.GetItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# LogFileCollection::GetItem method

Returns the file path of a log file in the collection.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT     index,
  [out] LPCWSTR *filePath
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The identifier of the log file.

</dd> <dt>

*filePath* \[out\]
</dt> <dd>

The file path.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

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

 

 





