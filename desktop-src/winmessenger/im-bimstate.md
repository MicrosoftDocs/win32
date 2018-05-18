---
title: BIMSTATE enumeration
description: Do not use.
ms.assetid: '31ed77d0-1315-4493-8d83-ca60222a4ade'
keywords: ["BIMSTATE enumeration Windows Messenger", "LockError enumeration Windows Messenger"]
topic_type:
- apiref
api_name:
- LockError
api_location:
- Basicim.h
api_type:
- HeaderDef
---

# BIMSTATE enumeration

\[**BIMSTATE** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Specifies local or remote client state.

> [!Note]  
> The **BIMSTATE** enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**MISTATUS**](im-mistatus.md) instead.

 

## Syntax


```C++
typedef enum  { 
  BIMSTATE_UNKNOWN                          = 0x0000,
  BIMSTATE_OFFLINE                          = 0x0001,
  BIMSTATE_ONLINE                           = 0x0002,
  BIMSTATE_INVISIBLE                        = 0x0006,
  BIMSTATE_BUSY                             = 0x000A,
  BIMSTATE_BE_RIGHT_BACK                    = 0x000E,
  BIMSTATE_IDLE                             = 0x0012,
  BIMSTATE_AWAY                             = 0x0022,
  BIMSTATE_ON_THE_PHONE                     = 0x0032,
  BIMSTATE_OUT_TO_LUNCH                     = 0x0042,
  BIMSTATE_LOCAL_FINDING_SERVER             = 0x0100,
  BIMSTATE_LOCAL_CONNECTING_TO_SERVER       = 0x0200,
  BIMSTATE_LOCAL_SYNCHRONIZING_WITH_SERVER  = 0x0300,
  BIMSTATE_LOCAL_DISCONNECTING_FROM_SERVER  = 0x0400
} LockError;
```



## Constants

<dl> <dt>

<span id="BIMSTATE_UNKNOWN"></span><span id="bimstate_unknown"></span>**BIMSTATE\_UNKNOWN**
</dt> <dd>

The state of the local or remote client is unknown.

</dd> <dt>

<span id="BIMSTATE_OFFLINE"></span><span id="bimstate_offline"></span>**BIMSTATE\_OFFLINE**
</dt> <dd>

The local or remote client is not connected to a server.

</dd> <dt>

<span id="BIMSTATE_ONLINE"></span><span id="bimstate_online"></span>**BIMSTATE\_ONLINE**
</dt> <dd>

The local or remote client is connected to a server.

</dd> <dt>

<span id="BIMSTATE_INVISIBLE"></span><span id="bimstate_invisible"></span>**BIMSTATE\_INVISIBLE**
</dt> <dd>

The local or remote client is connected to a server, but invisible to other users.

</dd> <dt>

<span id="BIMSTATE_BUSY"></span><span id="bimstate_busy"></span>**BIMSTATE\_BUSY**
</dt> <dd>

The local or remote client is connected to a server and in a user-selected busy state.

</dd> <dt>

<span id="BIMSTATE_BE_RIGHT_BACK"></span><span id="bimstate_be_right_back"></span>**BIMSTATE\_BE\_RIGHT\_BACK**
</dt> <dd>

The local or remote client user is away from the computer for a short time. This is a user-selected state.

</dd> <dt>

<span id="BIMSTATE_IDLE"></span><span id="bimstate_idle"></span>**BIMSTATE\_IDLE**
</dt> <dd>

The local or remote client has not detected mouse or keyboard input on the computer for a determined time. The user is most likely away from the computer. The user can select whether to transmit idle state and idle time threshold.

</dd> <dt>

<span id="BIMSTATE_AWAY"></span><span id="bimstate_away"></span>**BIMSTATE\_AWAY**
</dt> <dd>

The local or remote client user is away from the computer. This is a user-selected state.

</dd> <dt>

<span id="BIMSTATE_ON_THE_PHONE"></span><span id="bimstate_on_the_phone"></span>**BIMSTATE\_ON\_THE\_PHONE**
</dt> <dd>

The local or remote client user is on the phone. This is a user-selected state.

</dd> <dt>

<span id="BIMSTATE_OUT_TO_LUNCH"></span><span id="bimstate_out_to_lunch"></span>**BIMSTATE\_OUT\_TO\_LUNCH**
</dt> <dd>

The local or remote client user is at lunch. This is a user-selected state.

</dd> <dt>

<span id="BIMSTATE_LOCAL_FINDING_SERVER"></span><span id="bimstate_local_finding_server"></span>**BIMSTATE\_LOCAL\_FINDING\_SERVER**
</dt> <dd>

The local client is attempting to find the server.

</dd> <dt>

<span id="BIMSTATE_LOCAL_CONNECTING_TO_SERVER"></span><span id="bimstate_local_connecting_to_server"></span>**BIMSTATE\_LOCAL\_CONNECTING\_TO\_SERVER**
</dt> <dd>

The local client is connecting to the server.

</dd> <dt>

<span id="BIMSTATE_LOCAL_SYNCHRONIZING_WITH_SERVER"></span><span id="bimstate_local_synchronizing_with_server"></span>**BIMSTATE\_LOCAL\_SYNCHRONIZING\_WITH\_SERVER**
</dt> <dd>

The local client is synchronizing with the server.

</dd> <dt>

<span id="BIMSTATE_LOCAL_DISCONNECTING_FROM_SERVER"></span><span id="bimstate_local_disconnecting_from_server"></span>**BIMSTATE\_LOCAL\_DISCONNECTING\_FROM\_SERVER**
</dt> <dd>

The local client is disconnecting from the server.

</dd> </dl>

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                  |
| End of server support<br/> | Windows Server 2003<br/>                                                         |
| Header<br/>                | <dl> <dt>Basicim.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Basicim.idl</dt> </dl> |



 

 





