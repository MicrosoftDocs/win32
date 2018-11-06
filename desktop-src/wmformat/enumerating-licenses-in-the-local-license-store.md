---
title: Enumerating Licenses in the Local License Store
description: Enumerating Licenses in the Local License Store
ms.assetid: 1f380b9e-85e4-4190-a809-65dfd4658b7c
keywords:
- Windows Media Format SDK,enumerating licenses
- Windows Media Format SDK,licenses
- Windows Media Format SDK,local license store
- digital rights management (DRM),enumerating licenses
- DRM (digital rights management),enumerating licenses
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- digital rights management (DRM),local license store
- DRM (digital rights management),local license store
- DRM Client Extended APIs,enumerating licenses
- Client Extended APIs,enumerating licenses
- DRM Client Extended APIs,licenses
- Client Extended APIs,licenses
- DRM Client Extended APIs,local license store
- Client Extended APIs,local license store
- licenses,enumerating
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Licenses in the Local License Store

Enumeration is a process of getting information about the licenses in the local license store, by stepping through them one by one. You can create a license enumeration by calling the [**IWMDRMLicenseManagement::CreateLicenseEnumeration**](iwmdrmlicensemanagement-createlicenseenumeration.md).

The most common reason for enumerating through licenses in the store is to find a particular license for decryption of some content.

The [**IWMDRMLicense**](iwmdrmlicense.md) interface serves as both a portal to the individual license results and as the enumerator. When the license enumeration is created, the first license in the list is loaded into the **IWMDRMLicense** interface. Most of the methods of **IWMDRMLicense** enable you to get information about the license or to create objects to encrypt or decrypt content based on the license. However, there are two methods that control the enumeration: [**GetNext**](iwmdrmlicense-getnext.md) and [**ResetEnumeration**](iwmdrmlicense-resetenumeration.md). **GetNext** loads the next license in the list into the interface. **ResetEnumeration** returns the enumeration to the state it was in when it was first created. When the enumeration is reset, the first license in the list is loaded back into the **IWMDRMLicense** interface.

When you have reached the last license in the list, the next call to **GetNext** returns ERROR\_NO\_MORE\_ITEMS.

If your application performs an action with the content that is covered by DRM, you should check the licenses in the local license store for the rights and for other limiting factors, such as output protection levels (OPLs).

## Related topics

<dl> <dt>

[**Getting Information from Licenses in the Local License Store**](getting-information-from-licenses-in-the-local-license-store.md)
</dt> </dl>

 

 




