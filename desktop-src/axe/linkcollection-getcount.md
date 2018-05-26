---
title: LinkCollection GetCount method
description: Returns the count of Link objects in the LinkCollection.
ms.assetid: 097405BB-1440-4142-9FF6-9ECF4203D5DC
keywords:
- GetCount method Access Execution Engine
- GetCount method Access Execution Engine , LinkCollection interface
- LinkCollection interface Access Execution Engine , GetCount method
topic_type:
- apiref
api_name:
- LinkCollection.GetCount
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LinkCollection::GetCount method

Returns the count of [**Link**](link-struct.md) objects in the **LinkCollection**.

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

The count.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **LinkCollection** holds data from an **Issue/Solution/Links** or **Issue/AnalysisLinks** element.

A **Link** holds data from a **Links/Link** or **AnalysisLinks/Link** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**LinkCollection**](linkcollection.md)
</dt> </dl>

 

 





