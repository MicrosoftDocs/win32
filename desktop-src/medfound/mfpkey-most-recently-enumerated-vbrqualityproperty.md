---
description: Specifies the VBR quality level of the most recently enumerated output type.
ms.assetid: 7d67e41f-060b-49a1-9e17-5db081ef4210
title: MFPKEY_MOST_RECENT_ENUMERATED_VBRQUALITY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_MOST\_RECENT\_ENUMERATED\_VBRQUALITY Property

Specifies the VBR quality level of the most recently enumerated output type. Read-only.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

**VT\_UI4**

## Remarks

When the encoder is acting as an Media Foundation Transform (MFT) and it enumerates an output type on a call to [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype), you can query the MFT for the **MFPKEY\_MOST\_RECENTLY\_ENUMERATED\_VBRQUALITY** property. The value returned indicates the VBR quality of the most recently returned output media type. Then you can use that value to set the [**MFPKEY\_DESIRED\_VBRQUALITY**](mfpkey-desired-vbrqualityproperty.md) property of the encoder.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows Vista or Windows 7<br/>                                                   |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md)
</dt> <dt>

[**MFPKEY\_CONSTRAIN\_ENUMERATED\_VBRQUALITY**](mfpkey-constrain-enumerated-vbrqualityproperty.md)
</dt> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
