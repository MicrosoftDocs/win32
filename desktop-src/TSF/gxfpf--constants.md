---
title: GXFPF\_\ Constants
description: GXFPF\_\ constants specify the character position to return based on the screen coordinates of the point relative to a character bounding box.
ms.assetid: 'e69e5a4c-65e6-4d9b-8cb0-962524aa5d39'
topic_type:
- apiref
api_name:
- GXFPF_ROUND_NEAREST
- GXFPF_NEAREST
api_location:
- Textstor.h
api_type:
- HeaderDef
---

# GXFPF\_\* Constants

GXFPF\_\* constants specify the character position to return based on the screen coordinates of the point relative to a character bounding box.



| Constant/value                                                                                                                                                                                                                                | Description                                                                                                                                                                                       |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GXFPF_ROUND_NEAREST"></span><span id="gxfpf_round_nearest"></span><dl> <dt>**GXFPF\_ROUND\_NEAREST**</dt> <dt>( 0x1 )</dt> </dl> | If the screen coordinates of the point are contained in a character bounding box, the character position returned is the bounding edge closest to the screen coordinates of the point.<br/> |
| <span id="GXFPF_NEAREST"></span><span id="gxfpf_nearest"></span><dl> <dt>**GXFPF\_NEAREST**</dt> <dt>( 0x2 )</dt> </dl>                    | If the screen coordinates of the point are not contained in a character bounding box, the closest character position is returned.<br/>                                                      |



## Remarks

The *dwflags* parameters of the [ITextStoreACP::GetACPFromPoint](itextstoreacp-getacpfrompoint.md) and [ITfContextOwner::GetACPFromPoint](itfcontextowner-getacpfrompoint.md) methods use these constants.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                         |
| Header<br/>                   | <dl> <dt>Textstor.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Textstor.idl</dt> </dl> |



## See also

<dl> <dt>

[ITextStoreACP::GetACPFromPoint](itextstoreacp-getacpfrompoint.md)
</dt> <dt>

[ITfContextOwner::GetACPFromPoint](itfcontextowner-getacpfrompoint.md)
</dt> </dl>

 

 





