---
title: DMessengerEvents OnSignin event
description: Indicates that an attempt has been made to sign in to the primary service.
ms.assetid: '9a4153ce-2775-469c-a4b8-07a9283beed0'
keywords: ["OnSignin event Windows Messenger", "OnSignin event Windows Messenger , DMessengerEvents interface", "DMessengerEvents interface Windows Messenger , OnSignin event"]
topic_type:
- apiref
api_name:
- DMessengerEvents.OnSignin
api_location:
- Msgsc.dll
api_type:
- COM
---

# DMessengerEvents::OnSignin event

\[**OnSignin** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that an attempt has been made to sign in to the primary service.

## Syntax


```C++
void OnSignin(
  [in] LONG hr
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**. For a table of the MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

An error result for *hr* may result in all other event parameters being meaningless, **NULL**, or otherwise invalid. Always check for a successful *hr* before attempting to use the other event parameters.

A negative result indicates a failure to connect; a positive or zero result indicates a successful connection. Possible values are as follows:



| Value                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>S\_OK</dt> </dl>                          | The local client has successfully signed in. <br/>                                                                                                                                                                                                                                                            |
| <dl> <dt></dt> <dt>MSGR\_E\_INVALID\_SERVER\_NAME</dt> </dl> | The proxy server or Microsoft .NET Messenger Service specified could not be resolved. Host resolution is handled by an asynchronous Winsock function call. Although this sign-in request never actually reached a server, the return value is passed back as a self-generated **OnSignin** event. <br/>       |
| <dl> <dt></dt> <dt>MSGR\_E\_CONNECT</dt> </dl>               | The server or proxy IP addresses were resolved, but proxy configurations were incorrect, or some other Winsock  APIs error prevented full connection to the server. Warning, error, or Network Monitor trace output may display more information. <br/>                                                       |
| <dl> <dt></dt> <dt>MSGR\_E\_CANCEL</dt> </dl>                | The user has canceled the sign-in attempt before connecting to any server. <br/>                                                                                                                                                                                                                              |
| <dl> <dt></dt> <dt>MSGR\_E\_LOGON\_TIMEOUT</dt> </dl>        | The connection to the server was not established within 15 seconds of continuous negotiating or requesting states. (These are internal states that appear as the **MISTATUS\_LOCAL\_CONNECTING\_TO\_SERVER**state.) <br/>                                                                                     |
| <dl> <dt></dt> <dt>MSGR\_E\_SERVER\_VERSION</dt> </dl>       | The connection to the server was established, but version differences between client and server prevented further protocol exchange. The client might be unable to continue. <br/>                                                                                                                            |
| <dl> <dt></dt> <dt>MSGR\_E\_INVALID\_PASSWORD</dt> </dl>     | The password did not match the password for the given sign-in name in the server-side user store. Because there is no differentiation between the case of a nonexistent user and the case of an existing user but invalid password, **MSGR\_E\_USER\_NOT\_FOUND** is not a return *hr* for this method. <br/> |
| <dl> <dt></dt> <dt>MSGR\_E\_SERVER\_TOO\_BUSY</dt> </dl>     | Additional server-returned error code that translates to these locally generated error codes. <br/>                                                                                                                                                                                                           |
| <dl> <dt></dt> <dt>MSGR\_E\_SERVER\_UNAVAILABLE</dt> </dl>   | Additional server-returned error code that translates to these locally generated error codes. <br/>                                                                                                                                                                                                           |
| <dl> <dt></dt> <dt>MSGR\_E\_UNEXPECTED</dt> </dl>            | Additional server-returned error code that translates to these locally generated error codes. <br/>                                                                                                                                                                                                           |



 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event occurs on a successful or unsuccessful [**AutoSignin**](im-imessenger-autosignin.md) call, a user sign-in attempt through the UI, or through other internal methods that cause a sign-in attempt. Implementations should not rely on this event to assume that the local client is ready for other API calls and should instead wait for the [**OnMyStatusChange**](im-dmessengerevents-onmystatuschange.md) event to return mMYStatusOE = **MISTATUS\_ONLINE**.

This event applies only to the current primary service of the client. If secondary services are signed in, no event is issued in the Windows Messenger API.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type |
|-----------|-------------|--------------|
| hr        | 2           | VT\_I4       |



 

> [!Note]  
> This event is available for scripting languages.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.5<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





