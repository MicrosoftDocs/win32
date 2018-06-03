---
title: LinkCollection DeleteItem method
description: Deletes a Link from the LinkCollection.
ms.assetid: 3B366F9E-F9DF-4913-AF19-4803ED1F0168
keywords:
- DeleteItem method Access Execution Engine
- DeleteItem method Access Execution Engine , LinkCollection interface
- LinkCollection interface Access Execution Engine , DeleteItem method
topic_type:
- apiref
api_name:
- LinkCollection.DeleteItem
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

# LinkCollection::DeleteItem method

Deletes a [**Link**](link-struct.md) from the **LinkCollection**.

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

The **Link** identifier.

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

 

 





