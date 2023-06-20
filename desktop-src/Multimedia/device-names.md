---
title: Device Names
description: Device Names
ms.assetid: 0ba06439-cc33-43e1-a094-09bcc5e2f6b5
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Device Names

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

For each device type, there might be several MCI drivers that share the command set but operate on different data formats. To uniquely identify an MCI driver, MCI uses *device names*.

Device names are identified either in the \[mci\] section of the SYSTEM.INI file or in the appropriate part of the registry. This information identifies all MCI drivers to Windows. The entries in the \[mci\] section use the following form:

*device\_name* = *driver\_filename.extension*

The following example shows a typical \[mci\] section from SYSTEM.INI:


```C++
[mci]
cdaudio=mcicda.drv 
sequencer=mciseq.drv 
waveaudio=mciwave.drv 
avivideo=mciavi.drv
```



If an MCI driver is installed using a device name that already exists in SYSTEM.INI or the registry, the system appends an integer to the device name of the new driver, creating a unique device name. In the preceding example, an additional driver installed using the "cdaudio" device name would be assigned the device name "cdaudio1".

 

 




