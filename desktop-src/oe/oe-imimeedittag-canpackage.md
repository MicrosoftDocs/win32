---
title: IMimeEditTag CanPackage method
description: Called by the packer to make sure this tag should be packaged.
ms.assetid: '56de7400-de36-40dd-9aeb-212e2b994fa1'
keywords: ["CanPackage method Windows Mail (formerly Outlook Express)", "CanPackage method Windows Mail (formerly Outlook Express) , IMimeEditTag interface", "IMimeEditTag interface Windows Mail (formerly Outlook Express) , CanPackage method"]
topic_type:
- apiref
api_name:
- IMimeEditTag.CanPackage
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeEditTag::CanPackage method

\[**IMimeEditTag::CanPackage** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called by the packer to make sure this tag should be packaged.

## Syntax


```C++
HRESULT CanPackage();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





