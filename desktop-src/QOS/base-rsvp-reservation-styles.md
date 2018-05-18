---
title: Base RSVP Reservation Styles
description: RSVP recognizes three base reservation styles. Note that not all RSVP reservation styles are available without direct interaction (through the ProviderSpecific buffer) with RSVP.
ms.assetid: 'e77060fa-63f5-4b9f-9678-6501315c2a99'
---

# Base RSVP Reservation Styles

**Note**  RSVP signaling is not supported on Windows XP, Windows Server 2003, or later versions of Windows.

RSVP recognizes three base reservation styles. Note that not all RSVP reservation styles are available without direct interaction (through the **ProviderSpecific** buffer) with RSVP.

## RSVP Fixed Filter

The Fixed Filter (FF) RSVP reservation style implies a distinct reservation and an explicit sender. This contrasts with other reservation styles in that a reservation is made for individual senders, and the reservation is not shared with any other sender.

The Fixed Filter style is appropriate (and its definition implied) for use with unicast sessions. The RSVP SP uses the fixed filter for all TCP receivers, and for unicast UPD receivers attempting to establish a QOS-enabled connection.

## RSVP Wildcard Filter

The Wildcard Filter (WF) RSVP reservation style implies that a single reservation is shared among all senders in the session. The Wildcard Filter style is appropriate for use with applications such as audio conferencing, for example, in which only one or two speakers at a time can speak (in order for the audio conference to be meaningful); in which case only one reservation is necessary to service all participants.

## RSVP Shared Explicit

The Shared Explicit (SE) RSVP reservation style is a hybrid of the other two RSVP reservation styles; with the Shared Explicit style, the receiving application is making a reservation which can be shared (explicitly) by selected senders. The Shared Explicit style is appropriate for applications such as a video conference in which, unlike the WF reservation, only participants who are explicitly listed benefit from the RSVP reservation.

The RSVP SP does not use the Shared Explicit filter by default. Applications that want to use the Shared Explicit filter must set the Style member of the [**RSVP\_RESERVE\_INFO**](rsvp-reserve-info.md) object to RSVP\_SHARED\_EXPLICIT\_STYLE, and must specify the list of senders in flowdescriptors.

It is important to note that the number of senders included in any individual Shared Explicit reservation should be limited to a reasonable number of senders (such as 10). If more than approximately 10 senders will be included in a given reservation, receivers should use the WF reservation style.

 

 




