---
description: The H245\_CAPABILITY enum describes audio and video format support.
ms.assetid: 76aeb3a1-3233-4425-b9db-efacbedc309e
title: H245_CAPABILITY enumeration (H323priv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# H245\_CAPABILITY enumeration

\[**H245\_CAPABILITY** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **H245\_CAPABILITY** enum describes audio and video format support.

## Syntax


```C++
} H245_CAPABILITY;
```



## Constants

<dl> <dt>

<span id="HC_G711"></span><span id="hc_g711"></span>**HC\_G711**
</dt> <dd>

The G.711 audio protocol is supported.

</dd> <dt>

<span id="HC_G723"></span><span id="hc_g723"></span>**HC\_G723**
</dt> <dd>

The G.723 audio protocol is supported.

</dd> <dt>

<span id="HC_H263QCIF"></span><span id="hc_h263qcif"></span>**HC\_H263QCIF**
</dt> <dd>

The H.263 video protocol is supported.

</dd> <dt>

<span id="HC_H261QCIF"></span><span id="hc_h261qcif"></span>**HC\_H261QCIF**
</dt> <dd>

The H.263 video protocol is supported.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>H323priv.h</dt> </dl> |



## See also

<dl> <dt>

[**IH323LineEx::SetDefaultCapabilityPreferrence**](ih323lineex-setdefaultcapabilitypreferrence.md)
</dt> </dl>

 

 




