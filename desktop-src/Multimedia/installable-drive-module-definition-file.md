---
title: Installable Drive Module-Definition File
description: Installable Drive Module-Definition File
ms.assetid: d8d8d32e-18ac-47a5-a923-48b94b75e11d
keywords:
- installable drivers,module-definition files
- installable drivers,DEF files
- nstallable drivers,DriverProc function
- DriverProc function
- module-definition files
- DEF files
ms.topic: article
ms.date: 05/31/2018
---

# Installable Drive Module-Definition File

The module-definition (.DEF) file of an installable driver names the driver, exports the [DriverProc](/windows/win32/api/mmiscapi/nc-mmiscapi-driverproc) function, and defines a driver description. The following example shows a typical module-definition file for an installable driver:


```C++
LIBRARY OSCI 
DESCRIPTION 'FREQ,AMPL:Oscilloscope frequency and amplitude drivers.'
EXPORTS
    DriverProc
 
```



Some installation applications may open the driver and retrieve the description line to use when installing the driver. To remain compatible with these installation applications, the description line should have this form:

**DESCRIPTION**  *alias*\[,*alias*\]...**:***text*

The *alias* specifies a unique name for the driver that applications can use to open the driver. The alias also serves as the value name associated with the driver in the registry. Multiple aliases are separated by commas. The *text* describes the purpose of the driver.

 

 