---
title: Getting Current Usage Values
description: The following example shows how to get the usage and peak usage values for a directory that is limited by a quota.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7b755410-5520-4933-8859-9c201cbd13eb
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , getting current usage values
- usage values File Server Resource Manager
- peak usage values File Server Resource Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Getting Current Usage Values

The following example shows how to get the usage and peak usage values for a directory that is limited by a quota.


```C++
#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <FsrmQuota.h>  // Quota objects
#include <FsrmTlb.h>    // Contains CLSIDs.

// Get the usage and peak usage values for a directory.

void wmain(void)
{
    HRESULT hr = S_OK;
    IFsrmQuotaManager* pqm = NULL;
    IFsrmQuota* pQuota = NULL;
    VARIANT var;
    DATE date;
    SYSTEMTIME st;

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
    if (FAILED(hr))
    {
        wprintf(L"CoInitializeEx() failed, 0x%x.\n", hr);
        return;
    }

    hr = CoCreateInstance(CLSID_FsrmQuotaManager, 
        NULL,
        CLSCTX_LOCAL_SERVER,
        __uuidof(IFsrmQuotaManager),
        reinterpret_cast<void**> (&amp;pqm));

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(FsrmQuotaManager) failed, 0x%x.\n", hr);
        if (E_ACCESSDENIED == hr)
            wprintf(L"Access denied. You must run the client with an elevated token.\n");

        goto cleanup;
    }

    // Get the quota that applies to the specified directory.
    hr = pqm->GetQuota(_bstr_t(L"c:\\folder\\A"), &amp;pQuota);
    if (FAILED(hr))
    {
        wprintf(L"pqm->GetQuota failed, 0x%x.\n", hr);
        goto cleanup;
    }

    VariantInit(&amp;var);

    // Get the quota limit.
    hr = pQuota->get_QuotaLimit(&amp;var);
    if (FAILED(hr))
    {
        wprintf(L"pQuota->get_QuotaLimit failed, 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Limit: %I64u\n", var.ullVal);
    VariantClear(&amp;var);

    // Get the amount of disk space usage charged to this quota.
    hr = pQuota->get_QuotaUsed(&amp;var);
    if (FAILED(hr))
    {
        wprintf(L"pQuota->get_QuotaUsed failed, 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Used: %I64u\n", var.ullVal);
    VariantClear(&amp;var);

    // Get the highest amount of disk space usage charged to this quota.
    hr = pQuota->get_QuotaPeakUsage(&amp;var);
    if (FAILED(hr))
    {
        wprintf(L"pQuota->get_QuotaPeakUsage failed, 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"PeakUsage: %I64u\n", var.ullVal);

    // Get the date and time when the peak usage occurred.
    hr = pQuota->get_QuotaPeakUsageTime(&amp;date);
    if (FAILED(hr))
    {
        wprintf(L"pQuota->get_QuotaPeakUsageTime failed, 0x%x.\n", hr);
        goto cleanup;
    }

    if (VariantTimeToSystemTime(date, &amp;st))
        wprintf(L"Peak usage occurred on %d\\%d\\%d at %d:%d", st.wMonth, st.wDay, st.wYear, st.wHour, st.wMinute);

cleanup:

    if (pqm)
        pqm->Release();

    if (pQuota)
        pQuota->Release();

    VariantClear(&amp;var);

    CoUninitialize();
}
```



 

 




