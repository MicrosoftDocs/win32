---
title: IPropFindResponse GetHref method
description: IPropFindResponse GetHref method
ms.assetid: 'caf9a391-6789-464b-a344-e37a38b4d640'
keywords: ["GetHref method Windows Mail (formerly Outlook Express)", "GetHref method Windows Mail (formerly Outlook Express) , IPropFindResponse interface", "IPropFindResponse interface Windows Mail (formerly Outlook Express) , GetHref method"]
topic_type:
- apiref
api_name:
- IPropFindResponse.GetHref
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IPropFindResponse::GetHref method

\[**IPropFindResponse::GetHref** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

## Syntax


```C++
HRESULT GetHref(
  [out] LPSTR *ppszHref
);
```



## Parameters

<dl> <dt>

*ppszHref* \[out\]
</dt> <dd>

Type: **LPSTR\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





