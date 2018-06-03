---
title: AxeInitAssessment function
description: Initializes the assessment portion of the AXE core and instantiates the Support interface in C++.
ms.assetid: 35261115-4740-4B3B-B9B8-0AA4F219596B
keywords:
- AxeInitAssessment function Access Execution Engine
topic_type:
- apiref
api_name:
- AxeInitAssessment
api_location:
- AxeCore.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AxeInitAssessment function

Initializes the assessment portion of the AXE core and instantiates the [**Support**](support.md) interface in C++.

## Syntax


```C++
HRESULT WINAPI AxeInitAssessment(
  _Inout_opt_ LPVOID                                  pReserved,
  _Out_       Microsoft::Assessment::Runtime::Support **ppSupport
);
```



## Parameters

<dl> <dt>

*pReserved* \[in, out, optional\]
</dt> <dd>

This optional parameter is reserved.

</dd> <dt>

*ppSupport* \[out\]
</dt> <dd>

A double pointer to receive the instantiated [**Support**](support.md) pointer.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**.

If AXE assessment support has been initialized and the single object is already in use, the return value is **AXE\_E\_ALREADY\_INIT**.

If AXE assessment support could not be initialized, the return value is **AXE\_E\_INIT\_FAILED**.

If *ppSupport* is **NULL**, the return value is **E\_POINTER**.

## Remarks

This function is supported on Windows 7, Windows Server 2008 R2, Windows 8, and Windows Server 2012.

This function provides the solution with the primary interface or object in the AXE support. It increments the reference count on the [**Support**](support.md) interface before returning the interface or object to the assessment.

It is the assessment's responsibility to call **Release** on the interface when the solution is done using the interface.

In managed code, this function is a static method of the AssessmentSupport object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





