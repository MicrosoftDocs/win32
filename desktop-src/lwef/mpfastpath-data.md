---
title: MPFASTPATH_DATA structure (MpClient.h)
description: FastPath update notification.
ms.assetid: E19F153D-DD46-4E27-9A4B-33586794DAC2
keywords:
- MPFASTPATH_DATA structure Legacy Windows Environment Features
- PMPFASTPATH_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPFASTPATH_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPFASTPATH\_DATA structure

FastPath update notification.

## Syntax


```C++
typedef struct tagMPFASTPATH_DATA {
  MP_SIGNATURE_TYPE         SignatureType;
  MP_FASTPATH_TYPE          FastPathSignatureType;
  MP_MIDL_STRING LPWSTR     FastPathSignatureVersion;
  ULARGE_INTEGER            CompilationTimestamp;
  MP_PERSISTENCE_LIMIT_TYPE PersistenceType;
  MP_MIDL_STRING LPWSTR     PersistenceValue;
  MP_MIDL_STRING LPWSTR     PersistencePath;
  MP_REMOVAL_REASON         Reason;
} MPFASTPATH_DATA, *PMPFASTPATH_DATA;
```



## Members

<dl> <dt>

**SignatureType**
</dt> <dd>

Type: **[**MP\_SIGNATURE\_TYPE**](mp-signature-type.md)**

</dd> <dd>

Signature type.

</dd> <dt>

**FastPathSignatureType**
</dt> <dd>

Type: **[**MP\_FASTPATH\_TYPE**](mp-fastpath-type.md)**

</dd> <dd>

FastPath signature type.

</dd> <dt>

**FastPathSignatureVersion**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

FastPath signature version (optional).

</dd> <dt>

**CompilationTimestamp**
</dt> <dd>

Type: **ULARGE\_INTEGER**

</dd> <dd>

Compilation timestamp (UTC).

</dd> <dt>

**PersistenceType**
</dt> <dd>

Type: **[**MP\_PERSISTENCE\_LIMIT\_TYPE**](mp-persistence-limit-type.md)**

</dd> <dd>

Persistence type (optional).

</dd> <dt>

**PersistenceValue**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Persistence value (optional).

</dd> <dt>

**PersistencePath**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Persistence path (optional).

</dd> <dt>

**Reason**
</dt> <dd>

Type: **[**MP\_REMOVAL\_REASON**](mp-removal-reason.md)**

</dd> <dd>

Reason for signature removal.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MP\_FASTPATH\_TYPE**](mp-fastpath-type.md)
</dt> <dt>

[**MP\_PERSISTENCE\_LIMIT\_TYPE**](mp-persistence-limit-type.md)
</dt> <dt>

[**MP\_SIGNATURE\_TYPE**](mp-signature-type.md)
</dt> </dl>

 

 





