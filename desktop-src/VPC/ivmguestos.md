---
title: IVMGuestOS interface (VPCCOMInterfaces.h)
description: Defines the guest operating system running inside a virtual machine.
ms.assetid: fb31f294-94ad-4545-8d59-849a5f2fe780
keywords:
- IVMGuestOS interface Virtual PC
- IVMGuestOS interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMGuestOS
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the guest operating system running inside a virtual machine. This interface allows you to interact with the integration components running inside the guest operating system. The **IVMGuestOS** for a virtual machine can be retrieved using the [**IVMVirtualMachine::GuestOS**](ivmvirtualmachine-guestos.md) property.

## Members

The **IVMGuestOS** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMGuestOS** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMGuestOS** interface has these methods.



| Method                                                                          | Description                                                                                             |
|:--------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**GetOsVersionInfo**](ivmguestos-getosversioninfo.md)                         | Retrieves version information for the guest operating system running in the virtual machine.<br/> |
| [**GetParameter**](ivmguestos-getparameter.md)                                 | Retrieves a named parameter within the guest.<br/>                                                |
| [**InstallIntegrationComponents**](ivmguestos-installintegrationcomponents.md) | Locates and installs the latest Integration Components into the guest operating system.<br/>      |
| [**IsUserLoggedOn**](ivmguestos-isuserloggedon.md)                             | Determines whether the requested session is present.<br/>                                         |
| [**Logoff**](ivmguestos-logoff.md)                                             | Logs off all users from the guest operating system.<br/>                                          |
| [**Restart**](ivmguestos-restart.md)                                           | Restarts the guest operating system.<br/>                                                         |
| [**SetParameter**](ivmguestos-setparameter.md)                                 | Sets a named parameter within the guest.<br/>                                                     |
| [**Shutdown**](ivmguestos-shutdown.md)                                         | Shuts down the guest operating system.<br/>                                                       |



 

### Properties

The **IVMGuestOS** interface has these properties.



| Property                                                                                   | Access type           | Description                                                                                                                                 |
|:-------------------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| [**CanShutdown**](ivmguestos-canshutdown.md)<br/>                                   | Read-only<br/>  | Indicates whether the guest operating system can be cleanly shut down (requires Integration Components).<br/>                         |
| [**ComputerName**](ivmguestos-computername.md)<br/>                                 | Read-only<br/>  | The computer name of the guest operating system running in the virtual machine.<br/>                                                  |
| [**CSDVersion**](ivmguestos-csdversion.md)<br/>                                     | Read-only<br/>  | The CSDVersion of the guest operating system running in the virtual machine.<br/>                                                     |
| [**HeartbeatPercentage**](ivmguestos-heartbeatpercentage.md)<br/>                   | Read-only<br/>  | The percentage of expected heartbeats received over the past minute.<br/>                                                             |
| [**IntegrationComponentsVersion**](ivmguestos-integrationcomponentsversion.md)<br/> | Read-only<br/>  | The version of the Integration Components installed in the guest operating system.<br/>                                               |
| [**IsHeartbeating**](ivmguestos-isheartbeating.md)<br/>                             | Read-only<br/>  | Indicates whether the virtual machine has a heartbeat.<br/>                                                                           |
| [**IsHostTimeSyncEnabled**](ivmguestos-ishosttimesyncenabled.md)<br/>               | Read/write<br/> | Indicates whether the Integration Components in this virtual machine should synchronize the guest's clock with the host's clock.<br/> |
| [**MultipleUserSessionsAllowed**](ivmguestos-multipleusersessionsallowed.md)<br/>   | Read-only<br/>  | Indicates whether multiple simultaneous user sessions are allowed in the guest operating system.<br/>                                 |
| [**OSBuildNumber**](ivmguestos-osbuildnumber.md)<br/>                               | Read-only<br/>  | The build number of the guest operating system running in the virtual machine.<br/>                                                   |
| [**OSMajorVersion**](ivmguestos-osmajorversion.md)<br/>                             | Read-only<br/>  | The major version of the guest operating system running in the virtual machine.<br/>                                                  |
| [**OSMinorVersion**](ivmguestos-osminorversion.md)<br/>                             | Read-only<br/>  | The minor version of the guest operating system running in the virtual machine.<br/>                                                  |
| [**OSName**](ivmguestos-osname.md)<br/>                                             | Read-only<br/>  | The name of the guest operating system running in the virtual machine.<br/>                                                           |
| [**OSPlatformId**](ivmguestos-osplatformid.md)<br/>                                 | Read-only<br/>  | The platform identifier of the guest operating system running in the virtual machine.<br/>                                            |
| [**OSVersion**](ivmguestos-osversion.md)<br/>                                       | Read-only<br/>  | The version of the guest operating system running in the virtual machine.<br/>                                                        |
| [**ProductType**](ivmguestos-producttype.md)<br/>                                   | Read-only<br/>  | The product type of the guest operating system running in the virtual machine.<br/>                                                   |
| [**ScreenLocked**](ivmguestos-screenlocked.md)<br/>                                 | Read-only<br/>  | Indicates whether the screen is locked in the guest operating system.<br/>                                                            |
| [**ServicePackMajor**](ivmguestos-servicepackmajor.md)<br/>                         | Read-only<br/>  | The major version of the service pack of the guest operating system running in the virtual machine.<br/>                              |
| [**ServicePackMinor**](ivmguestos-servicepackminor.md)<br/>                         | Read-only<br/>  | The minor version of the service pack of the guest operating system running in the virtual machine.<br/>                              |
| [**SuiteMask**](ivmguestos-suitemask.md)<br/>                                       | Read-only<br/>  | The SuiteMask of the guest operating system running in the virtual machine.<br/>                                                      |
| [**TerminalServerPort**](ivmguestos-terminalserverport.md)<br/>                     | Read-only<br/>  | Port used by Remote Desktop Services in the guest operating system.<br/>                                                              |
| [**TerminalServicesInitialized**](ivmguestos-terminalservicesinitialized.md)<br/>   | Read-only<br/>  | The status of Terminal Services initialization in the guest operating system.<br/>                                                    |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMGuestOS is defined as 99fea0db-4880-499a-b6d8-73dff9bc91be<br/>                 |



 

