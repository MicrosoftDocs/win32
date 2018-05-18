---
title: IMimeMessageTree MoveBody method
description: Moves a body to a specified location within the message tree.
ms.assetid: 'be190629-64ef-4b9e-8f06-565661f66810'
keywords: ["MoveBody method Windows Mail (formerly Outlook Express)", "MoveBody method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface", "IMimeMessageTree interface Windows Mail (formerly Outlook Express) , MoveBody method"]
topic_type:
- apiref
api_name:
- IMimeMessageTree.MoveBody
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageTree::MoveBody method

Moves a body to a specified location within the message tree.

## Syntax


```C++
HRESULT MoveBody(
  [in] HBODY        hBody,
  [in] BODYLOCATION location
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body to move.

</dd> <dt>

*location* \[in\]
</dt> <dd>

Type: **[**BODYLOCATION**](oe-bodylocation.md)**

Specifies a [**BODYLOCATION**](oe-bodylocation.md) to move the body to. The value cannot be **IBL\_ROOT**. The new location is relative to the body's current location.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                    |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success.<br/>                                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Indicates that an unknown error has occurred.<br/>                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *hBody* is **NULL**. <br/>                                |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl>     | Indicates that *hBody* is an invalid handle. <br/>                       |
| <dl> <dt>**MIME\_E\_CANT\_MOVE\_BODY**</dt> </dl>    | Indicates that the body cannot be moved to the specified location. <br/> |
| <dl> <dt>**MIME\_E\_BAD\_BODY\_LOCATION**</dt> </dl> | Indicates that the value of *location* is invalid. <br/>                 |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





