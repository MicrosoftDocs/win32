---
description: The LINEFORWARDMODE\_ bit-flag constants describe the conditions under which calls to an address can be forwarded.
ms.assetid: 8cc053bd-1056-42be-b48a-d2312c456893
title: LINEFORWARDMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEFORWARDMODE\_ Constants

The **LINEFORWARDMODE\_** bit-flag constants describe the conditions under which calls to an address can be forwarded.

<dl> <dt>

<span id="LINEFORWARDMODE_BUSY"></span><span id="lineforwardmode_busy"></span>**LINEFORWARDMODE\_BUSY**
</dt> <dd> <dl> <dt>



Forward all calls on busy, irrespective of their origin. Use this value when forwarding for internal and external calls on busy and on no answer cannot be controlled separately.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_BUSYEXTERNAL"></span><span id="lineforwardmode_busyexternal"></span>**LINEFORWARDMODE\_BUSYEXTERNAL**
</dt> <dd> <dl> <dt>



Forward all external calls on busy. Use this value when forwarding for internal and external calls on busy and on no answer can be controlled separately.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_BUSYINTERNAL"></span><span id="lineforwardmode_busyinternal"></span>**LINEFORWARDMODE\_BUSYINTERNAL**
</dt> <dd> <dl> <dt>



Forward all internal calls on busy. Use this value when forwarding for internal and external calls on busy and on no answer can be controlled separately.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_BUSYNA"></span><span id="lineforwardmode_busyna"></span>**LINEFORWARDMODE\_BUSYNA**
</dt> <dd> <dl> <dt>



Forward all calls on busy/no answer, irrespective of their origin. Use this value when forwarding for internal and external calls on busy and on no answer cannot be controlled separately.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_BUSYNAEXTERNAL"></span><span id="lineforwardmode_busynaexternal"></span>**LINEFORWARDMODE\_BUSYNAEXTERNAL**
</dt> <dd> <dl> <dt>



Forward all external calls on busy/no answer. Use this value when call forwarding on busy and on no answer cannot be controlled separately for internal calls.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_BUSYNAINTERNAL"></span><span id="lineforwardmode_busynainternal"></span>**LINEFORWARDMODE\_BUSYNAINTERNAL**
</dt> <dd> <dl> <dt>



Forward all internal calls on busy/no answer. Use this value when call forwarding on busy and on no answer cannot be controlled separately for internal calls.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_BUSYNASPECIFIC"></span><span id="lineforwardmode_busynaspecific"></span>**LINEFORWARDMODE\_BUSYNASPECIFIC**
</dt> <dd> <dl> <dt>



Forward on busy/no answer all calls that originated at a specified address (selective call forwarding).


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_BUSYSPECIFIC"></span><span id="lineforwardmode_busyspecific"></span>**LINEFORWARDMODE\_BUSYSPECIFIC**
</dt> <dd> <dl> <dt>



Forward on busy all calls that originated at a specified address (selective call forwarding).


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_NOANSW"></span><span id="lineforwardmode_noansw"></span>**LINEFORWARDMODE\_NOANSW**
</dt> <dd> <dl> <dt>



Forward all calls on no answer, irrespective of their origin. Use this value when call forwarding for internal and external calls on no answer cannot be controlled separately.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_NOANSWEXTERNAL"></span><span id="lineforwardmode_noanswexternal"></span>**LINEFORWARDMODE\_NOANSWEXTERNAL**
</dt> <dd> <dl> <dt>



Forward all external calls on no answer. Use this value when forwarding for internal and external calls on no answer can be controlled separately.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_NOANSWINTERNAL"></span><span id="lineforwardmode_noanswinternal"></span>**LINEFORWARDMODE\_NOANSWINTERNAL**
</dt> <dd> <dl> <dt>



Forward all internal calls on no answer. Use this value when forwarding for internal and external calls on no answer can be controlled separately.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_NOANSWSPECIFIC"></span><span id="lineforwardmode_noanswspecific"></span>**LINEFORWARDMODE\_NOANSWSPECIFIC**
</dt> <dd> <dl> <dt>



Forward on no answer all calls that originated at a specified address (selective call forwarding).


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_UNAVAIL"></span><span id="lineforwardmode_unavail"></span>**LINEFORWARDMODE\_UNAVAIL**
</dt> <dd> <dl> <dt>



Calls are forwarded, but the conditions under which forwarding will occur are not known, and will never be known by the service provider. (TAPI versions 1.4 and later)


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_UNCOND"></span><span id="lineforwardmode_uncond"></span>**LINEFORWARDMODE\_UNCOND**
</dt> <dd> <dl> <dt>



Forward all calls unconditionally, irrespective of their origin. Use this value when unconditional forwarding for internal and external calls cannot be controlled separately. Unconditional forwarding overrides forwarding on busy and/or no answer conditions.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_UNCONDEXTERNAL"></span><span id="lineforwardmode_uncondexternal"></span>**LINEFORWARDMODE\_UNCONDEXTERNAL**
</dt> <dd> <dl> <dt>



Forward all external calls unconditionally. Use this value when unconditional forwarding for internal and external calls can be controlled separately.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_UNCONDINTERNAL"></span><span id="lineforwardmode_uncondinternal"></span>**LINEFORWARDMODE\_UNCONDINTERNAL**
</dt> <dd> <dl> <dt>



Forward all internal calls unconditionally. Use this value when unconditional forwarding for internal and external calls can be controlled separately.


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_UNCONDSPECIFIC"></span><span id="lineforwardmode_uncondspecific"></span>**LINEFORWARDMODE\_UNCONDSPECIFIC**
</dt> <dd> <dl> <dt>



Unconditionally forward all calls that originated at a specified address (selective call forwarding).


</dt> </dl> </dd> <dt>

<span id="LINEFORWARDMODE_UNKNOWN"></span><span id="lineforwardmode_unknown"></span>**LINEFORWARDMODE\_UNKNOWN**
</dt> <dd> <dl> <dt>



Calls are forwarded, but the conditions under which forwarding will occur are not known at this time. It is possible that the conditions may become known at a future time. (TAPI versions 1.4 and later)


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

The bit flags defined by LINEFORWARDMODE\_ are not orthogonal. Unconditional forwarding ignores any specific condition such as busy or no answer. If unconditional forwarding is not in effect, then forwarding on busy and on no answer can be controlled separately or not separately. If controlled separately, the LINEFORWARDMODE\_BUSY and LINEFORWARDMODE\_NOANSW flags can be used separately. If not controlled separately, the flag LINEFORWARDMODE\_BUSYNA must be used. Similarly, if forwarding of internal and external calls can be controlled separately, then LINEFORWARDMODE\_INTERNAL and LINEFORWARDMODE\_EXTERNAL flags can be used separately; otherwise the combination is used.

Address capabilities indicate which forwarding modes are available for each address assigned to a line. An application can use [**lineForward**](/windows/desktop/api/Tapi/nf-tapi-lineforward) to set forwarding conditions at the switch.

For backward compatibility, it is the responsibility of the service provider to examine the negotiated API version on the line, and to not use these LINEFORWARDMODE\_ values if the negotiated version does not support them.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




