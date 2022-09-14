---
description: The PARTICIPANT\_EVENT enum describes participant events.
ms.assetid: 678165f2-ad0b-415f-86bf-8c4e3bd8d793
title: PARTICIPANT_EVENT enumeration (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PARTICIPANT\_EVENT enumeration

\[ This enumeration is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **PARTICIPANT\_EVENT** enum describes participant events. The [**ITParticipantEvent::get\_Event**](itparticipantevent-get-event.md) method returns a member of this enum to indicate the type of conference participant event that occurred. This enum is used by applications that access the [IPConf MSP](ipconf-msp.md).

## Syntax


```C++
} PARTICIPANT_EVENT;
```



## Constants

<dl> <dt>

<span id="PE_NEW_PARTICIPANT"></span><span id="pe_new_participant"></span>**PE\_NEW\_PARTICIPANT**
</dt> <dd>

A new participant has been added to the conference.

</dd> <dt>

<span id="PE_INFO_CHANGE"></span><span id="pe_info_change"></span>**PE\_INFO\_CHANGE**
</dt> <dd>

Information on a participant has changed.

</dd> <dt>

<span id="PE_PARTICIPANT_LEAVE"></span><span id="pe_participant_leave"></span>**PE\_PARTICIPANT\_LEAVE**
</dt> <dd>

A participant has left the conference.

</dd> <dt>

<span id="PE_NEW_SUBSTREAM"></span><span id="pe_new_substream"></span>**PE\_NEW\_SUBSTREAM**
</dt> <dd>

A new substream has been added to the participant.

</dd> <dt>

<span id="PE_SUBSTREAM_REMOVED"></span><span id="pe_substream_removed"></span>**PE\_SUBSTREAM\_REMOVED**
</dt> <dd>

A new substream has been removed from the participant.

</dd> <dt>

<span id="PE_SUBSTREAM_MAPPED"></span><span id="pe_substream_mapped"></span>**PE\_SUBSTREAM\_MAPPED**
</dt> <dd>

A participant has been mapped to a substream.

</dd> <dt>

<span id="PE_SUBSTREAM_UNMAPPED"></span><span id="pe_substream_unmapped"></span>**PE\_SUBSTREAM\_UNMAPPED**
</dt> <dd>

A participant has been unmapped from a substream.

</dd> <dt>

<span id="PE_PARTICIPANT_TIMEOUT"></span><span id="pe_participant_timeout"></span>**PE\_PARTICIPANT\_TIMEOUT**
</dt> <dd>

A participant has been removed from the conference due to a timeout.

</dd> <dt>

<span id="PE_PARTICIPANT_RECOVERED"></span><span id="pe_participant_recovered"></span>**PE\_PARTICIPANT\_RECOVERED**
</dt> <dd>

A removed participant is again visible. Usually, this is a participant who timed out but signals are now being received.

</dd> <dt>

<span id="PE_PARTICIPANT_ACTIVE"></span><span id="pe_participant_active"></span>**PE\_PARTICIPANT\_ACTIVE**
</dt> <dd>

The participant has become active in the conference.

</dd> <dt>

<span id="PE_PARTICIPANT_INACTIVE"></span><span id="pe_participant_inactive"></span>**PE\_PARTICIPANT\_INACTIVE**
</dt> <dd>

The participant has become inactive in the conference.

</dd> <dt>

<span id="PE_LOCAL_TALKING"></span><span id="pe_local_talking"></span>**PE\_LOCAL\_TALKING**
</dt> <dd>

The local participant has started to talk.

</dd> <dt>

<span id="PE_LOCAL_SILENT"></span><span id="pe_local_silent"></span>**PE\_LOCAL\_SILENT**
</dt> <dd>

The local participant has become silent in the conference.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                              |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl> |



## See also

<dl> <dt>

[**ITParticipantEvent::get\_Event**](itparticipantevent-get-event.md)
</dt> <dt>

[IPConf MSP](ipconf-msp.md)
</dt> <dt>

[IPConf MSP Interfaces](ipconf-msp-interfaces.md)
</dt> </dl>

 

 




