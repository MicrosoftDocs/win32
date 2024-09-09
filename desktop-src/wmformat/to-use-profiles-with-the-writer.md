---
title: To Use Profiles with the Writer
description: To Use Profiles with the Writer
ms.assetid: 8805bc57-5f19-4544-bcb8-5af880ba8ea0
keywords:
- Windows Media Format SDK,writing ASF files
- Windows Media Format SDK,creating ASF files
- Windows Media Format SDK,Advanced Systems Format (ASF)
- Advanced Systems Format (ASF),writing files
- ASF (Advanced Systems Format),writing files
- Advanced Systems Format (ASF),creating files
- ASF (Advanced Systems Format),creating files
- profiles,creating ASF files
- profiles,writing ASF files
- profiles,ASF file creation
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Use Profiles with the Writer

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The writer uses profile data to create ASF files. You must specify a profile for use before doing anything else with the writer.

You can set a system profile for use with the writer by passing the profile ID to the [**IWMWriter::SetProfileByID**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmwriter-setprofilebyid) method.

To specify a custom profile for use with the writer, you must obtain an [**IWMProfile**](iwmprofile.md) interface to an object containing the desired profile data. You can use one of the loading methods of the [**IWMProfileManager**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager) interface to accomplish this. After you have a valid **IWMProfile** interface, you can pass a pointer to it to the [**IWMWriter::SetProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setprofile) method. For more information about profile settings, see [Working with Profiles](working-with-profiles.md).

If you make changes to the profile object by using the **IWMProfile** interface after setting the profile in the writer, you must call **SetProfile** again, or else the changes will not be reflected in the writer. However, calling **SetProfile** will reset all header attributes, so be sure to set any required header attributes after calling this method.

The following example function sets the profile to "Windows Media Video 8 for Dial-up Modems (56 Kbps)":


```C++
#include <wmsysprf.h>

HRESULT SetProfileExample()
{
  HRESULT hr;
  IWMWriter *pWriter = NULL;
  hr = WMCreateWriter(NULL, &pWriter);
  if (FAILED(hr)) return hr;
  hr = pWriter->SetProfileByID(WMProfile_V80_56Video);
  return hr;
}

```



> [!Note]  
> There are no predefined system profiles that use the Windows Media Audio and Video 9 Series codecs. For more information, see [Reusing Stream Configurations](reusing-stream-configurations.md).

 

## Related topics

<dl> <dt>

[**IWMWriter::SetProfileByID**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmwriter-setprofilebyid)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




