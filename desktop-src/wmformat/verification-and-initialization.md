---
title: Verification and Initialization
description: Verification and Initialization
ms.assetid: e92abaa2-0bac-4c78-bda7-d118c4f5b332
keywords:
- Windows Media Format SDK,verification
- Windows Media Format SDK,initialization
- digital rights management (DRM),verification
- DRM (digital rights management),verification
- digital rights management (DRM),initialization
- DRM (digital rights management),initialization
- DRM Client Extended APIs,verification
- Client Extended APIs,verification
- DRM Client Extended APIs,initialization
- Client Extended APIs,initialization
ms.topic: article
ms.date: 05/31/2018
---

# Verification and Initialization

You should perform the following steps to verify that transcryption is allowed and to initialize an object that will decrypt the content:

1.  If you already have the Key ID for the content, skip to step 5.
2.  Call the [**WMCreateEditor**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateeditor) function to create a metadata editor object and get an instance of that object's [**IWMMetadataEditor**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmetadataeditor) interface.
3.  Call **IWMMetadataEditor::QueryInterface** to get an instance of the [**IWMDRMEditor**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmeditor) interface.
4.  Call [**IWMDRMEditor::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmeditor-getdrmproperty) to get the **DRM\_DRMHeader\_KeyID** property.
5.  Initialize the Windows Media DRM Client Extended APIs by calling the [**WMDRMStartup**](wmdrmstartup.md) function.
6.  Call the [**WMDRMCreateProtectedProvider**](wmdrmcreateprotectedprovider.md) function to create a secure provider object and get an instance of that object's [**IWMDRMProvider**](iwmdrmprovider.md) interface.
7.  Call [**IWMDRMProvider::CreateObject**](iwmdrmprovider-createobject.md) to create a license management object and get an instance of its [**IWMDRMLicenseManagement**](iwmdrmlicensemanagement.md) interface.
8.  Call [**IWMDRMLicenseManagement::CreateLicenseEnumeration**](iwmdrmlicensemanagement-createlicenseenumeration.md), passing in the Key ID and the right that governs the actions to be taken with the content after it is transcrypted. This call will retrieve an instance of the [**IWMDRMLicense**](iwmdrmlicense.md) interface that can be used to enumerate through any matching licenses.
9.  Call [**IWMDRMLicense::GetInclusionList**](iwmdrmlicense-getinclusionlist.md) to retrieve the list of authorized content protection systems (CPS) as specified by the license issuer.
10. Parse the inclusion list to confirm that the GUID of the output CPS is allowed by the license.
11. If the desired export GUID is not in the inclusion list, call [**IWMDRMLicense::GetNext**](iwmdrmlicense-getnext.md) to get the next applicable license (if any) and repeat steps 9 and 10. If no license has the desired GUID in its inclusion list, the export cannot be performed.
12. Call [**IWMDRMLicense::CreateSecureDecryptor**](iwmdrmlicense-createsecuredecryptor.md) to create a decryptor object. Pass in the export application certificate. This call will provide a pointer to an instance of the decryptor object's [**IWMDRMDecrypt**](iwmdrmdecrypt.md) interface and a binary object containing the seed. Only the Windows Media **DRM\_PROTECTION\_TYPE\_RC4** constant is supported as an argument to the *dwFlags* parameter at this time.
13. Use the RSA OAEP encryption scheme to decrypt the initialization vector.
14. Use the ASF parsing library provided by Microsoft when you enter into the Windows Media DRM export agreement, to locate the offset in bytes for each payload.

## Related topics

<dl> <dt>

[**Exporting Compressed Content**](exporting-compressed-content.md)
</dt> </dl>

 

 




