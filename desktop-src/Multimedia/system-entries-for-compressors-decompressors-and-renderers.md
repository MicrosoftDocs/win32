---
title: System Entries for Compressors, Decompressors, and Renderers
description: System Entries for Compressors, Decompressors, and Renderers
ms.assetid: b27bbd5b-a218-49bb-b179-b24ce39869a1
keywords:
- Video for Windows (VFW),compressor system entries
- VFW (Video for Windows),compressor system entries
ms.topic: article
ms.date: 05/31/2018
---

# System Entries for Compressors, Decompressors, and Renderers

The system uses entries in the registry to find VCM drivers. These entries are in the form of two four-character codes separated by a period. The first four-character code is defined by the system and can be one of the following:



| Four-character code | Description                               |
|---------------------|-------------------------------------------|
| "VIDC"              | Identifies compressors and decompressors. |
| "VIDS"              | Identifies video-stream renderers.        |
| "TXTS"              | Identifies text-stream renderers.         |
| "AUDS"              | Identifies audio-stream handlers.         |



 

Custom renderers can define their own four-character codes.

The second four-character code is defined by the driver. Typically, the second four-character code corresponds to the type of data the driver can handle.

When opening a VCM driver, an application specifies the type of driver and the type of data handler it needs. Typically, this information comes from the stream header. The system tries to open the specified data handler, but if it fails, the system searches the registry for a driver that has the required handler.

When searching for the driver, the system tries to match the four-character codes specified for the driver type and data handler with those specified in the driver entry. For example, if an application specifies the compressor MSSQ, the system searches the registry for the driver entry VIDC.MSSQ. If it cannot find a match, it opens each driver corresponding to the driver type and locates one that can handle the type of data your application specifies. In the previous example, if the system could not find VIDC.MSSQ, it would open all drivers with the "VIDC" four-character code and locate one that can handle the data.

 

 




