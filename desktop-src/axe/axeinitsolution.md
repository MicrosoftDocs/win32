---
title: AxeInitSolution function
description: Initializes the solution portion of the AXE core and instantiates the Solution interface.
ms.assetid: 'B4144705-9AF8-4A0C-8D21-AFCE729DBA3B'
keywords: ["AxeInitSolution function Access Execution Engine"]
topic_type:
- apiref
api_name:
- AxeInitSolution
api_location:
- AxeCore.dll
api_type:
- DllExport
---

# AxeInitSolution function

Initializes the solution portion of the AXE core and instantiates the [**Solution**](solution-inf.md) interface.

## Syntax


```C++
HRESULT AxeInitSolution(
  _Inout_opt_ Microsoft::Assessments::Hosting::SolutionParameters *pParams,
  _Out_opt_   Microsoft::Assessments::Hosting::Solution           **ppSolution
);
```



## Parameters

<dl> <dt>

*pParams* \[in, out, optional\]
</dt> <dd>

A optional pointer to the [**SolutionParameters**](solutionparameters.md) structure used to configure the [**Solution**](solution-inf.md) interface. If this value is **NULL**, the **Solution** interface is initialized to run assessments rather than workloads.

</dd> <dt>

*ppSolution* \[out, optional\]
</dt> <dd>

A double pointer to receive the instantiated pointer to the [**Solution**](solution-inf.md) interface.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**.

If AXE solution support has been initialized and the single object is already in use, the return value is **AXE\_E\_ALREADY\_INIT**.

If the size of the [**SolutionParameters**](solutionparameters.md) structure specified by the **Size** member does not match the actual size, the return value is **E\_INVALIDARG**.

If there is insufficient memory to create a [**Solution**](solution-inf.md) object , the return value is **E\_OUTOFMEMORY**.

## Remarks

Managed code uses [**Solution::Initialize methods**](https://msdn.microsoft.com/library/windows/desktop/hh769334).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





