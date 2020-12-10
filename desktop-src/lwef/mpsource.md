---
title: MPSOURCE enumeration (MpClient.h)
description: Possible category of source.
ms.assetid: 1AD12D67-C74B-481A-AC9B-D119AABDB6E9
keywords:
- MPSOURCE enumeration Legacy Windows Environment Features
- PMPSOURCE enumeration pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPSOURCE
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPSOURCE enumeration

Possible category of source.

## Syntax


```C++
typedef enum tagMPSOURCE { 
  MPSOURCE_UNKNOWN             = 0,
  MPSOURCE_USER                = 1,
  MPSOURCE_SYSTEM              = 2,
  MPSOURCE_REALTIME            = 3,
  MPSOURCE_IOAV                = 4,
  MPSOURCE_NIS                 = 5,
  MPSOURCE_BHO                 = 6,
  MPSOURCE_IEPROTECT           = 6,
  MPSOURCE_ELAM                = 7,
  MPSOURCE_LOCAL_ATTESTATION   = 8,
  MPSOURCE_REMOTE_ATTESTATION  = 9,
  MPSOURCE_AMSI                = 10,
  MP_SOURCE_MAXVALUE           = 10
} MPSOURCE, *PMPSOURCE;
```



## Constants

<dl> <dt>

<span id="MPSOURCE_UNKNOWN"></span><span id="mpsource_unknown"></span>**MPSOURCE\_UNKNOWN**
</dt> <dd>

Source unknown.

</dd> <dt>

<span id="MPSOURCE_USER"></span><span id="mpsource_user"></span>**MPSOURCE\_USER**
</dt> <dd>

User initiated.

</dd> <dt>

<span id="MPSOURCE_SYSTEM"></span><span id="mpsource_system"></span>**MPSOURCE\_SYSTEM**
</dt> <dd>

system initiated.

</dd> <dt>

<span id="MPSOURCE_REALTIME"></span><span id="mpsource_realtime"></span>**MPSOURCE\_REALTIME**
</dt> <dd>

Realtime component initiated.

</dd> <dt>

<span id="MPSOURCE_IOAV"></span><span id="mpsource_ioav"></span>**MPSOURCE\_IOAV**
</dt> <dd>

IE Downloads and Outlook Express Attachments initiated.

</dd> <dt>

<span id="MPSOURCE_NIS"></span><span id="mpsource_nis"></span>**MPSOURCE\_NIS**
</dt> <dd>

Network inspection system.

</dd> <dt>

<span id="MPSOURCE_BHO"></span><span id="mpsource_bho"></span>**MPSOURCE\_BHO**
</dt> <dd>

BHO - web script (deprecated).

</dd> <dt>

<span id="MPSOURCE_IEPROTECT"></span><span id="mpsource_ieprotect"></span>**MPSOURCE\_IEPROTECT**
</dt> <dd>

IE - IExtensionValidation.

</dd> <dt>

<span id="MPSOURCE_ELAM"></span><span id="mpsource_elam"></span>**MPSOURCE\_ELAM**
</dt> <dd>

ELAM

</dd> <dt>

<span id="MPSOURCE_LOCAL_ATTESTATION"></span><span id="mpsource_local_attestation"></span>**MPSOURCE\_LOCAL\_ATTESTATION**
</dt> <dd>

Local attestation.

</dd> <dt>

<span id="MPSOURCE_REMOTE_ATTESTATION"></span><span id="mpsource_remote_attestation"></span>**MPSOURCE\_REMOTE\_ATTESTATION**
</dt> <dd>

Remote attestation.

</dd> <dt>

<span id="MPSOURCE_AMSI"></span><span id="mpsource_amsi"></span>**MPSOURCE\_AMSI**
</dt> <dd>

AMSI

</dd> <dt>

<span id="MP_SOURCE_MAXVALUE"></span><span id="mp_source_maxvalue"></span>**MP\_SOURCE\_MAXVALUE**
</dt> <dd>

Maximum value possible.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





