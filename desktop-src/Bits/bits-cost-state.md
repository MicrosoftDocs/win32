---
title: BITS_COST_STATE (Bits5\_0.h)
description: The BITS\_COST\_STATE enumeration defines the constant values that specify the BITS cost state.
ms.assetid: A8C36D4E-98B3-45C4-9ECD-9B5280133176
topic_type:
- apiref
api_name:
- BITS_COST_STATE_UNRESTRICTED
- BITS_COST_STATE_CAPPED_USAGE_UNKNOWN
- BITS_COST_STATE_BELOW_CAP
- BITS_COST_STATE_NEAR_CAP
- BITS_COST_STATE_OVERCAP_CHARGED
- BITS_COST_STATE_OVERCAP_THROTTLED
- BITS_COST_STATE_USAGE_BASED
- BITS_COST_OPTION_IGNORE_CONGESTION
- BITS_COST_STATE_RESERVED
- BITS_COST_STATE_TRANSFER_NOT_ROAMING
- BITS_COST_STATE_TRANSFER_NO_SURCHARGE
- BITS_COST_STATE_TRANSFER_STANDARD
- BITS_COST_STATE_TRANSFER_UNRESTRICTED
- BITS_COST_STATE_TRANSFER_ALWAYS
api_location:
- Bits5_0.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 02/20/2019
---

# BITS\_COST\_STATE

Defines constants that specify the BITS cost state.

<dl> <dt>

<span id="BITS_COST_STATE_UNRESTRICTED"></span><span id="bits_cost_state_unrestricted"></span>**BITS\_COST\_STATE\_UNRESTRICTED**
</dt> <dd> <dl> <dt>

0x1
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_CAPPED_USAGE_UNKNOWN"></span><span id="bits_cost_state_capped_usage_unknown"></span>**BITS\_COST\_STATE\_CAPPED\_USAGE\_UNKNOWN**
</dt> <dd> <dl> <dt>

0x2
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_BELOW_CAP"></span><span id="bits_cost_state_below_cap"></span>**BITS\_COST\_STATE\_BELOW\_CAP**
</dt> <dd> <dl> <dt>

0x4
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_NEAR_CAP"></span><span id="bits_cost_state_near_cap"></span>**BITS\_COST\_STATE\_NEAR\_CAP**
</dt> <dd> <dl> <dt>

0x8
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_OVERCAP_CHARGED"></span><span id="bits_cost_state_overcap_charged"></span>**BITS\_COST\_STATE\_OVERCAP\_CHARGED**
</dt> <dd> <dl> <dt>

0x10
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_OVERCAP_THROTTLED"></span><span id="bits_cost_state_overcap_throttled"></span>**BITS\_COST\_STATE\_OVERCAP\_THROTTLED**
</dt> <dd> <dl> <dt>

0x20
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_USAGE_BASED"></span><span id="bits_cost_state_usage_based"></span>**BITS\_COST\_STATE\_USAGE\_BASED**
</dt> <dd> <dl> <dt>

0x40
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_OPTION_IGNORE_CONGESTION"></span><span id="bits_cost_option_ignore_congestion"></span>**BITS\_COST\_OPTION\_IGNORE\_CONGESTION**
</dt> <dd> <dl> <dt>

0x80000000
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_RESERVED"></span><span id="bits_cost_state_reserved"></span>**BITS\_COST\_STATE\_RESERVED**
</dt> <dd> <dl> <dt>

0x40000000
</dt> <dt>



Reserved.


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_TRANSFER_NOT_ROAMING"></span><span id="bits_cost_state_transfer_not_roaming"></span>**BITS\_COST\_STATE\_TRANSFER\_NOT\_ROAMING**
</dt> <dd> <dl> <dt>

(BITS\_COST\_OPTION\_IGNORE\_CONGESTION \| BITS\_COST\_STATE\_USAGE\_BASED \| BITS\_COST\_STATE\_OVERCAP\_THROTTLED \| BITS\_COST\_STATE\_OVERCAP\_CHARGED \| BITS\_COST\_STATE\_NEAR\_CAP \| BITS\_COST\_STATE\_BELOW\_CAP \| BITS\_COST\_STATE\_CAPPED\_USAGE\_UNKNOWN \| BITS\_COST\_STATE\_UNRESTRICTED) 
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_TRANSFER_NO_SURCHARGE"></span><span id="bits_cost_state_transfer_no_surcharge"></span>**BITS\_COST\_STATE\_TRANSFER\_NO\_SURCHARGE**
</dt> <dd> <dl> <dt>

(BITS\_COST\_OPTION\_IGNORE\_CONGESTION \| BITS\_COST\_STATE\_USAGE\_BASED \| BITS\_COST\_STATE\_OVERCAP\_THROTTLED \| BITS\_COST\_STATE\_NEAR\_CAP \| BITS\_COST\_STATE\_BELOW\_CAP \| BITS\_COST\_STATE\_CAPPED\_USAGE\_UNKNOWN \| BITS\_COST\_STATE\_UNRESTRICTED)
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_TRANSFER_STANDARD"></span><span id="bits_cost_state_transfer_standard"></span>**BITS\_COST\_STATE\_TRANSFER\_STANDARD**
</dt> <dd> <dl> <dt>

(BITS\_COST\_OPTION\_IGNORE\_CONGESTION \| BITS\_COST\_STATE\_USAGE\_BASED \| BITS\_COST\_STATE\_OVERCAP\_THROTTLED \| BITS\_COST\_STATE\_BELOW\_CAP \| BITS\_COST\_STATE\_CAPPED\_USAGE\_UNKNOWN \| BITS\_COST\_STATE\_UNRESTRICTED) 
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_TRANSFER_UNRESTRICTED"></span><span id="bits_cost_state_transfer_unrestricted"></span>**BITS\_COST\_STATE\_TRANSFER\_UNRESTRICTED**
</dt> <dd> <dl> <dt>

(BITS\_COST\_OPTION\_IGNORE\_CONGESTION \| BITS\_COST\_STATE\_OVERCAP\_THROTTLED \| BITS\_COST\_STATE\_UNRESTRICTED)
</dt> <dt>


</dt> </dl> </dd> <dt>

<span id="BITS_COST_STATE_TRANSFER_ALWAYS"></span><span id="bits_cost_state_transfer_always"></span>**BITS\_COST\_STATE\_TRANSFER\_ALWAYS**
</dt> <dd> <dl> <dt>

(BITS\_COST\_OPTION\_IGNORE\_CONGESTION \| BITS\_COST\_STATE\_ROAMING \| BITS\_COST\_STATE\_USAGE\_BASED \| BITS\_COST\_STATE\_OVERCAP\_THROTTLED \| BITS\_COST\_STATE\_OVERCAP\_CHARGED \| BITS\_COST\_STATE\_NEAR\_CAP \| BITS\_COST\_STATE\_BELOW\_CAP \| BITS\_COST\_STATE\_CAPPED\_USAGE\_UNKNOWN \| BITS\_COST\_STATE\_UNRESTRICTED)
</dt> <dt>


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Bits5\_0.h (include Bits.h)</dt> </dl> |
| IDL<br/>                      | <dl> <dt>Bits5\_0.idl</dt> </dl>                |



 

 





