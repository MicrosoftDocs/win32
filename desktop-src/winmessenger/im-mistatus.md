---
title: MISTATUS enumeration
description: Do not use.
ms.assetid: 643e8887-9fa4-4c15-86df-12bcd846089e
keywords:
- MISTATUS enumeration Windows Messenger
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

# MISTATUS enumeration

\[**MISTATUS** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Specifies local or remote client state. The user can select these options from the **File** menu of the **Messenger** window or by clicking the **Messenger** icon in the taskbar. The current state of the local user is detected on the local client. The current state of the remote clients is detected through the server automatically. Not all states are valid for remote clients.

## Syntax


```C++
typedef enum  { 
  MISTATUS_UNKNOWN                          = 0x0000,
  MISTATUS_OFFLINE                          = 0x0001,
  MISTATUS_ONLINE                           = 0x0002,
  MISTATUS_INVISIBLE                        = 0x0006,
  MISTATUS_BUSY                             = 0x000A,
  MISTATUS_BE_RIGHT_BACK                    = 0x000E,
  MISTATUS_IDLE                             = 0x0012,
  MISTATUS_AWAY                             = 0x0022,
  MISTATUS_ON_THE_PHONE                     = 0x0032,
  MISTATUS_OUT_TO_LUNCH                     = 0x0042,
  MISTATUS_LOCAL_FINDING_SERVER             = 0x0100,
  MISTATUS_LOCAL_CONNECTING_TO_SERVER       = 0x0200,
  MISTATUS_LOCAL_SYNCHRONIZING_WITH_SERVER  = 0x0300,
  MISTATUS_LOCAL_DISCONNECTING_FROM_SERVER  = 0x0400
} LockError;
```



## Constants

<dl> <dt>

<span id="MISTATUS_UNKNOWN"></span><span id="mistatus_unknown"></span>**MISTATUS\_UNKNOWN**
</dt> <dd>

The state of the local or remote client is unknown.

</dd> <dt>

<span id="MISTATUS_OFFLINE"></span><span id="mistatus_offline"></span>**MISTATUS\_OFFLINE**
</dt> <dd>

The local or remote client is not connected to a server.

</dd> <dt>

<span id="MISTATUS_ONLINE"></span><span id="mistatus_online"></span>**MISTATUS\_ONLINE**
</dt> <dd>

The local or remote client is connected to a server.

</dd> <dt>

<span id="MISTATUS_INVISIBLE"></span><span id="mistatus_invisible"></span>**MISTATUS\_INVISIBLE**
</dt> <dd>

The local or remote client is connected to a server, but invisible to other users.

</dd> <dt>

<span id="MISTATUS_BUSY"></span><span id="mistatus_busy"></span>**MISTATUS\_BUSY**
</dt> <dd>

The local or remote client is connected to a server and in a user-selected busy state.

</dd> <dt>

<span id="MISTATUS_BE_RIGHT_BACK"></span><span id="mistatus_be_right_back"></span>**MISTATUS\_BE\_RIGHT\_BACK**
</dt> <dd>

The local or remote client user is away from the computer for a short time. This is a user-selected state.

</dd> <dt>

<span id="MISTATUS_IDLE"></span><span id="mistatus_idle"></span>**MISTATUS\_IDLE**
</dt> <dd>

The local or remote client has not detected mouse or keyboard input on the computer for a determined time. The user is most likely away from the computer. The user can select whether to transmit idle state and idle time threshold.

</dd> <dt>

<span id="MISTATUS_AWAY"></span><span id="mistatus_away"></span>**MISTATUS\_AWAY**
</dt> <dd>

The local or remote client user is away from the computer. This is a user-selected state.

</dd> <dt>

<span id="MISTATUS_ON_THE_PHONE"></span><span id="mistatus_on_the_phone"></span>**MISTATUS\_ON\_THE\_PHONE**
</dt> <dd>

The local or remote client user is on the phone. This is a user-selected state.

</dd> <dt>

<span id="MISTATUS_OUT_TO_LUNCH"></span><span id="mistatus_out_to_lunch"></span>**MISTATUS\_OUT\_TO\_LUNCH**
</dt> <dd>

The local or remote client user is at lunch. This is a user-selected state.

</dd> <dt>

<span id="MISTATUS_LOCAL_FINDING_SERVER"></span><span id="mistatus_local_finding_server"></span>**MISTATUS\_LOCAL\_FINDING\_SERVER**
</dt> <dd>

The local client is attempting to find the server.

</dd> <dt>

<span id="MISTATUS_LOCAL_CONNECTING_TO_SERVER"></span><span id="mistatus_local_connecting_to_server"></span>**MISTATUS\_LOCAL\_CONNECTING\_TO\_SERVER**
</dt> <dd>

The local client is connecting to the server.

</dd> <dt>

<span id="MISTATUS_LOCAL_SYNCHRONIZING_WITH_SERVER"></span><span id="mistatus_local_synchronizing_with_server"></span>**MISTATUS\_LOCAL\_SYNCHRONIZING\_WITH\_SERVER**
</dt> <dd>

The local client is synchronizing with the server.

</dd> <dt>

<span id="MISTATUS_LOCAL_DISCONNECTING_FROM_SERVER"></span><span id="mistatus_local_disconnecting_from_server"></span>**MISTATUS\_LOCAL\_DISCONNECTING\_FROM\_SERVER**
</dt> <dd>

The local client is disconnecting from the server.

</dd> </dl>

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |



 

 





