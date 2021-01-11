---
description: Retrieves the IAnalysisWarning object at the specified index.
ms.assetid: 8f5d5642-73ec-496e-bad7-9f636fc00217
title: IAnalysisWarnings::GetAnalysisWarning method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisWarnings.GetAnalysisWarning
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisWarnings::GetAnalysisWarning method

Retrieves the [**IAnalysisWarning**](ianalysiswarning.md) object at the specified index.

## Syntax


```C++
HRESULT GetAnalysisWarning(
  [in]  ULONG            ulIndex,
  [out] IAnalysisWarning **ppWarning
);
```



## Parameters

<dl> <dt>

*ulIndex* \[in\]
</dt> <dd>

The zero-based index of the [**IAnalysisWarning**](ianalysiswarning.md) object to get.

</dd> <dt>

*ppWarning* \[out\]
</dt> <dd>

A pointer to the [**IAnalysisWarning**](ianalysiswarning.md) object at the specified index.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**ppWarning* when you no longer need to use the warning.

 

## Examples

The following example shows an outline of an event handler for the [**\_IAnalysisEvents::Results**](-ianalysisevents-results.md) event. The handler checks [**IAnalysisStatus::IsSuccessful**](ianalysisstatus-issuccessful.md). If the analysis operation generates warnings, the handler iterates through the collection of [**IAnalysisWarning**](ianalysiswarning.md) objects.


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

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

