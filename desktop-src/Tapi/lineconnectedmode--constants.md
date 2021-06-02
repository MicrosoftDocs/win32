---
description: The LINECONNECTEDMODE\_ bit-flag constants describe different substates of a connected call.
ms.assetid: d75a5989-3f4e-4e5d-90b1-4e450def017e
title: LINECONNECTEDMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECONNECTEDMODE\_ Constants

The **LINECONNECTEDMODE\_** bit-flag constants describe different substates of a connected call. A mode is available as call status to the application after the call state transitions to connected, and within the LINE\_CALLSTATE message indicating the call is in LINECALLSTATE\_CONNECTED. These values are used when the call is on an address that is shared (bridged) with other stations (for more information, see [**LINEADDRESSSHARING\_ Constants**](lineaddresssharing--constants.md)), primarily electronic key systems. The **LINECONNECTEDMODE\_constants** have the following values:

<dl> <dt>

<span id="LINECONNECTEDMODE_ACTIVE"></span><span id="lineconnectedmode_active"></span>**LINECONNECTEDMODE\_ACTIVE**
</dt> <dd> <dl> <dt>



Indicates that the call is connected at the current station (the current station is a participant in the call). If the call state mode is 0 (zero), the application should assume that the value is "active" (which would be the situation on a non-bridged address). The mode can switch between ACTIVE and INACTIVE during a call if the user joins and leaves the call through manual action. In such a bridged situation, a [**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop) or [**lineHold**](/windows/desktop/api/Tapi/nf-tapi-linehold) operation may possibly not actually drop the call or place it on hold, because the status of other stations on the call may govern (for example, attempting to "hold" a call when other stations are participating is not possible); instead, the call may be changed to the INACTIVE mode if it remains CONNECTED at other stations.


</dt> </dl> </dd> <dt>

<span id="LINECONNECTEDMODE_ACTIVEHELD"></span><span id="lineconnectedmode_activeheld"></span>**LINECONNECTEDMODE\_ACTIVEHELD**
</dt> <dd> <dl> <dt>



Indicates that the station is an active participant in the call, but that the remote party has placed the call on hold (the other party considers the call to be in the onhold state). Normally, such information is available only when both endpoints of the call fall within the same switching domain. This flag is exposed only to applications that negotiate a TAPI version of 2.0 or higher. (TAPI versions 2.0 and later)


</dt> </dl> </dd> <dt>

<span id="LINECONNECTEDMODE_CONFIRMED"></span><span id="lineconnectedmode_confirmed"></span>**LINECONNECTEDMODE\_CONFIRMED**
</dt> <dd> <dl> <dt>



Indicates that the service provider received affirmative notification that the call has entered the connected state (for example, through answer supervision or similar mechanisms). This flag is exposed only to applications that negotiate a TAPI version of 2.0 or higher. (TAPI versions 2.0 and later)


</dt> </dl> </dd> <dt>

<span id="LINECONNECTEDMODE_INACTIVE"></span><span id="lineconnectedmode_inactive"></span>**LINECONNECTEDMODE\_INACTIVE**
</dt> <dd> <dl> <dt>



Indicates that the call is active at one or more other stations, but the current station is not a participant in the call. If the call state mode is ZERO, the application should assume that the value is "active" (which would be the situation on a non-bridged address). A call in the INACTIVE state can be joined using [**lineAnswer**](/windows/desktop/api/Tapi/nf-tapi-lineanswer). Many operations that are valid in calls in the CONNECTED state can be impossible in the INACTIVE mode, such as monitoring for tones and digits, because the station is not actually participating in the call; monitoring is usually suspended (although not canceled) while the call is in the INACTIVE mode.


</dt> </dl> </dd> <dt>

<span id="LINECONNECTEDMODE_INACTIVEHELD"></span><span id="lineconnectedmode_inactiveheld"></span>**LINECONNECTEDMODE\_INACTIVEHELD**
</dt> <dd> <dl> <dt>



Indicates that the station is not an active participant in the call, and that the remote party has placed the call on hold. This flag is exposed only to applications that negotiate a TAPI version of 2.0 or higher. (TAPI versions 2.0 and later)


</dt> </dl> </dd> </dl>

## Remarks

Not extensible. All 32 bits are reserved.

For backward compatibility, it is the responsibility of the service provider to examine the negotiated API version on the line, and to not use those LINECONNECTEDMODE\_ values that are not supported on the negotiated version. Applications that are not cognizant of LINECONNECTEDMODE\_ will most likely assume that a call that is in LINECALLSTATE\_CONNECTED is in LINECONNECTEDMODE\_ACTIVE.

The LINECONNECTEDMODE\_ACTIVE and LINECONNECTEDMODE\_INACTIVE values are used when the call is on an address that is shared with other stations (bridged; see [**LINEADDRESSSHARING\_ Constants**](lineaddresssharing--constants.md)), primarily electronic key systems. If the connected call state mode is "active," it means that the call is connected at the current station (the current station is a participant in the call). If the call state mode is "inactive," the call is active at one or more other stations, but the current station is not a participant in the call. If the call state mode is ZERO, the application should assume that the value is "active" (which would be the situation on a non-bridged address). The mode can switch between ACTIVE and INACTIVE during a call if the user joins and leaves the call through manual action.

In such a bridged situation, a [**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop) or [**lineHold**](/windows/desktop/api/Tapi/nf-tapi-linehold) operation may possibly not actually drop the call or place it on hold, because the status of other stations on the call may govern (for example, attempting to "hold" a call when other stations are participating will not be possible); instead, the call can simply be changed to the INACTIVE mode if it remains connected at other stations. A call in the INACTIVE state can be joined using the [**lineAnswer**](/windows/desktop/api/Tapi/nf-tapi-lineanswer).

Many operations that are valid in calls in the connected state can be impossible in the INACTIVE mode, such as monitoring for tones and digits, because the station is not actually participating in the call; monitoring is usually suspended (although not canceled) while the call is in the INACTIVE mode.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**lineAnswer**](/windows/desktop/api/Tapi/nf-tapi-lineanswer)
</dt> <dt>

[**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop)
</dt> <dt>

[**lineHold**](/windows/desktop/api/Tapi/nf-tapi-linehold)
</dt> </dl>

 

 




