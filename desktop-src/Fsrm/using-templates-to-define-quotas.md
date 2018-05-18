---
title: Using Templates to Define Quotas
description: You can create quotas directly but typically you create quota templates from which quotas derive.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '88ff3968-cb83-4b66-83e9-a58205b4be82'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["File Server Resource Manager examples File Server Resource Manager , using templates to define quotas", "quota templates File Server Resource Manager", "templates for quotas File Server Resource Manager"]
---

# Using Templates to Define Quotas

You can create quotas directly but typically you create quota templates from which quotas derive. The template is used to modify properties in bulk by applying the changes to quotas that derive from the file screen template.

The following example shows how to create a quota template. For details on applying the template to a quota, see [Defining a Quota](defining-a-quota.md).


```C++
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <FsrmQuota.h>  // quota objects
#include <FsrmTlb.h>    // Contains CLSIDs.


#define EVENT_TEXT L"User [Source Io Owner] has reached the quota limit for quota on " \
    L"[Quota Path] on server [Server]. The quota limit is [Quota Limit MB] MB " \
    L"and the current usage is [Quota Used MB] MB ([Quota Used Percent]% of limit)."


// Creates  qutoa template that limits storage to 8 KB (for testing). 
// When storage reaches 85%, an event is logged.
void wmain(void)
{
    HRESULT hr = S_OK;
    IFsrmQuotaTemplateManager* pqtm = NULL;
    IFsrmQuotaTemplate* pTemplate = NULL;
    IFsrmAction* pAction = NULL;
    IFsrmActionEventLog* pLog = NULL;
    ULONGLONG ullQuotaLimit = 8 * 1024;  // 8 KB

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
    if (FAILED(hr))
    {
        wprintf(L"CoInitializeEx() failed, 0x%x.\n", hr);
        return;
    }

    // Get an interface to the quota template manager.
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

    // Get an interface to a quota template.
    hr = pqtm->CreateTemplate(&amp;pTemplate);
    if (FAILED(hr))
    {
        wprintf(L"pqtm->CreateTemplate failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Name the template. You use the name when you create a quota.
    hr = pTemplate->put_Name(_bstr_t(L"Test Quota Template"));
    if (FAILED(hr))
    {
        wprintf(L"pTemplate->put_Name failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // If you use a VARIANT data type instead of the _variant_t template, 
    // define the variant as follows:
    // VariantInit(&amp;var);
    // V_VT(&amp;var) = VT_UI8;
    // var.ullVal = ullQuotaLimit;

    // Specify the quota limit.
    hr = pTemplate->put_QuotaLimit(_variant_t(ullQuotaLimit));
    if (FAILED(hr))
    {
        wprintf(L"pTemplate->put_QuotaLimit failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Set the quota flags to enforce the quota. If a threshold is violated,
    // the data is not written. If the threshold specifies an action, FSRM 
    // performs the action. 
    hr = pTemplate->put_QuotaFlags(FsrmQuotaFlags_Enforce);
    if (FAILED(hr))
    {
        wprintf(L"pTemplate->put_QuotaFlags failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Add a threshold. When the storage usage reaches 85% of the quota,
    // the defined actions will be performed.
    hr = pTemplate->AddThreshold(85);
    if (FAILED(hr))
    {
        wprintf(L"pTemplate->AddThreshold failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Create an action to log an event when the threshold reaches 85%.
    // The event is logged to the Windows Logs\Application event log;
    // the event ID is 12325.
    hr = pTemplate->CreateThresholdAction(85, FsrmActionType_EventLog, &amp;pAction);
    if (FAILED(hr))
    {
        wprintf(L"pTemplate->CreateThresholdAction failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Get the IFsrmActionEventLog interface and specify the severity
    // level of the event and the event text.
    hr = pAction->QueryInterface(IID_IFsrmActionEventLog, (void**)&amp;pLog);

    hr = pLog->put_EventType(FsrmEventType_Information);
    if (FAILED(hr))
    {
        wprintf(L"pLog->put_EventType failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pLog->put_MessageText(_bstr_t(EVENT_TEXT));
    if (FAILED(hr))
    {
        wprintf(L"pLog->put_MessageText failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Save the template.
    hr = pTemplate->Commit();
    if (FAILED(hr))
    {
        wprintf(L"pTemplate->Commit failed, 0x%x.\n", hr);
        goto cleanup;
    }

cleanup:

    if (pqtm)
        pqtm->Release();

    if (pTemplate)
        pTemplate->Release();

    if (pAction)
        pAction->Release();

    if (pLog)
        pLog->Release();

    CoUninitialize();
}
```



 

 




