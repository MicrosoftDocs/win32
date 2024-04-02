---
description: Provides the encoder a hint as to what feature map capabilities will be used during the encode sequence.
title: CODECAPI_FeatureMapFlagsUsed property (Codecapi.h)
ms.topic: reference
ms.date: 03/29/2024
---

# CODECAPI\_FeatureMapFlagsUsed property

Provides the encoder a hint as to what feature map capabilities will be used during the encode sequence.

## Data type

**UINT32**

## Property GUID

**CODECAPI\_FeatureMapFlagsUsed**

## Property value

A bitwise OR combination of any of the flag values that are valid to set on the *flags* field in the MACROBLOCK_DATA structure.

## Remarks

**CODECAPI_FeatureMapFlagsUsed** is a UINT32 property that can be set on an encoder MFT using the [ICodecAPI::SetValue](/windows/win32/api/strmif/nf-strmif-icodecapi-setvalue) method to provide the encoder a hint as to what feature map capabilities will be used during the encode sequence. In this context, “sequence” means all frames processed between [MFT_MESSAGE_NOTIFY_BEGIN_STREAMING](/windows/win32/api/mftransform/ne-mftransform-mft_message_type) and [MF_MESSAGE_NOTIFY_END_STREAMING](/windows/win32/api/mftransform/ne-mftransform-mft_message_type). This enables encoders that support the property to make stream level optimizations based on the specified set of unused capabilities, if any.

The encoder MFT should assume that any flag specified this way may be used in the feature map passed to the encoder, and alternately, any flag not present will never appear in the feature map.  If **CODECAPI_FeatureMapFlagsUsed** is not set, then the encoder will use the default value, 0xFFFFFFFF, and  assume that all feature map flags may be used.

[ICodecAPI::GetParameterValues](/windows/win32/api/strmif/nf-strmif-icodecapi-getparametervalues) can be used with **CODECAPI_FeatureMapFlagsUsed** to query which feature map flags are supported by an encoder. Any values present in the returned UINT32-type VARIANT are values for the *flags* field in the **MACROBLOCK_DATA** structure that the encoder is capable of processing.

[ICodecAPI::IsSupported](/windows/win32/api/strmif/nf-strmif-icodecapi-issupported) can be used with CODECAPI_FeatureMapFlagsUsed to determine if the encoder recognizes the new property.


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




