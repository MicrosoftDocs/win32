---
title: Difxapi.h
description: This section contains reference topics for the Difxapi.h header.
ms.assetid: 84da7e54-0677-495e-9dc5-aca4ac12c0b3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Difxapi.h

This section contains reference topics for the Difxapi.h header.

## In this section



| Topic                                                                 | Description                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*DIFLOGCALLBACK*](/windows/win32/Difxapi/?branch=master)<br/>                     | A **DIFLOGCALLBACK**-typed function is an application-supplied callback function that an application registers by calling [**SetDifxLogCallback**](/windows/win32/difxapi/?branch=master). DIFxAPI calls the callback function to log events that occur during DIFxAPI operation.<br/>                        |
| [*DIFXAPILOGCALLBACK*](/windows/win32/difxapi/?branch=master)<br/>             | A **DIFXAPILOGCALLBACK**-typed function is an application-supplied callback function that an application registers with DIFxAPI by calling [**DIFXAPISetLogCallback**](/windows/win32/Difxapi/?branch=master). DIFxAPI calls the callback function to log events that occur during DIFxAPI operation.<br/> |
| [**DIFXAPISetLogCallback**](/windows/win32/Difxapi/?branch=master)<br/>     | The **DIFXAPISetLogCallback** function registers a caller-supplied callback function that DIFxAPI calls to log information about events that occur during DIFxAPI operations. <br/>                                                                                                            |
| [**DriverPackageGetPath**](/windows/win32/Difxapi/?branch=master)<br/>       | The **DriverPackageGetPath** function retrieves the fully qualified path of the [INF file](https://msdn.microsoft.com/library/windows/hardware/ff547402) for a preinstalled [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840).<br/>                                                                                                               |
| [**DriverPackageInstall**](/windows/win32/difxapi/?branch=master)<br/>       | The **DriverPackageInstall** function preinstalls a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) and then installs the driver in the system.<br/>                                                                                                                                                 |
| [**DriverPackagePreinstall**](/windows/win32/difxapi/?branch=master)<br/> | The **DriverPackagePreinstall** function preinstalls a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) for a Plug and Play (PnP) [function driver](https://msdn.microsoft.com/library/windows/hardware/ff546516) and installs the [INF file](https://msdn.microsoft.com/library/windows/hardware/ff547402) for the driver package in the system INF file directory.<br/>             |
| [**DriverPackageUninstall**](/windows/win32/difxapi/?branch=master)<br/>   | The **DriverPackageUninstall** function uninstalls the specified [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) from the system and removes the driver package. <br/>                                                                                                                               |
| [**INSTALLERINFO**](/windows/win32/difxapi/ns-difxapi-installerinfo_a?branch=master)<br/>                     | The INSTALLERINFO structure contains information about an application that DIFxAPI associates with a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840). <br/>                                                                                                                                          |
| [**SetDifxLogCallback**](/windows/win32/difxapi/?branch=master)<br/>           | The **SetDifxLogCallback** function registers a caller-supplied callback function that DIFxAPI calls to log information about events that occur during DIFxAPI operations. <br/>                                                                                                               |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Difxapi.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





