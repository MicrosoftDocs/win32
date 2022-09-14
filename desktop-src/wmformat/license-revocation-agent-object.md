---
title: License Revocation Agent Object
description: License Revocation Agent Object
ms.assetid: 19b0e697-1648-40e3-b6ef-c726905a47a2
keywords:
- Windows Media Format SDK,license revocation agent objects
- Advanced Systems Format (ASF),license revocation agent objects
- ASF (Advanced Systems Format),license revocation agent objects
- objects,license revocation agent objects
- license revocation,license revocation agent objects
ms.topic: article
ms.date: 05/31/2018
---

# License Revocation Agent Object

The license revocation agent object manages the client side of license revocation. License revocation is the process by which a license server can remove licenses from the license store on the client computer. The process involves passing several messages between the client application and the license server. The methods exposed on this object process and generate those messages.

The license revocation agent object is created by the [**WMCreateLicenseRevocationAgent**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatelicenserevocationagent) function, which sets a pointer to an [**IWMLicenseRevocationAgent**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlicenserevocationagent) interface. **IUnknown** and **IWMLicenseRevocationAgent** are the only interfaces supported by this object.

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




