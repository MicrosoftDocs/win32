---
title: Committing a Data Collector Set
description: To commit a data collector set, you must call the IDataCollectorSet Commit method.
ms.assetid: acd3f66c-704a-425e-ad44-10c006625b4f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Committing a Data Collector Set

To commit a data collector set, you must call the [**IDataCollectorSet::Commit**](/windows/previous-versions/Pla/nf-pla-idatacollectorset-commit?branch=master) method. This method can be used to save a new set, update an existing set, flush a trace session, or validate the property values of the set.

To delete a data collector set that has been saved, call the [**IDataCollectorSet::Delete**](/windows/previous-versions/Pla/nf-pla-idatacollectorset-delete?branch=master) method.

The following example shows how to commit a new data collector set. This example builds on the example in [Creating a Data Collector Set](creating-a-data-collector-set.md).


```C++
HRESULT SaveDCS(IDataCollectorSet* pdcs)
{
    HRESULT hr = S_OK;
    IValueMap* pValidation = NULL;
    IEnumVARIANT* pItems = NULL;
    IValueMapItem* pItem = NULL;
    IUnknown* punk = NULL;
    _bstr_t bstrName = L"Service\\CreateDcs";
    VARIANT var;
    VARIANT vHResult;
    long count = 0;
    BSTR bstr = NULL;
    BOOL fErrorsExists = FALSE;

    // Save the data collector set to the local computer using the specified name. 
    // The set is named 'CreateDcs' and is saved in the 'Service' namespace. If the set
    // exists in the namespace, update the set with the contents of this instance.
    // The method returns the validation results. You need to check the validation 
    // results regardless of the return value of the method.
    hr = pdcs->Commit(bstrName, NULL, plaCreateOrModify, &amp;pValidation);
    if (FAILED(hr))
    {
        wprintf(L"pdcs->Commit failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Check the validation results. The results can contain both
    // warnings and errors.
    if (pValidation)
    {
        hr = pValidation->get_Count(&amp;count);
        wprintf(L"%ld validation errors:\n\n", count);

        if (count > 0)
        {
            // You can use either the _NewEnum collection or the Count
            // and Item properties to iterate through the results. This
            // example uses the _NewEnum collection.
            hr = pValidation->get__NewEnum(&amp;punk);
            pValidation->Release();

            hr = punk->QueryInterface(__uuidof(IEnumVARIANT), (void**)&amp;pItems);
            punk->Release();
 
            VariantInit(&amp;var);
            VariantInit(&amp;vHResult);

            while (S_OK == (hr = pItems->Next(1, &amp;var, NULL)))
            {
                // Get the value map item; the item contains the validation error
                // or warning. The result is a warning if the item's value is
                // a success code; otherwise, the result is an error.
                var.punkVal->QueryInterface(__uuidof(IValueMapItem), (void**)&amp;pItem);

                // Get the description of the error.
                hr = pItem->get_Description(&amp;bstr);
                wprintf(L"Description: %s", bstr);
                SysFreeString(bstr);

                // Get the XPath of the element in error.
                hr = pItem->get_Key(&amp;bstr);
                wprintf(L"Key: %s\n", bstr);
                SysFreeString(bstr);

                // Determine if the result is an error or warning.  
                hr = pItem->get_Value(&amp;vHResult);
                wprintf(L"hr: 0x%x\n", vHResult.ulVal);
                wprintf(L"Considered %s\n\n", (SUCCEEDED(vHResult.ulVal)) ? L"a warning" : L"an error");
                if (FAILED(vHResult.lVal))
                    fErrorsExists = TRUE;
                VariantClear(&amp;vHResult);

                pItem->Release();
                VariantClear(&amp;var);
            }

            pItems->Release();
        }
    }

cleanup:

    if (fErrorsExists)
    {
        hr = E_FAIL;
    }

    return hr;
}
```



 

 




