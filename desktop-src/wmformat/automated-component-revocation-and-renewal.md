---
title: Automated Component Revocation and Renewal
description: Automated Component Revocation and Renewal
ms.assetid: be4899d7-1d87-4450-8c0e-75cf112ca66a
keywords:
- Windows Media Format SDK,automated revocation and renewal
- Windows Media Format SDK,revocation
- Windows Media Format SDK,renewal
- digital rights management (DRM),automated revocation and renewal
- DRM (digital rights management),automated revocation and renewal
- digital rights management (DRM),revocation
- DRM (digital rights management),revocation
- digital rights management (DRM),renewal
- DRM (digital rights management),renewal
- DRM Client Extended APIs,automated revocation and renewal
- Client Extended APIs,automated revocation and renewal
- DRM Client Extended APIs,revocation
- Client Extended APIs,revocation
- DRM Client Extended APIs,renewal
- Client Extended APIs,renewal
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Automated Component Revocation and Renewal

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Software applications or components that are considered compromised can be revoked by Microsoft. The Windows Media Format Client Extended API provides a mechanism for the automated revocation and renewal of components.

Revoked components are listed in a certificate revocation list, which is published by Microsoft. When a component is revoked, its certificate is added to the certificate revocation list, and the revocation information BLOB (REV\_INFO) is updated on the Microsoft servers.

To perform automated revocation and renewal when a user attempts to process Windows Media DRM protected content, your application must do the following:

1.  Extract the REV\_INFO version from the license. The REV\_INFO version number is located in the following location in an XMR license:
    ```C++
    <LICENSE version="2.0.0.0">
        <LICENSORINFO/>
        <DATA>
            <LID>...</LID>
            <KID>...</KID>
            <RevInfoVersion>42</RevInfoVersion>
            ...
         </DATA>
    ....
    </LICENSE>
    ```

    

2.  Compare the REV\_INFO version number of the license with the REV\_INFO version number in the local store by calling the [**IWMDRMSecurity::GetRevocationDataVersion**](iwmdrmsecurity-getrevocationdataversion.md) method.
3.  If the REV\_INFO version is not up to date, call the [**IWMDRMSecurity::PerformSecurityUpdate**](iwmdrmsecurity-performsecurityupdate.md) method, passing the WMDRM\_SECURITY\_PERFORM\_REVOCATION\_REFRESH flag in the *dwFlags* parameter.
4.  Retrieve the certificate revocation list from the local store by calling the [**IWMDRMSecurity::GetRevocationData**](iwmdrmsecurity-getrevocationdata.md) method.
5.  Parse the revocation list, and check for Windows Media DRM revocations. For more information, see [Checking Certificate Revocation](checking-certificate-revocation.md).
6.  If there are any Windows Media DRM revocations:
    1.  Create a content enabler to renew the revoked components by calling the [**IWMDRMSecurity::GetContentEnablersForRevocations**](iwmdrmsecurity-getcontentenablersforrevocations.md) method.
    2.  Call **IMFContentEnabler::AutomaticEnable** which directs the user to a URL that contains component renewal information. This method is documented in the [Media Foundation SDK](../medfound/microsoft-media-foundation-sdk.md) (https://msdn.microsoft.com/library/ms694197(VS.85).aspx).
        > [!Note]  
        > You must clarify this process to the user through the use of a privacy statement because the update process sends information from the client computer to a Microsoft Web site.

         

    3.  If possible, the user will renew the component from the URL, either automatically or by following specific instructions. There will be some situations in which the component cannot be renewed.
    4.  Try to access the content again until there are no more revocations, or the process is halted for some reason.

## Related topics

<dl> <dt>

[**Programming Guide**](drm-programming-guide.md)
</dt> </dl>

 

 