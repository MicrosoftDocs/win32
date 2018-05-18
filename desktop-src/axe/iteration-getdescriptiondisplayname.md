---
title: Iteration GetDescriptionDisplayName method
description: Returns the description display name of the Iteration.
ms.assetid: '0103E615-C089-43BE-B935-5E495F996AA5'
keywords: ["GetDescriptionDisplayName method Access Execution Engine", "GetDescriptionDisplayName method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , GetDescriptionDisplayName method"]
topic_type:
- apiref
api_name:
- Iteration.GetDescriptionDisplayName
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::GetDescriptionDisplayName method

Returns the description display name of the **Iteration**.

## Syntax


```C++
virtual HRESULT GetDescriptionDisplayName(
  [out] LPCWSTR *descriptionDisplayName
) const = 0;
```



## Parameters

<dl> <dt>

*descriptionDisplayName* \[out\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





