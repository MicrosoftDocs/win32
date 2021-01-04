---
title: BITS_JOB_PROPERTY_VALUE structure (Deliveryoptimization.h)
description: The BITS_JOB_PROPERTY_VALUE union provides the property value of the DO job based on the value of the BITS_JOB_PROPERTY_ID enumeration.
ms.assetid: C24D9EA1-2E72-4403-939A-7B01D7133FE7
keywords:
- BITS_JOB_PROPERTY_VALUE structure
- BITS_JOB_PROPERTY_VALUE structure
topic_type:
- apiref
api_name:
- BITS_JOB_PROPERTY_VALUE
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# BITS_JOB_PROPERTY_VALUE structure

The **BITS_JOB_PROPERTY_VALUE** union provides the property value of the DO job based on the value of the [**BITS_JOB_PROPERTY_ID**](bits-job-property-id.md) enumeration.

## Syntax


```C++
typedef struct {
  DWORD          Dword;
  GUID           ClsID;
  BOOL           Enable;
  UINT64         Uint64;
  BG_AUTH_TARGET Target;
} BITS_JOB_PROPERTY_VALUE;
```



## Members

<dl> <dt>

**Dword**
</dt> <dd>

This value is returned when using the enum property ID **BITS_JOB_PROPERTY_ID_COST_FLAGS** and is applied as the [transfer policy](https://www.bing.com/search?q=transfer+policy) on the DO job.

</dd> <dt>

**ClsID**
</dt> <dd>

This value is returned when using the enum property ID **BITS_JOB_PROPERTY_NOTIFICATION_CLSID** and represents the CLSID of the callback object to register with the DO job.

</dd> <dt>

**Enable**
</dt> <dd>

Not supported.

</dd> <dt>

**Uint64**
</dt> <dd>

Not supported.

</dd> <dt>

**Target**
</dt> <dd>

Not supported.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



## See also

<dl> <dt>

[**BITS_JOB_PROPERTY_ID**](bits-job-property-id.md)
</dt> <dt>

[**BITS_JOB_TRANSFER_POLICY**](bits-job-transfer-policy-.md)
</dt> </dl>

 

 





