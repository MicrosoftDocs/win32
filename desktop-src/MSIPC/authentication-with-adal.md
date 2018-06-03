---
title: How-to use ADAL authentication
description: Authentication with Azure RMS for your app using Azure Active Directory Authentication Library (ADAL).
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 2A3FC93C-7B21-4E3F-B9E3-494E7617B45B
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How-to: use ADAL authentication

Authentication with Azure RMS for your app using Azure Active Directory Authentication Library (ADAL).

By updating your application to use ADAL authentication rather than the Microsoft Online Sign-in Assistant, you and your customers will be able to:

<dl> Utilize multi-factor authentication  
Install the RMS 2.1 client without requiring administrative privileges to the machine  
Certify your application for Windows 10  
</dl>

## Two approaches to authentication

This topic contains two approaches to authentication with corresponding code examples.

-   **Internal authentication** - OAuth authentication managed by the RMS SDK.

    Use this approach if you want the RMS client to display an ADAL authentication prompt when authentication is necessary. For details on how to configure your application, see the section, "Internal authentication".

    > [!Note]  
    > If your application currently uses AD RMS SDK 2.1 with the sign-in assistant, we recommend that you use the *internal authentication* method as your application migration path.

     

-   **External authentication** - OAuth authentication managed by your application.

    Use this approach if you want your application to manage its own OAuth authentication. With this approach, the RMS client will exercise an application defined callback when authentication is necessary. For a detailed example, see "External authentication" at the end of this topic.

    > [!Note]  
    > External authentication does not imply the ability to change users; the RMS client always uses the default user for a given RMS tenant.

     

## Internal authentication

<dl> 1. Follow the Azure configuration steps in [Configure Azure RMS for ADAL authentication](internal-authentication-with-adal.md) then return to the following app initialization step.  
2. You are now ready to configure your application to use the internal ADAL authentication provided by the RMS SDK 2.1.  
To configure you RMS client, add a call to [**IpcSetGlobalProperty**](ipcsetglobalproperty.md) right after calling [**IpcInitialize**](ipcinitialize.md) to configure the RMS client. Use the following code snippet as an example.  


```C++
     

    IpcInitialize();

    IPC_AAD_APPLICATION_ID applicationId = { 0 };
    applicationId.cbSize = sizeof(IPC_AAD_APPLICATION_ID);
    applicationId.wszClientId = L"GUID-provided-by-AAD-for-your-app-(no-brackets)";
    applicationId.wszRedirectUri = L"RedirectionUriWeProvidedAADForOurApp://authorize";
    HRESULT hr = IpcSetGlobalProperty(IPC_EI_APPLICATION_ID, &amp;applicationId);
    if (FAILED(hr)) {
        //Handle the error
    }
```



</dl>

## External authentication

Use this code as an example of how to manage your own authentication tokens.


```C++
extern HRESULT GetADALToken(LPVOID pContext, const IPC_NAME_VALUE_LIST&amp; Parameters, __out wstring wstrToken) throw();

HRESULT GetLicenseKey(PCIPC_BUFFER pvLicense, __in LPVOID pContextForAdal, __out IPC_KEY_HANDLE &amp;hKey)
{
    IPC_OAUTH2_CALLBACK pfGetADALToken =
        [](LPVOID pvContext, PIPC_NAME_VALUE_LIST pParameters, IPC_AUTH_TOKEN_HANDLE* phAuthToken) -> HRESULT
    {
        wstring wstrToken;
        HRESULT hr = GetADALToken(pvContext, *pParameters, wstrToken);
        return SUCCEEDED(hr) ? IpcCreateOAuth2Token(wstrToken.c_str(), OUT phAuthToken) : hr;
    };

    IPC_OAUTH2_CALLBACK_INFO callbackCredentialContext =
    {
        sizeof(IPC_OAUTH2_CALLBACK_INFO),
        pfGetADALToken,
        pContextForAdal
    };

    IPC_CREDENTIAL credentialContext = 
    {
        IPC_CREDENTIAL_TYPE_OAUTH2,
        NULL
    };
    credentialContext.pcOAuth2 = &amp;callbackCredentialContext;

    IPC_PROMPT_CTX promptContext = 
    {
        sizeof(IPC_PROMPT_CTX),
        NULL,
        IPC_PROMPT_FLAG_SILENT | IPC_PROMPT_FLAG_HAS_USER_CONSENT,
        NULL,
        &amp;credentialContext
    };

    hKey = 0L;
    return IpcGetKey(pvLicense, 0, &amp;promptContext, NULL, &amp;hKey);
}
```



## Related topics

<dl> <dt>

[**Data types**](microsoft-information-protection-and-control-client-data-types.md)
</dt> <dt>

[**Environment properties**](environment-properties.md)
</dt> <dt>

[**IpcCreateOAuth2Token**](ipccreateoauth2token.md)
</dt> <dt>

[**IpcGetKey**](ipcgetkey.md)
</dt> <dt>

[**IpcInitialize**](ipcinitialize.md)
</dt> <dt>

[**IPC\_CREDENTIAL**](ipc-credential.md)
</dt> <dt>

[**IPC\_NAME\_VALUE\_LIST**](ipc-name-value-list.md)
</dt> <dt>

[**IPC\_OAUTH2\_CALLBACK\_INFO**](ipc-oath2-callback-info.md)
</dt> <dt>

[**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md)
</dt> <dt>

[**IPC\_AAD\_APPLICATION\_ID**](ipc-aad-application-id.md)
</dt> </dl>

 

 




