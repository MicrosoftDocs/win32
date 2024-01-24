---
description: The ITQOSApplicationID interface exposes a method that allows an application to get the QOS identifier for the current call.
ms.assetid: 1df50b3a-bd16-4e9b-afca-b025bfe537a4
title: ITQOSApplicationID interface (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITQOSApplicationID interface

\[ This interface is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITQOSApplicationID** interface exposes a method that allows an application to get the QOS identifier for the current call.

This interface is implemented by the [IPConf MSP](ipconf-msp.md) and is exposed only when a call uses IP Conferencing.

## Members

The **ITQOSApplicationID** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ITQOSApplicationID** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITQOSApplicationID** interface has these methods.



| Method                                                                | Description                         |
|:----------------------------------------------------------------------|:------------------------------------|
| [**SetQOSApplicationID**](itqosapplicationid-setqosapplicationid.md) | Sets the QOS identifier.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                         |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



 

