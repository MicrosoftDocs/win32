---
title: MI Flags
description: The following flags are used by various functions in the MI API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '24E82AC6-A2E3-4EC6-931F-26AC54D5CAA7'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- Runtime Type Information (RTTI) Flags
- MI_OPERATIONFLAGS_NO_RTTI
- MI_OPERATIONFLAGS_BASIC_RTTI
- MI_OPERATIONFLAGS_STANDARD_RTTI
- MI_OPERATIONFLAGS_FULL_RTTI
- MI_OPERATIONFLAGS_DEFAULT_RTTI
- Polymorphism Flags
- MI_OPERATIONFLAGS_POLYMORPHISM_SHALLOW
- MI_OPERATIONFLAGS_POLYMORPHISM_DEEP_BASE_PROPS_ONLY
- Miscellaneous Flags
- MI_OPERATIONFLAGS_LOCALIZED_QUALIFIERS
- MI_OPERATIONFLAGS_EXPENSIVE_PROPERTIES
- MI_OPERATIONFLAGS_REPORT_OPERATION_STARTED
api_location:
- Mi.h
api_type:
- HeaderDef
---

# MI Flags

The following flags are used by various functions in the MI API.

<dl> <dt>


</dt> <dd> <dl> <dt>



 


</dt> </dl> </dd> <dt>

<span id="Runtime_Type_Information__RTTI__Flags"></span><span id="runtime_type_information__rtti__flags"></span><span id="RUNTIME_TYPE_INFORMATION__RTTI__FLAGS"></span>**Runtime Type Information (RTTI) Flags**
</dt> <dd> <dl> <dt>



The following RTTI bitmasks specify what options are acceptable to the client.

 


</dt> </dl> </dd> <dt>

<span id="MI_OPERATIONFLAGS_NO_RTTI"></span><span id="mi_operationflags_no_rtti"></span>**MI\_OPERATIONFLAGS\_NO\_RTTI**
</dt> <dd> <dl> <dt>

0x0400
</dt> <dt>



All instance elements are string types except embedded objects and references, but their elements will be strings also.


</dt> </dl> </dd> <dt>

<span id="MI_OPERATIONFLAGS_BASIC_RTTI"></span><span id="mi_operationflags_basic_rtti"></span>**MI\_OPERATIONFLAGS\_BASIC\_RTTI**
</dt> <dd> <dl> <dt>

0x0002
</dt> <dt>



All instance elements may be strings or the correct type.


</dt> </dl> </dd> <dt>

<span id="MI_OPERATIONFLAGS_STANDARD_RTTI"></span><span id="mi_operationflags_standard_rtti"></span>**MI\_OPERATIONFLAGS\_STANDARD\_RTTI**
</dt> <dd> <dl> <dt>

0x0800
</dt> <dt>



All instance elements are of the correct type, but some hierarchical information may be lost due to optimizations.


</dt> </dl> </dd> <dt>

<span id="MI_OPERATIONFLAGS_FULL_RTTI"></span><span id="mi_operationflags_full_rtti"></span>**MI\_OPERATIONFLAGS\_FULL\_RTTI**
</dt> <dd> <dl> <dt>

0x0004
</dt> <dt>



All instance elements at every level of the instances class hierarchy will be accurate. This will be the slowest option.


</dt> </dl> </dd> <dt>

<span id="MI_OPERATIONFLAGS_DEFAULT_RTTI"></span><span id="mi_operationflags_default_rtti"></span>**MI\_OPERATIONFLAGS\_DEFAULT\_RTTI**
</dt> <dd> <dl> <dt>

0x0000
</dt> <dt>



The protocol handler will pick the best option.


</dt> </dl> </dd> <dt>


</dt> <dd> <dl> <dt>



 


</dt> </dl> </dd> <dt>

<span id="Polymorphism_Flags"></span><span id="polymorphism_flags"></span><span id="POLYMORPHISM_FLAGS"></span>**Polymorphism Flags**
</dt> <dd> <dl> <dt>



The following polymorphism bitmasks specify what options are acceptable to the client.

 


</dt> </dl> </dd> <dt>

<span id="MI_OPERATIONFLAGS_POLYMORPHISM_SHALLOW"></span><span id="mi_operationflags_polymorphism_shallow"></span>**MI\_OPERATIONFLAGS\_POLYMORPHISM\_SHALLOW**
</dt> <dd> <dl> <dt>

0x0080
</dt> <dt>



Contains simple polymorphism.


</dt> </dl> </dd> <dt>

<span id="MI_OPERATIONFLAGS_POLYMORPHISM_DEEP_BASE_PROPS_ONLY"></span><span id="mi_operationflags_polymorphism_deep_base_props_only"></span>**MI\_OPERATIONFLAGS\_POLYMORPHISM\_DEEP\_BASE\_PROPS\_ONLY**
</dt> <dd> <dl> <dt>

0x0180
</dt> <dt>



Contains detailed polymorphism for base properties only.


</dt> </dl> </dd> <dt>


</dt> <dd> <dl> <dt>



 


</dt> </dl> </dd> <dt>

<span id="Miscellaneous_Flags"></span><span id="miscellaneous_flags"></span><span id="MISCELLANEOUS_FLAGS"></span>**Miscellaneous Flags**
</dt> <dd> <dl> <dt>



The following flags specify the other options that are acceptable to the client.

 


</dt> </dl> </dd> <dt>

<span id="MI_OPERATIONFLAGS_LOCALIZED_QUALIFIERS"></span><span id="mi_operationflags_localized_qualifiers"></span>**MI\_OPERATIONFLAGS\_LOCALIZED\_QUALIFIERS**
</dt> <dd> <dl> <dt>

0x0008
</dt> <dt>



Contains localized qualifiers. This flag is not supported for delete and invoke operations.


</dt> </dl> </dd> <dt>

<span id="MI_OPERATIONFLAGS_EXPENSIVE_PROPERTIES"></span><span id="mi_operationflags_expensive_properties"></span>**MI\_OPERATIONFLAGS\_EXPENSIVE\_PROPERTIES**
</dt> <dd> <dl> <dt>

0x0040
</dt> <dt>



Contains expensive properties.


</dt> </dl> </dd> <dt>

<span id="MI_OPERATIONFLAGS_REPORT_OPERATION_STARTED"></span><span id="mi_operationflags_report_operation_started"></span>**MI\_OPERATIONFLAGS\_REPORT\_OPERATION\_STARTED**
</dt> <dd> <dl> <dt>

0x0200
</dt> <dt>



Requires a report to be issued whenever an operation has started.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                                       |
| Redistributable<br/>          | Windows Management Framework 3.0 on Windows Server 2008 R2 with SP1, Windows 7 with SP1, and Windows Server 2008 with SP2<br/> |
| Header<br/>                   | <dl> <dt>Mi.h</dt> </dl>                                                      |



 

 





