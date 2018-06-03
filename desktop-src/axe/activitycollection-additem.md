---
title: ActivityCollection AddItem method
description: Creates an Activity and adds it to the ActivityCollection.
ms.assetid: 50C570F4-2C54-4D65-9312-AEDA87CD8ABC
keywords:
- AddItem method Access Execution Engine
- AddItem method Access Execution Engine , ActivityCollection interface
- ActivityCollection interface Access Execution Engine , AddItem method
topic_type:
- apiref
api_name:
- ActivityCollection.AddItem
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

# ActivityCollection::AddItem method

Creates an [**Activity**](activity-struct.md) and adds it to the **ActivityCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [out] Activity **activity
) = 0;
```



## Parameters

<dl> <dt>

*activity* \[out\]
</dt> <dd>

The **Activity** that this method creates.

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

 

 





