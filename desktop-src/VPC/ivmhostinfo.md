---
title: IVMHostInfo interface (VPCCOMInterfaces.h)
description: Retrieves information about the host machine. An IVMHostInfo object is returned from the IVMVirtualPC HostInfo property.
ms.assetid: f30fa377-2067-4e03-bc6e-2ada62fc56b4
keywords:
- IVMHostInfo interface Virtual PC
- IVMHostInfo interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMHostInfo
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHostInfo interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves information about the host machine. An **IVMHostInfo** object is returned from the [**IVMVirtualPC::HostInfo**](ivmvirtualpc-hostinfo.md) property.

## Members

The **IVMHostInfo** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMHostInfo** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMHostInfo** interface has these properties.



| Property                                                                                  | Access type          | Description                                                                                        |
|:------------------------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------|
| [**DVDDrives**](ivmhostinfo-dvddrives.md)<br/>                                     | Read-only<br/> | The drive letters associated with host CD and DVD devices.<br/>                              |
| [**FloppyDrives**](ivmhostinfo-floppydrives.md)<br/>                               | Read-only<br/> | The drive letters associated with host floppy drives.<br/>                                   |
| [**LogicalProcessorCount**](ivmhostinfo-logicalprocessorcount.md)<br/>             | Read-only<br/> | The number of logical processors in the host machine.<br/>                                   |
| [**Memory**](ivmhostinfo-memory.md)<br/>                                           | Read-only<br/> | The total amount of physical memory in the host machine, in megabytes.<br/>                  |
| [**MemoryAvail**](ivmhostinfo-memoryavail.md)<br/>                                 | Read-only<br/> | The amount of available physical memory in the host machine, in megabytes.<br/>              |
| [**MemoryAvailString**](ivmhostinfo-memoryavailstring.md)<br/>                     | Read-only<br/> | The amount of available physical memory in the host machine, in megabytes, as a string.<br/> |
| [**MemoryTotalString**](ivmhostinfo-memorytotalstring.md)<br/>                     | Read-only<br/> | The total amount of physical memory in the host machine, in megabytes, as a string.<br/>     |
| [**MMX**](ivmhostinfo-mmx.md)<br/>                                                 | Read-only<br/> | Indicates whether the processor supports the MMX instruction set.<br/>                       |
| [**NetworkAdapters**](ivmhostinfo-networkadapters.md)<br/>                         | Read-only<br/> | An enumerable collection of NICs in the host machine.<br/>                                   |
| [**NetworkAddresses**](ivmhostinfo-networkaddresses.md)<br/>                       | Read-only<br/> | An enumerable collection of TCP/IP addresses in the host machine.<br/>                       |
| [**OperatingSystem**](ivmhostinfo-operatingsystem.md)<br/>                         | Read-only<br/> | The operating system running on the host machine.<br/>                                       |
| [**OSMajorVersion**](ivmhostinfo-osmajorversion.md)<br/>                           | Read-only<br/> | The major version of the operating system running on the host machine.<br/>                  |
| [**OSMinorVersion**](ivmhostinfo-osminorversion.md)<br/>                           | Read-only<br/> | The minor version of the operating system running on the host machine.<br/>                  |
| [**OSServicePackString**](ivmhostinfo-osservicepackstring.md)<br/>                 | Read-only<br/> | The service pack information of the operating system running on the host machine.<br/>       |
| [**OSVersionString**](ivmhostinfo-osversionstring.md)<br/>                         | Read-only<br/> | The operating system version running on the host machine.<br/>                               |
| [**ParallelPort**](ivmhostinfo-parallelport.md)<br/>                               | Read-only<br/> | The host parallel port that can be attached to the guest.<br/>                               |
| [**PhysicalProcessorCount**](ivmhostinfo-physicalprocessorcount.md)<br/>           | Read-only<br/> | The number of physical processors in the host machine.<br/>                                  |
| [**ProcessorFeaturesString**](ivmhostinfo-processorfeaturesstring.md)<br/>         | Read-only<br/> | The list of features supported by the host processor.<br/>                                   |
| [**ProcessorManufacturerString**](ivmhostinfo-processormanufacturerstring.md)<br/> | Read-only<br/> | The manufacturer of the host processor.<br/>                                                 |
| [**ProcessorSpeed**](ivmhostinfo-processorspeed.md)<br/>                           | Read-only<br/> | The speed of the host processor, in megahertz (MHz) or gigahertz (GHz).<br/>                 |
| [**ProcessorSpeedString**](ivmhostinfo-processorspeedstring.md)<br/>               | Read-only<br/> | The speed of the host processor, in megahertz or gigahertz, as a string.<br/>                |
| [**ProcessorVersionString**](ivmhostinfo-processorversionstring.md)<br/>           | Read-only<br/> | The version of the host processor.<br/>                                                      |
| [**SerialPorts**](ivmhostinfo-serialports.md)<br/>                                 | Read-only<br/> | The serial port names associated with host serial ports.<br/>                                |
| [**SSE**](ivmhostinfo-sse.md)<br/>                                                 | Read-only<br/> | Indicates whether the processor supports the SSE instruction set.<br/>                       |
| [**SSE2**](ivmhostinfo-sse2.md)<br/>                                               | Read-only<br/> | Indicates whether the processor supports the SSE2 instruction set.<br/>                      |
| [**ThreeDNow**](ivmhostinfo-threednow.md)<br/>                                     | Read-only<br/> | Indicates whether the processor supports the 3DNow instruction set.<br/>                     |
| [**UTCTime**](ivmhostinfo-utctime.md)<br/>                                         | Read-only<br/> | The UTC time on the host machine.<br/>                                                       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMHostInfo is defined as 5b5cf343-05ad-453b-be99-adf4e27b2ebc<br/>                |



 

