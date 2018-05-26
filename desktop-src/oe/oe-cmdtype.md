---
title: CMDTYPE enumeration
description: Identifies the direction of interaction with a server.
ms.assetid: 2b6a6e23-9b94-42e3-84c8-9a2347ec38f7
keywords:
- CMDTYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMDTYPE enumeration

\[**CMDTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Identifies the direction of interaction with a server.

## Syntax


```C++
typedef enum tagCMDTYPE { 
  CMD_SEND  = 0,
  CMD_RESP  = 1
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="CMD_SEND"></span><span id="cmd_send"></span>**CMD\_SEND**
</dt> <dd>

Indicates a command sent to the server.

</dd> <dt>

<span id="CMD_RESP"></span><span id="cmd_resp"></span>**CMD\_RESP**
</dt> <dd>

Indicates a response received from the server.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





