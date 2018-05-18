---
title: How-to enable your service application to work with cloud based RMS
description: This topic outlines steps for setting up your service application to use Azure Rights Management.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'EA1457D1-282F-4CF3-A23C-46793D2C2F32'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["azure", "cloud", "rms", "app", "rights"]
---

# How-to: enable your service application to work with cloud based RMS

This topic outlines steps for setting up your service application to use Azure Rights Management. For more information, see [Getting started with Azure Rights Management](https://technet.microsoft.com/library/jj585016.aspx).

> \[!Important\]
>
> In order to use your Rights Management Services SDK 2.1 service application with Azure RMS, you'll need to create your own tenants. For more information, see [Azure RMS requirements: Cloud subscriptions that support Azure RMS](https://docs.microsoft.com/rights-management/get-started/requirements-subscriptions)

 

## Prerequisites

-   RMS SDK 2.1 must be installed and configured. For more information, see [Getting started with RMS SDK 2.1](getting-started-with-ad-rms-2-0.md).
-   You must [create a service identity via ACS](https://msdn.microsoft.com/library/gg185924.aspx) by using the symmetric key option, or through other means, and record the key information from that process.

## Connecting to the Azure Rights Management Service

Call [**IpcInitialize**](ipcinitialize.md).

Set [**IpcSetGlobalProperty**](ipcsetglobalproperty.md).


```C++
int mode = IPC_API_MODE_SERVER;
IpcSetGlobalProperty(IPC_EI_API_MODE, &amp;(mode));
```



> [!Note]  
> For more information, see [Setting the API security mode](setting-the-api-security-mode--api-mode-.md)

 

The following steps are the setup for creating an instance of an [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure with the **pcCredential** ([**IPC\_CREDENTIAL**](ipc-credential.md)) member populated with connection information from the Azure Rights Management Service.

Use the information from your symmetric key service identity creation (see the prerequisites listed earlier in this topic) to set the **wszServicePrincipal**, **wszBposTenantId**, and **cbKey** parameters when you create an instance of an [**IPC\_CREDENTIAL\_SYMMETRIC\_KEY**](ipc-credential-symmetric-key.md) structure.

> [!Note]
>
> Due to an existing condition with our discovery service, if you are not in North America, symmetric key credentials are not accepted from other regions therefore, you must specify your tenant URLs directly. This is done through the [**IPC\_CONNECTION\_INFO**](ipc-connection-info.md) parameter of [**IpcGetTemplateList**](ipcgettemplatelist.md) or [**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md).
>
> **Generate a symmetric key and collect the needed information**
>
> Instructions to generate a symmetric key
>
> -   Install [Microsoft Online Sign-in Assistant](http://go.microsoft.com/fwlink/p/?LinkID=286152)
> -   Install [Azure AD PowerShell Module](https://bposast.vo.msecnd.net/MSOPMW/8073.4/amd64/AdministrationConfig-en.msi).
>     **Note**  You must be a tenant administrator to use the PowerShell cmdlets.
>
>      
>
> -   Start PowerShell and run the following commands to generate a key <dl> `Import-Module MSOnline`  
>     `Connect-MsolService` (type-in your admin credentials)  
>     `New-MsolServicePrincipal` (type-in a display name)  
>     </dl>
> -   After it generates a symmetric key, it will output information about key including the key itself and **AppPrincipalId**.
>
>     ``` syntax
>     The following symmetric key was created as one was not supplied 
>     ZYbF/lTtwE28qplQofCpi2syWd11D83+A3DRlb2Jnv8=
>
>     DisplayName : RMSTestApp
>     ServicePrincipalNames : {7d9c1f38-600c-4b4d-8249-22427f016963}
>     ObjectId : 0ee53770-ec86-409e-8939-6d8239880518
>     AppPrincipalId : 7d9c1f38-600c-4b4d-8249-22427f016963
>     ```
>
> Instructions to find out **TenantBposId** and **Urls**
>
> -   Install [Azure RMS PowerShell module](https://technet.microsoft.com/library/jj585012.aspx).
> -   Start PowerShell and run the following commands to get the RMS configuration of the tenant. <dl> `Import-Module aadrm`  
>     `Connect-AadrmService` (type-in your admin credentials)  
>     `Get-AadrmConfiguration`  
>     </dl>
>
>     The command will generate output, something like this:
>
>     ``` syntax
>     BPOSId                                    : 23976bc6-dcd4-4173-9d96-dad1f48efd42
>     RightsManagementServiceId                 : 1a302373-f233-4406-9090-4cdf305e2e76
>     LicensingIntranetDistributionPointUrl     : https://1a302373-f233-4406-9090-4cdf305e2e76.rms.na.aadrm.com/_wmcs/licensing
>     LicensingExtranetDistributionPointUrl     : https://1a302373-f233-4406-9090-4cdf305e2e76.rms.na.aadrm.com/_wmcs/licensing
>     CertificationIntranetDistributionPointUrl : https://1a302373-f233-4406-9090-4cdf305e2e76.rms.na.aadrm.com/_wmcs/certification
>     CertificationExtranetDistributionPointUrl : https://1a302373-f233-4406-9090-4cdf305e2e76.rms.na.aadrm.com/_wmcs/certification
>     ```
>
>  
>
> <span codelanguage="ManagedCPlusPlus"></span>
>
> <table>
> <colgroup>
> <col style="width: 100%" />
> </colgroup>
> <thead>
> <tr class="header">
> <th>C++</th>
> </tr>
> </thead>
> <tbody>
> <tr class="odd">
> <td><pre><code>// Create a key structure.
> IPC_CREDENTIAL_SYMMETRIC_KEY symKey = {0};
>
> // Set each member with information from service creation.
> symKey.wszBase64Key = &quot;your service principal key&quot;;
> symKey.wszAppPrincipalId = &quot;your app principal identifier&quot;;
> symKey.wszBposTenantId = &quot;your tenent identifier&quot;;</code></pre></td>
> </tr>
> </tbody>
> </table>
>
> 
>
> For more information see, [**IPC\_CREDENTIAL\_SYMMETRIC\_KEY**](ipc-credential-symmetric-key.md).
>
> Create an instance of an [**IPC\_CREDENTIAL**](ipc-credential.md) structure containing your [**IPC\_CREDENTIAL\_SYMMETRIC\_KEY**](ipc-credential-symmetric-key.md) instance.
>
> > [!Note]  
> > The *conectionInfo* members are set with URLs from the previous call to `Get-AadrmConfiguration` and noted here with those field names.
>
>  
>
> <span codelanguage="ManagedCPlusPlus"></span>
>
> <table>
> <colgroup>
> <col style="width: 100%" />
> </colgroup>
> <thead>
> <tr class="header">
> <th>C++</th>
> </tr>
> </thead>
> <tbody>
> <tr class="odd">
> <td><pre><code>// Create a credential structure.
> IPC_CREDENTIAL cred = {0};
>
> IPC_CONNECTION_INFO connectionInfo = {0};
> connectionInfo.wszIntranetUrl = LicensingIntranetDistributionPointUrl;
> connectionInfo.wszExtranetUrl = LicensingExtranetDistributionPointUrl;
>
> // Set each member.
> cred.dwType = IPC_CREDENTIAL_TYPE_SYMMETRIC_KEY;
> cred.pcCertContext = (PCCERT_CONTEXT)&amp;symKey;
>
> // Create your prompt control.
> IPC_PROMPT_CTX promptCtx = {0};
>
> // Set each member.
> promptCtx.cbSize = sizeof(IPC_PROMPT_CTX);
> promptCtx.hwndParent = NULL;
> promptCtx.dwflags = IPC_PROMPT_FLAG_SILENT;
> promptCtx.hCancelEvent = NULL;
> promptCtx.pcCredential = &amp;cred;</code></pre></td>
> </tr>
> </tbody>
> </table>
>
> 
>
> ## Identify a template and then encrypt
>
> -   Select a template to use for your encryption.
>
>     <dl> <dt>

 Call [**IpcGetTemplateList**](ipcgettemplatelist.md) passing in the same instance of [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md).
>
>     <span codelanguage="ManagedCPlusPlus"></span>
>     <table>
>     <colgroup>
>     <col style="width: 100%" />
>     </colgroup>
>     <thead>
>     <tr class="header">
>     <th>C++</th>
>     </tr>
>     </thead>
>     <tbody>
>     <tr class="odd">
>     <td><pre><code>PCIPC_TIL pTemplates = NULL; 
>     IPC_TEMPLATE_ISSUER templateIssuer = (pTemplateIssuerList-&gt;aTi)[0];
>
>     hr = IpcGetTemplateList(&amp;(templateIssuer.connectionInfo),
>            IPC_GTL_FLAG_FORCE_DOWNLOAD, 
>            0, 
>            &amp;promptCtx, 
>            NULL, 
>            &amp;pTemplates);</code></pre></td>
>     </tr>
>     </tbody>
>     </table>
>
>     
>
>     
</dt> </dl>
>
>     > \[!Tip\]  
>     > You could choose to specify a custom license handle by calling [**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md) and [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md) instead of calling [**IpcGetTemplateList**](ipcgettemplatelist.md).
>
>      
>
> -   With the template from earlier in this topic, call [**IpcfEncrcyptFile**](ipcfencryptfile.md), passing in the same instance of [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md).
>
>     Example use of [**IpcfEncrcyptFile**](ipcfencryptfile.md):
>
>     <span codelanguage="ManagedCPlusPlus"></span>
>     <table>
>     <colgroup>
>     <col style="width: 100%" />
>     </colgroup>
>     <thead>
>     <tr class="header">
>     <th>C++</th>
>     </tr>
>     </thead>
>     <tbody>
>     <tr class="odd">
>     <td><pre><code>LPCWSTR wszContentTemplateId = pTemplates-&gt;aTi[0].wszID;
>     hr = IpcfEncryptFile(wszInputFilePath, 
>            wszContentTemplateId, 
>            IPCF_EF_TEMPLATE_ID, 
>            IPC_EF_FLAG_KEY_NO_PERSIST, 
>            &amp;promptCtx, 
>            NULL, 
>            &amp;wszOutputFilePath);</code></pre></td>
>     </tr>
>     </tbody>
>     </table>
>
>     
>
>     Example use of [**IpcfDecryptFile**](ipcfdecryptfile.md):
>
>     <span codelanguage="ManagedCPlusPlus"></span>
>     <table>
>     <colgroup>
>     <col style="width: 100%" />
>     </colgroup>
>     <thead>
>     <tr class="header">
>     <th>C++</th>
>     </tr>
>     </thead>
>     <tbody>
>     <tr class="odd">
>     <td><pre><code>hr = IpcfDecryptFile(wszInputFilePath, 
>            IPCF_DF_FLAG_DEFAULT, 
>            &amp;promptCtx,
>            NULL,
>            &amp;wszOutputFilePath);</code></pre></td>
>     </tr>
>     </tbody>
>     </table>
>
>     
>
> You have now completed the steps needed to enable your application to use Azure Rights Management.
>
> ## Related topics
>
> <dl> <dt>

[Get started](getting-started-with-ad-rms-2-0.md)
</dt> <dt>

[Getting started with Azure Rights Management](https://technet.microsoft.com/library/jj585016.aspx)
</dt> <dt>

[Create a service identity via ACS](https://msdn.microsoft.com/library/gg185924.aspx)
</dt> <dt>

[**IpcSetGlobalProperty**](ipcsetglobalproperty.md)
</dt> <dt>

[**IpcInitialize**](ipcinitialize.md)
</dt> <dt>

[**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md)
</dt> <dt>

[**IPC\_CREDENTIAL**](ipc-credential.md)
</dt> <dt>

[**IPC\_CREDENTIAL\_SYMMETRIC\_KEY**](ipc-credential-symmetric-key.md)
</dt> <dt>

[**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md)
</dt> <dt>

[**IpcGetTemplateList**](ipcgettemplatelist.md)
</dt> <dt>

[**IpcfDecryptFile**](ipcfdecryptfile.md)
</dt> <dt>

[**IpcfEncrcyptFile**](ipcfencryptfile.md)
</dt> <dt>

[**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md)
</dt> <dt>

[**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md)
</dt> </dl>
>
>  
>
>  
>



