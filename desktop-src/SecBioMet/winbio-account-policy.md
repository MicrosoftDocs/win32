---
title: WINBIO_ACCOUNT_POLICY structure (Winbio\_adapter.h)
description: Contains either a default or account-specific antispoofing policy.
ms.assetid: 7098FC53-E487-42B2-8B4B-EB7E2D296CB6
keywords:
- WINBIO_ACCOUNT_POLICY structure Windows Biometric Framework API
- PWINBIO_ACCOUNT_POLICY structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_ACCOUNT_POLICY
api_location:
- Winbio_adapter.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_ACCOUNT\_POLICY structure

The **WINBIO\_ACCOUNT\_POLICY** structure contains either a default or account-specific antispoofing policy.

## Syntax


```C++
typedef struct _WINBIO_ACCOUNT_POLICY {
  WINBIO_IDENTITY                 Identity;
  WINBIO_ANTI_SPOOF_POLICY_ACTION AntiSpoofBehavior;
} WINBIO_ACCOUNT_POLICY, *PWINBIO_ACCOUNT_POLICY;
```



## Members

<dl> <dt>

**Identity**
</dt> <dd>

A [**WINBIO\_IDENTITY**](winbio-identity.md) structure that specifies the account information.

</dd> <dt>

**AntiSpoofBehavior**
</dt> <dd>

One of the [**WINBIO\_ANTI\_SPOOF\_POLICY\_ACTION**](winbio-anti-spoof-policy-action.md) enumeration values that specifies what antispoofing policy action to use for the account.

</dd> </dl>

## Remarks

See the discussion of the [**EngineAdapterSetAccountPolicy**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_set_account_policy_fn) method for a description of how this structure is used.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                     |
| Header<br/>                   | <dl> <dt>Winbio\_adapter.h (include Winbio\_adapter.h)</dt> </dl> |



 

 





