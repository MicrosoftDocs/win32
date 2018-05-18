---
title: Video and Audio Chunk Granularity
description: Video and Audio Chunk Granularity
ms.assetid: '02c94de7-c7cb-4150-8b3e-0542d317c19b'
keywords: ["AVI files,chunk granularity", "AVICap class,filler chunks", "WM_CAP_GET_SEQUENCE_SETUP message", "capCaptureGetSetup macro", "WM_CAP_SET_SEQUENCE_SETUP message", "capCaptureSetSetup macro"]
---

# Video and Audio Chunk Granularity

The chunk granularity is a logical block size for an AVI file that is used for writing and retrieving audio and video data chunks. When writing audio and video chunks to disk, AVICap adds filler chunks (RIFF "JUNK" chunks) as necessary to fill each logical block of data.

You can retrieve the current chunk granularity setting by using the [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md) message (or the [**capCaptureGetSetup**](capcapturegetsetup.md) macro). The current chunk granularity is stored in the **wChunkGranularity** member of the [**CAPTUREPARMS**](captureparms.md) structure. You can specify a new chunk granularity as the value of **wChunkGranularity** and then send the updated **CAPTUREPARMS** structure to the capture window by using the [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md) message (or the [**capCaptureSetSetup**](capcapturesetsetup.md) macro). You can also specify zero for this member to set the chunk granularity to the sector size of the disk.

 

 




