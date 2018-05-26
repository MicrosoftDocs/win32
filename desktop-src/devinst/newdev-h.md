---
title: Newdev.h
description: This section contains reference topics for the Newdev.h header.
ms.assetid: 74195139-6899-4324-af77-d830c2642031
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Newdev.h

This section contains reference topics for the Newdev.h header.

## In this section



| Topic                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiInstallDevice**](/windows/win32/Newdev/nf-newdev-diinstalldevice?branch=master)<br/>                                     | The **DiInstallDevice** function installs a specified driver that is preinstalled in the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868) on a specified device that is present in the system.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**DiInstallDriver**](/windows/win32/Newdev/?branch=master)<br/>                                     | The **DiInstallDriver** function preinstalls a driver in the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868) and then installs the driver on devices present in the system that the driver supports.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**DiRollbackDriver**](/windows/win32/Newdev/nf-newdev-dirollbackdriver?branch=master)<br/>                                   | The **DiRollbackDriver** function rolls back the driver that is installed on a specified device.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**DiShowUpdateDevice**](/windows/win32/Newdev/nf-newdev-dishowupdatedevice?branch=master)<br/>                               | The **DiShowUpdateDevice** function displays the Hardware Update wizard for a specified device.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [**DiUninstallDevice**](/windows/win32/Newdev/nf-newdev-diuninstalldevice?branch=master)<br/>                                 | The [**DiUninstallDevice**](/windows/win32/Newdev/nf-newdev-diuninstalldevice?branch=master) function uninstalls a device and removes its device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) from the system. This differs from using [**SetupDiCallClassInstaller**](/windows/win32/Setupapi/nf-setupapi-setupdicallclassinstaller?branch=master) with the [**DIF\_REMOVE**](https://msdn.microsoft.com/library/windows/hardware/ff543717) code because it attempts to uninstall the device node in addition to child devnodes that are present at the time of the call.<br/> Prior to Windows 8 any child devices that are not present at the time of the call will not be uninstalled. However, beginning with Windows 8, any child devices that are not present at the time of the call will be uninstalled.<br/> |
| [**UpdateDriverForPlugAndPlayDevices**](/windows/win32/Newdev/?branch=master)<br/> | Given an INF file and a [hardware ID](https://msdn.microsoft.com/library/windows/hardware/ff546152), the **UpdateDriverForPlugAndPlayDevices** function installs updated drivers for devices that match the hardware ID. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Newdev.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





