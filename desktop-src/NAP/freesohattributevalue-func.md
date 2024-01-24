---
title: FreeSoHAttributeValue function (NapUtil.h)
description: Frees an SoHAttributeValue data structure.
ms.assetid: 21647ee6-2ea2-45fd-b1f2-fb1836196f94
keywords:
- FreeSoHAttributeValue function NAP
topic_type:
- apiref
api_name:
- FreeSoHAttributeValue
api_location:
- qutil.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# FreeSoHAttributeValue function

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **FreeSoHAttributeValue** function frees an [**SoHAttributeValue**](sohattributevalue-union.md) data structure.

## Syntax


```C++
NAPAPI VOID WINAPI FreeSoHAttributeValue(
  _In_ SoHAttributeType  type,
  _In_ SoHAttributeValue *value
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

A [**SoHAttributeType**](sohattributetype-enum.md) value that specifies the type of SoH attribute value to free.

</dd> <dt>

*value* \[in\]
</dt> <dd>

A pointer to the [**SoHAttributeValue**](sohattributevalue-union.md) to free.

</dd> </dl>

## Remarks

All the COM interfaces supported by the NAP system use standard COM memory management rules and the COM memory allocators (**CoTaskMemAlloc** and **CoTaskMemFree**):

-   **In** parameters are allocated and freed by the caller.
-   **Out** parameters are allocated by the callee and freed by the caller using **CoTaskMem**.
-   **In/out** parameters are allocated by the caller, freed and reallocated by the callee, and ultimately freed by the caller, using **CoTaskMem**.

All NAP functions for freeing memory also free all embedded pointers.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>NapUtil.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qutil.dll</dt> </dl> |



 

 





