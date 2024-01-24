---
description: These constants are used by a TSP to identify the type of a QoS (Quality of Service) level required.
ms.assetid: 9fc3f6eb-7103-43c5-84f8-3842757e5be7
title: LINEQOSSERVICELEVEL_ Constants (Tspi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEQOSSERVICELEVEL\_ Constants

These constants are used by a TSP to identify the type of a QoS (Quality of Service) level required.

<dl> <dt>

<span id="LINEQOSSERVICELEVEL_NEEDED"></span><span id="lineqosservicelevel_needed"></span>**LINEQOSSERVICELEVEL\_NEEDED**
</dt> <dd> <dl> <dt>

 0x00000001
</dt> <dt>



The quality of service level requested is a requirement.


</dt> </dl> </dd> <dt>

<span id="LINEQOSSERVICELEVEL_IFAVAILABLE"></span><span id="lineqosservicelevel_ifavailable"></span>**LINEQOSSERVICELEVEL\_IFAVAILABLE**
</dt> <dd> <dl> <dt>

 0x00000002
</dt> <dt>



The quality of service level required, if available.


</dt> </dl> </dd> <dt>

<span id="LINEQOSSERVICELEVEL_BESTEFFORT"></span><span id="lineqosservicelevel_besteffort"></span>**LINEQOSSERVICELEVEL\_BESTEFFORT**
</dt> <dd> <dl> <dt>

 0x00000003
</dt> <dt>



The quality of service level required is "best effort."


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tspi.h</dt> </dl> |



 

 




