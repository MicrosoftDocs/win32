---
description: Sets the root security identifier for the Microsoft Media Foundation HTTP byte stream.
ms.assetid: DD2B9487-53B0-4753-8C47-4D6BFE113109
title: MFPKEY_HTTP_ByteStream_Urlmon_Security_Id property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_HTTP\_ByteStream\_Urlmon\_Security\_Id property

Sets the root security identifier for the Microsoft Media Foundation HTTP byte stream.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**CAUB**

VT\_VECTOR \| VT\_UI1

**caub**



## Remarks

Use this property to configure the Media Foundation HTTP byte stream. To set the property, pass an [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

This property applies only when the [MFPKEY\_HTTP\_ByteStream\_Enable\_Urlmon](mfpkey-http-bytestream-enable-urlmon.md) property is set to **VARIANT\_TRUE**.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
