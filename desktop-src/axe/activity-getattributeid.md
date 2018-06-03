---
title: Activity GetAttributeID method
description: Returns the ID of the Activity.
ms.assetid: 5348C851-DC14-450E-AE83-133CC0DE0BE1
keywords:
- GetAttributeID method Access Execution Engine
- GetAttributeID method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetAttributeID method
topic_type:
- apiref
api_name:
- Activity.GetAttributeID
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

# Activity::GetAttributeID method

Returns the **ID** of the **Activity**.

## Syntax


```C++
virtual HRESULT GetAttributeID(
  [out] LPCWSTR *attributeID
) const = 0;
```



## Parameters

<dl> <dt>

*attributeID* \[out\]
</dt> <dd>

The ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The ID is the value of attribute **ID** of element **Activity**.

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

 

 





