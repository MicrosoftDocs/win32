---
title: Driver Instances
description: Driver Instances
ms.assetid: 93dba9e8-bfb3-4714-9466-cf5c78babcf2
keywords:
- installable drivers,instances
- installable drivers,multiple instances
- multiple driver instances
ms.topic: article
ms.date: 05/31/2018
---

# Driver Instances

Windows allows for multiples instances of an installable driver. The system creates an instance of the driver each time the driver is opened and destroys the instance when the driver is closed. Driver instances are especially useful for installable drivers that support multiple devices or that are opened by multiple applications or by the same application multiple times.

To help the driver keep track of the instances, the system sends a driver instance handle with each driver message after the instance has been created. Because this handle uniquely identifies the instance, installable drivers often associate the handle with memory and other resources that they have specifically allocated for the instance.

When the first instance is opened, the system sends the [**DRV\_LOAD**](drv-load.md), [**DRV\_ENABLE**](drv-enable.md), and [**DRV\_OPEN**](drv-open.md) messages to the driver in that order. The DRV\_LOAD and DRV\_ENABLE messages notify the driver that it is now in memory and is enabled for operation. The DRV\_OPEN message identifies the instance handle and may include configuration information for the instance. On each subsequent opening of an instance of the same driver, the system sends only a DRV\_OPEN message.

When processing a DRV\_LOAD message, a driver typically reads configuration settings from the registry, configures the driver and any associated hardware, and allocates memory for use by all instances of the driver. If a driver cannot complete the configuration or allocate memory, it returns zero to direct the system to immediately remove the driver from memory and prevent any subsequent messages from being sent. When processing the DRV\_ENABLE message, the driver prepares the hardware to receive and process input and output (I/O) requests. The preparation may include installing interrupt handlers.

When processing the DRV\_OPEN message, the driver allocates memory or resources required by the given instance of the driver and then returns a nonzero value. The system uses this nonzero value as the *driver identifier* in subsequent driver messages for the instance. The driver can use this identifier for any purpose. For example, some drivers use a memory handle for the identifier to gain quick access to memory containing information about the given instance.

Many installable drivers process the second parameter of the DRV\_OPEN message, giving the system and applications the means to send additional information to the driver when opening an instance. The parameter can be a single value or an address of a structure containing a set of values. When processing DRV\_OPEN, the driver checks the parameter to determine whether it is a value and uses the given values, if any, to complete the creation of the instance.

The system sends a [**DRV\_CLOSE**](drv-close.md) message each time an instance is closed. The instance handle sent with the message identifies which instance to close. When the last remaining instance is closed, the system sends the DRV\_CLOSE, [**DRV\_DISABLE**](drv-disable.md), and [**DRV\_FREE**](drv-free.md) messages in that order. The DRV\_CLOSE message directs the driver to close the instance, and the DRV\_DISABLE and DRV\_FREE messages notify the driver that it is now disabled and will be immediately freed from memory.

When processing the DRV\_CLOSE message, the driver typically frees any memory or resources allocated for the instance. When processing the DRV\_DISABLE message, the driver places any hardware in an inactive state, which may include the removal of interrupt handlers. When processing the DRV\_FREE message, the driver frees any memory or resources that are still allocated.

Installable drivers are not required to support multiple instances. A driver can prevent any instance from being created by returning zero for the [**DRV\_OPEN**](drv-open.md) message.

 

 




