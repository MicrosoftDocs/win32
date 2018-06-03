---
title: INNTPTransport CommandPOST method
description: Posts the specified message to the server.
ms.assetid: 6f502fb0-5910-4b53-bac8-0735245f69d9
keywords:
- CommandPOST method Windows Mail (formerly Outlook Express)
- CommandPOST method Windows Mail (formerly Outlook Express) , INNTPTransport interface
- INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandPOST method
topic_type:
- apiref
api_name:
- INNTPTransport.CommandPOST
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INNTPTransport::CommandPOST method

\[**INNTPTransport::CommandPOST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Posts the specified message to the server.

## Syntax


```C++
HRESULT CommandPOST(
  [in] LPNNTPMESSAGE pMessage
);
```



## Parameters

<dl> <dt>

*pMessage* \[in\]
</dt> <dd>

Type: **LPNNTPMESSAGE**

Specifies a stream that contains a valid RFC1036 message.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | An invalid parameter was passed in<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | An memory allocation failed<br/>        |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





