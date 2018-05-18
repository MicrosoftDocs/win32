---
title: Iteration GetActivities method
description: Returns the ActivityCollection for the Iteration.
ms.assetid: '15A4CE6A-6A30-4DB5-BFD7-CB2C4630C666'
keywords: ["GetActivities method Access Execution Engine", "GetActivities method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , GetActivities method"]
topic_type:
- apiref
api_name:
- Iteration.GetActivities
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::GetActivities method

Returns the [**ActivityCollection**](activitycollection.md) for the **Iteration**.

## Syntax


```C++
virtual HRESULT GetActivities(
  [out] ActivityCollection **activities
) = 0;
```



## Parameters

<dl> <dt>

*activities* \[out\]
</dt> <dd>

The **ActivityCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **ActivityCollection** holds information from element **Iteration/Activities**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





