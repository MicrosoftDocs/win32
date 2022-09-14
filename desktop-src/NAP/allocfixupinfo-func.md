---
title: AllocFixupInfo function (NapUtil.h)
description: Allocates memory for a FixupInfo structure of the specified size.
ms.assetid: e0b66a08-9714-4451-a22d-3822153c6a36
keywords:
- AllocFixupInfo function NAP
topic_type:
- apiref
api_name:
- AllocFixupInfo
api_location:
- qutil.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# AllocFixupInfo function

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **AllocFixupInfo** function allocates memory for a [**FixupInfo**](/windows/win32/api/naptypes/ns-naptypes-fixupinfo) structure of the specified size.

## Syntax


```C++
NAPAPI HRESULT WINAPI AllocFixupInfo(
  _Inout_ FixupInfo **fixupInfo,
  _In_    UINT16    countResultCodes
);
```



## Parameters

<dl> <dt>

*fixupInfo* \[in, out\]
</dt> <dd>

A pointer to the address of a newly allocated [**FixupInfo**](/windows/win32/api/naptypes/ns-naptypes-fixupinfo) structure.

</dd> <dt>

*countResultCodes* \[in\]
</dt> <dd>

The number of result codes to allocate to *fixupInfo*.

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

[**FreeFixupInfo**](freefixupinfo-func.md)
</dt> </dl>

 

 





