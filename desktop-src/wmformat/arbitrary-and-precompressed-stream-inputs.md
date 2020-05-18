---
title: Arbitrary and Precompressed Stream Inputs
description: Arbitrary and Precompressed Stream Inputs
ms.assetid: 6debbae5-0c54-48db-9ef8-f84f74e2f090
keywords:
- Advanced Systems Format (ASF),arbitrary stream inputs
- ASF (Advanced Systems Format),arbitrary stream inputs
- profiles,arbitrary stream inputs
- codecs,arbitrary stream inputs
- Advanced Systems Format (ASF),precompressed stream inputs
- ASF (Advanced Systems Format),precompressed stream inputs
- profiles,precompressed stream inputs
- codecs,precompressed stream inputs
- precompressed stream inputs
- arbitrary stream inputs
- streams,arbitrary stream inputs
- streams,precompressed stream inputs
ms.topic: article
ms.date: 05/31/2018
---

# Arbitrary and Precompressed Stream Inputs

Only inputs that are to be compressed by one of the Windows Media codecs have multiple possible inputs. The other types of possible inputs are arbitrary inputs and precompressed inputs. The requirements for input formats for these types are described in this section.

## Arbitrary Stream Inputs

Inputs for arbitrary stream types are the same as the stream formats described in the profile. You should not have to set input formats for these types.

## Precompressed Stream Inputs

When copying a stream from one file to another, you pass samples that are already compressed. In this case, you must set the input properties object to **NULL** to inform the writer that it does not need to validate the data you are passing in. To set the input format to **NULL**, call [**IWMWriter::SetInputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setinputprops) and pass **NULL** as the second parameter. When calling this method with a **NULL** parameter, you must make the call before calling [**BeginWriting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-beginwriting).

When using precompressed streams, you must manually copy codec information to the file header before writing. To obtain the codec information, call [**IWMHeaderInfo2::GetCodecInfoCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmheaderinfo2-getcodecinfocount) and [**IWMHeaderInfo2::GetCodecInfo**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo2-getcodecinfo) to enumerate the codecs associated with the file in the reader. Select the codec information that matches the stream configuration of the precompressed stream. Then set the codec information in the writer by calling [**IWMHeaderInfo3::AddCodecInfo**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-addcodecinfo), passing the information obtained from the reader.

## Related topics

<dl> <dt>

[**Working with Inputs**](working-with-inputs.md)
</dt> </dl>

 

 




