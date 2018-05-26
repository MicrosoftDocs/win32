---
title: WINBIO\_ANTI\_SPOOF\_POLICY structure
description: Represents the antispoofing policy for a user.
ms.assetid: 2B433AE8-21A0-4AF1-853C-9074527DB2E4
keywords:
- WINBIO_ANTI_SPOOF_POLICY structure Windows Biometric Framework API
- PWINBIO_ANTI_SPOOF_POLICY structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_ANTI_SPOOF_POLICY
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WINBIO\_ANTI\_SPOOF\_POLICY structure

Represents the antispoofing policy for a user.

## Syntax


```C++
typedef struct _WINBIO_ANTI_SPOOF_POLICY {
  WINBIO_ANTI_SPOOF_POLICY_ACTION Action;
  WINBIO_POLICY_SOURCE            Source;
} WINBIO_ANTI_SPOOF_POLICY, *PWINBIO_ANTI_SPOOF_POLICY;
```



## Members

<dl> <dt>

**Action**
</dt> <dd>

The type of action to take for the antispoofing policy.

</dd> <dt>

**Source**
</dt> <dd>

The source for the antispoofing policy.

</dd> </dl>

## Requirements



|                                     |                                                                                                                                                                          |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                                                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                                                                     |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h for client applications or Winbio\_adapters.h for adapters)</dt> </dl> |



## See also

<dl> <dt>

[**WINBIO\_ANTI\_SPOOF\_POLICY\_ACTION**](winbio-anti-spoof-policy-action.md)
</dt> <dt>

[**WINBIO\_POLICY\_SOURCE**](winbio-policy-source.md)
</dt> <dt>

[**WINBIO\_ASYNC\_RESULT**](/windows/win32/Winbio/ns-winbio-_winbio_async_result?branch=master)
</dt> <dt>

[**WinBioGetProperty**](/windows/win32/Winbio/nf-winbio-winbiogetproperty?branch=master)
</dt> <dt>

[**WinBioSetProperty**](/windows/win32/winbio/nf-winbio-winbiosetproperty?branch=master)
</dt> </dl>

 

 





