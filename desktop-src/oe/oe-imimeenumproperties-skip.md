---
title: IMimeEnumProperties Skip method
description: Skips over the next specified number of elements in the enumeration sequence.
ms.assetid: '293bd53a-8845-4274-b4d1-64465b70fd54'
keywords: ["Skip method Windows Mail (formerly Outlook Express)", "Skip method Windows Mail (formerly Outlook Express) , IMimeEnumProperties interface", "IMimeEnumProperties interface Windows Mail (formerly Outlook Express) , Skip method"]
topic_type:
- apiref
api_name:
- IMimeEnumProperties.Skip
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeEnumProperties::Skip method

Skips over the next specified number of elements in the enumeration sequence.

## Syntax


```C++
HRESULT Skip(
  [in] ULONG cItems
);
```



## Parameters

<dl> <dt>

*cItems* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that indicates the number of elements to skip.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                                                      |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the number of elements specified by *cItems* were skipped. <br/>            |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that fewer than the number of elements specified by *cItems* were skipped. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





