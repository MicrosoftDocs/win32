---
description: Advanced conferencing using IP-based networks is described in TAPI 3s Rendezvous IP Telephony Conferencing. The following material relates to basic conferencing.
ms.assetid: f685097b-1b54-412b-999f-d9bdb3120ab9
title: Conference
ms.topic: article
ms.date: 05/31/2018
---

# Conference

Advanced conferencing using IP-based networks is described in TAPI 3's [Rendezvous IP Telephony Conferencing](rendezvous-ip-telephony-conferencing.md). The following material relates to basic conferencing.

Conference sessions are sessions that include more than two parties simultaneously. They can be set up using either an external server-based bridge or a switch-based conference bridge.

In server-based conference sessions, all participating parties dial into the server, which mixes the media streams together and sends each participant the mix. There may be no notion of individual parties in the conference call, only that of a single call between the application and the bridge server. To TAPI, this type of conference call appears to be a normal one-to-one connection.

Switch-based conferencing proceeds in stages, some of which may be combined if the service provider supports it:

1.  Initiate an ordinary communications session.
2.  Create a conference session with its first member the party that initiated conferencing.
3.  Create a conference consultation session with the party at the other end of the current connection.
4.  Add the consultation session to the conference.

After a session becomes a member of a conference, the member's state reverts to conferenced. The state of the conference session typically becomes *connected*. The session identifiers to the conference and all the added parties remain valid. State events can be received about all calls. For example, if one of the members disconnects by hanging up, an appropriate state message can inform the application of this fact.

**TAPI 2.x:** Applications can use the "no hold conference" feature of PBXs by using the LINECALLPARAMFLAGS\_NOHOLDCONFERENCE option; this feature allows another device, such as a supervisor or recording device, to be silently attached to the line.

When canceling the consultation session to the third party for a conference or when removing the third party in a previously established conference, the service provider may release the conference and revert the session back to a normal two-party connection. If this is the case, the conference session will transition to the *idle* state, and the only remaining participating session will transition from the conferenced to the *connected* state.

Not all service providers support conferencing.

**TAPI 2.x:** The [**lineSetupConference**](/windows/win32/api/tapi/nf-tapi-linesetupconference) function takes the original two-party call as input, allocates a conference call, connects the original call to the conference, and allocates a consultation call whose handle is returned to the application.

If the application is going to add another member to the conference, a dial operation can be performed on the consultation call. The conference call handle and the consultation call connection are then used in the [**lineAddToConference**](/windows/win32/api/tapi/nf-tapi-lineaddtoconference) function. Conference members may also be added using [**linePrepareAddToConference**](/windows/win32/api/tapi/nf-tapi-lineprepareaddtoconference) function, if supported by the service provider.

Conference members are removed using the [**lineRemoveFromConference**](/windows/win32/api/tapi/nf-tapi-lineremovefromconference) function, if the service provider supports it.

Alternatively, a conference may be created using the [**lineSetupTransfer**](/windows/win32/api/tapi/nf-tapi-linesetuptransfer) function, which returns a consultation call handle, and the [**lineCompleteTransfer**](/windows/win32/api/tapi/nf-tapi-linecompletetransfer) function with the conference option (instead of the [transfer](transfer-ovr.md) option).

**TAPI 3.x:** The [**ITBasicCallControl::Conference**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-conference) method takes the existing session as input and creates a [CallHub object](callhub-object.md) if one does not already exist. The [**ITBasicCallControl::Finish**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-finish) method adds the consultation call to the CallHub. Additional consultation sessions may be created using [**ITAddress::CreateCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddress-createcall), and added using the **Conference** and **Finish** methods.

> [!Note]  
> The capabilities of the addressed line device can limit the number of parties conferenced in a single call and whether or not a conference starts out with a normal two-party call.

 

 

 
