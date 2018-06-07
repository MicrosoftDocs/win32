---
Description: Specifies whether the encoder uses variable-bit-rate (VBR) encoding.
ms.assetid: e6826802-99b7-4a38-9b58-8a9cb8b753fb
title: MFPKEY\_VBRENABLED Property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_VBRENABLED Property

Specifies whether the encoder uses variable-bit-rate (VBR) encoding. Read-write.

## Constant for IPropertyBag

**g\_wszWMVCVBREnabled**, **g\_wszWMCPAudioVBRSupported**

## Data Type

**VT\_BOOL**

## Default Value

**VARIANT\_FALSE**

## Remarks

This value must be set to **VARIANT\_TRUE** for any of the other VBR properties to be used by the codec.

After you set this value to **VARIANT\_TRUE** on the audio encoder, the output types retrieved by using the [**IMediaObject::GetOutputType**](https://msdn.microsoft.com/a7652472-4091-4ecf-b623-5c6eb01be44a) method are VBR types.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[**MFPKEY\_CONSTRAIN\_ENUMERATED\_VBRQUALITY**](mfpkey-constrain-enumerated-vbrqualityproperty.md)
</dt> <dt>

[**MFPKEY\_DESIRED\_VBRQUALITY**](mfpkey-desired-vbrqualityproperty.md)
</dt> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




