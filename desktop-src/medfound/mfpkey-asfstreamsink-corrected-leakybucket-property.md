---
description: Specifies the &\#0034;leaky bucket&\#0034; parameters for a stream on an ASF media sink.
ms.assetid: b01e59b6-0a7f-4125-867c-532385a27c15
title: MFPKEY_ASFSTREAMSINK_CORRECTED_LEAKYBUCKET property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_ASFSTREAMSINK\_CORRECTED\_LEAKYBUCKET property

Specifies the "leaky bucket" parameters (see Remarks) for a stream on an ASF media sink.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Array of **DWORD** values (**CAUL**)

VT\_VECTOR \| VT\_UI4

**caul**



## Remarks

An application can set this property on a stream of the ASF media sink after the media type for the stream is negotiated. Use this property to specify the actual buffer window that the Windows Media codec will use. You can obtain this information from the codec by using the **IWMCodecLeakyBucket** interface, which is documented in the Windows Media Format SDK.

The value of this property is an array of three **DWORD** values in the following order:

-   Bit rate, in bits per second.
-   Buffer size, in bytes.
-   Initial buffer fullness, in bytes.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[**IMFStreamSink**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamsink)
</dt> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




