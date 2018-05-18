---
Description: 'Base send time for the ASF media sink, in milliseconds.'
ms.assetid: '1b99845e-751a-4ec6-bd2d-e4644cd6863e'
title: 'MFPKEY\_ASFMEDIASINK\_BASE\_SENDTIME property'
---

# MFPKEY\_ASFMEDIASINK\_BASE\_SENDTIME property

Base send time for the ASF media sink, in milliseconds.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**ULONG**

VT\_UI4

**ulVal**



## Remarks

The send time is the time at which an ASF packet is sent across the network. It does not correspond directly to the presentation time of the data in the packet.

You can use this property to configure the ASF media sink. The usage depends on which function you call to create the ASF media sink:

-   [**MFCreateASFMediaSink**](mfcreateasfmediasink.md): Query the retrieved [**IMFMediaSink**](imfmediasink.md) pointer for the **IPropertyStore** interface.

-   [**MFCreateASFMediaSinkActivate**](mfcreateasfmediasinkactivate.md): Call [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](imfasfcontentinfo-getencodingconfigurationpropertystore.md) on the [**IMFASFContentInfo**](imfasfcontentinfo.md) pointer specified in the *pContentInfo* parameter.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




