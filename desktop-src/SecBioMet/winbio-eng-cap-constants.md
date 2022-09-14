---
title: WINBIO_ENG_CAP Constants (Winbio\_types.h)
description: Specify generic engine capabilities.
ms.assetid: 31C4E8AF-6EF8-43FF-A944-D7363A26BB1A
topic_type:
- apiref
api_name:
- WINBIO_ENG_CAP_ITERATIVE_IMPROVEMENT
- WINBIO_ENG_CAP_SPOOF_DETECTION
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_ENG\_CAP Constants

The following constants are **WINBIO\_CAPABILITIES** values that can be used to specify generic capabilities of the engine component that is connected to a specific biometric unit. You specify these capabilities in **GenericEngineCapabilities** member of the [**WINBIO\_EXTENDED\_ENGINE\_INFO**](winbio-extended-engine-info.md) structure.



| Constant/value                                                                                                                                                                                                                                                                                        | Description                                                                  |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| <span id="WINBIO_ENG_CAP_ITERATIVE_IMPROVEMENT"></span><span id="winbio_eng_cap_iterative_improvement"></span><dl> <dt>**WINBIO\_ENG\_CAP\_ITERATIVE\_IMPROVEMENT**</dt> <dt>0x00000001</dt> </dl> | The biometric engine component can perform iterative improvement.<br/> |
| <span id="WINBIO_ENG_CAP_SPOOF_DETECTION"></span><span id="winbio_eng_cap_spoof_detection"></span><dl> <dt>**WINBIO\_ENG\_CAP\_SPOOF\_DETECTION**</dt> <dt>0x00000002</dt> </dl>                   | The biometric engine component can perform spoof detection.<br/>       |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



 

 





