---
title: IVMGuestOS2 interface
description: The IVMGuestOS2 interface extends the IVMGuestOS interface, adding a method to retrieve a parameter set in the guest operating system and a property containing the name of the guest operating system.
ms.assetid: df820310-b4be-4278-abb2-01a7b0504938
keywords:
- IVMGuestOS2 interface Virtual Server
- IVMGuestOS2 interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMGuestOS2
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

# IVMGuestOS2 interface

The **IVMGuestOS2** interface extends the [**IVMGuestOS**](ivmguestos.md) interface, adding a method to retrieve a parameter set in the guest operating system and a property containing the name of the guest operating system. The **IVMGuestOS2** for a virtual machine can be retrieved using the [**IVMVirtualMachine::GuestOS**](ivmvirtualmachine-guestos.md) property.

## Members

The **IVMGuestOS2** interface inherits from [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) and [**IVMGuestOS**](ivmguestos.md). **IVMGuestOS2** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMGuestOS2** interface has these methods.



| Method                                                  | Description                                                                                                                                                                                     |
|:--------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExecuteCommand**](ivmguestos-executecommand.md)     | Executes the specified file in the guest operating system.<br/> (Inherited from [**IVMGuestOS**](ivmguestos.md)[**VMGuestOS**](ivmguestos.md)**IVMGuestOS2VMGuestOS2**)                 |
| [**GetParameter**](ivmguestos2-getparameter.md)        | Retrieves a named parameter within the guest operating system running in the virtual machine.<br/> (Inherited from **IVMGuestOS2VMGuestOS2**)                                             |
| [**InstallAdditions**](ivmguestos-installadditions.md) | Locates and installs the latest Additions into the guest operating system.<br/> (Inherited from [**IVMGuestOS**](ivmguestos.md)[**VMGuestOS**](ivmguestos.md)**IVMGuestOS2VMGuestOS2**) |
| [**SetParameter**](ivmguestos-setparameter.md)         | Sets a configuration parameter inside the guest operating system.<br/> (Inherited from [**IVMGuestOS**](ivmguestos.md)[**VMGuestOS**](ivmguestos.md)**IVMGuestOS2VMGuestOS2**)          |
| [**Shutdown**](ivmguestos-shutdown.md)                 | Tells the guest operating system to shut down.<br/> (Inherited from [**IVMGuestOS**](ivmguestos.md)[**VMGuestOS**](ivmguestos.md)**IVMGuestOS2VMGuestOS2**)                             |



 

### Properties

The **IVMGuestOS2** interface has these properties.



| Property                                                                     | Access type           | Description                                                                                                                                                                                                                              |
|:-----------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdditionsVersion**](ivmguestos-additionsversion.md)<br/>           | Read-only<br/>  | The version of the Additions installed in the guest operating system.<br/> (Inherited from [**IVMGuestOS**](ivmguestos.md)[**VMGuestOS**](ivmguestos.md)**IVMGuestOS2VMGuestOS2**)                                               |
| [**CanShutdown**](ivmguestos-canshutdown.md)<br/>                     | Read-only<br/>  | Indicates whether the guest operating system can be cleanly shut down.<br/> (Inherited from [**IVMGuestOS**](ivmguestos.md)[**VMGuestOS**](ivmguestos.md)**IVMGuestOS2VMGuestOS2**)                                              |
| [**ComputerName**](ivmguestos2-computername.md)<br/>                  | Read-only<br/>  | The computer name of the guest operating system running in the virtual machine.<br/> (Inherited from **IVMGuestOS2VMGuestOS2**)                                                                                                    |
| [**HeartbeatPercentage**](ivmguestos-heartbeatpercentage.md)<br/>     | Read-only<br/>  | The percentage of expected heartbeats received over the past minute.<br/> (Inherited from [**IVMGuestOS**](ivmguestos.md)[**VMGuestOS**](ivmguestos.md)**IVMGuestOS2VMGuestOS2**)                                                |
| [**IsHeartbeating**](ivmguestos-isheartbeating.md)<br/>               | Read-only<br/>  | Indicates whether the guest operating system appears to be alive.<br/> (Inherited from [**IVMGuestOS**](ivmguestos.md)[**VMGuestOS**](ivmguestos.md)**IVMGuestOS2VMGuestOS2**)                                                   |
| [**IsHostTimeSyncEnabled**](ivmguestos-ishosttimesyncenabled.md)<br/> | Read/write<br/> | Indicates whether the Additions in this virtual machine should synchronize the guest's clock with the host's clock.<br/> (Inherited from [**IVMGuestOS**](ivmguestos.md)[**VMGuestOS**](ivmguestos.md)**IVMGuestOS2VMGuestOS2**) |
| [**OSName**](ivmguestos-osname.md)<br/>                               | Read-only<br/>  | The name of the guest operating system running in the virtual machine.<br/> (Inherited from [**IVMGuestOS**](ivmguestos.md)[**VMGuestOS**](ivmguestos.md)**IVMGuestOS2VMGuestOS2**)                                              |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[Virtual Server Interfaces](interfaces.md)
</dt> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> <dt>

[IVMGuestOS2 Methods](ivmguestos2-methods.md)
</dt> <dt>

[IVMGuestOS2 Properties](ivmguestos2-properties.md)
</dt> </dl>

 

 





