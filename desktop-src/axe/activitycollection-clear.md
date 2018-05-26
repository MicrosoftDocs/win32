---
title: ActivityCollection Clear method
description: Deletes all Activity objects from the ActivityCollection.
ms.assetid: D8D9C9D2-8A94-4226-B617-8481661637E3
keywords:
- Clear method Access Execution Engine
- Clear method Access Execution Engine , ActivityCollection interface
- ActivityCollection interface Access Execution Engine , Clear method
topic_type:
- apiref
api_name:
- ActivityCollection.Clear
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

# ActivityCollection::Clear method

Deletes all [**Activity**](activity-struct.md) objects from the **ActivityCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

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

 

 





