---
description: Starts the first encoding pass.
ms.assetid: a062be3f-7806-4f1c-b98e-2c9ed31f010c
title: AVEncCommonPassStart property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonPassStart property

Starts the first encoding pass.

This property is write-only.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncCommonPassStart**

## Property value

The value of this property is the encoding pass to start. To get the range of supported values, query the encoder's [**AVEncCommonMultipassMode**](avenccommonmultipassmode-property.md) property.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 




