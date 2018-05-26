---
title: Activity GetReferences method
description: Returns the ReferenceCollection of the Activity.
ms.assetid: BBB8A867-D1D3-4769-89AB-9524449CD2D5
keywords:
- GetReferences method Access Execution Engine
- GetReferences method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetReferences method
topic_type:
- apiref
api_name:
- Activity.GetReferences
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

# Activity::GetReferences method

Returns the [**ReferenceCollection**](referencecollection.md) of the **Activity**.

## Syntax


```C++
virtual HRESULT GetReferences(
  [out] ReferenceCollection **references
) = 0;
```



## Parameters

<dl> <dt>

*references* \[out\]
</dt> <dd>

The **ReferenceCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The **ReferenceCollection** holds data from element **Activity/References**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





