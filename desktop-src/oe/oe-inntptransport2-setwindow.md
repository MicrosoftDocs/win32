---
title: INNTPTransport2 SetWindow method
description: Creates a new window for async winsock processing.
ms.assetid: '1ccb2ae2-f87e-4c34-a149-83a93d5d2148'
keywords: ["SetWindow method Windows Mail (formerly Outlook Express)", "SetWindow method Windows Mail (formerly Outlook Express) , INNTPTransport2 interface", "INNTPTransport2 interface Windows Mail (formerly Outlook Express) , SetWindow method"]
topic_type:
- apiref
api_name:
- INNTPTransport2.SetWindow
api_location:
- Inetcomm.dll
api_type:
- COM
---

# INNTPTransport2::SetWindow method

\[**INNTPTransport2::SetWindow** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a new window for async winsock processing.

## Syntax


```C++
HRESULT SetWindow();
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



 

 





