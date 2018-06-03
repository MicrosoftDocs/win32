---
title: ErrorWarningCollection GetCount method
description: Provides the count of the items in the collection.
ms.assetid: AA51D629-0FF0-412F-B49E-83242646E6EA
keywords:
- GetCount method Access Execution Engine
- GetCount method Access Execution Engine , ErrorWarningCollection interface
- ErrorWarningCollection interface Access Execution Engine , GetCount method
topic_type:
- apiref
api_name:
- ErrorWarningCollection.GetCount
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

# ErrorWarningCollection::GetCount method

Provides the count of the items in the collection.

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

A variable to receive the count.

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

[**ErrorWarningCollection**](errorwarningcollection.md)
</dt> </dl>

 

 





