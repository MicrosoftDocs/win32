---
title: Updating a File Screen
description: If the file screen derives from a template, you should update the template and then apply the changes to all derived file screens.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 298e7e37-709a-4b13-87d3-605d540d8f85
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , updating a file screen
- file screens File Server Resource Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Updating a File Screen

If the file screen derives from a template, you should update the template and then apply the changes to all derived file screens. If you update the file screen directly, you may lose your changes if later, the template is updated.

When you update a template, you can apply the updates to only those derived file screens that still match the template, or you can force the updates on all derived file screens. To determine if a file screen matches the template from which it derives, access the [**IFsrmFileScreen::MatchesSourceTemplate**](/windows/previous-versions/FsrmScreen/nf-fsrmscreen-ifsrmfilescreen-get_matchessourcetemplate?branch=master) property.

The following example shows how to update a template and apply the changes to derived file screens.


```C++
#include <stdio.h>
#include <comutil.h>
#include <FsrmScreen.h> // File screen and group objects
#include <fsrmtlb.h>    // For CLSIDs


void ShowDerivedResults(IFsrmDerivedObjectsResult* pDerivedResults);

//
// Updates a templates and applies the changes to all derived screens.
//
void wmain(void)
{
    HRESULT hr = S_OK;
    IFsrmFileScreenTemplateManager* pfstm = NULL;
    IFsrmFileScreenTemplate* pTemplate = NULL;
    IFsrmDerivedObjectsResult* pDerivedResults = NULL;
    IFsrmCollection* pCollection = NULL;
    IFsrmMutableCollection* pBlockedList = NULL;
    VARIANT var;

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
    if (FAILED(hr))
    {
        wprintf(L"CoInitializeEx() failed, 0x%x.\n", hr);
        return;
    }

    hr = CoCreateInstance(CLSID_FsrmFileScreenTemplateManager, 
        NULL,
        CLSCTX_LOCAL_SERVER,
        __uuidof(IFsrmFileScreenTemplateManager),
        reinterpret_cast<void**> (&amp;pfstm));

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(FsrmFileScreenTemplateManager) failed, 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Successfully created FileScreenTemplateManager object.\n");

    // Get the Test Template template created in the Using Templates to Define 
    // File Screens example.
    hr = pfstm->GetTemplate(_bstr_t(L"Test Template"), &amp;pTemplate);
    if (FAILED(hr))
    {
        wprintf(L"pfstm->GetTemplate failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Get the blocked files list and add a new group to the list.
    // The Text Files group is an FSRM-defined file group.
    hr = pTemplate->get_BlockedFileGroups(&amp;pBlockedList);
    if (FAILED(hr))
    {
        wprintf(L"pTemplate->get_BlockedFileGroups failed, 0x%x.\n", hr);
        goto cleanup;
    }

    VariantInit(&amp;var);
    V_VT(&amp;var) = VT_BSTR;
    var.bstrVal = SysAllocString(L"Text Files");

    hr = pBlockedList->Add(var);
    if (FAILED(hr))
    {
        wprintf(L"pBlockedList->Add failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTemplate->put_BlockedFileGroups(pBlockedList);
    if (FAILED(hr))
    {
        wprintf(L"pTemplate->get_BlockedFileGroups failed, 0x%x.\n", hr);
        goto cleanup;
    }

    VariantClear(&amp;var);

    // If you just want to save the changes to the template, call the
    // pTemplate->Commit method. If you want to save the changes and
    // apply them to derived screen objects, call the CommitAndUpdateDerived
    // method. The FsrmTemplateApplyOptions enumeration contains the
    // options for applying the template changes to the derived screens.
    // This example applies the changes to all derived screens. Note that this 
    // option will overwrite any changes that were made to the screen since the 
    // template was originally applied to the screen. To prevent overwriting
    // screens that have been changed, use the ApplyToDerivedMatching option.

    hr = pTemplate->CommitAndUpdateDerived(FsrmCommitOptions_None, 
        FsrmTemplateApplyOptions_ApplyToDerivedAll, 
        &amp;pDerivedResults);

    if (FAILED(hr))
    {
        wprintf(L"pTemplate->CommitAndUpdateDerived failed, 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Committed template. Checking updates to derived objects.\n");

    // Check the results of updating each derived object.
    ShowDerivedResults(pDerivedResults);

cleanup:

    if (pfstm)
        pfstm->Release();

    if (pTemplate)
        pTemplate->Release();

    if (pCollection)
        pCollection->Release();

    if (pDerivedResults)
        pDerivedResults->Release();

    VariantClear(&amp;var);

    if (pBlockedList)
        pBlockedList->Release();

    CoUninitialize();
}

//
// List the derived file screens that failed to update.
//
void ShowDerivedResults(IFsrmDerivedObjectsResult* pDerivedResults)
{
    HRESULT hr = S_OK;
    IFsrmCollection* pResultsCollection = NULL;
    IFsrmCollection* pDerivedCollection = NULL;
    IFsrmFileScreen* pScreen = NULL;
    VARIANT varResult;
    VARIANT varDerived;
    BSTR bstr = NULL;
    long countResults = 0;
    long failed = 0;

    hr = pDerivedResults->get_Results(&amp;pResultsCollection);
    if (FAILED(hr))
    {
        wprintf(L"pDerivedResults->get_Results failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pResultsCollection->get_Count(&amp;countResults);
    if (FAILED(hr))
    {
        wprintf(L"pResultsCollection->get_Count failed, 0x%x.\n", hr);
        goto cleanup;
    }

    VariantInit(&amp;varResult);

    // Loop through the collection of HRESULTs. If the result is not success,
    // get the related derived object that failed and print the path.
    for (long i = 1; i <= countResults; i++)
    {
        hr = pResultsCollection->get_Item(i, &amp;varResult);

        if (FAILED(varResult.ulVal))
        {
            failed++;

            if (NULL == pDerivedCollection)
            {
                hr = pDerivedResults->get_DerivedObjects(&amp;pDerivedCollection);
                if (FAILED(hr))
                {
                    wprintf(L"pDerivedResults->get_DerivedObjects failed, 0x%x.\n", hr);
                    goto cleanup;
                }

                VariantInit(&amp;varDerived);
            }

            hr = pDerivedCollection->get_Item(i, &amp;varDerived);
            if (FAILED(hr))
            {
                wprintf(L"pDerivedCollection->get_Item failed, 0x%x.\n", hr);
                goto cleanup;
            }

            varDerived.pdispVal->QueryInterface(__uuidof(IFsrmFileScreen),
                reinterpret_cast<void**> (&amp;pScreen));

            hr = pScreen->get_Path(&amp;bstr);
            if (FAILED(hr))
            {
                wprintf(L"pScreen->get_Path failed, 0x%x.\n", hr);
                goto cleanup;
            }

            wprintf(L"Failed to update the screen applied to %s. Failed with 0x%x.\n",
                bstr, varResult.ulVal);
            SysFreeString(bstr);

            pScreen->Release();
            pScreen = NULL;

            VariantClear(&amp;varDerived);
        }

        VariantClear(&amp;varResult);
    }

    wprintf(L"\n%d of %d derived screens updated.\n", countResults - failed, countResults);

cleanup:

    if (pResultsCollection)
        pResultsCollection->Release();

    if (pDerivedCollection)
        pDerivedCollection->Release();

    if (pScreen)
        pScreen->Release();

    VariantClear(&amp;varResult);
    VariantClear(&amp;varDerived);
}
```



 

 




