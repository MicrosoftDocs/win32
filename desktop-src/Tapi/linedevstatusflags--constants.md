---
description: The LINEDEVSTATUSFLAGS\_ bit-flag constants describe a collection of Boolean line device status items.
ms.assetid: 5fa754d3-07b2-4b75-91ef-1bf961d9fef4
title: LINEDEVSTATUSFLAGS_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEDEVSTATUSFLAGS\_ Constants

The **LINEDEVSTATUSFLAGS\_** bit-flag constants describe a collection of Boolean line device status items.

<dl> <dt>

<span id="LINEDEVSTATUSFLAGS_CONNECTED"></span><span id="linedevstatusflags_connected"></span>**LINEDEVSTATUSFLAGS\_CONNECTED**
</dt> <dd> <dl> <dt>



Specifies whether the line is connected to TAPI. If **TRUE**, the line is connected and TAPI is able to operate on the line device. If **FALSE**, the line is disconnected and the application is unable to control the line device through TAPI.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATUSFLAGS_INSERVICE"></span><span id="linedevstatusflags_inservice"></span>**LINEDEVSTATUSFLAGS\_INSERVICE**
</dt> <dd> <dl> <dt>



Indicates whether the line is in service. If **TRUE**, the line is in service; if **FALSE**, the line is out of service.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATUSFLAGS_LOCKED"></span><span id="linedevstatusflags_locked"></span>**LINEDEVSTATUSFLAGS\_LOCKED**
</dt> <dd> <dl> <dt>



Indicates whether the line is locked or unlocked. This bit is most often used with line devices associated with cellular phones. Many cellular phones have a security mechanism that requires the entry of a password to enable the phone to place calls. This bit can be used to indicate to applications that the phone is locked and cannot place calls until the password is entered on the user interface of the phone so that the application can present an appropriate alert to the user.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATUSFLAGS_MSGWAIT"></span><span id="linedevstatusflags_msgwait"></span>**LINEDEVSTATUSFLAGS\_MSGWAIT**
</dt> <dd> <dl> <dt>



Indicates whether the line has a message waiting. If **TRUE**, a message is waiting; if **FALSE**, no message is waiting.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

LINEDEVSTATUSFLAGS\_ constants are used within the **dwDevStatusFlags** member of the [**LINEDEVSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linedevstatus) data structure.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




