---
title: Defining a File Screen
description: A file screen restricts the files that can be written to the directory and any of its descendant subdirectories.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b5227e7-4272-4e23-ba55-d6161e2987bc
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , defining a file screen
- file screens File Server Resource Manager
- defining file screens File Server Resource Manager
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Defining a File Screen

A file screen restricts the files that can be written to the directory and any of its descendant subdirectories. You can define the properties of the file screen directly or you can derive the properties from a file screen template. Typically, you want to derive the properties from a template.

The following example shows how to create a file screen and derive its properties from a template. The example derives the file screen from the template shown in [Using Templates to Define File Screens](using-templates-to-define-file-screens.md).


```C++
//
// Create a file screen. Initialize the screen using the Test Template template.
// Apply the screen to the c:\folderA\folderB path. The folderB folder will 
// be subject to this screen and any screen applied higher in the path.
//
HRESULT CreateScreen()
{
    HRESULT hr = S_OK;
    IFsrmFileScreenManager* pfsm = NULL;
    IFsrmFileScreen* pScreen = NULL;

    hr = CoCreateInstance(CLSID_FsrmFileScreenManager, 
        NULL,
        CLSCTX_LOCAL_SERVER,
        __uuidof(IFsrmFileScreenManager),
        reinterpret_cast<void**> (&amp;pfsm));

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(FsrmFileScreenManager) failed, 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Successfully created FileScreenManager object.\n");

    // Specify the path to which to apply the screen.
    hr = pfsm->CreateFileScreen(_bstr_t(L"c:\\folderA\\folderB"), &amp;pScreen);
    if (FAILED(hr))
    {
        wprintf(L"pfsm->CreateFileScreen failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pScreen->ApplyTemplate(_bstr_t(L"Test Template"));
    if (FAILED(hr))
    {
        wprintf(L"pScreen->ApplyTemplate failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pScreen->Commit();
    if (FAILED(hr))
    {
        wprintf(L"pScreen->Commit failed, 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Created screen.\n");

cleanup:

    if (pfsm)
        pfsm->Release();

    if (pScreen)
        pScreen->Release();

    return hr;
}]
```



 

 




