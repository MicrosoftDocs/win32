---
description: The LINEPROXYSTATUS\_ constants indicate the status of the proxy on a line that the application currently has open.
ms.assetid: a5cf3512-ee42-4f64-8fe3-73a14589f78c
title: LINEPROXYSTATUS_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEPROXYSTATUS\_ Constants

The **LINEPROXYSTATUS\_ constants** indicate the status of the proxy on a line that the application currently has open.

See [**LINEPROXYREQUEST\_ Constants**](lineproxyrequest--constants.md) for a list and description of all possible proxy request values.

<dl> <dt>

<span id="LINEPROXYSTATUS_ALLOPENFORACD"></span><span id="lineproxystatus_allopenforacd"></span>**LINEPROXYSTATUS\_ALLOPENFORACD**
</dt> <dd> <dl> <dt>



The line now has proxies open for all the proxy request types required for ACD operations by TAPI version 3.0 and higher.


</dt> </dl> </dd> <dt>

<span id="LINEPROXYSTATUS_CLOSE"></span><span id="lineproxystatus_close"></span>**LINEPROXYSTATUS\_CLOSE**
</dt> <dd> <dl> <dt>



A proxy has closed.


</dt> </dl> </dd> <dt>

<span id="LINEPROXYSTATUS_OPEN"></span><span id="lineproxystatus_open"></span>**LINEPROXYSTATUS\_OPEN**
</dt> <dd> <dl> <dt>



A new proxy has opened.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




