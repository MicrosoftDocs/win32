---
description: Retrieves the best-result string of the recognition operation for the entire context node tree in the IInkAnalyzer.
ms.assetid: 4aa57f41-3122-47a9-a60d-4a229e23f63c
title: IInkAnalyzer::GetRecognizedString method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetRecognizedString
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetRecognizedString method

Retrieves the best-result string of the recognition operation for the entire context node tree in the [**IInkAnalyzer**](iinkanalyzer.md).

## Syntax


```C++
HRESULT GetRecognizedString(
  [out] BSTR *pbstrRecognizedString
);
```



## Parameters

<dl> <dt>

*pbstrRecognizedString* \[out\]
</dt> <dd>

The best-result string of the recognition operation for the entire context node tree in the [**IInkAnalyzer**](iinkanalyzer.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) for *pbstrRecognizedString* when you no longer need to use the string.

 

This method returns the same value as the root node's property data for the recognized string. (See [**IInkAnalyzer::GetRootNode Method**](iinkanalyzer-getrootnode.md), [**IContextNode::GetPropertyData**](icontextnode-getpropertydata.md), and [Context Node Properties](context-node-properties.md).)

## Examples

The following example shows a method that walks the ink analyzer's [**IContextNode**](icontextnode.md) results tree. If the IInkAnlyzer is not currently performing ink analysis, the method does the following.

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

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

