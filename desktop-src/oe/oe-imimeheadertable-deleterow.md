---
title: IMimeHeaderTable DeleteRow method
description: Deletes the specified row from the header table.
ms.assetid: 'b1dd67b7-b965-4b4e-aabd-eaa26585827b'
keywords: ["DeleteRow method Windows Mail (formerly Outlook Express)", "DeleteRow method Windows Mail (formerly Outlook Express) , IMimeHeaderTable interface", "IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , DeleteRow method"]
topic_type:
- apiref
api_name:
- IMimeHeaderTable.DeleteRow
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeHeaderTable::DeleteRow method

Deletes the specified row from the header table.

## Syntax


```C++
HRESULT DeleteRow(
  [in] HHEADERROW hRow
);
```



## Parameters

<dl> <dt>

*hRow* \[in\]
</dt> <dd>

Type: **HHEADERROW**

Specifies the handle of the row to delete.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                             |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                           |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hRow* is an invalid handle. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





