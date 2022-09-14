---
description: The BLOB\_CHARACTER\_SET enum indicates the character set used by the current conference blob.
ms.assetid: 79131b84-19b5-492b-a44e-9d47c365b298
title: BLOB_CHARACTER_SET enumeration (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# BLOB\_CHARACTER\_SET enumeration

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **BLOB\_CHARACTER\_SET** enum indicates the character set used by the current conference blob.

## Syntax


```C++
} BLOB_CHARACTER_SET;
```



## Constants

<dl> <dt>

<span id="BCS_ASCII"></span><span id="bcs_ascii"></span>**BCS\_ASCII**
</dt> <dd>

Standard ASCII format.

</dd> <dt>

<span id="BCS_UTF7"></span><span id="bcs_utf7"></span>**BCS\_UTF7**
</dt> <dd>

Seven-bit transformation format of Unicode. For details on this format, conduct an Internet search for RFC 1642.

</dd> <dt>

<span id="BCS_UTF8"></span><span id="bcs_utf8"></span>**BCS\_UTF8**
</dt> <dd>

UCS Transformation Format 8. For details on this format, conduct an Internet search for ISO (the International Organization for Standardization) and IEC (the International Electrotechnical Commission) document ISO/IEC JTC1/SC2/WG2 N 1036, dated August 1, 1994, by WG2 Project Editor.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                               |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl> |



## See also

<dl> <dt>

[**ITDirectoryObjectConference**](/windows/desktop/api/Rend/nn-rend-itdirectoryobjectconference)
</dt> <dt>

[**get\_CharacterSet**](itconferenceblob-get-characterset.md)
</dt> <dt>

[**Init**](itconferenceblob-init.md)
</dt> <dt>

[**SetConferenceBlob**](itconferenceblob-setconferenceblob.md)
</dt> </dl>

 

 




