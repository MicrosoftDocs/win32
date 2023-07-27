---
description: MPEG Decoder Preprocessing Transformations
ms.assetid: c7ae0137-0d02-46da-9532-738d805e327d
title: MPEG Decoder Preprocessing Transformations
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MPEG Decoder Preprocessing Transformations

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

**Letterbox and PanScan**

The 4x3 image can be formed by either padding the top and bottom of the image (referred to as a Letterbox image) or by extracting a 4x3 portion of the image (referred to as a PanScan image). The menus and subpicture streams are overlaid on top of the final video image. The 16x9 ratio images are stored in a 4x3 anamorphic format. Stretching the anamorphic 4x3 aspect ratio 720x480 source video to a 16x9 aspect ratio forms the original 16x9 aspect image.

Below is a description of how to correctly display each of the modes and their highlights:

-   **Widescreen:** The source video stretched into the largest 16x9 area of the output window. The highlights are relative to the inside of the 16x9 area. Black bars should be added to either the top and bottom or to the sides to maintain a 16x9 area.
-   **Pan Scan:** From the 16x9 video, use the horizontal offset provided in the MPEG2 stream to extract a 4x3 subwindow. Place the 4x3 subwindow into the largest 4x3 area of the output client window. The highlight's coordinates are relative to the 4x3 output window and have no relationship to the source 16x9 video. Black bars should be added to either the top and bottom or to the sides to maintain a 4x3 area.
-   **Letterbox:** Compute the largest 4x3 area of the output window. Black bars should be added to either the top and bottom or to the sides to maintain a 4x3 area. The source anamorphic 4x3 video (representing a 16x9 image) is placed in the largest 16x9 subwindow inside of the 4x3 area. Black bars should be added to the top and bottom of the subwindow to maintain a 16x9 area. The highlight's coordinates are relative to the 4x3 area and have no relationship to the source 16x9 video. It is possible for a disk to specify a highlight that lies outside of the 16x9 area (but still in the 4x3 window). For 4x3 video, the video is placed in the largest 4x3 output area of the output client window. Black bars should be added to either the top and bottom or to the sides to maintain a 4x3 area.

**MPEG preprocessing with the DVD Navigator and VMR**

Currently, the decoder is passed a FORMAT\_MPEG2\_VIDEO media type (whose format block points to a [**MPEG2VIDEOINFO**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-mpeg2videoinfo) structure). On the output pins, the decoder produces a FORMAT\_VideoInfo2 media type, whose format block points to a [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) structure. The structure's **dwReserved** field has been renamed to **dwControls** flags.

The **dwControlFlags** member will now contain the new bits.



| Label | Value |
|--------------------------|------------|
| AMCONTROL\_USED          | 0x00000001 |
| AMCONTROL\_PAD\_TO\_4x3  | 0x00000002 |
| AMCONTROL\_PAD\_TO\_16x9 | 0x00000004 |



 

AMCONTROL\_USED is used to test whether these new flags are supported. A source filter should set the AMCONTROL\_USED flag and see if QueryAccept(MediaType) succeeds on the downstream pin. If it is rejected, then the AMCONTROL flags cannot be used and dwReserved1 must be set to 0.

AMCONTROL\_PAD\_TO\_4x3 indicates that the image should be padded and displayed in a 4x3 area.

AMCONTROL\_PAD\_TO\_16x9 indicates that the image should be padded and displayed in a 16x9 area.

The decoder should either blindly copy or process the bits. If the decoder performs letterboxing itself, then it must alter the pixel aspect ratio, pad the image and remove the corresponding AMCONTROL\_\* bits.

The MPEG2VIDEOINFO.dwFlags now contains three flags for controlling for controlling how the content should be displayed:

-   `AMMPEG2_DoPanScan (0x00000001)`: If this flag is set, the MPEG-2 video decoder should crop the output image based on pan-scan vectors in picture\_display\_extension and change the picture aspect ratio to 4x3. The VMR should not receive a 16x9 sample with this flag. A simple implementation might alter the source rectangle to indicate a 540 wide source region with a left edge equal to the display offset in the picture\_display\_extension.
-   `AMMPEG2_LetterboxAnalogOut (0x00000020)`: When a hardware decoder displays this stream to a video output (usually an SVIDEO connector on the card), it should apply the rules for displaying a 16x9 sample on a 4x3 display.

    A software decoder (or a hardware decoder producing output sent to the VMR) has two options when processing images:

    1.  Ignore this flag and pass the VideoInfoHeader2 contents to the VMR (the AMCONTROL\_PAD\_TO\_4x3 flag will already be set by the [DVD Navigator](dvd-navigator-filter.md) on the sample). The VMR will encounter a 16x9 video sample with the AMCONTROL\_PAD\_TO\_4x3 flag set and a 4x3 subpicture stream. The application must set the output normalized destination rectangles of the two streams to be the same width.
    2.  Convert the anamorphic stream to a 4x3 image by padding the top and bottom of the image and setting the image aspect ratio to 4x3 (see Letterbox above) and removing the AMCONTROL\_PAD\_TO\_4x3 bit from the VIDEOINFOHEADER2.

    DirectXVA decoders that blend the video and subpicture streams will have to process this flag. If the hardware cannot scale the blended subpicture, then the decoder should produce a separate subpicture stream for the VMR to blend with the video.

-   `AMMPEG2_WidescreenAnalogOut (0x00000200)`: When a hardware decoder displays this stream to a video output (usually an SVIDEO connector on the card), it should assume a 16x9 (anamorphic) display.

    A software decoder (or a hardware decoder producing output sent to the VMR) has two options when processing an anamorphic image:

    1.  Ignore this flag and copy the VideoInfoHeader2 contents to the VMR. The VMR will pad 4x3 images to 16x9 if they have the AMCONTROL\_PAD\_TO\_16x9 set.
    2.  Pad the output image to a 16x9 image and remove the AMCONTROL\_PAD\_TO\_16x9 bit.

Most decoders should use **GetMediaType** to detect a media change on the input pin and copy the **VIDEOINFOHEADER2** contents (contained in the **MPEG2INFOHEADER**) to the output pin. They will probably only process the PanScan bit.

The following example code shows how to copy the **VIDEOINFOHEADER2** contents from an input pin to an output pin.


```C++
#include <dvdmedia.h>
HRESULT CopyMPeg2ToVideoInfoHeader2(CMediaSample* pInSample, CMediaSample* pOutSample)
{
    HRESULT hr = S_OK;
    // Check for a media type on the input sample.
    AM_MEDIA_TYPE* pInType;
    if (pInSample->GetMediaType(&pInType) == S_OK) 
    {
        // Make sure it's an MPEG2 Video format.
        if ((pInType->formattype == FORMAT_MPEG2_VIDEO) &&
            (pInType->cbFormat >= sizeof(MPEG2VIDEOINFO)))
        {
            hr = S_OK; // Initialize hr for the CMediaType constructor.
            CMediaType outType(*pInType, &hr);
            if (FAILED(hr))
            {
                DeleteMediaType( pInType );
                return hr;
            }

            // Set the format type GUID.
            outType.SetFormatType(&FORMAT_VideoInfo2);
                
            // Truncate the format block to include just the VIDEOINFOHEADER part.
            MPEG2VIDEOINFO *pMPeg2Header = (MPEG2VIDEOINFO*)pInType->pbFormat;
            BYTE *pVIH = (BYTE*)&pMPeg2Header->hdr;
            hr = (outType.SetFormat(pVIH, sizeof(VIDEOINFOHEADER2)) ? S_OK : E_OUTOFMEMORY);
            if (SUCCEEDED(hr))
            {
                hr = pOutSample->SetMediaType(&outType);
            }
        } 
        else 
        {
            ASSERT(FALSE); // Not a MPEG2 header.
            hr = VFW_E_INVALIDMEDIATYPE;
        }
        DeleteMediaType( pInType );
    } 

    return hr;
}
```



 

 



