---
title: ActivityCollection DeleteItem method
description: Deletes an Activity from the ActivityCollection.
ms.assetid: 1F195F02-C069-4B9B-967B-9C36F0B156B0
keywords:
- DeleteItem method Access Execution Engine
- DeleteItem method Access Execution Engine , ActivityCollection interface
- ActivityCollection interface Access Execution Engine , DeleteItem method
topic_type:
- apiref
api_name:
- ActivityCollection.DeleteItem
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

# ActivityCollection::DeleteItem method

Deletes an [**Activity**](activity-struct.md) from the **ActivityCollection**.

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

The **Activity** identifier.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

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

 

 





