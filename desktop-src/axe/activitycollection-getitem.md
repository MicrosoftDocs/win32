---
title: ActivityCollection GetItem method
description: Returns an Activity from the ActivityCollection.
ms.assetid: E583AC3B-627B-490A-A2D3-DA295B6F31F1
keywords:
- GetItem method Access Execution Engine
- GetItem method Access Execution Engine , ActivityCollection interface
- ActivityCollection interface Access Execution Engine , GetItem method
topic_type:
- apiref
api_name:
- ActivityCollection.GetItem
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

# ActivityCollection::GetItem method

Returns an [**Activity**](activity-struct.md) from the **ActivityCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT      index,
  [out] Activity **activity
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **Activity** identifier.

</dd> <dt>

*activity* \[out\]
</dt> <dd>

The **Activity**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

The **ActivityCollection** holds data from element **Iteration/Activities**.

The **Activity** objects hold data from **Activities/Activity** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ActivityCollection**](activitycollection.md)
</dt> </dl>

 

 





