---
title: Difxapi.h
description: This section contains reference topics for the Difxapi.h header.
ms.assetid: 84da7e54-0677-495e-9dc5-aca4ac12c0b3
ms.topic: article
ms.date: 05/31/2018
---

# Difxapi.h

This section contains reference topics for the Difxapi.h header.

## In this section



| Topic                                                                 | Description                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*DIFLOGCALLBACK*](/previous-versions/windows/hardware/difxapi/diflogcallback)<br/>                     | A **DIFLOGCALLBACK**-typed function is an application-supplied callback function that an application registers by calling [**SetDifxLogCallback**](/previous-versions/windows/hardware/difxapi/setdifxlogcallback). DIFxAPI calls the callback function to log events that occur during DIFxAPI operation.<br/>                        |
| [*DIFXAPILOGCALLBACK*](/previous-versions/windows/hardware/difxapi/difxapilogcallback)<br/>             | A **DIFXAPILOGCALLBACK**-typed function is an application-supplied callback function that an application registers with DIFxAPI by calling [**DIFXAPISetLogCallback**](/previous-versions/windows/hardware/difxapi/difxapisetlogcallback). DIFxAPI calls the callback function to log events that occur during DIFxAPI operation.<br/> |
| [**DIFXAPISetLogCallback**](/previous-versions/windows/hardware/difxapi/difxapisetlogcallback)<br/>     | The **DIFXAPISetLogCallback** function registers a caller-supplied callback function that DIFxAPI calls to log information about events that occur during DIFxAPI operations. <br/>                                                                                                            |
| [**DriverPackageGetPath**](/previous-versions/windows/hardware/difxapi/driverpackagegetpath)<br/>       | The **DriverPackageGetPath** function retrieves the fully qualified path of the [INF file](/windows-hardware/drivers/install/overview-of-inf-files) for a preinstalled [driver package](/windows-hardware/drivers/install/driver-packages).<br/>                                                                                                               |
| [**DriverPackageInstall**](/previous-versions/windows/hardware/difxapi/driverpackageinstall)<br/>       | The **DriverPackageInstall** function preinstalls a [driver package](/windows-hardware/drivers/install/driver-packages) and then installs the driver in the system.<br/>                                                                                                                                                 |
| [**DriverPackagePreinstall**](/previous-versions/windows/hardware/difxapi/driverpackagepreinstall)<br/> | The **DriverPackagePreinstall** function preinstalls a [driver package](/windows-hardware/drivers/install/driver-packages) for a Plug and Play (PnP) [function driver](/windows-hardware/drivers/kernel/function-drivers) and installs the [INF file](/windows-hardware/drivers/install/overview-of-inf-files) for the driver package in the system INF file directory.<br/>             |
| [**DriverPackageUninstall**](/previous-versions/windows/hardware/difxapi/driverpackageuninstall)<br/>   | The **DriverPackageUninstall** function uninstalls the specified [driver package](/windows-hardware/drivers/install/driver-packages) from the system and removes the driver package. <br/>                                                                                                                               |
| [**INSTALLERINFO**](/previous-versions/windows/hardware/difxapi/installerinfo)<br/>                     | The INSTALLERINFO structure contains information about an application that DIFxAPI associates with a [driver package](/windows-hardware/drivers/install/driver-packages). <br/>                                                                                                                                          |
| [**SetDifxLogCallback**](/previous-versions/windows/hardware/difxapi/setdifxlogcallback)<br/>           | The **SetDifxLogCallback** function registers a caller-supplied callback function that DIFxAPI calls to log information about events that occur during DIFxAPI operations. <br/>                                                                                                               |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Difxapi.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")