---
title: ActivityReference GetAttributeActivityID method
description: Returns the activity ID of the ActivityReference.
ms.assetid: 677D4CF9-84CA-4F36-B0AB-9521306B3DED
keywords:
- GetAttributeActivityID method Access Execution Engine
- GetAttributeActivityID method Access Execution Engine , ActivityReference interface
- ActivityReference interface Access Execution Engine , GetAttributeActivityID method
topic_type:
- apiref
api_name:
- ActivityReference.GetAttributeActivityID
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

# ActivityReference::GetAttributeActivityID method

Returns the activity ID of the **ActivityReference**.

## Syntax


```C++
virtual HRESULT GetAttributeActivityID(
  [out] LPCWSTR *attributeActivityID
) const = 0;
```



## Parameters

<dl> <dt>

*attributeActivityID* \[out\]
</dt> <dd>

The activity ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

An **ActivityReference** holds data from an **Issue/Impact/RelatedActivities/ActivityReference** element.

The activity ID is the value of attribute **ActivityID** of element **ActivityReference**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ActivityReference**](activityreference-struct.md)
</dt> </dl>

 

 





