---
title: Specifying the Actions To Be Performed
description: Specifying the Actions To Be Performed
ms.assetid: b6b094b1-276d-4f90-adc7-0f3507fdfe27
keywords:
- Advanced Systems Format (ASF),specifying actions
- ASF (Advanced Systems Format),specifying actions
- digital rights management (DRM),specifying actions
- DRM (digital rights management),specifying actions
ms.topic: article
ms.date: 05/31/2018
---

# Specifying the Actions To Be Performed

When you first call [**WMCreateReader**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatereader) to create the reader object, the second parameter is a bitwise **OR** of [**WMT\_RIGHTS**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_rights) values. Use this parameter to specify which action(s) the application will take on the first file to be opened. These actions correspond directly to rights that can be specified in the license. On subsequent calls to [**IWMReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-open), you can modify the rights that you are requesting by calling [**IWMDRMReader::SetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-setdrmproperty), specifying the defined constant for the [**DRM\_Rights**](drm-rights.md) property, and using string literals (of type **WCHAR**) separated by semicolons to identify the rights. The following code snippet requests four rights: play the file, copy it to a device, and play it as part of a collaborative playlist.


```C++
WCHAR wszRights[] = L"Play;Copy;CollaborativePlay";
p_WMDRMReader->SetDRMProperty(g_wszWMDRM_Rights, WMT_TYPE_STRING,
                              (BYTE*)wszRights, sizeof(wszRights));
```



> [!Note]  
> Do not confuse the [**DRM\_Rights**](drm-rights.md) property with the [**DRM\_Flags**](drm-flags.md) property, which is a **DWORD** used to specify which rights to apply to a local DRM version 1 license when copying content from a CD.

 

## Related topics

<dl> <dt>

[**Reading Protected Files**](reading-protected-files.md)
</dt> </dl>

 

 




