---
title: IVMVirtualServer interface
description: The IVMVirtualServer interface defines the top-level Virtual Server application object.
ms.assetid: '52aad81c-3331-419a-bb43-5c774582cc65'
keywords: ["IVMVirtualServer interface Virtual Server", "IVMVirtualServer interface Virtual Server , described"]
topic_type:
- apiref
api_name:
- IVMVirtualServer
api_location:
- VsComInterfaces.lib
- VsComInterfaces.dll
api_type:
- COM
---

# IVMVirtualServer interface

The **IVMVirtualServer** interface defines the top-level Virtual Server application object.

## When to use

All other Virtual Server interface objects are retrieved through this object. **IVMVirtualServer** can notify clients about events by using the [**IVMVirtualServerEvents**](ivmvirtualserverevents.md) outgoing interface.

## Members

The **IVMVirtualServer** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMVirtualServer** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMVirtualServer** interface has these methods.



| Method                                                                                                    | Description                                                                                                                                             |
|:----------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AttachScriptToEvent**](ivmvirtualserver-attachscripttoevent.md)                                       | Specifies a script to run when an event occurs.<br/>                                                                                              |
| [**CreateDifferencingVirtualHardDisk**](ivmvirtualserver-createdifferencingvirtualharddisk.md)           | Creates a differencing virtual hard disk.<br/>                                                                                                    |
| [**CreateDynamicVirtualHardDisk**](ivmvirtualserver-createdynamicvirtualharddisk.md)                     | Creates a dynamically resizing virtual hard disk.<br/>                                                                                            |
| [**CreateFixedVirtualHardDisk**](ivmvirtualserver-createfixedvirtualharddisk.md)                         | Creates a fixed-size virtual hard disk.<br/>                                                                                                      |
| [**CreateFloppyDiskImage**](ivmvirtualserver-createfloppydiskimage.md)                                   | Creates a floppy disk image file.<br/>                                                                                                            |
| [**CreateHostDriveVirtualHardDisk**](ivmvirtualserver-createhostdrivevirtualharddisk.md)                 | Creates a virtual hard disk that is linked to a host drive.<br/>                                                                                  |
| [**CreateVirtualMachine**](ivmvirtualserver-createvirtualmachine.md)                                     | Creates a new virtual machine configuration and returns the virtual machine object.<br/>                                                          |
| [**CreateVirtualNetwork**](ivmvirtualserver-createvirtualnetwork.md)                                     | Creates a new virtual network.<br/>                                                                                                               |
| [**DeleteVirtualMachine**](ivmvirtualserver-deletevirtualmachine.md)                                     | Deletes a virtual machine configuration.<br/>                                                                                                     |
| [**DeleteVirtualNetwork**](ivmvirtualserver-deletevirtualnetwork.md)                                     | Deletes a virtual network.<br/>                                                                                                                   |
| [**FetchScriptByEvent**](ivmvirtualserver-fetchscriptbyevent.md)                                         | Retrieves the script command line associated with the specified event type.<br/>                                                                  |
| [**FindVirtualMachine**](ivmvirtualserver-findvirtualmachine.md)                                         | Retrieves a virtual machine object that matches the requested configuration.<br/>                                                                 |
| [**FindVirtualNetwork**](ivmvirtualserver-findvirtualnetwork.md)                                         | Retrieves a virtual network object that matches the requested name.<br/>                                                                          |
| [**GetConfigurationValue**](ivmvirtualserver-getconfigurationvalue.md)                                   | Retrieves the value of the specified configuration setting for this virtual server.<br/>                                                          |
| [**GetDVDFiles**](ivmvirtualserver-getdvdfiles.md)                                                       | Retrieves an array of known virtual DVD files.<br/>                                                                                               |
| [**GetFloppyDiskFiles**](ivmvirtualserver-getfloppydiskfiles.md)                                         | Retrieves an array of known virtual floppy disk files.<br/>                                                                                       |
| [**GetFloppyDiskImageType**](ivmvirtualserver-getfloppydiskimagetype.md)                                 | Retrieves the type of an existing floppy disk image file.<br/>                                                                                    |
| [**GetHardDisk**](ivmvirtualserver-getharddisk.md)                                                       | Retrieves an [**IVMHardDisk**](ivmharddisk.md) object that corresponds to an existing disk image file.<br/>                                      |
| [**GetHardDiskFiles**](ivmvirtualserver-getharddiskfiles.md)                                             | Retrieves an array of known virtual hard disk files.<br/>                                                                                         |
| [**GetVirtualMachineFiles**](ivmvirtualserver-getvirtualmachinefiles.md)                                 | Retrieves an array of known virtual machine configuration files.<br/>                                                                             |
| [**GetVirtualNetworkFiles**](ivmvirtualserver-getvirtualnetworkfiles.md)                                 | Retrieves an array of known virtual network configuration files.<br/>                                                                             |
| [**QueryLocale**](ivmvirtualserver-querylocale.md)                                                       | Retrieves the preferred Virtual Server service locale selected from the set of languages specified by an RFC-2616 compliant language string.<br/> |
| [**RegisterVirtualMachine**](ivmvirtualserver-registervirtualmachine.md)                                 | Registers an existing virtual machine configuration and returns the virtual machine object.<br/>                                                  |
| [**RegisterVirtualNetwork**](ivmvirtualserver-registervirtualnetwork.md)                                 | Registers an existing virtual network configuration and returns the virtual network object.<br/>                                                  |
| [**RemoveConfigurationValue**](ivmvirtualserver-removeconfigurationvalue.md)                             | Removes the value of the specified configuration setting for this virtual server.<br/>                                                            |
| [**RemoveScriptFromEvent**](ivmvirtualserver-removescriptfromevent.md)                                   | Disassociates a script from an event.<br/>                                                                                                        |
| [**SetConfigurationValue**](ivmvirtualserver-setconfigurationvalue.md)                                   | Sets the value of the specified configuration setting for this virtual server.<br/>                                                               |
| [**UnregisterVirtualMachine**](ivmvirtualserver-unregistervirtualmachine.md)                             | Unregisters a virtual machine configuration without deleting the configuration file.<br/>                                                         |
| [**UnregisterVirtualNetwork**](ivmvirtualserver-unregistervirtualnetwork.md)                             | Unregisters a virtual network configuration without deleting the configuration file.<br/>                                                         |
| [**VMRCCreateEncryptionCertificateRequest**](ivmvirtualserver-vmrccreateencryptioncertificaterequest.md) | Creates a new security certificate request.<br/>                                                                                                  |



 

### Properties

The **IVMVirtualServer** interface has these properties.



| Property                                                                                                 | Access type           | Description                                                                                                                                                  |
|:---------------------------------------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AvailableSystemCapacity**](ivmvirtualserver-availablesystemcapacity.md)<br/>                   | Read-only<br/>  | The percentage of currently available system capacity, based on the number of virtual machines currently running and their scheduling parameters.<br/> |
| [**DefaultLocale**](ivmvirtualserver-defaultlocale.md)<br/>                                       | Read-only<br/>  | The default user interface locale of the Virtual Server service.<br/>                                                                                  |
| [**DefaultVMConfigurationPath**](ivmvirtualserver-defaultvmconfigurationpath.md)<br/>             | Read/write<br/> | The default directory searched by the web application to create lists of available virtual machine configuration files.<br/>                           |
| [**DefaultVNConfigurationPath**](ivmvirtualserver-defaultvnconfigurationpath.md)<br/>             | Read-only<br/>  | The default directory searched by the web application to create lists of available virtual network configuration files.<br/>                           |
| [**HostInfo**](ivmvirtualserver-hostinfo.md)<br/>                                                 | Read-only<br/>  | Information about the physical computer.<br/>                                                                                                          |
| [**Locale**](ivmvirtualserver-locale.md)<br/>                                                     | Write-only<br/> | The locale for this session with the Virtual Server service.<br/>                                                                                      |
| [**MaximumFloppyDrivesPerVM**](ivmvirtualserver-maximumfloppydrivespervm.md)<br/>                 | Read-only<br/>  | The maximum number of floppy drives per virtual machine.<br/>                                                                                          |
| [**MaximumMemoryPerVM**](ivmvirtualserver-maximummemorypervm.md)<br/>                             | Read-only<br/>  | The maximum allowable quantity, in megabytes, of physical RAM per virtual machine.<br/>                                                                |
| [**MaximumNetworkAdaptersPerVM**](ivmvirtualserver-maximumnetworkadapterspervm.md)<br/>           | Read-only<br/>  | The maximum number of network interfaces per virtual machine.<br/>                                                                                     |
| [**MaximumNumberOfIDEBuses**](ivmvirtualserver-maximumnumberofidebuses.md)<br/>                   | Read-only<br/>  | The maximum number of buses allowed for IDE.<br/>                                                                                                      |
| [**MaximumNumberOfSCSIControllers**](ivmvirtualserver-maximumnumberofscsicontrollers.md)<br/>     | Read-only<br/>  | The maximum number of adapters allowed for SCSI.<br/>                                                                                                  |
| [**MaximumParallelPortsPerVM**](ivmvirtualserver-maximumparallelportspervm.md)<br/>               | Read-only<br/>  | The maximum number of parallel ports per virtual machine.<br/>                                                                                         |
| [**MaximumSerialPortsPerVM**](ivmvirtualserver-maximumserialportspervm.md)<br/>                   | Read-only<br/>  | The maximum number of serial ports per virtual machine.<br/>                                                                                           |
| [**MinimumMemoryPerVM**](ivmvirtualserver-minimummemorypervm.md)<br/>                             | Read-only<br/>  | The minimum allowable quantity, in megabytes, of physical RAM per virtual machine.<br/>                                                                |
| [**Name**](ivmvirtualserver-name.md)<br/>                                                         | Read-only<br/>  | The name of the Virtual Server application.<br/>                                                                                                       |
| [**ProductID**](ivmvirtualserver-productid.md)<br/>                                               | Read-only<br/>  | The ProductID of this instance of Virtual Server.<br/>                                                                                                 |
| [**SearchPaths**](ivmvirtualserver-searchpaths.md)<br/>                                           | Read/write<br/> | An array of file system paths used to find files associated with Virtual Server.<br/>                                                                  |
| [**Security**](ivmvirtualserver-security.md)<br/>                                                 | Read/write<br/> | The [**IVMSecurity**](ivmsecurity.md) object associated with Virtual Server.<br/>                                                                     |
| [**SuggestedMaximumMemoryPerVM**](ivmvirtualserver-suggestedmaximummemorypervm.md)<br/>           | Read-only<br/>  | The suggested maximum allowable quantity, in megabytes, of physical RAM per virtual machine to avoid low memory conditions on the host.<br/>           |
| [**SupportDrivers**](ivmvirtualserver-supportdrivers.md)<br/>                                     | Read-only<br/>  | A collection of support drivers.<br/>                                                                                                                  |
| [**Tasks**](ivmvirtualserver-tasks.md)<br/>                                                       | Read-only<br/>  | A collection of tasks.<br/>                                                                                                                            |
| [**UnconnectedNetworkAdapters**](ivmvirtualserver-unconnectednetworkadapters.md)<br/>             | Read-only<br/>  | A collection of unconnected [**IVMNetworkAdapter**](ivmnetworkadapter.md) objects.<br/>                                                               |
| [**UpTime**](ivmvirtualserver-uptime.md)<br/>                                                     | Read-only<br/>  | The number of seconds the Virtual Server application has been running.<br/>                                                                            |
| [**Version**](ivmvirtualserver-version.md)<br/>                                                   | Read-only<br/>  | The version of this instance of Virtual Server.<br/>                                                                                                   |
| [**VirtualMachines**](ivmvirtualserver-virtualmachines.md)<br/>                                   | Read-only<br/>  | A collection of [**IVMVirtualMachine**](ivmvirtualmachine.md) objects.<br/>                                                                           |
| [**VirtualNetworks**](ivmvirtualserver-virtualnetworks.md)<br/>                                   | Read-only<br/>  | A collection of [**IVMVirtualNetwork**](ivmvirtualnetwork.md) objects.<br/>                                                                           |
| [**VMRCAdminAddress**](ivmvirtualserver-vmrcadminaddress.md)<br/>                                 | Read/write<br/> | The TCP/IP address of the host network adapter over which VMRC connections are accepted.<br/>                                                          |
| [**VMRCAdminPortNumber**](ivmvirtualserver-vmrcadminportnumber.md)<br/>                           | Read/write<br/> | The VMRC administration port number.<br/>                                                                                                              |
| [**VMRCAuthenticator**](ivmvirtualserver-vmrcauthenticator.md)<br/>                               | Read/write<br/> | The authentication method to use for new VMRC connections.<br/>                                                                                        |
| [**VMRCAuthenticators**](ivmvirtualserver-vmrcauthenticators.md)<br/>                             | Read-only<br/>  | The VMRC authentication methods supported by Virtual Server.<br/>                                                                                      |
| [**VMRCEnabled**](ivmvirtualserver-vmrcenabled.md)<br/>                                           | Read/write<br/> | Indicates whether server administration using Virtual Machine Remote Control (VMRC) is enabled.<br/>                                                   |
| [**VMRCEncryptionCertificate**](ivmvirtualserver-vmrcencryptioncertificate.md)<br/>               | Read/write<br/> | The security certificate used by SSL/TLS encryption to protect VMRC session data.<br/>                                                                 |
| [**VMRCEncryptionCertificateRequest**](ivmvirtualserver-vmrcencryptioncertificaterequest.md)<br/> | Read-only<br/>  | The current security certificate request.<br/>                                                                                                         |
| [**VMRCEncryptionEnabled**](ivmvirtualserver-vmrcencryptionenabled.md)<br/>                       | Read/write<br/> | Indicates whether server administration VMRC session data is encrypted using SSL/TLS encryption.<br/>                                                  |
| [**VMRCIdleConnectionTimeout**](ivmvirtualserver-vmrcidleconnectiontimeout.md)<br/>               | Read/write<br/> | The time in seconds after which idle VMRC connections are disconnected.<br/>                                                                           |
| [**VMRCIdleConnectionTimeoutEnabled**](ivmvirtualserver-vmrcidleconnectiontimeoutenabled.md)<br/> | Read/write<br/> | Indicates whether idle VMRC connections are automatically disconnected.<br/>                                                                           |
| [**VMRCXResolution**](ivmvirtualserver-vmrcxresolution.md)<br/>                                   | Read/write<br/> | The horizontal resolution used for server administration.<br/>                                                                                         |
| [**VMRCYResolution**](ivmvirtualserver-vmrcyresolution.md)<br/>                                   | Read/write<br/> | The vertical resolution used for server administration.<br/>                                                                                           |
| [**VMScriptsEnabled**](ivmvirtualserver-vmscriptsenabled.md)<br/>                                 | Read/write<br/> | Indicates whether scripts attached to any virtual machine are allowed to run.<br/>                                                                     |
| [**VSScriptsEnabled**](ivmvirtualserver-vsscriptsenabled.md)<br/>                                 | Read/write<br/> | Indicates whether scripts attached to Virtual Server events are allowed to run.<br/>                                                                   |



 

## Examples

The following example shows how to create an **IVMVirtualServer** object from VBScript.


```VB
Dim vsApp;
Set vsApp = WScript.CreateObject("VirtualServer.Application");
```



The following example displays the current property values of the **IVMVirtualServer** object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Available system capacity: " & objVS.AvailableSystemCapacity

Wscript.Echo "Default Locale: " & CInt(objVS.DefaultLocale)

Wscript.Echo "Default VM configuration path: " & objVS.DefaultVMConfigurationPath

Wscript.Echo "Default VN configuration path: " & objVS.DefaultVNConfigurationPath

Set objHI = objVS.HostInfo
Wscript.Echo "Host info:"
Wscript.Echo "    Host operating system: " & objHI.OperatingSystem
Wscript.Echo "    Host operating system version: " & objHI.OSMajorVersion & "." & objHI.OSMinorVersion
Wscript.Echo "    Number of processors on host: " & objHI.PhysicalProcessorCount

Wscript.Echo "Maximum floppy drives per VM: " & objVS.MaximumFloppyDrivesPerVM

Wscript.Echo "Maximum memory per VM: " & objVS.MaximumMemoryPerVM

Wscript.Echo "Maximum network adapters per VM: " & objVS.MaximumNetworkAdaptersPerVM

Wscript.Echo "Maximum number of IDE buses: " & objVS.MaximumNumberOfIDEBuses

Wscript.Echo "Maximum number of SCSI controllers: " & objVS.MaximumNumberOfSCSIControllers

Wscript.Echo "Maximum parallel ports per VM: " & objVS.MaximumParallelPortsPerVM

Wscript.Echo "Maximum serial ports per VM: " & objVS.MaximumSerialPortsPerVM

Wscript.Echo "Minimum memory per VM: " & objVS.MinimumMemoryPerVM

Wscript.Echo "Name: " & objVS.Name

Wscript.Echo "Product ID: " & objVS.ProductID

Dim allPaths
allPaths = objVS.SearchPaths
If UBound (allPaths) = -1 Then
  Wscript.Echo "File search paths: [empty]"
Else
  Wscript.Echo "File search paths: "
  For i = LBound(allPaths) to UBound(allPaths)
    wscript.echo "    " & allPaths(i)
  Next
End If

Set objSec = objVS.Security
Wscript.Echo "Security principle: "
Wscript.Echo "    Owner Name: " & objSec.OwnerName
Wscript.Echo "    Owner SID: " & objSec.OwnerSID
Wscript.Echo "    Group Name: " & objSec.GroupName
Wscript.Echo "    Group SID: " & objSec.GroupSID
Wscript.Echo "Suggested maximum memory per VM: " & objVS.SuggestedMaximumMemoryPerVM

Set objSDColl = objVS.SupportDrivers
If objSDColl.Count > 0 Then
  Wscript.Echo "Support drivers: "
  For Each objSD in objSDColl
    Wscript.Echo "    Type: " & objSD.Type & " (" & objSD.Description & ")"
  Next
End If

Set objTColl = objVS.Tasks
If objTColl.Count = 0 Then
  Wscript.Echo "Current tasks: [none]"
Else
  Wscript.Echo "Current tasks: "
  For Each objT in objTColl
    Wscript.Echo "    Task: " & objT.ID & ":" & objT.Description
  Next
End If

Set objUNA = objVS.UnconnectedNetworkAdapters
Wscript.Echo "Unconnected network adapters: " & objUNA.Count
Wscript.Echo "Uptime: " & objVS.Uptime
Wscript.Echo "Version: " & objVS.Version

Set objVMColl = objVS.VirtualMachines
If objVMColl.Count = 0 Then
  Wscript.Echo "    Virtual machines: [none]"
Else
  Wscript.Echo "Virtual machines: " & objVMColl.Count
  For Each objVM in objVMColl
    Wscript.Echo "    Name: " & objVM.Name
  Next
End If

Set objVNColl = objVS.VirtualNetworks
If objVNColl.Count = 0 Then
  Wscript.Echo "Virtual networks: [none]"
Else
  Wscript.Echo "Virtual networks: " & objVNColl.Count
  For Each objVN in objVNColl
    Wscript.Echo "    Name: " & objVN.Name
  Next
End If

If objVS.VMRCAdminAddress = "" Then
  Wscript.Echo "VMRC admin address: [all]"
Else
  Wscript.Echo "VMRC admin address: " & objVS.VMRCAdminAddress
End If

Wscript.Echo "VMRC admin port number: " & objVS.VMRCAdminPortNumber

Set objVMA = objVS.VMRCAuthenticator
Wscript.Echo "Current VMRC authenticator: " & objVMA.Name & " (" & objVMA.Description & ")"

Set objVMAColl = objVS.VMRCAuthenticators
Dim objAuth
If isNUll(objVMAColl) Then
  Wscript.Echo "VMRC authenticators: [none]"
Else
  Wscript.Echo "VMRC authenticators: "
  For Each objAuth in objVMAColl
    Wscript.Echo "    Name: " & objAuth.Name & " (" & objAuth.Description & ")"
  Next
End If

Wscript.Echo "VMRC enabled: " & objVS.VMRCEnabled

If objVS.VMRCEncryptionCertificate = "" Then
  Wscript.Echo "VMRC encryption certificate: [none]"
Else
  Wscript.Echo "VMRC encryption certificate: " & objVS.VMRCEncryptionCertificate
End If

If objVS.VMRCEncryptionCertificateRequest = "" Then
  Wscript.Echo "VMRC encryption certificate request: [none]"
Else
  Wscript.Echo "VMRC encryption certificate request: " & objVS.VMRCEncryptionCertificateRequest
End If

Wscript.Echo "VMRC encryption enabled: " & objVS.VMRCEncryptionEnabled

Wscript.Echo "VMRC idle connection timeout: " & objVS.VMRCIdleConnectionTimeout

Wscript.Echo "VMRC idle connection timeout enabled: " & objVS.VMRCIdleConnectionTimeoutEnabled

Wscript.Echo "VMRC X-Resolution: " & objVS.VMRCXResolution

Wscript.Echo "VMRC Y-Resolution: " & objVS.VMRCYResolution

Wscript.Echo "Virtual machine scripts enabled: " & objVS.VMScriptsEnabled

Wscript.Echo "Virtual server event scripts enabled: " & objVS.VSScriptsEnabled
```



The following example shows how to create an **IVMVirtualServer**object from JScript.


```JScript
var vsApp = WScript.CreateObject("VirtualServer.Application");
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |
| Library<br/>  | <dl> <dt>VsComInterfaces.lib</dt> </dl>    |
| IID<br/>      | IID\_IVMVirtualServer is defined as D1E64C50-A25D-450f-BE0B-9CA5A354CFF4<br/>               |



 

 





