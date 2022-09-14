---
title: MPTHREAT_INFOEX_BEHAVIOR structure (MpClient.h)
description: Contains behavior modification-specific information.
ms.assetid: 762E755F-5BA1-476D-B395-6617093309C5
keywords:
- MPTHREAT_INFOEX_BEHAVIOR structure Legacy Windows Environment Features
- PMPTHREAT_INFOEX_BEHAVIOR structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_INFOEX_BEHAVIOR
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_INFOEX\_BEHAVIOR structure

Contains behavior modification-specific information.

## Syntax


```C++
typedef struct tagMPTHREAT_INFOEX_BEHAVIOR {
  ULARGE_INTEGER         SignatureID;
  ULONGLONG              EngineVersion;
  ULONGLONG              ASDeltaSignatureVersion;
  ULONGLONG              AVDeltaSignatureVersion;
  MP_HASH_TYPE           HashType;
  DWORD                  FidelityValue;
  MP_MIDL_STRING  LPWSTR HashValue;
  MP_MIDL_STRING  LPWSTR TargetFileName;
  MP_MIDL_STRING  LPWSTR TargetFileHash;
} MPTHREAT_INFOEX_BEHAVIOR, *PMPTHREAT_INFOEX_BEHAVIOR;
```



## Members

<dl> <dt>

**SignatureID**
</dt> <dd>

Type: **ULARGE\_INTEGER**

</dd> <dd>

Behavior modification signature ID given by the engine at the time of detection.

</dd> <dt>

**EngineVersion**
</dt> <dd>

Type: **ULONGLONG**

</dd> <dd>

Engine module version.

</dd> <dt>

**ASDeltaSignatureVersion**
</dt> <dd>

Type: **ULONGLONG**

</dd> <dd>

Antispyware signature version.

</dd> <dt>

**AVDeltaSignatureVersion**
</dt> <dd>

Type: **ULONGLONG**

</dd> <dd>

Antivirus signature version

</dd> <dt>

**HashType**
</dt> <dd>

Type: **[**MP\_HASH\_TYPE**](mp-hash-type.md)**

</dd> <dd>

Hash type used. See [**MP\_HASH\_TYPE**](mp-hash-type.md).

</dd> <dt>

**FidelityValue**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Fidelity value.

</dd> <dt>

**HashValue**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

The hash of the file.

</dd> <dt>

**TargetFileName**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

The path and name of the targeted file.

</dd> <dt>

**TargetFileHash**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

The hash of the targeted file.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MP\_HASH\_TYPE**](mp-hash-type.md)
</dt> </dl>

 

 





