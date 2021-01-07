---
description: ASF Multiplexer
ms.assetid: 007a6da5-47cf-476a-b0f7-566a68ad19ce
title: ASF Multiplexer
ms.topic: article
ms.date: 05/31/2018
---

# ASF Multiplexer

The ASF *multiplexer* is a WMContainer layer object that works with the [ASF Data Object](asf-file-structure.md) and gives an application the ability to generate data packets for an ASF container. The multiplexer accepts media data in the form of [Media Samples](media-samples.md) and outputs media samples based on streaming and ASF packet parameters defined in the [ASF Header Object](asf-file-structure.md). The output media samples hold references to one or more media buffers that contain packetized digital media data.You can use this object in a file encoding scenario where it receives encoded stream samples from the encoder or for ASF-ASF transcoding (remuxing).

The following diagram illustrates ASF data packet generation for an ASF file using the multiplexer.

![diagram showing asf data packet generation](images/bb2da6a9-5e50-4dea-9b79-ae32759ac48a.gif)

For information about the structure of an ASF file, see [ASF File Structure](asf-file-structure.md).

This section contains the following topics:



| Topic                                                                  | Description                                                       |
|------------------------------------------------------------------------|-------------------------------------------------------------------|
| [Creating the Multiplexer Object](creating-the-multiplexer-object.md) | How to create and initialize the multiplexer.                     |
| [Generating New ASF Data Packets](generating-new-asf-data-packets.md) | How to generate data packets to constitute a new ASF Data Object. |



 

## Related topics

<dl> <dt>

[WMContainer ASF Components](wmcontainer-asf-components.md)
</dt> <dt>

[Tutorial: Copying ASF Streams from One File to Another](tutorial--copying-asf-streams-from-one-file-to-another.md)
</dt> <dt>

[Tutorial: Writing a WMA File by Using CBR Encoding](tutorial--writing-a-wma-file-by-using-cbr-encoding.md)
</dt> </dl>

 

 



