---
title: LinkCollection GetItem method
description: Returns a Link from the LinkCollection.
ms.assetid: BB5F4BE4-D6EA-4685-9FF8-DC6B8542DD91
keywords:
- GetItem method Access Execution Engine
- GetItem method Access Execution Engine , LinkCollection interface
- LinkCollection interface Access Execution Engine , GetItem method
topic_type:
- apiref
api_name:
- LinkCollection.GetItem
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

# LinkCollection::GetItem method

Returns a [**Link**](link-struct.md) from the **LinkCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT  index,
  [out] Link **link
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **Link** identifier.

</dd> <dt>

*link* \[out\]
</dt> <dd>

The link.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

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

 

 





