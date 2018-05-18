---
title: IOECriteria Clone method
description: IOECriteria Clone is no longer available for use as of Windows Vista.
ms.assetid: 'f2089252-48b3-4161-b7a6-09687925579f'
keywords: ["Clone method Windows Mail (formerly Outlook Express)", "Clone method Windows Mail (formerly Outlook Express) , IOECriteria interface", "IOECriteria interface Windows Mail (formerly Outlook Express) , Clone method"]
topic_type:
- apiref
api_name:
- IOECriteria.Clone
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IOECriteria::Clone method

\[**IOECriteria::Clone** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT Clone(
  [out] IOECriteria **ppICriteria
);
```



## Parameters

<dl> <dt>

*ppICriteria* \[out\]
</dt> <dd>

Type: **[**IOECriteria**](oe-ioecriteria.md)\*\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





