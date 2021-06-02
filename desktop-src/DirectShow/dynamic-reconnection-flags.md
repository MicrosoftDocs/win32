---
description: The following flags specify the level of dynamic reconnection to use during rendering.
ms.assetid: 5e9d5f11-6716-4539-96fd-a0b37036555b
title: Dynamic Reconnection Flags (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CONNECTF_DYNAMIC_NONE
- CONNECTF_DYNAMIC_SOURCES
- CONNECTF_DYNAMIC_EFFECTS
api_type: 
- HeaderDef
api_location: 
- Qedit.h
---

# Dynamic Reconnection Flags

\[Deprecated. This API may be removed from future releases of Windows.\]

The following flags specify the level of dynamic reconnection to use during rendering.



| Constant/value                                                                                                                                                                                                                                            | Description                                                                       |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| <span id="CONNECTF_DYNAMIC_NONE"></span><span id="connectf_dynamic_none"></span><dl> <dt>**CONNECTF\_DYNAMIC\_NONE**</dt> <dt>0x00</dt> </dl>          | No dynamic reconnection. Load everything before rendering the project.<br/> |
| <span id="CONNECTF_DYNAMIC_SOURCES"></span><span id="connectf_dynamic_sources"></span><dl> <dt>**CONNECTF\_DYNAMIC\_SOURCES**</dt> <dt>0x01</dt> </dl> | Load sources only as needed.<br/>                                           |
| <span id="CONNECTF_DYNAMIC_EFFECTS"></span><span id="connectf_dynamic_effects"></span><dl> <dt>**CONNECTF\_DYNAMIC\_EFFECTS**</dt> <dt>0x02</dt> </dl> | Reserved. Do not use.<br/>                                                  |



## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Qedit.h</dt> </dl> |



## See also

<dl> <dt>

[**IRenderEngine::SetDynamicReconnectLevel**](irenderengine-setdynamicreconnectlevel.md)
</dt> </dl>

 

 




