---
title: To Configure Quality-Based VBR
description: To Configure Quality-Based VBR
ms.assetid: 077a18c5-1895-4241-8c31-5f7caf38b22e
keywords:
- streams,configuring VBR streams
- streams,variable bit rate (VBR)
- variable bit rate (VBR),streams
- VBR (variable bit rate),streams
- streams,configuring quality-based VBR
- variable bit rate (VBR),configuring quality-based
- VBR (variable bit rate),configuring quality-based
- profiles,configuring quality-based VBR
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Configure Quality-Based VBR

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use quality-based variable bit rate (VBR) encoding on a stream to specify a quality level that will be maintained for the entire stream, regardless of the bit-rate requirements that result.

For quality-based VBR video streams, you must specify a quality level from 1 to 100, with 100 representing the highest quality. At present there are only 30 discrete quality settings. The following quality levels equate to discrete quality settings: 1, 4, 8, 11, 15, 18, 22, 25, 29, 33, 36, 40, 43, 47, 50, 54, 58, 61, 65, 68, 72, 75, 79, 83, 86, 90, 93, 97, 100. Numbers between two consecutive values in the preceding list equate to the same quality setting as the lower number. For example, 1 and 4 are listed, so 2 and 3 both result in the same quality setting as 1.

For audio streams, you can enumerate the available modes and retrieve a stream configuration object. For more information, see [To Enumerate Codec Formats](to-enumerate-codec-formats.md).

When using quality-based VBR video, you must set the **dwBitrate** member of the [**WMVIDEOINFOHEADER**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmvideoinfoheader) structure to a positive value. This value is not used by the writer, but passing zero or a negative number can cause errors when writing.

To configure a stream in a profile to be encoded with quality-based VBR, perform the following steps.

1.  Create a profile manager object by calling the [**WMCreateProfileManager**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager) function.
2.  Open an existing profile to which you want to add VBR support. For more information about opening profiles, see [Working with Profiles](working-with-profiles.md).
3.  Get a stream configuration object for the stream you want to use by calling either [**IWMProfile::GetStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream) or [**IWMProfile::GetStreamByNumber**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmprofile-getstreambynumber).
4.  Get a pointer to the [**IWMPropertyVault**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpropertyvault) interface of the stream configuration object by calling **IWMStreamConfig::QueryInterface**.
5.  Enable VBR for the stream by calling [**IWMPropertyVault::SetProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmpropertyvault-setproperty) for the **g\_wszVBREnabled** property.
6.  Set the quality level for the VBR stream by calling **IWMPropertyVault::SetProperty** for the **g\_wszVBRQuality** property.
7.  Set **g\_wszVBRBitrateMax** and **g\_wszVBRBufferWindowMax** both to zero with **IWMPropertyVault::SetProperty**.
8.  Save the changes made to the stream by calling [**IWMProfile::ReconfigStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-reconfigstream).
9.  Save the profile, or pass it to the writer object and start writing.

## Related topics

<dl> <dt>

[**Configuring VBR Streams**](configuring-vbr-streams.md)
</dt> </dl>

 

 




