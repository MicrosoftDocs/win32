---
title: LogFileCollection DeleteItem method
description: Deletes a log file from the collection.
ms.assetid: BAE50F09-BAD1-4DC1-8F7C-4F0A6761F221
keywords:
- DeleteItem method Access Execution Engine
- DeleteItem method Access Execution Engine , LogFileCollection interface
- LogFileCollection interface Access Execution Engine , DeleteItem method
topic_type:
- apiref
api_name:
- LogFileCollection.DeleteItem
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LogFileCollection::DeleteItem method

Deletes a log file from the collection.

## Syntax


```C++
virtual HRESULT DeleteItem(
  [in] INT index
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The identifier of the log file.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**LogFileCollection**](logfilecollection.md)
</dt> </dl>

 

 





