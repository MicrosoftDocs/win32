---
title: IEnumTfRenderingMarkup interface
description: The IEnumTfRenderingMarkup interface is implemented by TSF Manager and used by applications. This interface can be retrieved by ITfContextRenderingMarkup GetRenderingMarkup and enumerates the rendering markup information.
ms.assetid: 6062a6f5-f973-4cd5-94d3-05aa418e0198
keywords:
- IEnumTfRenderingMarkup interface Text Services Framework
- IEnumTfRenderingMarkup interface Text Services Framework , described
topic_type:
- apiref
api_name:
- IEnumTfRenderingMarkup
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IEnumTfRenderingMarkup interface

The **IEnumTfRenderingMarkup** interface is implemented by TSF Manager and used by applications. This interface can be retrieved by [ITfContextRenderingMarkup::GetRenderingMarkup](itfcontextrenderingmarkup-getrenderingmarkup.md) and enumerates the rendering markup information.



| IEnumTfRenderingMarkup methods            | Description                                                                                                                                            |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Clone](ienumtfrenderingmarkup-clone.md) | The **IEnumTfRenderingMarkup::Clone** method creates a copy of the enumerator object.                                                                  |
| [Next](ienumtfrenderingmarkup-next.md)   | The **IEnumTfRenderingMarkup::Next** method obtains, from the current position, the specified number of elements in the enumeration sequence.          |
| [Reset](ienumtfrenderingmarkup-reset.md) | The **IEnumTfRenderingMarkup::Reset** method resets the enumerator object by moving the current position to the beginning of the enumeration sequence. |
| [Skip](ienumtfrenderingmarkup-skip.md)   | The **IEnumTfRenderingMarkup::Skip** method obtains, from the current position, the specified number of elements in the enumeration sequence.          |



 

## Members

The **IEnumTfRenderingMarkup** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Remarks

> [!Note]  
> This interface is not currently in the public header files. To use this API, you must MIDL-compile the [prototype](prototypes.md).

 

 

 