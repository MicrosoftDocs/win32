---
description: This topic provides a procedure for performing track-controlled recording of audio streams.
ms.assetid: 57df081f-df41-4187-910b-939e3d82d7a0
title: Track-Controlled Record
ms.topic: article
ms.date: 05/31/2018
---

# Track-Controlled Record

This topic provides a procedure for performing track-controlled recording of audio streams.

**To perform track-controlled recording of audio streams**

1.  Select File Track Terminals onto streams.
2.  Create the File Record Terminal.
3.  Set the file name.
4.  Enumerate streams on the TAPI call. For these steps, see the following procedure.
5.  Call the [**Start**](/windows/desktop/api/tapi3if/nf-tapi3if-itmediacontrol-start) method on the File Record Terminal to start stream recording.

**To enumerate streams on the TAPI call**

1.  Create a track of the same audio type and direction as the stream.
2.  Set the track properties for audio format. If not set, the format will be the same as the streams format.
3.  Select the track on the stream.

If one track is selected on multiple streams, this implies mixing streams.

 

 



