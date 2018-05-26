---
title: Using Templates to Define File Screens
description: You can create file screens directly but typically you create file screen templates from which file screens derive. The template is used to modify properties in bulk by applying the changes to file screens that derive from the file screen template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c76c0cc5-1109-46ec-be4d-c6c5f14a6df7
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , using templates to define file screens
- templates for file screens File Server Resource Manager
- file screen templates File Server Resource Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Templates to Define File Screens

You can create file screens directly but typically you create file screen templates from which file screens derive. The template is used to modify properties in bulk by applying the changes to file screens that derive from the file screen template.

The following example shows how to create a file screen template. For details on applying the template to a file screen, see [Defining a File Screen](defining-a-file-screen.md).


```C++
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <fsrmscreen.h>  // File screen and group objects
#include <fsrmtlb.h>  // For CLSIDs
#include <fsrmerr.h>


HRESULT CreateTemplate();
HRESULT CreateGroup();
HRESULT AddAction(IFsrmFileScreenTemplate* pTemplate);


// This example creates a template on the local server. The examples calls the 
// CreateGroup function to add a file group to the template that blocks 
// specific file types. The CreateGroup function is not shown in this example but
// is included in the Creating File Groups to Specify the Files to Restrict topic. The 
// AddAction function is also not shown but is included in the Performing Actions Based 
// on File Screen Violations topic.

void wmain(void)
{
  HRESULT hr = S_OK;

  hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
  if (FAILED(hr))
  {
    wprintf(L"CoInitializeEx() failed, 0x%x.\n", hr);
    return;
  }

  // The CreateGroup function is not shown in this example but
  // is included in the Creating File Groups to Specify the Files to Restrict topic. 
  hr = CreateGroup();
  if (FAILED(hr))
  {
    wprintf(L"CreateGroup() failed, 0x%x.\n", hr);
    goto cleanup;
  }

  hr = CreateTemplate();
  if (FAILED(hr))
  {
    wprintf(L"CreateTemplate() failed, 0x%x.\n", hr);
    goto cleanup;
  }

cleanup:

  CoUninitialize();
}


//
// Create a new template. The template will exclude files from the "Test Group"
// file group.
//
HRESULT CreateTemplate()
{
  HRESULT hr = S_OK;
  IFsrmFileScreenTemplateManager* pfstm = NULL;
  IFsrmFileScreenTemplate* pTemplate = NULL;
  IFsrmMutableCollection* pCollection = NULL;
  VARIANT var;

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

  hr = pfstm->CreateTemplate(&amp;pTemplate);
  if (FAILED(hr))
  {
    wprintf(L"pfstm->CreateTemplate failed, 0x%x.\n", hr);
    goto cleanup;
  }

  // If the name already exists, the template will fail when you commit
  // the template, not when you name the template.
  hr = pTemplate->put_Name(_bstr_t(L"Test Template"));
  if (FAILED(hr))
  {
    wprintf(L"pTemplate->put_Name failed, 0x%x.\n", hr);
    goto cleanup;
  }

  hr = pTemplate->put_Description(_bstr_t(L"For testing file screen templates."));
  if (FAILED(hr))
  {
    wprintf(L"pTemplate->put_Description failed, 0x%x.\n", hr);
    goto cleanup;
  }

  // The default is to enforce the file screen (prevents IO operations that 
  // violate the screen). Disable enforcement so that IO does not fail. Note 
  // that the defined actions are still executed.
  hr = pTemplate->put_FileScreenFlags(0);
  if (FAILED(hr))
  {
    wprintf(L"pTemplate->put_FileScreenFlags failed, 0x%x.\n", hr);
    goto cleanup;
  }

  // For a new template, you need to get the collection, add groups
  // to the collection, and then put the collection.
  hr = pTemplate->get_BlockedFileGroups(&amp;pCollection);
  if (FAILED(hr))
  {
    wprintf(L"pTemplate->get_BlockedFileGroups failed, 0x%x.\n", hr);
    goto cleanup;
  }

  // Add the unique names of the file groups to add to the blocked files list.
  // A group defines the file patterns that are blocked from being written to 
  // the file screen path (and its descendants), depending on FileScreenFlags.
  // This example adds the "Test Group" file group created earlier.
  VariantInit(&amp;var);
  V_VT(&amp;var) = VT_BSTR;
  var.bstrVal = SysAllocString(L"Test Group");

  hr = pCollection->Add(var);
  if (FAILED(hr))
  {
    wprintf(L"pCollection->Add failed, 0x%x.\n", hr);
    goto cleanup;
  }

  hr = pTemplate->put_BlockedFileGroups(pCollection);
  if (FAILED(hr))
  {
    wprintf(L"pTemplate->put_BlockedFileGroups failed, 0x%x.\n", hr);
    goto cleanup;
  }

  // Add an action to the template. The action is executed if a file is 
  // written to the directory that violates the screen. The AddAction function is
  // included in the Performing Actions Based on File Screen Violations topic.
  hr = AddAction(pTemplate);
  if (FAILED(hr))
  {
    wprintf(L"AddAction failed, 0x%x.\n", hr);
    goto cleanup;
  }

  // Save the template to the database.
  hr = pTemplate->Commit();
  if (FAILED(hr))
  {
    wprintf(L"pTemplate->Commit failed, 0x%x.\n", hr);
    if (FSRM_E_ALREADY_EXISTS)
      wprintf(L"Template already exists\n");

    goto cleanup;
  }

  wprintf(L"Added template.\n");

cleanup:

  if (pfstm)
    pfstm->Release();

  if (pTemplate)
    pTemplate->Release();

  if (pCollection)
    pCollection->Release();

  VariantClear(&amp;var);

  return hr;
}
```



For details on updating a template and applying the changes to derived file screens, see [Updating a File Screen](updating-a-file-screen.md).

You could also copy an existing template and change the properties as appropriate. Note that FSRM defines several templates that you can use, however, they may not exist because users can delete these templates.

 

 




