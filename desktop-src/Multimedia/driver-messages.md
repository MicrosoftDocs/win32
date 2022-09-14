---
title: Driver Messages
description: Driver Messages
ms.assetid: ed3748ac-08e6-418e-b345-30c796fa38f3
keywords:
- installable drivers,messages
- installable drivers,custom messages
- driver messages
- custom driver messages
- installable drivers,DriverProc function
ms.topic: article
ms.date: 05/31/2018
---

# Driver Messages

Each driver message consists of a message identifier and two 32-bit parameters. The message identifier is a unique value that the [DriverProc](/windows/win32/api/mmiscapi/nc-mmiscapi-driverproc) function checks to determine which action to carry out. The meaning of the message parameters depends on the message. The parameters may represent values or addresses. In many cases, the parameters are not used and are set to zero.

Driver messages can be standard or custom. Windows sends standard driver messages, such as [**DRV\_OPEN**](drv-open.md), [**DRV\_CLOSE**](drv-close.md), and [**DRV\_CONFIGURE**](drv-configure.md), to an installable driver in response to a request to open, close, or configure the driver. The standard messages direct the installable driver to load or unload its resources, enable or disable its operation, open or close a driver instance, and display a configuration dialog box. Some standard messages, such as [**DRV\_POWER**](drv-power.md) and [**DRV\_EXITSESSION**](drv-exitsession.md), notify the driver of system-wide events that affect the operation of the driver or any related hardware.

Applications and DLLs send custom driver messages to direct an installable driver to carry out driver-specific actions. Installable drivers that support custom messages must include appropriate processing in the **DriverProc** function. To prevent conflict between custom and standard driver messages, custom message identifiers must have values ranging from DRV\_RESERVED to DRV\_USER. Custom messages passed to the [DefDriverProc](/windows/win32/api/mmiscapi/nf-mmiscapi-defdriverproc) function are ignored.

 

 