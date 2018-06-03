---
title: Activity SetAttributeID method
description: Sets the ID of the Activity.
ms.assetid: C370E963-C614-467C-83D3-F06AC9D1113C
keywords:
- SetAttributeID method Access Execution Engine
- SetAttributeID method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetAttributeID method
topic_type:
- apiref
api_name:
- Activity.SetAttributeID
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

# Activity::SetAttributeID method

Sets the ID of the **Activity**.

## Syntax


```C++
virtual HRESULT SetAttributeID(
  [in] LPCWSTR attributeID
) = 0;
```



## Parameters

<dl> <dt>

*attributeID* \[in\]
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

 

 





