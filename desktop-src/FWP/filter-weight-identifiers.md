---
title: Filter Weight Identifiers (Fwpmu.h)
description: Filter weight identifiers used by the Base Filtering Engine (BFE) to compute auto-generated filter weights.
ms.assetid: 73d2e9e0-0d3a-474e-b660-f91675f9000e
topic_type:
- apiref
api_name:
- FWPM_AUTO_WEIGHT_BITS
- FWPM_AUTO_WEIGHT_MAX
- FWPM_WEIGHT_RANGE_IKE_EXEMPTIONS
- FWPM_WEIGHT_RANGE_IPSEC
- FWPM_WEIGHT_RANGE_MAX
api_location:
- fwpmu.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Filter Weight Identifiers

The filter weight identifiers used by the Base Filtering Engine (BFE) to compute auto-generated filter weights are listed below.

See [Filter Weight Assignment](filter-weight-assignment.md) for more information on filter weight generation.

<dl> <dt>

<span id="FWPM_AUTO_WEIGHT_BITS"></span><span id="fwpm_auto_weight_bits"></span>**FWPM\_AUTO\_WEIGHT\_BITS**
</dt> <dd> <dl> <dt>

(60)
</dt> <dt>



Number of bits used for auto-generated filter weights.


</dt> </dl> </dd> <dt>

<span id="FWPM_AUTO_WEIGHT_MAX"></span><span id="fwpm_auto_weight_max"></span>**FWPM\_AUTO\_WEIGHT\_MAX**
</dt> <dd> <dl> <dt>

(**MAXUINT64** >> 4)
</dt> <dt>



Maximum auto-generated filter weight.


</dt> </dl> </dd> <dt>

<span id="FWPM_WEIGHT_RANGE_IKE_EXEMPTIONS"></span><span id="fwpm_weight_range_ike_exemptions"></span>**FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**
</dt> <dd> <dl> <dt>

(0xC)
</dt> <dt>



BFE assigns a weight with this range value to IKE and AuthIP filters.

See [IKE/AuthIP Exemptions](ike-exemptions.md) for more information on IKE/AuthIP filters.


</dt> </dl> </dd> <dt>

<span id="FWPM_WEIGHT_RANGE_IPSEC"></span><span id="fwpm_weight_range_ipsec"></span>**FWPM\_WEIGHT\_RANGE\_IPSEC**
</dt> <dd> <dl> <dt>

(0x0)
</dt> <dt>



BFE assigns a weight with this range value to IPsec policy filters.


</dt> </dl> </dd> <dt>

<span id="FWPM_WEIGHT_RANGE_MAX"></span><span id="fwpm_weight_range_max"></span>**FWPM\_WEIGHT\_RANGE\_MAX**
</dt> <dd> <dl> <dt>

(**MAXUINT64** >> 60)
</dt> <dt>



Maximum allowed filter weight range value.


</dt> </dl> </dd> </dl>

> [!Note]  
> **MAXUINT64** represents the largest possible value of **UINT64**. The value of this constant is 0xFFFFFFFFFFFFFFFF.

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Fwpmu.h</dt> </dl> |



 

 





