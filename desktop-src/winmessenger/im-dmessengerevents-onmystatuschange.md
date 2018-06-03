---
title: DMessengerEvents OnMyStatusChange event
description: Indicates that the status of the local client has changed or that a status change was attempted, and returns the current status of the local client.
ms.assetid: f6137eae-7a80-4c6d-a312-934e77cf0628
keywords:
- OnMyStatusChange event Windows Messenger
- OnMyStatusChange event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnMyStatusChange event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnMyStatusChange
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DMessengerEvents::OnMyStatusChange event

\[**OnMyStatusChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the status of the local client has changed or that a status change was attempted, and returns the current status of the local client.

## Syntax


```C++
void OnMyStatusChange(
  [in] LONG     hr,
  [in] MISTATUS mMYStatusOE
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**. For a table of the MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

An error result for *hr* might result in all other event parameters being meaningless, **NULL**, or otherwise invalid. Always check for a successful *hr* before attempting to use the other event parameters.

Possible values are as follows:



| Value                                                                                                                                                         | Meaning                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>S\_OK</dt> </dl>                        | The local state was successfully changed.<br/>                                             |
| <dl> <dt></dt> <dt>MSGR\_E\_DISCONNECTED</dt> </dl>        | The client signed out between attempting to change the state and receiving the event.<br/> |
| <dl> <dt></dt> <dt>MSGR\_E\_UNEXPECTED</dt> </dl>          | The server has returned an unexpected error code.<br/>                                     |
| <dl> <dt></dt> <dt>MSGR\_E\_SERVER\_TOO\_BUSY</dt> </dl>   | The server is not processing requests or not accepting new connections.<br/>               |
| <dl> <dt></dt> <dt>MSGR\_E\_SERVER\_UNAVAILABLE</dt> </dl> | The server was contacted, but was unavailable for unspecified reasons.<br/>                |



 

</dd> <dt>

*mMYStatusOE* \[in\]
</dt> <dd>

The new local state as a member of the [**MISTATUS**](im-mistatus.md) enumerated state. Possible values are as follows:



| Value                                                                                                                                                                         | Meaning                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>MISTATUS\_BUSY</dt> </dl>                               | The local client is connected to a server and in a user-selected busy state.<br/>                                                                     |
| <dl> <dt></dt> <dt>MISTATUS\_INVISIBLE</dt> </dl>                          | The local client is connected to a server but is invisible to other users. (Some services might not support this status.)<br/>                        |
| <dl> <dt></dt> <dt>MISTATUS\_LOCAL\_CONNECTING\_TO\_SERVER</dt> </dl>      | The local client is connecting to the server.<br/>                                                                                                    |
| <dl> <dt></dt> <dt>MISTATUS\_LOCAL\_FINDING\_SERVER</dt> </dl>             | The local client is attempting to find the server.<br/>                                                                                               |
| <dl> <dt></dt> <dt>MISTATUS\_LOCAL\_DISCONNECTING\_FROM\_SERVER</dt> </dl> | The local client is disconnecting from the server.<br/>                                                                                               |
| <dl> <dt></dt> <dt>MISTATUS\_LOCAL\_SYNCHRONIZING\_WITH\_SERVER</dt> </dl> | The local client is synchronizing with the server.<br/>                                                                                               |
| <dl> <dt></dt> <dt>MISTATUS\_OFFLINE</dt> </dl>                            | The local client is not connected to a server.<br/>                                                                                                   |
| <dl> <dt></dt> <dt>MISTATUS\_ONLINE</dt> </dl>                             | The local client is connected to a server.<br/>                                                                                                       |
| <dl> <dt></dt> <dt>MISTATUS\_BE\_RIGHT\_BACK</dt> </dl>                    | The local client user has stepped away from the computer for a short time. (This is a user-selected state.)<br/>                                      |
| <dl> <dt></dt> <dt>MISTATUS\_IDLE</dt> </dl>                               | The local client has not detected mouse or keyboard input on the computer for a determined time. The user is most likely away from the computer.<br/> |
| <dl> <dt></dt> <dt>MISTATUS\_AWAY</dt> </dl>                               | The local client user is away from the computer. (This is a user-selected state.)<br/>                                                                |
| <dl> <dt></dt> <dt>MISTATUS\_ON\_THE\_PHONE</dt> </dl>                     | The local client user is on the phone. (This is a user-selected state.)<br/>                                                                          |
| <dl> <dt></dt> <dt>MISTATUS\_OUT\_TO\_LUNCH</dt> </dl>                     | The local client user is at lunch. (This is a user-selected state.)<br/>                                                                              |



 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event is received upon successfully invoking [**MyStatus**](im-imessenger-mystatus.md) or through API or user-driven actions that change status, such as signing in to the service. If the API or user set the local client status to the last known state value, the **OnMyStatusChange** event still fires. Upon sign-in to the service, client implementations should handle this event to verify that the local client is **MISTATUS\_ONLINE**. Do not assume that *hr*=**MSGR\_S\_OK** for the [**OnSignin**](im-dmessengerevents-onsignin.md) event indicates that the local client is successfully online.

Unlike other events, such as [**OnContactStatusChange**](im-dmessengerevents-oncontactstatuschange.md), this event returns the local client's current, not previous, status.

Each change to a local client's transitional status, such as **MISTATUS\_LOCAL\_FINDING\_SERVER**, generates another **OnMyStatusChange** event. The state may briefly appear to be offline when the server is being contacted and the user's list information is being synchronized or retrieved.

The [**MISTATUS**](im-mistatus.md) enumeration is set up in such a way that all possible online status codes have the **MISTATUS\_ONLINE** bit set. The following can be used to determine whether a user is in any of the possible online states:


```C++
pContact->get_Status(&amp;uStatus);
if (MISTATUS_ONLINE  &amp;uStatus) { // pContact is online }
```



> [!Note]  
> This event is available for scripting languages.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.5<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





