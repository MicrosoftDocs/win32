---
title: IWMDRMLicense interface
description: The IWMDRMLicense interface represents a list of one or more licenses.
ms.assetid: afef7f9a-6621-4de7-bd40-3211c5c7ba09
keywords:
- IWMDRMLicense interface windows Media Format
- IWMDRMLicense interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMLicense
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IWMDRMLicense interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IWMDRMLicense** interface represents a list of one or more licenses.

## Members

The **IWMDRMLicense** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMDRMLicense** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMLicense** interface has these methods.



| Method                                                                                   | Description                                                                                                                                                                                                                        |
|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CanPersist**](iwmdrmlicense-canpersist.md)                                           | Queries whether the license can be persisted on in a local license store.<br/>                                                                                                                                               |
| [**CreateDecryptor**](iwmdrmlicense-createdecryptor.md)                                 | Creates a decryptor object using the settings of the current license.<br/>                                                                                                                                                   |
| [**CreateEncryptor**](iwmdrmlicense-createencryptor.md)                                 | Creates an encryptor object using the settings of the current license.<br/>                                                                                                                                                  |
| [**CreateSecureDecryptor**](iwmdrmlicense-createsecuredecryptor.md)                     | Creates a secure decryptor object. The secure decryptor differs from the normal decryptor in that it decrypts the content and then re-encrypts it according to the settings specified in the parameters of this method.<br/> |
| [**GetAnalogVideoRestrictionLevels**](iwmdrmlicense-getanalogvideorestrictionlevels.md) | Retrieves all analog video restrictions set on the current license.<br/>                                                                                                                                                     |
| [**GetInclusionList**](iwmdrmlicense-getinclusionlist.md)                               | Retrieves the entire inclusion list for the current license or license chain.<br/>                                                                                                                                           |
| [**GetLicense**](iwmdrmlicense-getlicense.md)                                           | Retrieves the license as Extensible Markup Language (XML) or Extensible Media Rights (XMR) data.<br/>                                                                                                                        |
| [**GetLicenseProperty**](iwmdrmlicense-getlicenseproperty.md)                           | Retrieves a property from the current license.<br/>                                                                                                                                                                          |
| [**GetNext**](iwmdrmlicense-getnext.md)                                                 | Loads the information about the next license in the list.<br/>                                                                                                                                                               |
| [**GetOutputProtectionLevels**](iwmdrmlicense-getoutputprotectionlevels.md)             | Retrieves information about all output protection levels (OPLs) assigned to the license.<br/>                                                                                                                                |
| [**PersistLicense**](iwmdrmlicense-persistlicense.md)                                   | Saves the current license from the temporary store into the permanent local license store.<br/>                                                                                                                              |
| [**ResetEnumeration**](iwmdrmlicense-resetenumeration.md)                               | Resets the license list to its original state.<br/>                                                                                                                                                                          |



 

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> </dl>

 

