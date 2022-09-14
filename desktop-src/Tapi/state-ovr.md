---
description: Session or call state indicates the current status of a session, such as &\#0034;offering&\#0034; or &\#0034;connected.&\#0034; Proper handling of state information is vital to the proper functioning of most TAPI applications.
ms.assetid: a6a49b77-4e9b-4f23-bfe6-26f26549b18f
title: State
ms.topic: article
ms.date: 05/31/2018
---

# State

Session or call state indicates the current status of a session, such as "offering" or "connected." Proper handling of state information is vital to the proper functioning of most TAPI applications. For example, the answer operation can be performed only on an offered session, but a transfer will fail if the session is in that state.

A session's state changes as a result of events. Events can be solicited or unsolicited. *Solicited events* are caused by the application controlling the session, such as when it invokes a TAPI session operation. *Unsolicited events* are caused by the switch, the telephone network, the user pressing buttons on the local phone, or the actions of the remote party.

Whenever a service provider detects a session state change, it reports the change to TAPI and TAPI issues an event notification to all owner and monitor applications. The application must react to these notifications appropriately. Please see Event Notification under [TAPI Initialization](tapi-initialization.md) for information on controlling which events are reported to an application.

An application should always process state event notifications. State transitions valid for one physical configuration may be invalid for another. For example, consider a line that physically terminates both at the computer and at a separate phone set, creating a party line configuration between the computer and the phone set. An application running on the computer may not know about phone set activities. That is, the line may be in use without the service provider being aware of it. An application that attempts to make an outgoing call will succeed in allocating a call appearance from TAPI, but this results in sharing the active call on the line. Blindly sending a DTMF dial string without first checking for a dial tone may not result in intended (or polite) behavior.

An application should not assume a rigid progression from one state to another. State events arrive and are forwarded asynchronously and notifications may not be received in a predictable order. Therefore, call-state notifications should be viewed as telling the application the call's new state instead of as reporting the transitions between two states.

All telephony service providers must supply this information.

**TAPI 2.x:  **[**lineGetCallStatus**](/windows/win32/api/tapi/nf-tapi-linegetcallstatus), [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo), [**LINE\_CALLSTATE**](./line-callstate.md) message, [LINECALLSTATE\_ Constants](./linecallstate--constants.md)

**TAPI 3.x:  **[**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong) (**CIL\_CALLID** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long)), [**ITCallStateEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallstateevent) notification, [**CALL\_STATE**](/windows/desktop/api/Tapi3if/ne-tapi3if-call_state) enumerator

 

 
