---
Description: 'Specifies whether a Media Foundation transform (MFT) supports dynamic format changes.'
ms.assetid: '64d32c78-8bee-4d3c-a770-5a097cb71b13'
title: 'MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE attribute'
---

# MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE attribute

Specifies whether a Media Foundation transform (MFT) supports dynamic format changes.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute can have the following values.



| Value     | Description                                                            |
|-----------|------------------------------------------------------------------------|
| **TRUE**  | The client can change the input format during streaming.               |
| **FALSE** | The MFT must be drained before the client can change the input format. |



 

To get this attribute, first call [**IMFTransform::GetAttributes**](imftransform-getattributes.md) to get the global attribute store for the MFT. Then call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md) to get the attribute value.

If [**GetAttributes**](imftransform-getattributes.md) fails or the attribute is not present, the default value if **FALSE**.

[Asynchronous MFTs](asynchronous-mfts.md) must return the value **TRUE**.

For more information, see [Handling Stream Changes](handling-stream-changes.md).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Asynchronous MFTs](asynchronous-mfts.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFTransform**](imftransform.md)
</dt> </dl>

 

 




