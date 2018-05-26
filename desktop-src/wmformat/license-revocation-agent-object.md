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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# License Revocation Agent Object

The license revocation agent object manages the client side of license revocation. License revocation is the process by which a license server can remove licenses from the license store on the client computer. The process involves passing several messages between the client application and the license server. The methods exposed on this object process and generate those messages.

The license revocation agent object is created by the [**WMCreateLicenseRevocationAgent**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatelicenserevocationagent?branch=master) function, which sets a pointer to an [**IWMLicenseRevocationAgent**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmlicenserevocationagent?branch=master) interface. **IUnknown** and **IWMLicenseRevocationAgent** are the only interfaces supported by this object.

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




