---
description: Specifies whether the ASF media sink automatically adjusts the bit rate.
ms.assetid: 0a6f4dd4-4ad7-4aab-a33d-14b4716f9902
title: MFPKEY_ASFMEDIASINK_AUTOADJUST_BITRATE property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_ASFMEDIASINK\_AUTOADJUST\_BITRATE property

Specifies whether the ASF media sink automatically adjusts the bit rate.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**VARIANT\_BOOL**

VT\_BOOL

**boolVal**



## Remarks

If the value of this property is VARIANT\_TRUE, the ASF media sink automatically adjusts the bit rate of the ASF content in response to the characteristics of the streams being multiplexed.

This property affects how the ASF media sink behaves when a stream overflows the sink's "leaky bucket" parameters:



| Value              | Behavior                                                                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **VARIANT\_TRUE**  | The ASF media sink automatically adjusts the bit rate of the ASF content in response to the characteristics of the streams being multiplexed. |
| **VARIANT\_FALSE** | The ASF media sink uses the stream bit rate value provided by the application.                                                                |



 

The default value is **VARIANT\_FALSE**.

Set this property when you configure the ASF media sink. The usage depends on which function you call to create the ASF media sink:

-   [**MFCreateASFMediaSink**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfmediasink): Query the retrieved [**IMFMediaSink**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasink) pointer for the **IPropertyStore** interface.

-   [**MFCreateASFMediaSinkActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfmediasinkactivate): Call [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore) on the [**IMFASFContentInfo**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfcontentinfo) pointer specified in the *pContentInfo* parameter.

Setting this property to VARIANT\_TRUE causes the ASF media sink to set the **MFASF\_MULTIPLEXER\_AUTOADJUST\_BITRATE** flag on the ASF multiplexer. See [**IMFASFMultiplexer::SetFlags**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-setflags).

For more information about the leaky bucket concept, see the topic "The Leaky Bucket Buffer Model" in the Windows Media Format SDK documentation.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1**](mf-asfstreamconfig-leakybucket1-attribute.md)
</dt> <dt>

[**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET2**](mf-asfstreamconfig-leakybucket2-attribute.md)
</dt> </dl>

 

 




