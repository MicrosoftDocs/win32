---
title: MSTATE enumeration
description: Do not use.
ms.assetid: a16deca4-4cb4-4fd8-be3c-d33c5a1ea951
keywords:
- MSTATE enumeration Windows Messenger
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Mdisp.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSTATE enumeration

\[**MSTATE** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Specifies local or remote client state.

> [!Note]  
> The **MSTATE** enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**MISTATUS**](im-mistatus.md) instead.

 

## Syntax


```C++
typedef enum  { 
  MSTATE_UNKNOWN                          = 0x0000,
  MSTATE_OFFLINE                          = 0x0001,
  MSTATE_ONLINE                           = 0x0002,
  MSTATE_INVISIBLE                        = 0x0006,
  MSTATE_BUSY                             = 0x000A,
  MSTATE_BE_RIGHT_BACK                    = 0x000E,
  MSTATE_IDLE                             = 0x0012,
  MSTATE_AWAY                             = 0x0022,
  MSTATE_ON_THE_PHONE                     = 0x0032,
  MSTATE_OUT_TO_LUNCH                     = 0x0042,
  MSTATE_LOCAL_FINDING_SERVER             = 0x0100,
  MSTATE_LOCAL_CONNECTING_TO_SERVER       = 0x0200,
  MSTATE_LOCAL_SYNCHRONIZING_WITH_SERVER  = 0x0300,
  MSTATE_LOCAL_DISCONNECTING_FROM_SERVER  = 0x0400
} LockError;
```



## Constants

<dl> <dt>

<span id="MSTATE_UNKNOWN"></span><span id="mstate_unknown"></span>**MSTATE\_UNKNOWN**
</dt> <dd>

The state of the local or remote client is unknown.

</dd> <dt>

<span id="MSTATE_OFFLINE"></span><span id="mstate_offline"></span>**MSTATE\_OFFLINE**
</dt> <dd>

The local or remote client is not connected to a server.

</dd> <dt>

<span id="MSTATE_ONLINE"></span><span id="mstate_online"></span>**MSTATE\_ONLINE**
</dt> <dd>

The local or remote client is connected to a server.

</dd> <dt>

<span id="MSTATE_INVISIBLE"></span><span id="mstate_invisible"></span>**MSTATE\_INVISIBLE**
</dt> <dd>

The local or remote client is connected to a server, but invisible to other users.

</dd> <dt>

<span id="MSTATE_BUSY"></span><span id="mstate_busy"></span>**MSTATE\_BUSY**
</dt> <dd>

The local or remote client is connected to a server and in a user-selected busy state.

</dd> <dt>

<span id="MSTATE_BE_RIGHT_BACK"></span><span id="mstate_be_right_back"></span>**MSTATE\_BE\_RIGHT\_BACK**
</dt> <dd>

The local or remote client user is away from the computer for a short time. This is a user-selected state.

</dd> <dt>

<span id="MSTATE_IDLE"></span><span id="mstate_idle"></span>**MSTATE\_IDLE**
</dt> <dd>

The local or remote client has not detected mouse or keyboard input on the computer for a determined time. The user is most likely away from the computer. The user can select whether to transmit idle state and idle time threshold.

</dd> <dt>

<span id="MSTATE_AWAY"></span><span id="mstate_away"></span>**MSTATE\_AWAY**
</dt> <dd>

The local or remote client user is away from the computer. This is a user-selected state.

</dd> <dt>

<span id="MSTATE_ON_THE_PHONE"></span><span id="mstate_on_the_phone"></span>**MSTATE\_ON\_THE\_PHONE**
</dt> <dd>

The local or remote client user is on the phone. This is a user-selected state.

</dd> <dt>

<span id="MSTATE_OUT_TO_LUNCH"></span><span id="mstate_out_to_lunch"></span>**MSTATE\_OUT\_TO\_LUNCH**
</dt> <dd>

The local or remote client user is at lunch. This is a user-selected state.

</dd> <dt>

<span id="MSTATE_LOCAL_FINDING_SERVER"></span><span id="mstate_local_finding_server"></span>**MSTATE\_LOCAL\_FINDING\_SERVER**
</dt> <dd>

The local client is attempting to find the server.

</dd> <dt>

<span id="MSTATE_LOCAL_CONNECTING_TO_SERVER"></span><span id="mstate_local_connecting_to_server"></span>**MSTATE\_LOCAL\_CONNECTING\_TO\_SERVER**
</dt> <dd>

The local client is connecting to the server.

</dd> <dt>

<span id="MSTATE_LOCAL_SYNCHRONIZING_WITH_SERVER"></span><span id="mstate_local_synchronizing_with_server"></span>**MSTATE\_LOCAL\_SYNCHRONIZING\_WITH\_SERVER**
</dt> <dd>

The local client is synchronizing with the server.

</dd> <dt>

<span id="MSTATE_LOCAL_DISCONNECTING_FROM_SERVER"></span><span id="mstate_local_disconnecting_from_server"></span>**MSTATE\_LOCAL\_DISCONNECTING\_FROM\_SERVER**
</dt> <dd>

The local client is disconnecting from the server.

</dd> </dl>

## Requirements



|                                  |                                                                                      |
|----------------------------------|--------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                |
| End of server support<br/> | Windows Server 2003<br/>                                                       |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl> |



 

 





