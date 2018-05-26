---
title: MMESSENGERPROPERTY enumeration
description: Do not use. Used to retrieve the Messenger client version and client locale ID (LCID).
ms.assetid: ea8729a3-4513-4f92-9703-44489b186015
keywords:
- MMESSENGERPROPERTY enumeration Windows Messenger
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Msgrua.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MMESSENGERPROPERTY enumeration

\[**MMESSENGERPROPERTY** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Used to retrieve the Messenger client version and client locale ID (LCID).

## Syntax


```C++
typedef enum  { 
  MMESSENGERPROP_VERSION,
  MMESSENGERPROP_PLCID    = 1
} LockError;
```



## Constants

<dl> <dt>

<span id="MMESSENGERPROP_VERSION"></span><span id="mmessengerprop_version"></span>**MMESSENGERPROP\_VERSION**
</dt> <dd>

Used to retrieve the Messenger client version.

</dd> <dt>

<span id="MMESSENGERPROP_PLCID"></span><span id="mmessengerprop_plcid"></span>**MMESSENGERPROP\_PLCID**
</dt> <dd>

Used to retrieve the LCID of the Messenger client.

</dd> </dl>

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |



 

 





