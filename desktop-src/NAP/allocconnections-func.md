---
title: AllocConnections function (NapUtil.h)
description: Allocates memory for a specified number of Connections structures.
ms.assetid: 0e0075ed-6e4c-43f7-af40-c6dea2808d05
keywords:
- AllocConnections function NAP
topic_type:
- apiref
api_name:
- AllocConnections
api_location:
- qutil.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# AllocConnections function

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **AllocConnections** function allocates memory for a specified number of [**Connections**](connections-struct.md) structures.

## Syntax


```C++
NAPAPI HRESULT WINAPI AllocConnections(
  _Inout_ Connections **connections,
  _In_    UINT16      connectionsCount
);
```



## Parameters

<dl> <dt>

*connections* \[in, out\]
</dt> <dd>

A pointer to an array of newly allocated [**Connections**](connections-struct.md) structures.

</dd> <dt>

*connectionsCount* \[in\]
</dt> <dd>

The number of structures to allocate to *connections*.

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

[**FreeConnections**](freeconnections-func.md)
</dt> </dl>

 

 





