---
description: Retrieves a value indicating whether the IInkAnalyzer is performing ink analysis.
ms.assetid: 3f3f6f29-0c90-47e1-938c-f1ce6ed8df47
title: IInkAnalyzer::IsAnalyzing method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.IsAnalyzing
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::IsAnalyzing method

Retrieves a value indicating whether the [**IInkAnalyzer**](iinkanalyzer.md) is performing ink analysis.

## Syntax


```C++
HRESULT IsAnalyzing(
  [out] VARIANT_BOOL *pbAnalyzing
);
```



## Parameters

<dl> <dt>

*pbAnalyzing* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if the [**IInkAnalyzer**](iinkanalyzer.md) is performing ink analysis; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

This property is **VARIANT\_TRUE** if the [**IInkAnalyzer**](iinkanalyzer.md) is performing synchronous or asynchronous analysis.

## Examples

The following example shows a method that walks the ink analyzer's [**IContextNode**](icontextnode.md) results tree. If the ink analyzer is not currently performing ink analysis, the method does the following.

-   Gets the top recognition string.
-   Gets the ink analyzer's root node.
-   Calls a helper method, `ExploreContextNode`, to examine the root node and its child nodes.


```C++
// Helper method that explores the current analysis results of an ink analyzer.
HRESULT CMyClass::ExploreAnalysisResults(
    IInkAnalyzer *pInkAnalyzer)
{
    // Check that the ink analyzer is not currently analyzing ink.
    VARIANT_BOOL bIsAnalyzing;
    HRESULT hr = pInkAnalyzer->IsAnalyzing(&bIsAnalyzing);

    if (SUCCEEDED(hr))
    {
        if (bIsAnalyzing)
        {
            return E_PENDING;
        }

        // Get the ink analyzer's best-result string.
        BSTR recognizedString = NULL;
        hr = pInkAnalyzer->GetRecognizedString(&recognizedString);

        if (SUCCEEDED(hr))
        {
            // Insert code that records the ink analyzer's best-result string here.

            // Get the ink analyzer's root node.
            IContextNode *pRootNode = NULL;
            hr = pInkAnalyzer->GetRootNode(&pRootNode);

            if (SUCCEEDED(hr))
            {
                // Call a helper method that recursively explores context
                // nodes and their subnodes.
                hr = this->ExploreContextNode(pRootNode);
            }

            // Release this reference to the root node.
            if (pRootNode != NULL)
            {
                pRootNode->Release();
                pRootNode = NULL;
            }
        }

        // Free the system resources for the recognized string.
        SysFreeString(recognizedString);
    }

    return hr;
}
```



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

[**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




