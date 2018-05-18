---
title: IMimeEnumHeaderRows Count method
description: On success, obtains the total number of elements in the enumerator object.
ms.assetid: '35f89513-a06e-43a1-aa6d-364facce0273'
keywords: ["Count method Windows Mail (formerly Outlook Express)", "Count method Windows Mail (formerly Outlook Express) , IMimeEnumHeaderRows interface", "IMimeEnumHeaderRows interface Windows Mail (formerly Outlook Express) , Count method"]
topic_type:
- apiref
api_name:
- IMimeEnumHeaderRows.Count
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeEnumHeaderRows::Count method

\[**IMimeEnumHeaderRows::Count** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

On success, obtains the total number of elements in the enumerator object.

## Syntax


```C++
HRESULT Count(
  [out] ULONG *pcItems
);
```



## Parameters

<dl> <dt>

*pcItems* \[out\]
</dt> <dd>

Type: **ULONG\***

On success, contains the total number of elements in the enumerator.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                       |
|----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pcItems* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





