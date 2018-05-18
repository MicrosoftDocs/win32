---
title: Managing the Data of a Data Collector Set
description: To enable the data manager for a data collector set, set the IDataManager Enabled property to VARIANT\_TRUE.
ms.assetid: '131d4e41-ef32-4058-9342-b365309333d5'
---

# Managing the Data of a Data Collector Set

To enable the data manager for a data collector set, set the [**IDataManager::Enabled**](idatamanager-enabled.md) property to VARIANT\_TRUE. The data manager is used to create reports, create cabinet files, and manage the disk resources used by the data collector set.

The data manager runs after the data collectors in the set complete. To have the data manager verify available disk space before the data collector set runs, set the [**IDataCollectorSet::CheckBeforeRunning**](idatamanager-checkbeforerunning.md) property to VARIANT\_TRUE.

To run the data manager manually, call the [**IDataManager::Run**](idatamanager-run.md) method and specify the steps to run.

The following example shows how to enable the data manager. This example builds on the example in [Creating a Data Collector Set](creating-a-data-collector-set.md).


```C++
HRESULT ManageDCS(IDataCollectorSet* pdcs)
{
    HRESULT hr = S_OK;
    IDataManager* pdm = NULL;
    IFolderActionCollection* pActions = NULL;
    IFolderAction* pAction = NULL;

    // Get the data manager.
    hr = pdcs->get_DataManager(&amp;pdm);
    if (FAILED(hr))
    {
        wprintf(L"get_DataManager failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Enable the data manager.
    hr = pdm->put_Enabled(VARIANT_TRUE);
    if (FAILED(hr))
    {
        wprintf(L"put_Enabled failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Specify the maximum disk space to be used by the set to 1 MB.
    hr = pdm->put_MaxSize(1);
    if (FAILED(hr))
    {
        wprintf(L"put_MaxSize failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Get the collection of folder actions. You can add one or more
    // actions that can be triggered by different constraints. This
    // example always creates a cabinet file that contains all the data 
    // and reports in the folder. 
    hr = pdm->get_FolderActions(&amp;pActions);
    if (FAILED(hr))
    {
        wprintf(L"get_FolderActions failed, 0x%x\n", hr);
        goto cleanup;
    }

    hr = pActions->CreateFolderAction(&amp;pAction);
    if (FAILED(hr))
    {
        wprintf(L"CreateFolderAction failed, 0x%x\n", hr);
        goto cleanup;
    }

    hr = pAction->put_Actions(plaCreateCab);
    if (FAILED(hr))
    {
        wprintf(L"put_Actions failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Add the action to the collection.
    hr = pActions->Add(pAction);
    if (FAILED(hr))
    {
        wprintf(L"pActions->Add failed, 0x%x\n", hr);
        goto cleanup;
    }

cleanup:

    if (pdm)
        pdm->Release();

    if (pAction)
        pAction->Release();

    if (pActions)
        pActions->Release();

    return hr;
}
```



 

 




