---
description: Enables no frame ordering operation in the video decoder Media Foundation Transform.
ms.assetid: 3F5B106F-6BC2-4EE3-B7ED-8902C18F5351
title: MF_MT_VIDEO_NO_FRAME_ORDERING attribute (Mfapi.h)
ms.topic: reference
ms.date: 02/14/2025
---

# MF\_MT\_VIDEO_\_NO_\_FRAME_\_ORDERING attribute

MF_MT_VIDEO_NO_FRAME_ORDERING set to non-zero (true) implies external users/apps wish that MFT does not perform any frame reordering while decoding the input video bitstream,
that is, the output and display order is the same as the input and decoding order. It will overwrite bitstream syntaxes even if bitstream syntaxes do not indicate that the
output and display order is the same as the input and decoding order.

It is an attribute set on input media type and takes effect once when streaming begins. Call [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the [**MFT\_MESSAGE\_NOTIFY\_BEGIN\_STREAMING**](mft-message-notify-begin-streaming.md) message.

## Data type

**BOOL** stored as **UINT32**

### Example Code

The following code shows how to set the MF_MT_VIDEO_NO_FRAME_ORDERING property. The functionality within
SetNoFrameReorderOnInput should be called before 

```C++
HRESULT SetNoFrameReorderOnInput(
    const BOOL    bNoFrameReorder,
    IMFMediaType *inputType     // Pointer to the input media type.
    )
{
    HRESULT hr = S_OK;

    if (bNoFrameReorder)
    {
        hr = inputType->SetUINT32(MF_MT_VIDEO_NO_FRAME_ORDERING, 1);
        if (FAILED(hr))
        {
            goto done;
        }
    }
done:
    return hr;
}
```

## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

