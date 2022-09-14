---
title: MP_SIGNATURE_TYPE enumeration (MpClient.h)
description: Possible signature types.
ms.assetid: 44B195A8-866D-4B87-9576-54E00658F9B3
keywords:
- MP_SIGNATURE_TYPE enumeration Legacy Windows Environment Features
- PMP_SIGNATURE_TYPE enumeration pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MP_SIGNATURE_TYPE
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MP\_SIGNATURE\_TYPE enumeration

Possible signature types.

## Syntax


```C++
typedef enum tagMP_SIGNATURE_TYPE { 
  MP_SIGNATURE_ANTIMALWARE     = 0,
  MP_SIGNATURE_ANTIVIRUS       = 1,
  MP_SIGNATURE_ANTISPYWARE     = 2,
  MP_SIGNATURE_NIS             = 3,
  MP_SIGNATURE_TYPES_MAXVALUE  = 3
} MP_SIGNATURE_TYPE, *PMP_SIGNATURE_TYPE;
```



## Constants

<dl> <dt>

<span id="MP_SIGNATURE_ANTIMALWARE"></span><span id="mp_signature_antimalware"></span>**MP\_SIGNATURE\_ANTIMALWARE**
</dt> <dd>

Both antivirus and antispyware signatures.

</dd> <dt>

<span id="MP_SIGNATURE_ANTIVIRUS"></span><span id="mp_signature_antivirus"></span>**MP\_SIGNATURE\_ANTIVIRUS**
</dt> <dd>

Only antivirus signatures.

</dd> <dt>

<span id="MP_SIGNATURE_ANTISPYWARE"></span><span id="mp_signature_antispyware"></span>**MP\_SIGNATURE\_ANTISPYWARE**
</dt> <dd>

Only antispyware signatures.

</dd> <dt>

<span id="MP_SIGNATURE_NIS"></span><span id="mp_signature_nis"></span>**MP\_SIGNATURE\_NIS**
</dt> <dd>

NIS signatures.

</dd> <dt>

<span id="MP_SIGNATURE_TYPES_MAXVALUE"></span><span id="mp_signature_types_maxvalue"></span>**MP\_SIGNATURE\_TYPES\_MAXVALUE**
</dt> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





