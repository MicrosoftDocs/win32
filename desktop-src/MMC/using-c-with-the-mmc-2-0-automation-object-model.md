---
title: Using C++ with the MMC 2.0 Automation Object Model
description: The following C++ code example is for a console application that uses the MMC 2.0 automation object model to programmatically start the MMC application, load a snap-in, set text on the status bar, and leave the user in control of the MMC console.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c527de98-1270-4437-93aa-1e103960e4fa
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using C++ with the MMC 2.0 Automation Object Model

The following C++ code example is for a console application that uses the MMC 2.0 automation object model to programmatically start the MMC application, load a snap-in, set text on the status bar, and leave the user in control of the MMC console.

## Example Code


```C++
////////////////////////////////////////////////////////////////
// This example is for a command line utility that starts
// MMC 2.0, loads a snap-in, sets text on the status bar,
// and leaves the user in control of the MMC console upon
// exit.
//
// A necessary link library is Mmc.lib.
////////////////////////////////////////////////////////////////

#define _WIN32_WINNT 0x0501

#include <mmcobj.h>
#include <stdio.h>

void __cdecl main()
{
    // MMC 2.0 automation object pointers.
    _Application * pApp = NULL;
    Document * pDoc = NULL;
    SnapIns * pSnapIns = NULL;
    SnapIn * pSnapIn = NULL;
    View * pView = NULL;

    // Local BSTRs.
    BSTR bstrSnapInName = NULL; // Used by Snapins::Add().
    BSTR bstrSBText = NULL;     // Used by View::put_StatusBarText().

    HRESULT    hr;

    // Initialize COM.
    hr = CoInitializeEx(NULL,
                        COINIT_APARTMENTTHREADED);

    // Check status.
    if (FAILED(hr))
    {
        printf("Failed CoInitializeEx - [%x]\n", hr);
        goto error;
    }

    // Create an instance of the MMC Application object.
    hr = CoCreateInstance( CLSID_Application,
                           NULL,
                           CLSCTX_LOCAL_SERVER,
                           IID__Application,
                           (void **)&amp;pApp);

    // Check status.
    if (FAILED(hr))
    {
        printf("Failed CoCreateInstance (pApp) [%x]\n", hr);
        goto error;
    }

    // Show the MMC application.
    hr = pApp->Show();
    if (FAILED(hr))
    {
        printf("Failed Application::Show() - [%x]\n", hr);
        goto error;
    }

    // Use the Application object to obtain the Document object.
    hr = pApp->get_Document(&amp;pDoc);
    if (FAILED(hr))
    {
        printf("Failed Application::get_Document - [%x]\n", hr);
        goto error;
    }

    // Use the Document object to obtain the SnapIns object.
    hr = pDoc->get_SnapIns(&amp;pSnapIns);
    if (FAILED(hr))
    {
        printf("Failed Document::get_SnapIns - [%x]\n", hr);
        goto error;
    }

    // With the SnapIns object now add a new snap-in.
    // This application adds the Folder snap-in, by name.
    // First, allocate a BSTR for the snap-in name.
    bstrSnapInName = SysAllocString(L"Folder");
    if (NULL == bstrSnapInName)
    {
        printf("Not enough memory\n");
        goto error;
    }
    // Two [optional] parameters are used in the call
    // to SnapIns::Add. In Visual Basic and VBScript, you may omit
    // these parameters. In C++ compilation, a variant is required
    // for these parameters. To cause MMC to ignore these parameters,
    // set the vt and scode members to VT_ERROR and DISP_E_PARAMNOTFOUND.
    VARIANT var1, var2;
    VariantInit(&amp;var1);
    VariantInit(&amp;var2);
    var1.vt = var2.vt = VT_ERROR;
    var1.scode = var2.scode =  DISP_E_PARAMNOTFOUND;
    // Use the SnapIns object to add the desired snap-in.
    hr = pSnapIns->Add(bstrSnapInName,
                   var1,        // No parent node specified.
                   var2,        // No properties specified.
                   &amp;pSnapIn);
    if (FAILED(hr))
    {
        printf("Failed SnapIns::Add(%S) - [%x]\n",
               bstrSnapInName,
               hr);
        goto error;
    }
    // Done using the variants, so they should be cleared.
    VariantClear(&amp;var1);
    VariantClear(&amp;var2);

    // Obtain the View object.
    hr = pDoc->get_ActiveView(&amp;pView);
    if (FAILED(hr))
    {
        printf("Failed Document::get_ActiveView - [%x]\n", hr);
        goto error;
    }
    
    // Use the View object to add text to the status bar.
    #define MySBText L"This is the left pane|middle pane|right pane"
    bstrSBText = SysAllocString(MySBText);
    if (NULL == bstrSnapInName)
    {
        printf("Not enough memory\n");
        goto error;
    }
    hr = pView->put_StatusBarText(bstrSBText);
    if (FAILED(hr))
    {
        printf("Failed View::put_StatusBarText - [%x]\n", hr);
        goto error;
    }

    // Leave the MMC application in user control.
    // If this call is omitted, then the MMC application
    // started by this example would be terminated when this
    // example ends.
    hr = pApp->put_UserControl(1);
    if (FAILED(hr))
    {
        printf("Failed Application::put_UserControl - [%x]\n", hr);
        goto error;
    }

error:

    // Done processing.
    // Clean up resources.
    if (NULL != pApp)
        pApp->Release();
    if (NULL != pDoc)
        pDoc->Release();
    if (NULL != pSnapIns)
        pSnapIns->Release();
    if (NULL != pSnapIn)
        pSnapIn->Release();
    if (NULL != pView)
        pView->Release();

    // Free BSTRs.
    if (NULL != bstrSnapInName)
        SysFreeString(bstrSnapInName); 
    if (NULL != bstrSBText)
        SysFreeString(bstrSBText); 

    // Free COM resources.
    CoUninitialize();

    printf("Finished processing\n");

}
```



 

 




