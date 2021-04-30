---
description: These constants are used by a TSP to identify the result of a QoS (Quality of Service) request.
ms.assetid: 617ddbf4-212f-4990-93c2-f38f04b035ab
title: LINEEQOSINFO_ Constants (Tspi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEEQOSINFO\_ Constants

These constants are used by a TSP to identify the result of a QoS (Quality of Service) request.

<dl> <dt>

<span id="LINEEQOSINFO_NOQOS"></span><span id="lineeqosinfo_noqos"></span>**LINEEQOSINFO\_NOQOS**
</dt> <dd> <dl> <dt>

 0x00000001
</dt> <dt>



QoS is not available.


</dt> </dl> </dd> <dt>

<span id="LINEEQOSINFO_ADMISSIONFAILURE"></span><span id="lineeqosinfo_admissionfailure"></span>**LINEEQOSINFO\_ADMISSIONFAILURE**
</dt> <dd> <dl> <dt>

 0x00000002
</dt> <dt>



The QoS request could not be met.


</dt> </dl> </dd> <dt>

<span id="LINEEQOSINFO_POLICYFAILURE"></span><span id="lineeqosinfo_policyfailure"></span>**LINEEQOSINFO\_POLICYFAILURE**
</dt> <dd> <dl> <dt>

 0x00000003
</dt> <dt>



The type of QoS requested is not supported.


</dt> </dl> </dd> <dt>

<span id="LINEEQOSINFO_GENERICERROR"></span><span id="lineeqosinfo_genericerror"></span>**LINEEQOSINFO\_GENERICERROR**
</dt> <dd> <dl> <dt>

 0x00000004
</dt> <dt>



Unspecified QoS error.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tspi.h</dt> </dl> |



 

 




