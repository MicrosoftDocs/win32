---
title: IMimeBody GetOffsets method
description: Gets the offsets of the body.
ms.assetid: 'b935351e-8d80-48cd-a915-abf280867918'
keywords: ["GetOffsets method Windows Mail (formerly Outlook Express)", "GetOffsets method Windows Mail (formerly Outlook Express) , IMimeBody interface", "IMimeBody interface Windows Mail (formerly Outlook Express) , GetOffsets method"]
topic_type:
- apiref
api_name:
- IMimeBody.GetOffsets
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeBody::GetOffsets method

Gets the offsets of the body.

## Syntax


```C++
HRESULT GetOffsets(
  [out] LPBODYOFFSETS pOffsets
);
```



## Parameters

<dl> <dt>

*pOffsets* \[out\]
</dt> <dd>

Type: **LPBODYOFFSETS**

Receives a pointer to the [**BODYOFFSETS**](oe-bodyoffsets.md) structure containing the offsets.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                      | Description                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | Indicates success.<br/>                                                                                                                                                                                                                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>     | Indicates that *pOffsets* is **NULL**.<br/>                                                                                                                                                                                                                      |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl> | Indicates that the body has no offsets. This can happen if the body is not loaded from a storage source or if the body has not been saved because of a call to [IMimeMessageTree::Save](http://msdn.microsoft.com/library/com/htm/cmi_n2p_47z9.asp). <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





