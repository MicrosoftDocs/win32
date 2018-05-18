---
title: INNTPTransport2 ResetWindow method
description: Closes a window for async winsock processing.
ms.assetid: '7e56a461-fa1d-4dd8-bba6-304565ccb530'
keywords: ["ResetWindow method Windows Mail (formerly Outlook Express)", "ResetWindow method Windows Mail (formerly Outlook Express) , INNTPTransport2 interface", "INNTPTransport2 interface Windows Mail (formerly Outlook Express) , ResetWindow method"]
topic_type:
- apiref
api_name:
- INNTPTransport2.ResetWindow
api_location:
- Inetcomm.dll
api_type:
- COM
---

# INNTPTransport2::ResetWindow method

\[**INNTPTransport2::ResetWindow** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Closes a window for async winsock processing.

## Syntax


```C++
HRESULT ResetWindow();
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
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





