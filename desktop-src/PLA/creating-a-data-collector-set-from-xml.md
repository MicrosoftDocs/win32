---
title: Creating a Data Collector Set from XML
description: You can use the properties of the IDataCollectorSet interface to specify the property values of the set, or you can use XML to specify the values. If you use XML, pass the XML string to the IDataCollectorSet SetXml method.
ms.assetid: a8e1868c-3fd4-4859-a923-29877c3b99b6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Data Collector Set from XML

You can use the properties of the [**IDataCollectorSet**](/previous-versions/windows/desktop/api/Pla/nn-pla-idatacollectorset) interface to specify the property values of the set, or you can use XML to specify the values. If you use XML, pass the XML string to the [**IDataCollectorSet::SetXml**](/previous-versions/windows/desktop/api/Pla/nf-pla-idatacollectorset-setxml) method.

The following example shows how to use XML to create a data collector set. The example uses the data collector set to add a data collector, save the changes, and then run the data collector set.


```C++
#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <pla.h>

#pragma comment(lib, "comsupp.lib")

// XML string that defines the property values for the data collector set.
_bstr_t pXml = L"<DataCollectorSet>"
    L"<Duration>60</Duration>"
    L"<Description>Test Setting Properties Using XML</Description>"
    L"<DisplayName>XML Test</DisplayName>"
    L"<Subdirectory>MyLogs</Subdirectory>"
    L"<SubdirectoryFormat>0x1000</SubdirectoryFormat>"
L"</DataCollectorSet>";

HRESULT CreateDCS(IDataCollectorSet* & pdcs);
HRESULT AddDataCollector(IDataCollectorSet* pdcs);
HRESULT SaveDCS(IDataCollectorSet* pdcs);

void main(void)
{
    HRESULT hr = S_OK;
    IDataCollectorSet* pdcs = NULL;

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);

    hr = CreateDCS(pdcs);
    if (FAILED(hr))
    {
        wprintf(L"CreateDCS failed.\n");
        goto cleanup;
    }

    hr = AddDataCollector(pdcs);
    if (FAILED(hr))
    {
        wprintf(L"AddDataCollector failed.\n");
        goto cleanup;
    }

    hr = SaveDCS(pdcs);
    if (FAILED(hr))
    {
        wprintf(L"SaveDCS failed.\n");
        goto cleanup;
    }

    hr = pdcs->Start(VARIANT_TRUE);
    if (FAILED(hr))
    {
        wprintf(L"pdcs->Start failed.\n");
        goto cleanup;
    }

cleanup:

    if (pdcs)
        pdcs->Release();

    CoUninitialize();
}


HRESULT CreateDCS(IDataCollectorSet* & pdcs)
{
    HRESULT hr = S_OK;
    HRESULT hrSetXml = S_OK;
    IValueMap* pValidation = NULL;
    IValueMapItem* pItem = NULL;
    BSTR bstr = NULL;
    VARIANT vIndex;
    VARIANT vHResult;
    long count = 0;
    BOOL fErrorsExists = FALSE;

    hr = CoCreateInstance(__uuidof(DataCollectorSet), 
                          NULL, 
                          CLSCTX_SERVER,
                          __uuidof(IDataCollectorSet),
                          (void**) &amp;pdcs);

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(__uuidof(DataCollectorSet) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Use the XML string to define the property values for the data collector set.
    // The method returns the validation results. You need to check the validation
    // results regardless of the return value of the method.
    hr = pdcs->SetXml(pXml, &amp;pValidation);
    if (FAILED(hr))
    {
        wprintf(L"pdcs->SetXml failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Check the validation results. The results can contain both
    // warnings and errors.
    if (pValidation)
    {
        hr = pValidation->get_Count(&amp;count);
        wprintf(L"%ld validation errors:\n\n", count);

        VariantInit(&amp;vIndex);
        VariantInit(&amp;vHResult);

        V_VT(&amp;vIndex) = VT_I4;  // for iterating through the results

        // You can use either the _NewEnum collection or the Count
        // and Item properties to iterate through the results. This
        // example uses the Count and Item properties.
        for (int i = 0; i < count; i++)
        {
            V_I4(&amp;vIndex) = i;

            // Get the value map item; the item contains the validation error
            // or warning. The result is a warning if the item's value is
            // a success code; otherwise, the result is an error.
            hr = pValidation->get_Item(vIndex, &amp;pItem);
            if (SUCCEEDED(hr))
            {
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
                wprintf(L"hr: 0x%x\n", vHResult.lVal);
                wprintf(L"Considered %s\n\n", (SUCCEEDED(vHResult.lVal)) ? L"a warning" : L"an error");
                if (FAILED(vHResult.lVal))
                    fErrorsExists = TRUE;
                VariantClear(&amp;vHResult);

                pItem->Release();
            }
            else
            {
                wprintf(L"get_Item failed, 0x%x\n", hr);
            }
        }

        pValidation->Release();
        pValidation = NULL;

        VariantClear(&amp;vIndex);
    }

cleanup:

    if (fErrorsExists)
    {
        hr = E_FAIL;
    }

    return hr;
}


HRESULT AddDataCollector(IDataCollectorSet* pdcs)
{
    HRESULT hr = S_OK;
    IDataCollectorCollection* pCollectors = NULL;
    IDataCollector* pdc = NULL;
    IAlertDataCollector* pdcAlert = NULL;
    SAFEARRAY* psaAlerts = NULL;
    BSTR bstr = NULL;
    long index = 0;

    // Retrieve the collection of data collectors from the data
    // collector set.
    hr = pdcs->get_DataCollectors(&amp;pCollectors);
    if (FAILED(hr))
    {
        wprintf(L"pdcs->get_DataCollectors failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Create an alert data collector. The method returns an IDataCollector
    // interface that contains the base properties for all data collectors.
    // Query IDataCollector for the IAlertDataCollector interface.
    hr = pCollectors->CreateDataCollector(plaAlert, &amp;pdc);
    hr = pdc->QueryInterface(IID_IAlertDataCollector, (void**)&amp;pdcAlert);
    pdc->Release();

    // TODO: Set one or more of the Alert properties; you must specify one or 
    // or more alerts. You can also change the sample interval (the rate at which
    // PLA checks the alert threshold), have PLA log an event, start a Task 
    // Scheduler task, or start another data collector set when the threshold 
    // is crossed.

    // Create an array of alert thresholds. An alert threshold is a performance
    // counter string with the threshold appended. In this example, the threshold
    // is crossed when the processor time exceeds 60 percent.
    psaAlerts = SafeArrayCreateVector(VT_BSTR, 0, 1);
    if (psaAlerts)
    {
        bstr = SysAllocString(L"\\Processor(0)\\% Processor Time>60");
        hr = SafeArrayPutElement(psaAlerts, &amp;index, bstr);
        SysFreeString(bstr);

        hr = pdcAlert->put_AlertThresholds(psaAlerts);
        if (FAILED(hr))
        {
            wprintf(L"put_AlertThresholds failed, 0x%x\n", hr);
            goto cleanup;
        }

        hr = SafeArrayDestroy(psaAlerts);
        psaAlerts = NULL;
    }
    else
    {
        wprintf(L"Failed to create alert safearray\n");
        goto cleanup;
    }

    // Log an event when the threshold is crossed.
    hr = pdcAlert->put_EventLog(VARIANT_TRUE);
    if (FAILED(hr))
    {
        wprintf(L"put_EventLog failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Change the sample interval to every 5 seconds.
    hr = pdcAlert->put_SampleInterval(5);
    if (FAILED(hr))
        wprintf(L"put_SampleInterval failed, 0x%x\n", hr);


    // TODO: Set one or more of the IDataCollector properties.

    hr = pdcAlert->put_Name(_bstr_t(L"Test Alert"));
    if (FAILED(hr))
        wprintf(L"put_Name failed, 0x%x\n", hr);

    // Add the alert data collector to the collection of data collectors in the set.
    hr = pCollectors->Add(pdcAlert);
    if (FAILED(hr))
    {
        wprintf(L"pCollectors->Add failed, 0x%x\n", hr);
        goto cleanup;
    }

cleanup:

    if (pdcAlert)
        pdcAlert->Release();

    if (psaAlerts)
        SafeArrayDestroy(psaAlerts);

    if (pCollectors)
        pCollectors->Release();

    return hr;
}

HRESULT SaveDCS(IDataCollectorSet* pdcs)
{
    HRESULT hr = S_OK;
    IValueMap* pValidation = NULL;
    IEnumVARIANT* pItems = NULL;
    IValueMapItem* pItem = NULL;
    IUnknown* punk = NULL;
    _bstr_t bstrDCSName = L"Service\\TestXml";
    VARIANT var;
    VARIANT vHResult;
    long count = 0;
    BSTR bstr = NULL;
    BOOL fErrorsExists = FALSE;

    // Save the data collector set to the local computer using the specified name. 
    // The set is named 'TestXml' and is saved in the 'Service' namespace. If the set
    // exists in the namespace, update the set with the contents of this instance.
    // The method returns the validation results.
    hr = pdcs->Commit(bstrDCSName, NULL, plaCreateOrModify, &amp;pValidation);
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



You can also use XML to define the entire data collector set. For example, the XML string can also contain the data collectors, schedules, and data management rules as shown in the following example.


```C++
#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <pla.h>

#pragma comment(lib, "comsupp.lib")

// XML string that defines the property values for the data collector set, 
// performance counter data collector, schedule, and data management rule.
_bstr_t pXml = L"<DataCollectorSet>"
    L"<Duration>60</Duration>"
    L"<Description>Test Setting Properties Using XML</Description>"
    L"<DisplayName>XML Full DCS Test</DisplayName>"
    L"<SchedulesEnabled>-1</SchedulesEnabled>"
    L"<Subdirectory>MyLogs</Subdirectory>"
    L"<SubdirectoryFormat>0x1000</SubdirectoryFormat>"
    L"<PerformanceCounterDataCollector>"
        L"<Counter>\\Processor(0)\\% Processor Time</Counter>"
        L"<SampleInterval>1</SampleInterval>"
        L"<Name>Test Perf XML</Name>"
        L"<FileName>PerfXmlTest</FileName>"
        L"<FileNameFormat>0x0200</FileNameFormat>"
    L"</PerformanceCounterDataCollector>"
    L"<Schedule>"
        L"<StartDate>5/27/2009</StartDate>"
        L"<EndDate>5/27/2009</EndDate>"
        L"<StartTime>13:22:00</StartTime>"
        L"<Days>0x00</Days>"
    L"</Schedule>"
    L"<DataManager>"
        L"<Enabled>-1</Enabled>"
        L"<MaxSize>1</MaxSize>"
        L"<FolderAction>"
            L"<Actions>1</Actions>"
        L"</FolderAction>"
    L"</DataManager>"
L"</DataCollectorSet>";

HRESULT CreateDCS(IDataCollectorSet* & pdcs);
HRESULT SaveDCS(IDataCollectorSet* pdcs);

void main(void)
{
    HRESULT hr = S_OK;
    IDataCollectorSet* pdcs = NULL;

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);

    hr = CreateDCS(pdcs);
    if (FAILED(hr))
    {
        wprintf(L"CreateDCS failed.\n");
        goto cleanup;
    }

    hr = SaveDCS(pdcs);
    if (FAILED(hr))
    {
        wprintf(L"SaveDCS failed.\n");
        goto cleanup;
    }

cleanup:

    if (pdcs)
        pdcs->Release();

    CoUninitialize();
}


HRESULT CreateDCS(IDataCollectorSet* & pdcs)
{
    HRESULT hr = S_OK;
    IValueMap* pValidation = NULL;
    IValueMapItem* pItem = NULL;
    BSTR bstr = NULL;
    VARIANT vIndex;
    VARIANT vHResult;
    long count = 0;
    BOOL fErrorsExists = FALSE;

    hr = CoCreateInstance(__uuidof(DataCollectorSet), 
                          NULL, 
                          CLSCTX_SERVER,
                          __uuidof(IDataCollectorSet),
                          (void**) &amp;pdcs);

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(__uuidof(DataCollectorSet) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Use the XML string to define the property values for the data collector set.
    // The method returns the validation results. You need to check the validation
    // results regardless of the return value of the method.
    hr = pdcs->SetXml(pXml, &amp;pValidation);
    if (FAILED(hr))
    {
        wprintf(L"pdcs->SetXml failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Check the validation results. The results can contain both
    // warnings and errors.
    if (pValidation)
    {
        hr = pValidation->get_Count(&amp;count);
        wprintf(L"%ld validation errors:\n\n", count);

        VariantInit(&amp;vIndex);
        VariantInit(&amp;vHResult);

        V_VT(&amp;vIndex) = VT_I4;  // for iterating through the results

        // You can use either the _NewEnum collection or the Count
        // and Item properties to iterate through the results. This
        // example uses the Count and Item properties.
        for (int i = 0; i < count; i++)
        {
            V_I4(&amp;vIndex) = i;

            // Get the value map item; the item contains the validation error
            // or warning. The result is a warning if the item's value is
            // a success code; otherwise, the result is an error.
            hr = pValidation->get_Item(vIndex, &amp;pItem);
            if (SUCCEEDED(hr))
            {
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
                wprintf(L"hr: 0x%x\n", vHResult.lVal);
                wprintf(L"Considered %s\n\n", (SUCCEEDED(vHResult.lVal)) ? L"a warning" : L"an error");
                if (FAILED(vHResult.lVal))
                    fErrorsExists = TRUE;
                VariantClear(&amp;vHResult);

                pItem->Release();
            }
            else
            {
                wprintf(L"get_Item failed, 0x%x\n", hr);
            }
        }

        pValidation->Release();
        pValidation = NULL;

        VariantClear(&amp;vIndex);
    }

cleanup:

    if (fErrorsExists)
    {
        hr = E_FAIL;
    }

    return hr;
}


HRESULT SaveDCS(IDataCollectorSet* pdcs)
{
    HRESULT hr = S_OK;
    IValueMap* pValidation = NULL;
    IEnumVARIANT* pItems = NULL;
    IValueMapItem* pItem = NULL;
    IUnknown* punk = NULL;
    _bstr_t bstrDCSName = L"Service\\TestXml2";
    VARIANT var;
    VARIANT vHResult;
    long count = 0;
    BSTR bstr = NULL;
    BOOL fErrorsExists = FALSE;

    // Save the data collector set to the local computer using the specified name. 
    // The set is named 'TestXml2' and is saved in the 'Service' namespace. If the set
    // exists in the namespace, update the set with the contents of this instance.
    // The method returns the validation results. You need to check the validation 
    // results regardless of the return value of the method.
    hr = pdcs->Commit(bstrDCSName, NULL, plaCreateOrModify, &amp;pValidation);
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



 

 




