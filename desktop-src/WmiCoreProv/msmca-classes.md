---
description: A set of WMI classes that expose the Machine Check Architecture (MCA). The System Abstraction Layer (SAL) provides all events reported in the MSMCA class. The Intel Corporation develops and owns the MCA.
ms.assetid: 4e35f871-5bce-49ed-a3e8-d2d967e6e2dc
title: MSMCA Classes
ms.topic: article
ms.date: 05/31/2018
---

# MSMCA Classes

The Microsoft Machine Check Architecture (MSMCA) classes are a set of WMI classes that expose the Machine Check Architecture (MCA). The System Abstraction Layer (SAL) provides all events reported in the MSMCA class. The Intel Corporation develops and owns the MCA.



| Class                                                                               | Description                                                                                            |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**MSMCAEvent\_CPUError**](msmcaevent-cpuerror.md)                                 | Represents a CPU error event.                                                                          |
| [**MSMCAEvent\_Header**](msmcaevent-header.md)                                     | Represents the common header that all MSMCAEvent classes use.                                          |
| [**MSMCAEvent\_InvalidError**](msmcaevent-invaliderror.md)                         | Represents a Memory Check Architecture (MCA) invalid error.                                            |
| [**MSMCAEvent\_MemoryError**](msmcaevent-memoryerror.md)                           | Represents an MCA memory error event.                                                                  |
| [**MSMCAEvent\_MemoryPageRemoved**](msmcaevent-memorypageremoved.md)               | Indicates that the operating system removed a physical page of memory.                                 |
| [**MSMCAEvent\_PCIBusError**](msmcaevent-pcibuserror.md)                           | Represents an MCA PCI bus error.                                                                       |
| [**MSMCAEvent\_PCIComponentError**](msmcaevent-pcicomponenterror.md)               | Represents an MCA PCI component error.                                                                 |
| [**MSMCAEvent\_PlatformSpecificError**](msmcaevent-platformspecificerror.md)       | Represents an MCA platform-specific error.                                                             |
| [**MSMCAEvent\_SMBIOSError**](msmcaevent-smbioserror.md)                           | Represents an MCA system bios error.                                                                   |
| [**MSMCAEvent\_SwitchToCMCPolling**](msmcaevent-switchtocmcpolling.md)             | Indicates that the corrected machine check handling is switched to polling.                            |
| [**MSMCAEvent\_SystemEventError**](msmcaevent-systemeventerror.md)                 | Represents an MCA system event error.                                                                  |
| [**MSMCAInfo**](msmcainfo.md)                                                      | Abstract base class from which all Machine Check Architecture (MCA) provider data classes are derived. |
| [**MSMCAInfo\_Entry**](msmcainfo-entry.md)                                         | Represents an MCA, Corrected Machine Check (CMC), or Corrected Platform Error (CPE) information entry. |
| [**MSMCAInfo\_RawCMCEvent**](msmcainfo-rawcmcevent.md)                             | Contains a CMC event.                                                                                  |
| [**MSMCAInfo\_RawCorrectedPlatformEvent**](msmcainfo-rawcorrectedplatformevent.md) | Contains a Corrected Platform Event.                                                                   |
| [**MSMCAInfo\_RawMCAData**](msmcainfo-rawmcadata.md)                               | Specifies the raw MCA logs.                                                                            |
| [**MSMCAInfo\_RawMCAEvent**](msmcainfo-rawmcaevent.md)                             | Contains a MCA event.                                                                                  |
| [**WmiEvent**](wmievent.md)                                                        | Abstract base class from which all MCA provider event classes are derived.                             |



 

 

 



