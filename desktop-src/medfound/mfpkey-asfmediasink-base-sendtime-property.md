---
Description: Base send time for the ASF media sink, in milliseconds.
ms.assetid: 1b99845e-751a-4ec6-bd2d-e4644cd6863e
title: MFPKEY\_ASFMEDIASINK\_BASE\_SENDTIME property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

-   [**MFCreateASFMediaSink**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreateasfmediasink?branch=master): Query the retrieved [**IMFMediaSink**](/windows/win32/mfidl/nn-mfidl-imfmediasink?branch=master) pointer for the **IPropertyStore** interface.

-   [**MFCreateASFMediaSinkActivate**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreateasfmediasinkactivate?branch=master): Call [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore?branch=master) on the [**IMFASFContentInfo**](/windows/win32/wmcontainer/nn-wmcontainer-imfasfcontentinfo?branch=master) pointer specified in the *pContentInfo* parameter.

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

 

 




