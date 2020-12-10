---
title: AllocCountedString function (NapUtil.h)
description: Allocates memory for a null-terminated string and returns it in a CountedString structure.
ms.assetid: 6dd503bf-8853-499b-adcd-54de696f01d6
keywords:
- AllocCountedString function NAP
topic_type:
- apiref
api_name:
- AllocCountedString
api_location:
- qutil.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# AllocCountedString function

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **AllocCountedString** function allocates memory for a null-terminated string and returns it in a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure.

## Syntax


```C++
NAPAPI HRESULT WINAPI AllocCountedString(
  _Inout_       CountedString **countedString,
  _In_    const WCHAR         *string
);
```



## Parameters

<dl> <dt>

*countedString* \[in, out\]
</dt> <dd>

A pointer to the address of a newly allocated [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure.

</dd> <dt>

*string* \[in\]
</dt> <dd>

A pointer to the null-terminated string that is to be returned in *countedString*.

</dd> </dl>

## Return value



| Return code                                                                                   | Description                                                                |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The operation has completed successfully.<br/>                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | An invalid argument was passed.<br/>                                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The system is out of virtual memory. This operation has failed.<br/> |



 

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



## See also

<dl> <dt>

[**FreeCountedString**](freecountedstring-func.md)
</dt> </dl>

 

 





