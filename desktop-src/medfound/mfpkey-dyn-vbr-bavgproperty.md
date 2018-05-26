---
Description: Specifies the buffer window, in milliseconds, for an encoder that is configured to use average-controllable VBR encoding.
ms.assetid: ce330ce0-4bda-4340-b21c-63a8b9168cf4
title: MFPKEY\_DYN\_VBR\_BAVG Property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFPKEY\_DYN\_VBR\_BAVG Property

Specifies the buffer window, in milliseconds, for an encoder that is configured to use average-controllable VBR encoding.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](properties.IPropertyStore).

## Data Type

**VT\_I4**

## Remarks

If the [**MFPKEY\_AVGCONSTRAINED**](mfpkey-avgconstrainedproperty.md) and [**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md) properties are both set to **VARIANT\_TRUE**, the encoder uses average-controllable VBR encoding. In that case, the encoder configures itself according to the value of this property and the [**MFPKEY\_DYN\_VBR\_RAVG**](mfpkey-dyn-vbr-ravgproperty.md) property.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




