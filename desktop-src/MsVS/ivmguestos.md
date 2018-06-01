---
title: IVMGuestOS interface
description: The IVMGuestOS interface defines the guest operating system running inside a virtual machine.
ms.assetid: cf3d6a66-8466-49f0-bd01-3904e9aebd03
keywords:
- IVMGuestOS interface Virtual Server
- IVMGuestOS interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMGuestOS
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IVMGuestOS interface

The **IVMGuestOS** interface defines the guest operating system running inside a virtual machine. This interface allows you to interact with the Microsoft Additions running inside the guest operating system. The **IVMGuestOS** for a virtual machine can be retrieved using the [**IVMVirtualMachine::GuestOS**](ivmvirtualmachine-guestos.md) property. Folder sharing is an experimental feature in Virtual Server 1.0 and may not function properly in all configurations.

## Inheritance

The **IVMGuestOS** interface has been extended by the following interface:

-   [**IVMGuestOS2**](ivmguestos2.md)

## Members

The **IVMGuestOS** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMGuestOS** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMGuestOS** interface has these methods.



| Method                                                  | Description                                                                                                                                                                                       |
|:--------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExecuteCommand**](ivmguestos-executecommand.md)     | Executes the specified file in the guest operating system.<br/> (Inherited from **IVMGuestOSVMGuestOS**[**IVMGuestOS2**](ivmguestos2.md)[**VMGuestOS2**](ivmguestos2.md))                 |
| [**InstallAdditions**](ivmguestos-installadditions.md) | Locates and installs the latest Additions into the guest operating system.<br/> (Inherited from **IVMGuestOSVMGuestOS**[**IVMGuestOS2**](ivmguestos2.md)[**VMGuestOS2**](ivmguestos2.md)) |
| [**SetParameter**](ivmguestos-setparameter.md)         | Sets a configuration parameter inside the guest operating system.<br/> (Inherited from **IVMGuestOSVMGuestOS**[**IVMGuestOS2**](ivmguestos2.md)[**VMGuestOS2**](ivmguestos2.md))          |
| [**Shutdown**](ivmguestos-shutdown.md)                 | Tells the guest operating system to shut down.<br/> (Inherited from **IVMGuestOSVMGuestOS**[**IVMGuestOS2**](ivmguestos2.md)[**VMGuestOS2**](ivmguestos2.md))                             |



 

### Properties

The **IVMGuestOS** interface has these properties.



| Property                                                                     | Access type           | Description                                                                                                                                                                                                                           |
|:-----------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdditionsVersion**](ivmguestos-additionsversion.md)<br/>           | Read-only<br/>  | The version of the Additions installed in the guest operating system.<br/> (Inherited from **IVMGuestOSVMGuestOS**[**IVMGuestOS2**](ivmguestos2.md)[**VMGuestOS2**](ivmguestos2.md))                                          |
| [**CanShutdown**](ivmguestos-canshutdown.md)<br/>                     | Read-only<br/>  | Indicates whether the guest operating system can be cleanly shut down.<br/> (Inherited from **IVMGuestOSVMGuestOS**[**IVMGuestOS2**](ivmguestos2.md)[**VMGuestOS2**](ivmguestos2.md))                                         |
| [**HeartbeatPercentage**](ivmguestos-heartbeatpercentage.md)<br/>     | Read-only<br/>  | The percentage of expected heartbeats received over the past minute.<br/> (Inherited from **IVMGuestOSVMGuestOS**[**IVMGuestOS2**](ivmguestos2.md)[**VMGuestOS2**](ivmguestos2.md))                                           |
| [**IsHeartbeating**](ivmguestos-isheartbeating.md)<br/>               | Read-only<br/>  | Indicates whether the guest operating system appears to be alive.<br/> (Inherited from **IVMGuestOSVMGuestOS**[**IVMGuestOS2**](ivmguestos2.md)[**VMGuestOS2**](ivmguestos2.md))                                              |
| [**IsHostTimeSyncEnabled**](ivmguestos-ishosttimesyncenabled.md)<br/> | Read/write<br/> | Specifies if the Additions in this virtual machine should synchronize the guest's clock with the host's clock.<br/> (Inherited from **IVMGuestOSVMGuestOS**[**IVMGuestOS2**](ivmguestos2.md)[**VMGuestOS2**](ivmguestos2.md)) |
| [**OSName**](ivmguestos-osname.md)<br/>                               | Read-only<br/>  | The name of the guest operating system running in the virtual machine.<br/> (Inherited from **IVMGuestOSVMGuestOS**[**IVMGuestOS2**](ivmguestos2.md)[**VMGuestOS2**](ivmguestos2.md))                                         |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[Virtual Server Interfaces](interfaces.md)
</dt> <dt>

[**IVMGuestOS2**](ivmguestos2.md)
</dt> <dt>

[IVMGuestOS Methods](ivmguestos-methods.md)
</dt> <dt>

[IVMGuestOS Properties](ivmguestos-properties.md)
</dt> </dl>

 

 





