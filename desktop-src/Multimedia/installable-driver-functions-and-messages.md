---
title: Installable Driver Functions and Messages
description: Installable Driver Functions and Messages
ms.assetid: f487705a-ae8e-4ea8-bfd5-9b0f6087ddbb
keywords:
- installable drivers,functions
- installable drivers,messages
- installable drivers,OpenDriver function
- OpenDriver function
- installable drivers,custom messages
- driver messages
- custom driver messages
ms.topic: article
ms.date: 05/31/2018
---

# Installable Driver Functions and Messages

You can open an installable driver from an application by using the [**OpenDriver**](https://msdn.microsoft.com/en-us/library/Dd743639(v=VS.85).aspx) function. This function creates an instance of the driver, loading the driver into memory if no other instance exists, and returns the handle of the new instance. When opening an installable driver, you must supply either the full path of the driver or the names of the registry key and value associated with the driver.

Once a driver is open, you can direct it to carry out tasks by using the [**SendDriverMessage**](https://msdn.microsoft.com/en-us/library/Dd798653(v=VS.85).aspx) function to send driver messages to the driver. For example, you can direct the driver to display its configuration dialog box by sending the [**DRV\_CONFIGURE**](drv-configure.md) message. Before sending this message, you must determine whether the driver has a configuration dialog box by sending the [**DRV\_QUERYCONFIGURE**](drv-queryconfigure.md) message and checking for a nonzero return value. Many drivers provide a set of custom messages that you can send to direct the operations of the driver.

If you need special access to an installable driver, such as access to its resources, you can retrieve the module handle of the driver by using the [**GetDriverModuleHandle**](https://msdn.microsoft.com/en-us/library/Dd797983(v=VS.85).aspx) function.

When you no longer need the installable driver, you can close it by using the [**CloseDriver**](https://msdn.microsoft.com/en-us/library/Dd797785(v=VS.85).aspx) function.

You can use the installable driver functions and messages to open and manage any installable driver. However, the recommended course of action for opening and managing multimedia devices is to first use standard services (such as [**waveOutOpen**](https://msdn.microsoft.com/en-us/library/Dd743866(v=VS.85).aspx), [**waveOutMessage**](https://msdn.microsoft.com/en-us/library/Dd743865(v=VS.85).aspx), and [**waveOutClose**](https://msdn.microsoft.com/en-us/library/Dd743856(v=VS.85).aspx) for waveform output devices), if they exist. If standard services do not exist for a multimedia driver, then open and manage the driver using the installable driver functions and messages.

> [!Note]  
> The [**SendDriverMessage**](https://msdn.microsoft.com/en-us/library/Dd798653(v=VS.85).aspx) and [**GetDriverModuleHandle**](https://msdn.microsoft.com/en-us/library/Dd797983(v=VS.85).aspx) functions are the preferred functions to use to send messages to a driver and to obtain a handle to a module instance. The older [**DrvGetModuleHandle**](https://msdn.microsoft.com/en-us/library/Dd797924(v=VS.85).aspx) function, however, has been included to maintain compatibility with previous versions of the Windows operating system.

 

 

 




