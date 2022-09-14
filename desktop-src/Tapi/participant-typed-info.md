---
description: The members of the PARTICIPANT\_TYPED\_INFO enum identify the type of participant information being retrieved by the ITParticipant::get\_ParticipantTypedInfo method. This enum is used by applications that access the IPConf MSP.
ms.assetid: ca933d8c-bfb4-4a92-b412-112e228ccca2
title: PARTICIPANT_TYPED_INFO enumeration (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PARTICIPANT\_TYPED\_INFO enumeration

\[**PARTICIPANT\_TYPED\_INFO** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The members of the **PARTICIPANT\_TYPED\_INFO** enum identify the type of participant information being retrieved by the [**ITParticipant::get\_ParticipantTypedInfo**](itparticipant-get-participanttypedinfo.md) method. This enum is used by applications that access the [IPConf MSP](ipconf-msp.md).

## Syntax


```C++
} PARTICIPANT_TYPED_INFO;
```



## Constants

<dl> <dt>

<span id="PTI_CANONICALNAME"></span><span id="pti_canonicalname"></span>**PTI\_CANONICALNAME**
</dt> <dd>

Canonical name of participant, such as someone@example.com.

</dd> <dt>

<span id="PTI_NAME"></span><span id="pti_name"></span>**PTI\_NAME**
</dt> <dd>

Displayable name of participant.

</dd> <dt>

<span id="PTI_EMAILADDRESS"></span><span id="pti_emailaddress"></span>**PTI\_EMAILADDRESS**
</dt> <dd>

Participant's email address.

</dd> <dt>

<span id="PTI_PHONENUMBER"></span><span id="pti_phonenumber"></span>**PTI\_PHONENUMBER**
</dt> <dd>

Participant's phone address.

</dd> <dt>

<span id="PTI_LOCATION"></span><span id="pti_location"></span>**PTI\_LOCATION**
</dt> <dd>

Participant's geographical address.

</dd> <dt>

<span id="PTI_TOOL"></span><span id="pti_tool"></span>**PTI\_TOOL**
</dt> <dd>

Participant's application.

</dd> <dt>

<span id="PTI_NOTES"></span><span id="pti_notes"></span>**PTI\_NOTES**
</dt> <dd>

Notes concerning participant.

</dd> <dt>

<span id="PTI_PRIVATE"></span><span id="pti_private"></span>**PTI\_PRIVATE**
</dt> <dd>

Defines an experimental or application-specific Source Description (SDES) extension. See RFC 1889 for details.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |



## See also

<dl> <dt>

[**ITParticipant::get\_ParticipantTypedInfo**](itparticipant-get-participanttypedinfo.md)
</dt> <dt>

[IPConf MSP](ipconf-msp.md)
</dt> <dt>

[IPConf MSP Interfaces](ipconf-msp-interfaces.md)
</dt> </dl>

 

 




