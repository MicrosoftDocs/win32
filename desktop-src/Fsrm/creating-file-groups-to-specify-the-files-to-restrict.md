---
title: Creating File Groups to Specify the Files to Restrict
description: A file group is a logical collection of filename patterns identified by name which is used to define file screens and file screen exceptions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 951f5757-28fb-4583-9850-a11f60df05f5
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , creating file groups to specify files to restrict
- file groups File Server Resource Manager
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating File Groups to Specify the Files to Restrict

A file group is a logical collection of filename patterns identified by name which is used to define file screens and file screen exceptions. A filename pattern is a string expression that defines a set of filenames. The expression may contain the following wildcard characters: "\*" and "?". The "\*" wildcard matches 0 or more characters and the "?" wildcard matches exactly 1 character. For example, the filename "example.cpp" matches the pattern "e\*.cpp", but not "e?.cpp". The filename "ex.cpp" would match both patterns. Note that when the filename pattern is used to compare against a specific filename, the pattern match is case-insensitive.

A file group is formed by including all members and then excluding all non-members. For example, to list all files except for *FileA*, set members set to "\*.\*" and non-members to *FileA*.

File group definitions can also be used for generating storage report jobs based on file type. FSRM defines several groups that you can use, however, they may not exist because users can delete these groups.

The following example shows how to create a file group. To see how to apply the file group to a file screen template, see [Using Templates to Define File Screens](using-templates-to-define-file-screens.md).


```C++
//
// Creates a file group named "Test." The group contains
// a single file pattern that prevents files where the
// first letter is 'a' and the third letter is 'c'. However,
// the group allows files that begin 'abc'.
//
HRESULT CreateGroup()
{
    HRESULT hr = S_OK;
    IFsrmFileGroupManager* pfgm = NULL;
    IFsrmFileGroup* pGroup = NULL;
    IFsrmMutableCollection* pCollection = NULL;
    VARIANT var;

    hr = CoCreateInstance(CLSID_FsrmFileGroupManager, 
        NULL,
        CLSCTX_LOCAL_SERVER,
        __uuidof(IFsrmFileGroupManager),
        reinterpret_cast<void**> (&amp;pfgm));

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(FsrmFileGroupManager) failed, 0x%x.\n", hr);
        if (E_ACCESSDENIED == hr)
            wprintf(L"Access denied. You must run the client with an elevated token.\n");

        goto cleanup;
    }

    wprintf(L"Successfully created FileGroupManager object.\n");

    hr = pfgm->CreateFileGroup(&amp;pGroup);
    if (FAILED(hr))
    {
        wprintf(L"pfgm->CreateFileGroup failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // If the name already exists, the group will fail when you commit
    // the group, not when you name the group.
    hr = pGroup->put_Name(_bstr_t("Test Group"));
    if (FAILED(hr))
    {
        wprintf(L"pGroup->put_Name failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pGroup->put_Description(_bstr_t("Test group."));
    if (FAILED(hr))
    {
        wprintf(L"pGroup->put_Description failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Specify the files that are not excluded by the group. 
    // In this example, files that begin with abc are allowed.
    // Get the NonMembers collection, add the pattern, and then
    // put the NonMembers collection.
    hr = pGroup->get_NonMembers(&amp;pCollection);
    if (FAILED(hr))
    {
        wprintf(L"pGroup->get_NonMembers failed, 0x%x.\n", hr);
        goto cleanup;
    }

    VariantInit(&amp;var);
    V_VT(&amp;var) = VT_BSTR;
    var.bstrVal = SysAllocString(L"abc*");

    hr = pCollection->Add(var);
    if (FAILED(hr))
    {
        wprintf(L"pCollection->Add failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pGroup->put_NonMembers(pCollection);
    if (FAILED(hr))
    {
        wprintf(L"pGroup->put_NonMembers failed, 0x%x.\n", hr);
        goto cleanup;
    }

    pCollection->Release();
    pCollection = NULL;

    // Specify the files to excluded. In this example, files 
    // where the first letter is 'a' and the third letter is 'c'.
    // Get the Members collection, add the pattern, and then
    // put the Members collection.
    hr = pGroup->get_Members(&amp;pCollection);
    if (FAILED(hr))
    {
        wprintf(L"pGroup->get_Members failed, 0x%x.\n", hr);
        goto cleanup;
    }

    VariantClear(&amp;var);
    V_VT(&amp;var) = VT_BSTR;
    var.bstrVal = SysAllocString(L"a?c*");

    hr = pCollection->Add(var);
    if (FAILED(hr))
    {
        wprintf(L"pCollection->Add failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pGroup->put_Members(pCollection);
    if (FAILED(hr))
    {
        wprintf(L"pGroup->put_Members failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Save the group to the database.
    hr = pGroup->Commit();
    if (FAILED(hr))
    {
        wprintf(L"pGroup->Commit failed, 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Added group.\n");

cleanup:

    if (pfgm)
        pfgm->Release();

    if (pGroup)
        pGroup->Release();

    if (pCollection)
        pCollection->Release();

    VariantClear(&amp;var);

    return hr;
}
```



 

 




