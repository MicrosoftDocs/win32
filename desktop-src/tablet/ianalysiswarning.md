---
description: Represents a warning or error that occurs during an ink analysis operation.
ms.assetid: a9b0564b-8a49-44bc-9dbc-60a2fd5b60f2
title: IAnalysisWarning interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisWarning
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisWarning interface

Represents a warning or error that occurs during an ink analysis operation.

## Members

The **IAnalysisWarning** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IAnalysisWarning** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAnalysisWarning** interface has these methods.



| Method                                                            | Description                                                                                                                            |
|:------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| [**GetBackgroundError**](ianalysiswarning-getbackgrounderror.md) | Retrieves the error code for the background ink analysis operation if an error occurred.<br/>                                    |
| [**GetHint**](ianalysiswarning-gethint.md)                       | Retrieves the analysis hint that caused this warning<br/>                                                                        |
| [**GetNodeIds**](ianalysiswarning-getnodeids.md)                 | Retrieves the identifiers of any relevant context nodes that are associated with this warning.<br/>                              |
| [**GetWarningCode**](ianalysiswarning-getwarningcode.md)         | Retrieves the type of warning that occurred by using the [**AnalysisWarningCode**](/windows/desktop/tablet/analysiswarningcode) enumeration.<br/> |



 

## Remarks

The types of warnings that can occur are described by the [**AnalysisWarningCode**](/windows/desktop/tablet/analysiswarningcode) enumeration. Often warnings occur when you try to use a feature that is not supported by the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) that the [**IInkAnalyzer**](iinkanalyzer.md) is using.

Some warnings indicate that the [**IInkAnalyzer**](iinkanalyzer.md) did not complete the analysis operation. For more information, see [**AnalysisWarningCode**](/windows/desktop/tablet/analysiswarningcode).

## Examples

The following example shows an outline of an event handler for the [**\_IAnalysisEvents::Results**](-ianalysisevents-results.md) event. The handler checks [**IAnalysisStatus::IsSuccessful**](ianalysisstatus-issuccessful.md). If the analysis operation generates warnings, the handler iterates through the collection of **IAnalysisWarning** objects.


```C++
// _IAnalysisEvents::Results event handler.
STDMETHODIMP CMyClass::Results(
    IInkAnalyzer *pInkAnalyzer,
    IAnalysisStatus *pAnalysisStatus)
{
    // Check the status of the analysis operation.
    VARIANT_BOOL bResult = VARIANT_FALSE;
    HRESULT hr = pAnalysisStatus->IsSuccessful(&bResult);

    if( SUCCEEDED(hr) )
    {
        if( bResult )
        {
            // Insert code that handles a successful result.
        }
        else
        {
            // Get the analysis warnings.
            IAnalysisWarnings* pAnalysisWarnings = NULL;
            hr = pAnalysisStatus->GetWarnings(&pAnalysisWarnings);
            if (SUCCEEDED(hr))
            {
                // Iterate through the warning collection.
                ULONG warningCount = 0;
                hr = pAnalysisWarnings->GetCount(&warningCount);
                if (SUCCEEDED(hr))
                {
                    IAnalysisWarning *pAnalysisWarning = NULL;
                    AnalysisWarningCode analysisWarningCode;
                    for (ULONG index=0; index<warningCount; index++)
                    {
                        // Get an analysis warning.
                        hr = pAnalysisWarnings->GetAnalysisWarning(
                            index, &pAnalysisWarning);

                        if (SUCCEEDED(hr))
                        {
                            // Get the warning code for the warning.
                            hr = pAnalysisWarning->GetWarningCode(
                                &analysisWarningCode);

                            if (SUCCEEDED(hr))
                            {
                                // Insert code that handles each
                                // analysis warning.
                            }
                        }

                        // Release this reference to the analysis warning.
                        if (pAnalysisWarning != NULL)
                        {
                            pAnalysisWarning->Release();
                            pAnalysisWarning = NULL;
                        }

                        if (FAILED(hr))
                        {
                            break;
                        }
                    }
                }
            }

            // Release this reference to the analysis warnings collection.
            if (pAnalysisWarnings != NULL)
            {
                pAnalysisWarnings->Release();
                pAnalysisWarnings = NULL;
            }
        }
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

[**IAnalysisWarnings**](ianalysiswarnings.md)
</dt> <dt>

[**AnalysisWarningCode**](analysiswarningcode.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

