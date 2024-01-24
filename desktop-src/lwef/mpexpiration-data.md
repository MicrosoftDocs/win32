---
title: MPEXPIRATION_DATA structure (MpClient.h)
description: Product expiration status notification.
ms.assetid: BF464FFD-16AE-4F46-83CD-E0355478180C
keywords:
- MPEXPIRATION_DATA structure Legacy Windows Environment Features
- PMPEXPIRATION_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPEXPIRATION_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPEXPIRATION\_DATA structure

Product expiration status notification.

## Syntax


```C++
typedef struct tagMPEXPIRATION_DATA {
  MP_EXPIRE_REASON       Reason;
  MP_EXPIRE_STATE_REPORT State;
} MPEXPIRATION_DATA, *PMPEXPIRATION_DATA;
```



## Members

<dl> <dt>

**Reason**
</dt> <dd>

Type: **MP\_EXPIRE\_REASON**

</dd> <dd>

Expiration reason. This is one of the following possible values:



| Value                                                                                                                                                                                                                                | Meaning                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| <span id="MP_EXPIRED_UNKNOWN"></span><span id="mp_expired_unknown"></span><dl> <dt>**MP\_EXPIRED\_UNKNOWN**</dt> <dt>0</dt> </dl> | Unknown.<br/>    |
| <span id="MP_EXPIRED_EVAL"></span><span id="mp_expired_eval"></span><dl> <dt>**MP\_EXPIRED\_EVAL**</dt> <dt>1</dt> </dl>          | Evaluation.<br/> |
| <span id="MP_EXPIRED_WAT"></span><span id="mp_expired_wat"></span><dl> <dt>**MP\_EXPIRED\_WAT**</dt> <dt>2</dt> </dl>             | WAT.<br/>        |



 

</dd> <dt>

**State**
</dt> <dd>

Type: **MP\_EXPIRE\_STATE\_REPORT**

</dd> <dd>

Expiration state. This is one of the following possible values:



| Value                                                                                                                                                                                                                                                                      | Meaning                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| <span id="MP_EXPIRE_STATE_REPORT_UNKNOWN"></span><span id="mp_expire_state_report_unknown"></span><dl> <dt>**MP\_EXPIRE\_STATE\_REPORT\_UNKNOWN**</dt> <dt>0</dt> </dl> | State unknown.<br/> |
| <span id="MP_EXPIRE_STATE_REPORT_VALID"></span><span id="mp_expire_state_report_valid"></span><dl> <dt>**MP\_EXPIRE\_STATE\_REPORT\_VALID**</dt> <dt>1</dt> </dl>       | No expiration.<br/> |
| <span id="MP_EXPIRE_STATE_REPORT_WARNING"></span><span id="mp_expire_state_report_warning"></span><dl> <dt>**MP\_EXPIRE\_STATE\_REPORT\_WARNING**</dt> <dt>2</dt> </dl> | Near expired.<br/>  |
| <span id="MP_EXPIRE_STATE_REPORT_EXPIRED"></span><span id="mp_expire_state_report_expired"></span><dl> <dt>**MP\_EXPIRE\_STATE\_REPORT\_EXPIRED**</dt> <dt>3</dt> </dl> | Expired.<br/>       |



 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





