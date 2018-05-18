---
Description: 'Specifies how the ASF media sink should apply Windows Media DRM.'
ms.assetid: '5f81294b-859a-4325-98dd-6267c736e1f1'
title: 'MFPKEY\_ASFMEDIASINK\_DRMACTION property'
---

# MFPKEY\_ASFMEDIASINK\_DRMACTION property

Specifies how the ASF media sink should apply Windows Media DRM.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**ULONG**

VT\_UI4

**ulVal**



## Remarks

The value of this property is a member of the [**MFSINK\_WMDRMACTION**](mfsink-wmdrmaction.md) enumeration.

You can use this attribute to configure the ASF media sink. The usage depends on which function you call to create the ASF media sink:

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

 

 




