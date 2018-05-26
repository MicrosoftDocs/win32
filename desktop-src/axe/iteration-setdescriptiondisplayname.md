---
title: Iteration SetDescriptionDisplayName method
description: Sets the description display name of the Iteration.
ms.assetid: DC1C0E54-5D77-4663-9FA3-B1A3590158F8
keywords:
- SetDescriptionDisplayName method Access Execution Engine
- SetDescriptionDisplayName method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , SetDescriptionDisplayName method
topic_type:
- apiref
api_name:
- Iteration.SetDescriptionDisplayName
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

# Iteration::SetDescriptionDisplayName method

Sets the description display name of the **Iteration**.

## Syntax


```C++
virtual HRESULT SetDescriptionDisplayName(
  [in] LPCWSTR descriptionDisplayName
) = 0;
```



## Parameters

<dl> <dt>

*descriptionDisplayName* \[in\]
</dt> <dd>

The description display name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The description display name is the value of element **Iteration/Description/DisplayName**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





