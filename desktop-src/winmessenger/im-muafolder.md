---
title: MUAFOLDER enumeration
description: Do not use. Used for selecting the folder for the count of unread messages.
ms.assetid: 970226a1-2adc-4244-b9ee-0441b56b83fb
keywords:
- MUAFOLDER enumeration Windows Messenger
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Msgrua.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# MUAFOLDER enumeration

\[**MUAFOLDER** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Used for selecting the folder for the count of unread messages.

## Syntax


```C++
typedef enum  { 
  MUAFOLDER_INBOX,
  MUAFOLDER_ALL_OTHER_FOLDERS  = 1
} LockError;
```



## Constants

<dl> <dt>

<span id="MUAFOLDER_INBOX"></span><span id="muafolder_inbox"></span>**MUAFOLDER\_INBOX**
</dt> <dd>

Refers to the Outlook.com Inbox.

</dd> <dt>

<span id="MUAFOLDER_ALL_OTHER_FOLDERS"></span><span id="muafolder_all_other_folders"></span>**MUAFOLDER\_ALL\_OTHER\_FOLDERS**
</dt> <dd>

Not currently implemented. Do not use.

</dd> </dl>

## Remarks

This constant is used as values for e-mail properties and methods. In some cases, when the client is a Microsoft Exchange-enabled client, the enumeration is not specific to Microsoft Outlook.com and instead designates the Exchange Inbox enabled by that client.

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |



 

 





