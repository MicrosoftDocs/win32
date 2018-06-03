---
title: Updating a Quota
description: If the quota derives from a template, you should update the template and then apply the changes to all derived quotas.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fce6ce55-3fb5-46bc-8f26-3071df54767e
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , updating a quota
- quotas File Server Resource Manager
- templates for quotas File Server Resource Manager
- updating quotas File Server Resource Manager
- updating templates File Server Resource Manager
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Updating a Quota

If the quota derives from a template, you should update the template and then apply the changes to all derived quotas. If you update the quota directly, you may lose your changes if later, the template is updated.

When you update a template, you can apply the updates to only those quotas that match the template, or you can force the updates on all derived quotas. To determine if a quota matches the template from which it derives, access the [**IFsrmQuotaObject::MatchesSourceTemplate**](/previous-versions/windows/desktop/api/FsrmQuota/nf-fsrmquota-ifsrmquotaobject-get_matchessourcetemplate) property.

The following example shows how to update a template and apply the changes to derived quotas. The example updates the template that you created for the example in [Defining and Using Automatic Quotas](defining-and-using-automatic-quotas.md).


```C++
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <FsrmQuota.h>  // quota objects
#include <FsrmTlb.h>  // Contains CLSIDs.

void ShowDerivedResults(IFsrmDerivedObjectsResult* pDerivedResults);

// Adds a report action to the 85% threshold for the Test Automatic 
// Quota Template template. Also increases the quota limit. Applies 
// the updates to all derived quotas that match the automatic quota.

void wmain(void)
{
  HRESULT hr = S_OK;
  IFsrmQuotaTemplateManager* pqtm = NULL;
  IFsrmQuotaTemplate* pTemplate = NULL;
  IFsrmAction* pAction = NULL;
  IFsrmActionReport* pReport = NULL;
  IFsrmDerivedObjectsResult* pDerivedResults = NULL;
  SAFEARRAY* psaReportsToRun = NULL;
  long index = 0;
  _variant_t var;
  ULONGLONG ullQuotaLimit = 10 * 1024;  // 10 KB


  hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
  if (FAILED(hr))
  {
    wprintf(L"CoInitializeEx() failed, 0x%x.\n", hr);
    return;
  }

  hr = CoCreateInstance(CLSID_FsrmQuotaTemplateManager, 
    NULL,
    CLSCTX_LOCAL_SERVER,
    __uuidof(IFsrmQuotaTemplateManager),
    reinterpret_cast<void**> (&amp;pqtm));

  if (FAILED(hr))
  {
    wprintf(L"CoCreateInstance(FsrmQuotaTemplateManager) failed, 0x%x.\n", hr);
    goto cleanup;
  }

  // Get the template used to define the automatic quota.
  hr = pqtm->GetTemplate(_bstr_t(L"Test Automatic Quota Template"), &amp;pTemplate);
  if (FAILED(hr))
  {
    wprintf(L"pqtm->GetTemplate failed, 0x%x.\n", hr);
    goto cleanup;
  }

  // Change the quota.
  hr = pTemplate->put_QuotaLimit(_variant_t(ullQuotaLimit));
  if (FAILED(hr))
  {
    wprintf(L"pTemplate->put_QuotaLimit failed, 0x%x.\n", hr);
    goto cleanup;
  }

  // Add a report action to the 85% threshold. When the storage use 
  // reaches 85% of the quota limit, FSRM generates the requested
  // report.
  hr = pTemplate->CreateThresholdAction(85, FsrmActionType_Report, &amp;pAction);
  if (FAILED(hr))
  {
    wprintf(L"pTemplate->CreateThresholdAction failed, 0x%x.\n", hr);
    goto cleanup;
  }

  hr = pAction->QueryInterface(IID_IFsrmActionReport, (void**)&amp;pReport);

  // Email address of the person receiving the report.
  hr = pReport->put_MailTo(_bstr_t(L"<EMAILADDRESSGOESHERE>"));
  if (FAILED(hr))
  {
    wprintf(L"pReport->put_MailTo failed, 0x%x.\n", hr);
    goto cleanup;
  }

  // Specify the reports to run. This example requests a quota
  // usage report.
  psaReportsToRun = SafeArrayCreateVector(VT_VARIANT, 0, 1);
  if (psaReportsToRun)
  {
    var = (long)FsrmReportType_QuotaUsage;
    hr = SafeArrayPutElement(psaReportsToRun, &amp;index, &amp;var);

    hr = pReport->put_ReportTypes(psaReportsToRun);
    if (FAILED(hr))
    {
      wprintf(L"pReport->put_ReportTypes failed, 0x%x.\n", hr);
      goto cleanup;
    }

    SafeArrayDestroy(psaReportsToRun);
    psaReportsToRun = NULL;
  }
  else
  {
    wprintf(L"Failed to create reports safearray.\n", hr);
    goto cleanup;
  }

  // Save the template changes and update all derived quotas that 
  // match the template. Given the directory structure defined in the
  // Defining and Using Automatic Quotas topic, the automatic quota defined
  // for folder is update as well as the quotas for subdirectories A,
  // C, and D; the quota for subdirectoy B is not updated because 
  // it derives from another template.
  hr = pTemplate->CommitAndUpdateDerived(FsrmCommitOptions_None, 
    FsrmTemplateApplyOptions_ApplyToDerivedMatching,
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

  if (pqtm)
    pqtm->Release();

  if (pTemplate)
    pTemplate->Release();

  if (pAction)
    pAction->Release();

  if (pReport)
    pReport->Release();

  if (psaReportsToRun)
    SafeArrayDestroy(psaReportsToRun);

  CoUninitialize();
}


//
// List the derived quota objects that failed to update.
//
void ShowDerivedResults(IFsrmDerivedObjectsResult* pDerivedResults)
{
  HRESULT hr = S_OK;
  IFsrmCollection* pResultsCollection = NULL;
  IFsrmCollection* pDerivedCollection = NULL;
  IFsrmAutoApplyQuota* pQuota = NULL;
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

    if (FAILED(varResult.lVal))
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
        wprintf(L"pDerivedResults->get_DerivedObjects failed, 0x%x.\n", hr);
        goto cleanup;
      }

      varDerived.pdispVal->QueryInterface(__uuidof(IFsrmAutoApplyQuota),
        reinterpret_cast<void**> (&amp;pQuota));

      hr = pQuota->get_Path(&amp;bstr);
      if (FAILED(hr))
      {
        wprintf(L"pQuota->get_Path failed, 0x%x.\n", hr);
        goto cleanup;
      }

      wprintf(L"Failed to update the quota applied to %s. Failed with 0x%x.\n",
        bstr, varResult.ulVal);
      SysFreeString(bstr);

      pQuota->Release();
      pQuota = NULL;

      VariantClear(&amp;varDerived);
    }

    VariantClear(&amp;varResult);
  }

  wprintf(L"\n%d of %d derived quotas updated.\n", countResults - failed, countResults);

cleanup:

  if (pResultsCollection)
    pResultsCollection->Release();

  if (pDerivedCollection)
    pDerivedCollection->Release();

  if (pQuota)
    pQuota->Release();

  VariantClear(&amp;varResult);
  VariantClear(&amp;varDerived);
}
```



 

 




