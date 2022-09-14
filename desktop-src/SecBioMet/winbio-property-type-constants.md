---
title: WINBIO_PROPERTY_TYPE Constants (Winbio.h)
description: Specify the source of the property information in the WinBioGetProperty function.
ms.assetid: 82C54092-032B-4F32-820E-A1D4BB81ECCE
topic_type:
- apiref
api_name:
- WINBIO_PROPERTY_TYPE_SESSION
- WINBIO_PROPERTY_TYPE_TEMPLATE
- WINBIO_PROPERTY_TYPE_UNIT
- WINBIO_PROPERTY_TYPE_ACCOUNT
api_location:
- Winbio.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_PROPERTY\_TYPE Constants

The following **WINBIO\_PROPERTY\_TYPE** constants can be used to specify the source of the property information in the [**WinBioGetProperty**](/windows/desktop/api/Winbio/nf-winbio-winbiogetproperty) function.

<dl> <dt>

<span id="WINBIO_PROPERTY_TYPE_SESSION"></span><span id="winbio_property_type_session"></span>**WINBIO\_PROPERTY\_TYPE\_SESSION**
</dt> <dd> <dl> <dt>



The property applies to a specific biometric session.


</dt> </dl> </dd> <dt>

<span id="WINBIO_PROPERTY_TYPE_TEMPLATE"></span><span id="winbio_property_type_template"></span>**WINBIO\_PROPERTY\_TYPE\_TEMPLATE**
</dt> <dd> <dl> <dt>



The property applies to a specific biometric template.


</dt> </dl> </dd> <dt>

<span id="WINBIO_PROPERTY_TYPE_UNIT"></span><span id="winbio_property_type_unit"></span>**WINBIO\_PROPERTY\_TYPE\_UNIT**
</dt> <dd> <dl> <dt>



The property applies to a specific biometric unit.


</dt> </dl> </dd> <dt>

<span id="WINBIO_PROPERTY_TYPE_ACCOUNT"></span><span id="winbio_property_type_account"></span>**WINBIO\_PROPERTY\_TYPE\_ACCOUNT**
</dt> <dd> <dl> <dt>



The property applies to a specific user account that has a biometric enrollment. This value is supported starting in Windows 10.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>Winbio.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Constants](client-application-constants.md)
</dt> <dt>

[**WinBioGetProperty**](/windows/desktop/api/Winbio/nf-winbio-winbiogetproperty)
</dt> </dl>

 

 





