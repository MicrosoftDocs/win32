---
description: Creates an IContextNodes object.
ms.assetid: d6d37595-307b-4cbc-9d48-ad10f8b272dd
title: IInkAnalyzer::CreateContextNodes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.CreateContextNodes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::CreateContextNodes method

Creates an [**IContextNodes**](icontextnodes.md) object.

## Syntax


```C++
HRESULT CreateContextNodes(
  [out] IContextNodes **ppContextNodes
);
```



## Parameters

<dl> <dt>

*ppContextNodes* \[out\]
</dt> <dd>

A pointer to the [**IContextNodes**](icontextnodes.md) object.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppContextNodes* when you no longer need to use the object.

 

Use this method to create an empty [**IContextNodes**](icontextnodes.md) collection that is associated with the [**IInkAnalyzer**](iinkanalyzer.md). The new **IContextNodes** collection is not part of the **IInkAnalyzer** object's context tree.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[**IContextNodes**](icontextnodes.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

