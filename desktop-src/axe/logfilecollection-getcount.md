---
title: LogFileCollection GetCount method
description: Gets the count of log files in the collection.
ms.assetid: BEC648B0-EA2B-48EE-ABCD-9A28716C5507
keywords:
- GetCount method Access Execution Engine
- GetCount method Access Execution Engine , LogFileCollection interface
- LogFileCollection interface Access Execution Engine , GetCount method
topic_type:
- apiref
api_name:
- LogFileCollection.GetCount
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

# LogFileCollection::GetCount method

Gets the count of log files in the collection.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
) const = 0;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

The log file count returned by this method.

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

 

 





