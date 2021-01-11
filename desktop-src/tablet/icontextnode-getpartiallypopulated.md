---
description: Retrieves the value that indicates whether an IContextNode object is partially populated or fully populated.
ms.assetid: 13ac3fb2-7baa-48d7-bf8e-f36b4031fbc4
title: IContextNode::GetPartiallyPopulated method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.GetPartiallyPopulated
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::GetPartiallyPopulated method

Retrieves the value that indicates whether an [**IContextNode**](icontextnode.md) object is partially populated or fully populated.

## Syntax


```C++
HRESULT GetPartiallyPopulated(
  [out] VARIANT_BOOL *pfPartiallyPopulated
);
```



## Parameters

<dl> <dt>

*pfPartiallyPopulated* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if this [**IContextNode**](icontextnode.md) object does not contain complete data; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Use this method when your application maintains its own data structure, which is synchronized with that of the [**IInkAnalyzer**](iinkanalyzer.md). For more information, see [Data Proxy with Ink Analysis](data-proxy-with-ink-analysis.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[**IContextNode::SetPartiallyPopulated**](icontextnode-setpartiallypopulated.md)
</dt> <dt>

[**IContextNode::CreatePartiallyPopulatedSubNode**](icontextnode-createpartiallypopulatedsubnode.md)
</dt> <dt>

[**\_IAnalysisProxyEvents::PopulateContextNode**](-ianalysisproxyevents-populatecontextnode.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




