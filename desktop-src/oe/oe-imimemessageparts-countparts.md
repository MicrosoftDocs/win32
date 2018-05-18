---
title: IMimeMessageParts CountParts method
description: Gets the total number of partial messages currently in the collection.
ms.assetid: 'df1a1d1d-6162-4978-8024-68e0929ea47e'
keywords: ["CountParts method Windows Mail (formerly Outlook Express)", "CountParts method Windows Mail (formerly Outlook Express) , IMimeMessageParts interface", "IMimeMessageParts interface Windows Mail (formerly Outlook Express) , CountParts method"]
topic_type:
- apiref
api_name:
- IMimeMessageParts.CountParts
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageParts::CountParts method

Gets the total number of partial messages currently in the collection.

## Syntax


```C++
HRESULT CountParts(
  [out] ULONG *pcParts
);
```



## Parameters

<dl> <dt>

*pcParts* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of partial messages in the collection.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns the following value.



| Return code                                                                          | Description                   |
|--------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Indicates success.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





