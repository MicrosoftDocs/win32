---
description: Specifies the complexity profile of the encoded content.
ms.assetid: 2e238d31-98b2-4c79-96b0-9e6949010a73
title: MFPKEY_DECODERCOMPLEXITYPROFILE Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_DECODERCOMPLEXITYPROFILE Property

Specifies the complexity profile of the encoded content.

## Constant for IPropertyBag

g\_wszWMVCDecoderComplexityProfile

## Data Type

**VT\_BSTR**

## Remarks

You can read this value only after encoding is completed.

For audio, this property has one of the following values.



| Value | Description                                                                                    |
|-------|------------------------------------------------------------------------------------------------|
| "L1"  | Standard encoding with a sampling rate of 44.1 KHz and a maximum bit rate of 161 Kbps.         |
| "L2"  | Standard encoding with sampling rates up to 48 KHz and a maximum bit rate of 161 Kbps.         |
| "L3"  | Standard encoding with sampling rates up to 48 KHz and a maximum bit rate of 385 Kbps.         |
| "M0a" | Professional encoding with sampling rates up to 48 KHz and bit rates between 48 and 192 Kbps.  |
| "M0b" | Professional encoding with sampling rates up to 48 KHz and a maximum bitrate of 192 Kbps.      |
| "M1"  | Professional encoding with sampling rates up to 48 KHz and a maximum bitrate of 384 Kbps.      |
| "M2"  | Professional encoding with sampling rates up to 96 KHz and a maximum bitrate of 768 Kbps.      |
| "M3"  | Professional encoding with sampling rates up to 96 KHz and a maximum bitrate of 1.5 Mbps.      |
| "N1"  | Lossless encoding with sampling rates up to 48 KHz and a maximum of 2 channels.                |
| "N2"  | Lossless encoding with sampling rates up to 96 KHz and a maximum of 6 channels (5.1 surround). |
| "N3"  | Lossless encoding with sampling rates up to 96 KHz and a maximum of 8 channels (7.1 surround). |



 

For video, this property has one of the following values:



| Value | Description                                                                       |
|-------|-----------------------------------------------------------------------------------|
| "AP"  | advanced profile (available only on Windows Media Video 9 Advanced Profile codec) |
| "CP"  | no longer supported                                                               |
| "MP"  | main profile                                                                      |
| "SP"  | simple profile                                                                    |



 

For video content, you can request a profile level by setting [MFPKEY\_DECODERCOMPLEXITYREQUESTED](mfpkey-decodercomplexityrequestedproperty.md) before you begin encoding. The codec will attempt to encode within the parameters of the requested complexity level, but the other settings that you configure will take precedence. You should always check the actual complexity profile value after encoding in case your request could not be honored.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




