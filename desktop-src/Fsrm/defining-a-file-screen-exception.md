---
title: Defining a File Screen Exception
description: A file screen exception defines a list of file groups that are allowed in the directory and its subdirectories. Files with names that match the name patterns are not be blocked.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a046f092-5b6d-452d-826b-fd4b83c774fb'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["File Server Resource Manager examples File Server Resource Manager , defining a file screen exception", "file screen exceptions File Server Resource Manager", "defining file screen exceptions File Server Resource Manager"]
---

# Defining a File Screen Exception

A file screen exception defines a list of file groups that are allowed in the directory and its subdirectories. Files with names that match the name patterns are not be blocked. Typically, you apply an exception to a subdirectory of the directory that contains the file screen.

The following example shows how to add an exception to a subdirectory of a file screen path. The exception allow files that match a file pattern of a?c\*. This examples builds on the example in [Creating File Groups to Specify the Files to Restrict](creating-file-groups-to-specify-the-files-to-restrict.md) that restricts such files. The exception is applied to the file screen created in [Defining a File Screen](defining-a-file-screen.md), not the template.


```C++
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <FsrmScreen.h> // File screen and group objects
#include <fsrmtlb.h>    // For CLSIDs


// Add a file screen exception that allows files of the form a?c*.
void wmain(void)
{
    HRESULT hr = S_OK;
    IFsrmFileScreenManager* pfsm = NULL;
    IFsrmFileScreenException* pScreenException = NULL;
    IFsrmFileGroupManager* pfgm = NULL;
    IFsrmFileGroup* pFileGroup = NULL;
    IFsrmMutableCollection* pMembers = NULL;
    IFsrmMutableCollection* pAllowedList = NULL;
    VARIANT var;

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
    if (FAILED(hr))
    {
        wprintf(L"CoInitializeEx() failed, 0x%x.\n", hr);
        return;
    }


    // Create a file group and add the allowed file patterns to the group.
    hr = CoCreateInstance(CLSID_FsrmFileGroupManager, 
        NULL,
        CLSCTX_LOCAL_SERVER,
        __uuidof(IFsrmFileGroupManager),
        reinterpret_cast<void**> (&amp;pfgm));

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(FsrmFileGroupManager) failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pfgm->CreateFileGroup(&amp;pFileGroup);
    if (FAILED(hr))
    {
        wprintf(L"pfgm->CreateFileGroup failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Name the group. The name is used later when you add the group
 // to the list of allowed file groups.
    hr = pFileGroup->put_Name(_bstr_t(L"Exception Test"));
    if (FAILED(hr))
    {
        wprintf(L"pFileGroup->put_Name failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Get the collection of file name patterns that specify the files
    // to allow in the directory.
    hr = pFileGroup->get_Members(&amp;pMembers);
    if (FAILED(hr))
    {
        wprintf(L"pFileGroup->get_Members failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Add the pattern.
    VariantInit(&amp;var);
    V_VT(&amp;var) = VT_BSTR;
    var.bstrVal = SysAllocString(L"a?c*");

    hr = pMembers->Add(var);
    if (FAILED(hr))
    {
        wprintf(L"pMembers->Add failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pFileGroup->put_Members(pMembers);
    if (FAILED(hr))
    {
        wprintf(L"pFileGroup->put_Members failed, 0x%x.\n", hr);
        goto cleanup;
    }

    VariantClear(&amp;var);

    // Save the group.
    hr = pFileGroup->Commit();
    if (FAILED(hr))
    {
        wprintf(L"pFileGroup->Commit failed, 0x%x.\n", hr);
        goto cleanup;
    }

    
    // Create a file screen exception. The exception is added to a 
    // subdirectory of the file screen path. 
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

    hr = pfsm->CreateFileScreenException(_bstr_t(L"c:\\folderA\\folderB\\folderC"), &amp;pScreenException);
    if (FAILED(hr))
    {
        wprintf(L"pfsm->CreateFileScreenException failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Get the list of allowed file groups and add the new group 
    // defined above to the list.
    hr = pScreenException->get_AllowedFileGroups(&amp;pAllowedList);
    if (FAILED(hr))
    {
        wprintf(L"pScreenException->get_AllowedFileGroups failed, 0x%x.\n", hr);
        goto cleanup;
    }

    VariantInit(&amp;var);
    V_VT(&amp;var) = VT_BSTR;
    var.bstrVal = SysAllocString(L"Exception Test");

    hr = pAllowedList->Add(var);
    if (FAILED(hr))
    {
        wprintf(L"pAllowedList->Add failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pScreenException->put_AllowedFileGroups(pAllowedList);
    if (FAILED(hr))
    {
        wprintf(L"pScreenException->put_AllowedFileGroups failed, 0x%x.\n", hr);
        goto cleanup;
    }

    VariantClear(&amp;var);

    // Save the exception.
    hr = pScreenException->Commit();
    if (FAILED(hr))
    {
        wprintf(L"pScreenException->Commit failed, 0x%x.\n", hr);
        goto cleanup;
    }


cleanup:

    if (pfsm)
        pfsm->Release();

    if (pScreenException)
        pScreenException->Release();

    if (pAllowedList)
        pAllowedList->Release();

    if (pfgm)
        pfgm->Release();

    if (pFileGroup)
        pFileGroup->Release();

    if (pMembers)
        pMembers->Release();

    VariantClear(&amp;var);

    CoUninitialize();
}
```



 

 




