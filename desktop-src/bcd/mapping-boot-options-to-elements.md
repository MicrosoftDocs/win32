---
title: Mapping Boot Options to Elements
description: A mapping from the boot options in Boot.ini to the BCD elements.
ms.assetid: 60f43709-543c-41d5-afa7-7f2076d7380d
keywords:
- boot options Boot Config
- mapping boot options to elements Boot Config
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Mapping Boot Options to Elements

The following table provides a mapping from the boot options in Boot.ini to the BCD elements.



| Option               | Element type                               |
|----------------------|--------------------------------------------|
| /3GB                 | BcdOSLoaderInteger\_IncreaseUserVa         |
| /BASEVIDEO           | BcdOSLoaderBoolean\_UseVgaDriver           |
| /BAUDRATE=           | BcdLibraryInteger\_SerialDebuggerBaudRate  |
| /BOOTLOG             | BcdOSLoaderBoolean\_BootLogInitialization  |
| /BOOTLOGO            |                                            |
| /BREAK               | BcdOSLoaderBoolean\_DebuggerHalBreakpoint  |
| /BURNMEMORY=         | BcdOSLoaderInteger\_RemoveMemory           |
| /CHANNEL=            | BcdLibraryInteger\_1394DebuggerChannel     |
| /CLKLVL              |                                            |
| /CMDCONS             |                                            |
| /CRASHDEBUG          |                                            |
| /DEBUG, BOOTDEBUG    | BcdLibraryBoolean\_DebuggerEnabled         |
| /DEBUG               | BcdOSLoaderBoolean\_KernelDebuggerEnabled  |
| /DEBUGPORT=          | BcdLibraryInteger\_DebuggerType            |
| /DEBUGPORT=          | BcdLibraryInteger\_SerialDebuggerPort      |
| /EXECUTE             | BcdOSLoaderInteger\_NxPolicy               |
| /FASTDETECT          |                                            |
| /HAL=                | BcdOSLoaderString\_HalPath                 |
| /INTAFFINITY         |                                            |
| /KERNEL=             | BcdOSLoaderString\_KernelPath              |
| /LASTKNOWNGOOD       | BcdOSLoaderBoolean\_UseLastGoodSettings    |
| /MAXMEM=             | BcdLibraryInteger\_TruncatePhysicalMemory  |
| /MAXPROCSPERCLUSTER= | BcdOSLoaderInteger\_ClusterModeAddressing  |
| /MININIT             | BcdOSLoaderBoolean\_WinPEMode              |
| /NODEBUG             |                                            |
| /NOEXECUTE           | BcdOSLoaderInteger\_NxPolicy               |
| /NOGUIBOOT           | BcdOSLoaderBoolean\_DisableBootDisplay     |
| /NOLOWMEM            | BcdOSLoaderBoolean\_NoLowMemory            |
| /NOPAE               | BcdOSLoaderInteger\_PAEPolicy              |
| /NOSERIALMICE=       |                                            |
| /NUMPROC=            | BcdOSLoaderInteger\_NumberOfProcessors     |
| /ONECPU              | BcdOSLoaderBoolean\_UseBootProcessorOnly   |
| /PAE                 | BcdOSLoaderInteger\_PAEPolicy              |
| /PCILOCK             | BcdOSLoaderInteger\_UseFirmwarePciSettings |
| /RDRPATH=            |                                            |
| /REDIRECT            | BcdOSLoaderBoolean\_EmsEnabled             |
| /SAFEBOOT:           | BcdOSLoaderInteger\_SafeBoot               |
| /SCIORDINAL:         |                                            |
| /SDIBOOT=            |                                            |
| /SOS                 |                                            |
| /TIMERES=            |                                            |
| /USE8254             |                                            |
| /USERVA=             | BcdOSLoaderInteger\_IncreaseUserVa         |
| /WIN95               |                                            |
| /WIN95DOS            |                                            |
| /YEAR=               |                                            |



 

## Related topics

<dl> <dt>

[**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
</dt> <dt>

[**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)
</dt> </dl>

 

 




