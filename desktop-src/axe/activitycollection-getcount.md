---
title: ActivityCollection GetCount method
description: Returns the count of Activity objects in the ActivityCollection.
ms.assetid: '02159778-9F17-4796-B7B6-D4EC49A0C3CF'
keywords: ["GetCount method Access Execution Engine", "GetCount method Access Execution Engine , ActivityCollection interface", "ActivityCollection interface Access Execution Engine , GetCount method"]
topic_type:
- apiref
api_name:
- ActivityCollection.GetCount
api_location:
- AxeCore.dll
api_type:
- COM
---

# ActivityCollection::GetCount method

Returns the count of [**Activity**](activity-struct.md) objects in the **ActivityCollection**.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
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

The **ActivityCollection** holds data from element **Iteration/Activities**.

The **Activity** objects hold data from **Activities/Activity** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ActivityCollection**](activitycollection.md)
</dt> </dl>

 

 





