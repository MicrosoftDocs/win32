---
title: Direct2D Constants
description: Direct2D defines the following list of constants.
ms.assetid: 98a443af-4bb7-486d-bc87-ff34c3671bdd
topic_type:
- apiref
api_name:
- D2D1_DEFAULT_FLATTENING_TOLERANCE
- D2D1_INVALID_TAG
- D2D1_INVALID_PROPERTY_INDEX
- D2D1_APPEND_ALIGNED_ELEMENT
api_location:
- d2d1.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Direct2D Constants

Direct2D defines the following list of constants.

<dl> <dt>

<span id="D2D1_DEFAULT_FLATTENING_TOLERANCE"></span><span id="d2d1_default_flattening_tolerance"></span>**D2D1\_DEFAULT\_FLATTENING\_TOLERANCE**
</dt> <dd> <dl> <dt>

0.25f
</dt> <dt>



The default tolerance for geometric flattening operations.


</dt> </dl> </dd> <dt>

<span id="D2D1_INVALID_TAG"></span><span id="d2d1_invalid_tag"></span>**D2D1\_INVALID\_TAG**
</dt> <dd> <dl> <dt>

ULONGLONG\_MAX
</dt> <dt>



Reserved; do not use.


</dt> </dl> </dd> <dt>

<span id="D2D1_INVALID_PROPERTY_INDEX"></span><span id="d2d1_invalid_property_index"></span>**D2D1\_INVALID\_PROPERTY\_INDEX**
</dt> <dd> <dl> <dt>

UINT\_MAX
</dt> <dt>



When the invalid property index is specified to GetValue or GetValueByName, the call fails and the output buffer is zero-filled.


</dt> </dl> </dd> <dt>

<span id="D2D1_APPEND_ALIGNED_ELEMENT"></span><span id="d2d1_append_aligned_element"></span>**D2D1\_APPEND\_ALIGNED\_ELEMENT**
</dt> <dd> <dl> <dt>

-1
</dt> <dt>



This constant is used when packing input layout elements. It indicates that the elements must be packed contiguously.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                                                                                       |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7, Windows Vista with SP2 and Platform Update for Windows Vista \[desktop apps \| UWP apps\]<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2, Windows Server 2008 with SP2 and Platform Update for Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\], Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Header<br/>                   | <dl> <dt>D2d1.h</dt> </dl>                                                                                     |



 

 





