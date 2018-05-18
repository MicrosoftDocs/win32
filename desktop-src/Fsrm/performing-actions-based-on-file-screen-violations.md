---
title: Performing Actions Based on File Screen Violations
description: When a file screen exception occurs, you can perform up to four unique actions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '45b16b46-7c03-4af5-889f-64047ec5ca98'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["File Server Resource Manager examples File Server Resource Manager , performing actions based on file screen violations", "file screen violations File Server Resource Manager"]
---

# Performing Actions Based on File Screen Violations

When a file screen exception occurs, you can perform up to four unique actions.

You can perform the following actions:

-   Send an email notification
-   Run a command
-   Log an event
-   Run a report

The following example shows how to create an email action. The *pTemplate* parameter is passed from the example in [Using Templates to Define File Screens](using-templates-to-define-file-screens.md).


```C++
// The body of the email message to send when the file screen is violated.
// The bracketed text are action variables. The bracketed text is substituted with
// the actual values at the time the action is performed (see IFileScreenManager::ActionVariables).
#define MESSAGE_TEXT \
    L"The [Source File Path] file violated the [Violated File Group] file group. The group applies " \
    L"to the [File Screen Path] directory and its descendant directories.\n\n" \
    L"Source File Owner: [Source File Owner]\n" \
    L"Source File Owner Email: [Source File Owner Email]\n" \
    L"Source IO Owner: [Source Io Owner]\n" \
    L"Source IO Owner Email: [Source Io Owner Email]\n" \
    L"Server: [Server]\n" \
    L"Server Domain: [Server Domain]\n" 


//
// Add an Email action to the template. The Email is sent when
// an IO operation violates the screen. For Email to work, all
// addresses (and the name of the SMTP server) have to be correct.
// To verify that the Email was sent, look in the C:\Inetpub\mailroot\Drop
// folder. Note that to specify a Microsoft Exchange email address,
// you need to setup forwarding from the SMTP server to Microsoft Exchange server;
// otherwise, the email action fails.
//
HRESULT AddAction(IFsrmFileScreenTemplate* pTemplate)
{
    HRESULT hr = S_OK;
    IFsrmAction* pAction = NULL;
    IFsrmActionEmail* pEmail = NULL;

    hr = pTemplate->CreateAction(FsrmActionType_Email, &amp;pAction);
    if (FAILED(hr))
    {
        wprintf(L"pTemplate->CreateAction failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Query for the Email action interface.
    pAction->QueryInterface(__uuidof(IFsrmActionEmail),
        reinterpret_cast<void**> (&amp;pEmail));

    // You only need to specify the MailFrom address if it is different
    // from the IFsrmSetting::MailFrom address.

    //hr = pEmail->put_MailFrom(_bstr_t(L"<USERGOESHERE>@<SMTPSERVERGOESHERE>"));
    //if (FAILED(hr))
    //{
    //  wprintf(L"pEmail->put_MailFrom failed, 0x%x.\n", hr);
    //  goto cleanup;
    //}

    hr = pEmail->put_MailTo(_bstr_t(L"<USERGOESHERE>@<SMTPSERVERGOESHERE>")); 
    if (FAILED(hr))
    {
        wprintf(L"pEmail->put_MailTo failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pEmail->put_MailSubject(_bstr_t(L"File Screen Violation"));
    if (FAILED(hr))
    {
        wprintf(L"pEmail->put_MailSubject failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pEmail->put_MessageText(_bstr_t(MESSAGE_TEXT));
    if (FAILED(hr))
    {
        wprintf(L"pEmail->put_MessageText failed, 0x%x.\n", hr);
        goto cleanup;
    }

cleanup:

    if (pAction)
        pAction->Release();

    if (pEmail)
        pEmail->Release();

    return hr;
}
```



 

 




