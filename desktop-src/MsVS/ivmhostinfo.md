---
title: IVMHostInfo interface
description: The IVMHostInfo interface retrieves information about the host machine. An IVMHostInfo object is returned from the IVMVirtualServer HostInfo property.
ms.assetid: 0bd8a1d7-7a60-4b55-b48e-a24873f6a8a7
keywords:
- IVMHostInfo interface Virtual Server
- IVMHostInfo interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMHostInfo
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

# IVMHostInfo interface

The **IVMHostInfo** interface retrieves information about the host machine. An IVMHostInfo object is returned from the [**IVMVirtualServer::HostInfo**](ivmvirtualserver-hostinfo.md) property.

## Members

The **IVMHostInfo** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMHostInfo** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMHostInfo** interface has these methods.



| Method                                                       | Description                                                       |
|:-------------------------------------------------------------|:------------------------------------------------------------------|
| [**GetHostDriveSize**](ivmhostinfo-gethostdrivesize.md)     | Retrieves the size of a host drive, in MB.<br/>             |
| [**IsHostDriveMounted**](ivmhostinfo-ishostdrivemounted.md) | Indicates whether the specified host drive is mounted.<br/> |



 

### Properties

The **IVMHostInfo** interface has these properties.



| Property                                                                                  | Access type          | Description                                                                                                 |
|:------------------------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------|
| [**DVDDrives**](ivmhostinfo-dvddrives.md)<br/>                                     | Read-only<br/> | An array of drive letters associated with host CD-ROM or DVD-ROM devices.<br/>                        |
| [**FloppyDrives**](ivmhostinfo-floppydrives.md)<br/>                               | Read-only<br/> | An array of drive letters associated with host floppy drives.<br/>                                    |
| [**HostDrives**](ivmhostinfo-hostdrives.md)<br/>                                   | Read-only<br/> | An array of drive letters associated with host hard disk drives.<br/>                                 |
| [**LogicalProcessorCount**](ivmhostinfo-logicalprocessorcount.md)<br/>             | Read-only<br/> | The number of logical processors in the host machine.<br/>                                            |
| [**Memory**](ivmhostinfo-memory.md)<br/>                                           | Read-only<br/> | The total quantity, in megabytes, of physical RAM in the host machine.<br/>                           |
| [**MemoryAvail**](ivmhostinfo-memoryavail.md)<br/>                                 | Read-only<br/> | The total quantity, in megabytes, of available RAM in the host machine.<br/>                          |
| [**MemoryAvailString**](ivmhostinfo-memoryavailstring.md)<br/>                     | Read-only<br/> | The total quantity, in megabytes, of available RAM in the host machine, in the form of a string.<br/> |
| [**MemoryTotalString**](ivmhostinfo-memorytotalstring.md)<br/>                     | Read-only<br/> | The total quantity, in megabytes, of physical RAM in the host machine, in the form of a string.<br/>  |
| [**MMX**](ivmhostinfo-mmx.md)<br/>                                                 | Read-only<br/> | Indicates whether the host processor supports the MMX instruction set.<br/>                           |
| [**NetworkAdapters**](ivmhostinfo-networkadapters.md)<br/>                         | Read-only<br/> | An enumerable collection of the network interface cards that are installed on the host machine.<br/>  |
| [**NetworkAddresses**](ivmhostinfo-networkaddresses.md)<br/>                       | Read-only<br/> | Contains an array of TCP/IP addresses in the host computer.<br/>                                      |
| [**OperatingSystem**](ivmhostinfo-operatingsystem.md)<br/>                         | Read-only<br/> | The name of the operating system currently running on the host machine.<br/>                          |
| [**OSMajorVersion**](ivmhostinfo-osmajorversion.md)<br/>                           | Read-only<br/> | The major operating system release version currently running on the host machine.<br/>                |
| [**OSMinorVersion**](ivmhostinfo-osminorversion.md)<br/>                           | Read-only<br/> | The minor operating system release version currently running on the host machine.<br/>                |
| [**OSServicePackString**](ivmhostinfo-osservicepackstring.md)<br/>                 | Read-only<br/> | The service pack version currently installed on the host machine.<br/>                                |
| [**OSVersionString**](ivmhostinfo-osversionstring.md)<br/>                         | Read-only<br/> | The version of the operating system currently running on the host machine.<br/>                       |
| [**ParallelPort**](ivmhostinfo-parallelport.md)<br/>                               | Read-only<br/> | The name of the parallel port on the host computer.<br/>                                              |
| [**PhysicalProcessorCount**](ivmhostinfo-physicalprocessorcount.md)<br/>           | Read-only<br/> | The number of physical processors in the host machine.<br/>                                           |
| [**ProcessorFeaturesString**](ivmhostinfo-processorfeaturesstring.md)<br/>         | Read-only<br/> | A list of features supported by the host processor.<br/>                                              |
| [**ProcessorManufacturerString**](ivmhostinfo-processormanufacturerstring.md)<br/> | Read-only<br/> | The manufacturer of the host processor.<br/>                                                          |
| [**ProcessorSpeed**](ivmhostinfo-processorspeed.md)<br/>                           | Read-only<br/> | The speed, in megahertz, of the host processor.<br/>                                                  |
| [**ProcessorSpeedString**](ivmhostinfo-processorspeedstring.md)<br/>               | Read-only<br/> | The speed, in megahertz, of the host processor.<br/>                                                  |
| [**ProcessorVersionString**](ivmhostinfo-processorversionstring.md)<br/>           | Read-only<br/> | The version of the host processor.<br/>                                                               |
| [**SerialPorts**](ivmhostinfo-serialports.md)<br/>                                 | Read-only<br/> | A list of serial ports on the host computer.<br/>                                                     |
| [**SSE**](ivmhostinfo-sse.md)<br/>                                                 | Read-only<br/> | Specifies whether the host processor supports the SSE instruction set.<br/>                           |
| [**SSE2**](ivmhostinfo-sse2.md)<br/>                                               | Read-only<br/> | Specifies whether the host processor supports the SSE2 instruction set.<br/>                          |
| [**ThreeDNow**](ivmhostinfo-threednow.md)<br/>                                     | Read-only<br/> | Specifies whether the host processor supports the 3DNow! instruction set.<br/>                        |
| [**UTCTime**](ivmhostinfo-utctime.md)<br/>                                         | Read-only<br/> | The current UTC time on the host machine.<br/>                                                        |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





