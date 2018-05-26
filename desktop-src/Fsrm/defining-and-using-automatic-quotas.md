---
title: Defining and Using Automatic Quotas
description: An automatic quota is used to automatically create a quota for each new subdirectory that is created under the directory to which the automatic quota is applied.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2727655d-11d7-4d23-838b-028c46ee79e4
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , defining and using automatic quotas
- quotas File Server Resource Manager
- automatic quotas File Server Resource Manager
- defining automatic quotas File Server Resource Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Defining and Using Automatic Quotas

An automatic quota is used to automatically create a quota for each new subdirectory that is created under the directory to which the automatic quota is applied. The automatic quota is also used to create a quota for all existing subdirectories under the specified directory that do not contain a quota.

For example, if you apply an automatic quota to *folder*, and folder contains subdirectories *A*, *B*, and *C*, FSRM creates a quota for *folder*\\*A* and *folder*\\*C*, assuming *folder*\\*B* already contains the quota created in [Defining a Quota](defining-a-quota.md). If later you add *folder*\\*D*, FSRM will create a quota for it.

To prevent FSRM from automatically creating a quota for one or more subdirectories, use the [**IFsrmAutoApplyQuota::ExcludeFolders**](/windows/previous-versions/FsrmQuota/nf-fsrmquota-ifsrmautoapplyquota-get_excludefolders?branch=master) property to specify the subdirectories.

An automatic quota differs from a quota in the following ways:

-   The automatic quota is not enforced on the directory to which it is applied.
-   The automatic quota must derive from a quota template.

For information on updating an automatic quota, see [Updating a Quota](updating-a-quota.md).

The following example shows how to create an automatic quota. Use the example in [Using Templates to Define Quotas](using-templates-to-define-quotas.md) to create a similar template, and name it "Test Automatic Quota Template".


```C++
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <FsrmQuota.h> // quota objects
#include <FsrmTlb.h>   // Contains CLSIDs.

// Create an automatic quota that derives from the Test Automatic 
// Quota Template template. Save the quota.

void wmain(void)
{
 HRESULT hr = S_OK;
 IFsrmQuotaManager* pqm = NULL;
 IFsrmAutoApplyQuota* pQuota = NULL;

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

 hr = pqm->CreateAutoApplyQuota(_bstr_t(L"Test Automatic Quota Template"), 
                                _bstr_t(L"c:\\folder"), &amp;pQuota);
 if (FAILED(hr))
 {
  wprintf(L"pqm->CreateAutoApplyQuota failed, 0x%x.\n", hr);
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



 

 




