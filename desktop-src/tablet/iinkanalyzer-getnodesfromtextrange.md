---
description: Retrieves a collection of IContextNode objects that are relevant to the specified text range for the specified context nodes.
ms.assetid: 39a5dd52-7007-4395-8668-261eca78a090
title: IInkAnalyzer::GetNodesFromTextRange method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetNodesFromTextRange
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetNodesFromTextRange method

Retrieves a collection of [**IContextNode**](icontextnode.md) objects that are relevant to the specified text range for the specified context nodes.

## Syntax


```C++
HRESULT GetNodesFromTextRange(
  [in, out] LONG          *plStart,
  [in, out] LONG          *plLength,
  [out]     IContextNodes **ppContextNodes,
  [in]      IContextNodes *pNodesToSearch = defaultvalue
);
```



## Parameters

<dl> <dt>

*plStart* \[in, out\]
</dt> <dd>

A reference to the start of the text range in the *pNodesToSearch* portion of the recognized string.

</dd> <dt>

*plLength* \[in, out\]
</dt> <dd>

A reference to the length of the text range in the *pNodesToSearch* portion of the recognized string.

</dd> <dt>

*ppContextNodes* \[out\]
</dt> <dd>

A pointer to the [**IContextNode**](icontextnode.md) objects that are relevant to the specified text range for the specified context nodes.

</dd> <dt>

*pNodesToSearch* \[in\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) objects to which to limit the search.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The specified text range should be relative to the *pNodesToSearch* portion of the recognized string of the [**IInkAnalyzer**](iinkanalyzer.md), rather than to the recognized string of the entire **IInkAnalyzer**.

This method modifies the values of the *plStart* and *plLength* parameters by expanding the text range to the nearest word boundaries.

For example, if the recognized string is "I am late" and you call this method using the parameter values of 6 for *plStart* and 1 for *plLength*, which corresponds to the letter "a" in "late", this method returns a collection containing a single [**IContextNode**](icontextnode.md), the InkWord or TextWord that corresponds to the word "late". For this example, this method also modifies the value of *plStart* to 5 and the value of *plLength* to 4, which corresponds to the word "late".

> [!Note]  
> The *plStart* parameter is relative to the recognized string of the *pNodesToSearch* parameter.

 

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
</dt> </dl>

 

 




