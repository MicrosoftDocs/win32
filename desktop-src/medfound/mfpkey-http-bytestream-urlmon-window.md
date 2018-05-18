---
Description: 'Sets a window for the Microsoft Media Foundation HTTP byte stream.'
ms.assetid: '52761AC1-4974-4087-B5EE-A797F5BAD86D'
title: 'MFPKEY\_HTTP\_ByteStream\_Urlmon\_Window property'
---

# MFPKEY\_HTTP\_ByteStream\_Urlmon\_Window property

Sets a window for the Microsoft Media Foundation HTTP byte stream. The window is used to present information in the user interface during a bind operation.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**IUnknown\***

VT\_UNKNOWN

**punkVal**



## Remarks

Use this property to configure the Media Foundation HTTP byte stream. To set the property, pass an [**IPropertyStore**](properties.IPropertyStore) pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

The value of this property is a pointer to the **IWindowForBindingUI** interface. This property applies only when the [MFPKEY\_HTTP\_ByteStream\_Enable\_Urlmon](mfpkey-http-bytestream-enable-urlmon.md) property is set to **VARIANT\_TRUE**.

## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




