---
title: IMimeHeaderTable SetRowNumber method
description: Changes the row number for a row in the header table.
ms.assetid: '3ae7d5a2-f756-4050-b6d4-3edc6193ebf9'
keywords: ["SetRowNumber method Windows Mail (formerly Outlook Express)", "SetRowNumber method Windows Mail (formerly Outlook Express) , IMimeHeaderTable interface", "IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , SetRowNumber method"]
topic_type:
- apiref
api_name:
- IMimeHeaderTable.SetRowNumber
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeHeaderTable::SetRowNumber method

Changes the row number for a row in the header table.

## Syntax


```C++
HRESULT SetRowNumber(
  [in] HHEADERROW hRow,
  [in] DWORD      dwRowNumber
);
```



## Parameters

<dl> <dt>

*hRow* \[in\]
</dt> <dd>

Type: **HHEADERROW**

Specifies the handle of the row to set the row number for.

</dd> <dt>

*dwRowNumber* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the row number.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                             |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                           |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hRow* is an invalid handle. <br/> |



 

## Remarks

The row number specifies the row's relative position in the header when it is saved. Rows are positioned in ascending numerical order from the top to the bottom of the header.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





