---
Description: Creates a copy of the IAnalysisRegion.
ms.assetid: eb94e1ce-7801-409d-9ae6-e7db0a9b861f
title: IAnalysisRegion::Clone method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAnalysisRegion::Clone method

Creates a copy of the [**IAnalysisRegion**](ianalysisregion.md).

## Syntax


```C++
HRESULT Clone(
  [out] IAnalysisRegion **pClonedRegion
);
```



## Parameters

<dl> <dt>

*pClonedRegion* \[out\]
</dt> <dd>

A pointer to a copy of the [**IAnalysisRegion**](ianalysisregion.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

This method is eqivalent to theSystem.Windows.Ink.AnalysisCore.AnalysisRegionBase.Clone Method in the .NET Framework.

> \[!Caution\]  
> To avoid a memory leak, call [**IUnknown::Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) on \**pClonedRegion* when you no longer need to use the cloned analysis region.

 

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisRegion**](ianalysisregion.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




