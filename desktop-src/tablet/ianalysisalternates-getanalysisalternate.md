---
description: Retrieves the IAnalysisAlternate object at the specified index within the collection.
ms.assetid: d927e2f1-ca21-415d-90ad-d1ded575fcb7
title: IAnalysisAlternates::GetAnalysisAlternate method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisAlternates.GetAnalysisAlternate
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisAlternates::GetAnalysisAlternate method

Retrieves the [**IAnalysisAlternate**](ianalysisalternate.md) object at the specified index within the collection.

## Syntax


```C++
HRESULT GetAnalysisAlternate(
  [in]  ULONG              ulIndex,
  [out] IAnalysisAlternate **ppAlternate
);
```



## Parameters

<dl> <dt>

*ulIndex* \[in\]
</dt> <dd>

The zero-based index of the [**IAnalysisAlternate**](ianalysisalternate.md) object to get.

</dd> <dt>

*ppAlternate* \[out\]
</dt> <dd>

A pointer to the [**IAnalysisAlternate**](ianalysisalternate.md) object at the specified index within the collection.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**ppAlternate* when you no longer need to use the analysis alternate.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisAlternates**](ianalysisalternates.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

