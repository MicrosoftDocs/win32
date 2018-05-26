---
title: Defining a Quota
description: The following example shows how to derive a quota from the quota template created in Using Templates to Define Quotas.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b4471a75-f8c9-48aa-8ce3-1e998dbe6952
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , defining a quota
- quotas File Server Resource Manager
- defining quotas File Server Resource Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Defining a Quota

The following example shows how to derive a quota from the quota template created in [Using Templates to Define Quotas](using-templates-to-define-quotas.md).


```C++
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <FsrmQuota.h>  // quota objects
#include <FsrmTlb.h>    // Contains CLSIDs.


// Create a quota. Apply a template. Save the quota.

void wmain(void)
{
    HRESULT hr = S_OK;
    IFsrmQuotaManager* pqm = NULL;
    IFsrmQuota* pQuota = NULL;

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
        goto cleanup;
    }

    hr = pqm->CreateQuota(_bstr_t(L"c:\\folder\\B"), &amp;pQuota);
    if (FAILED(hr))
    {
        wprintf(L"pqm->CreateQuota failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pQuota->ApplyTemplate(_bstr_t(L"Test Quota Template"));
    if (FAILED(hr))
    {
        wprintf(L"pQuota->ApplyTemplate failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pQuota->Commit();
    if (FAILED(hr))
    {
        wprintf(L"pQuota->Commit failed, 0x%x.\n", hr);
        goto cleanup;
    }

cleanup:

    if (pqm)
        pqm->Release();

    if (pQuota)
        pQuota->Release();

    CoUninitialize();
}
```



 

 




