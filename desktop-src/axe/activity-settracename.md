---
title: Activity SetTraceName method
description: Sets the trace name of the Activity.
ms.assetid: 'AB7CE95C-D1D5-467E-9F64-026DAF009871'
keywords: ["SetTraceName method Access Execution Engine", "SetTraceName method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , SetTraceName method"]
topic_type:
- apiref
api_name:
- Activity.SetTraceName
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::SetTraceName method

Sets the trace name of the **Activity**.

## Syntax


```C++
virtual HRESULT SetTraceName(
  [in] LPCWSTR traceName
) = 0;
```



## Parameters

<dl> <dt>

*traceName* \[in\]
</dt> <dd>

The trace name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The trace name is the value of element **Activity/Trace/Description/Name**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





