---
title: IWMDRMSecurity interface
description: The IWMDRMSecurity interface manages a variety of security-related information for the client computer and digital rights management (DRM) subsystem.To obtain an instance of this interface, call IWMDRMProvider CreateObject.
ms.assetid: 9439aedc-359d-4b2c-a88c-7b0e8eacb5a0
keywords:
- IWMDRMSecurity interface windows Media Format
- IWMDRMSecurity interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMSecurity
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IWMDRMSecurity interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IWMDRMSecurity** interface manages a variety of security-related information for the client computer and digital rights management (DRM) subsystem.

To obtain an instance of this interface, call [**IWMDRMProvider::CreateObject**](iwmdrmprovider-createobject.md). Pass **IID\_IWMDRMSecurity** as the *riid* parameter.

## Members

The **IWMDRMSecurity** interface inherits from [**IWMDRMEventGenerator**](iwmdrmeventgenerator.md). **IWMDRMSecurity** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMSecurity** interface has these methods.



| Method                                                                                      | Description                                                                                                      |
|:--------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**CheckCertForRevocation**](iwmdrmsecurity-checkcertforrevocation.md)                     | Determines whether a certificate has been revoked.<br/>                                                    |
| [**GetContentEnablersForRevocations**](iwmdrmsecurity-getcontentenablersforrevocations.md) | Retrieves content enabler interfaces that enable renewal of components based on revoked certificates.<br/> |
| [**GetContentEnablersFromHashes**](iwmdrmsecurity-getcontentenablersfromhashes.md)         | Retrieves content enabler interfaces that enable renewal of components based on hashed certificates.<br/>  |
| [**GetMachineCertificate**](iwmdrmsecurity-getmachinecertificate.md)                       | Retrieves the machine certificate of the DRM subsystem on the client computer.<br/>                        |
| [**GetRevocationData**](iwmdrmsecurity-getrevocationdata.md)                               | Retrieves a certificate revocation list from the local store.<br/>                                         |
| [**GetRevocationDataVersion**](iwmdrmsecurity-getrevocationdataversion.md)                 | Retrieves the version number of a certificate revocation list in the local store.<br/>                     |
| [**GetSecurityVersion**](iwmdrmsecurity-getsecurityversion.md)                             | Retrieves the version of the DRM subsystem on the client computer.<br/>                                    |
| [**PerformSecurityUpdate**](iwmdrmsecurity-performsecurityupdate.md)                       | Initiates a security update to the DRM subsystem on the client computer.<br/>                              |
| [**SetRevocationData**](iwmdrmsecurity-setrevocationdata.md)                               | Sets a certificate revocation list in the local store.<br/>                                                |



 

## See also

<dl> <dt>

[**DRM Individualization Example**](drm-individualization-example.md)
</dt> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> <dt>

[**IWMDRMEventGenerator**](iwmdrmeventgenerator.md)
</dt> </dl>

 

 





