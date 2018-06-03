---
title: Initializing and Binding a Pipeline Module
description: Pipeline modules must create and bind to a pipeline module connector when their IFsrmPipelineModuleImplementation OnLoad implementation is called. This can be done as the last step of any module initialization that is performed in the function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 92568969-7ee6-4584-a400-ee2aa79961e8
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , initializing and binding a pipeline module
- pipeline modules File Server Resource Manager
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Initializing and Binding a Pipeline Module

Pipeline modules must create and bind to a pipeline module connector when their [**IFsrmPipelineModuleImplementation::OnLoad**](/previous-versions/windows/desktop/api/fsrmpipeline/nf-fsrmpipeline-ifsrmpipelinemoduleimplementation-onload) implementation is called. This can be done as the last step of any module initialization that is performed in the function.

The following example shows how to create and bind to a pipeline module connector:


```C++
#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <atlbase.h>
#include <atlcom.h>
#include <FsrmQuota.h>  // quota objects
#include <FsrmTlb.h>    // Contains CLSIDs.
// <...>
STDMETHODIMP CCustomModule::OnLoad(
    IFsrmPipelineModuleDefinition   *pDefinition,
    IFsrmPipelineModuleConnector    **ppModuleConnector
    )
{
    HRESULT hr = S_OK;

    //
    //  ...perform module initialization...
    //

    //  Create the connector
    CComPtr<IFsrmPipelineModuleConnector> spConnector;
    hr = CoCreateInstance(CLSID_FsrmPipelineModuleConnector,
                          NULL,
                          CLSCTX_INPROC_SERVER,
                          __uuidof(IFsrmPipelineModuleConnector),
                          (LPVOID *)&amp;spConnector);
    if (FAILED(hr))
    {
        ATLTRACE(L"CoCreateInstance(FsrmPipelineModuleConnector) failed, 0x%x.\n", hr);
        goto cleanup;
    }

    CComQIPtr<IFsrmPipelineModuleImplementation> spModuleImpl = GetControllingUnknown();
    if (spModuleImpl == NULL)
    {
        ATLTRACE(L"GetControllingUnknown failed.\n");
        hr = E_OUTOFMEMORY;
        goto cleanup;
    }

    //  Bind the connector to the module
    hr = spConnector->Bind(pDefinition, spModuleImpl);
    if (FAILED(hr))
    {
        ATLTRACE(L"spConnector->Bind failed, 0x%x.\n", hr);
        goto cleanup;
    }

    //  Return the connector
    *ppModuleConnector = spConnector.Detach();

cleanup:

    return hr;
}
```



 

 




