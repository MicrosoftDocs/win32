---
title: Process Snapshotting Functions
description: The Process Snapshotting API defines the following functions.
ms.assetid: E211E589-A95F-4BE6-B9B1-74218D4B0F3A
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Process Snapshotting Functions

The Process Snapshotting API defines the following functions.



| Function                                                             | Description                                                                                             |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**PssCaptureSnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psscapturesnapshot?branch=master)                     | Captures a snapshot of a target process.<br/>                                                     |
| [**PssDuplicateSnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssduplicatesnapshot?branch=master)                 | Duplicates a snapshot handle from one process to another.<br/>                                    |
| [**PssFreeSnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssfreesnapshot?branch=master)                           | Frees a snapshot.<br/>                                                                            |
| [**PssQuerySnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssquerysnapshot?branch=master)                         | Queries the snapshot.<br/>                                                                        |
| [**PssWalkMarkerCreate**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalkmarkercreate?branch=master)                   | Creates a walk marker.<br/>                                                                       |
| [**PssWalkMarkerFree**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalkmarkerfree?branch=master)                       | Frees a walk marker created by [**PssWalkMarkerCreate**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalkmarkercreate?branch=master). <br/>          |
| [**PssWalkMarkerGetPosition**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalkmarkergetposition?branch=master)         | Returns the current position of a walk marker.<br/>                                               |
| [**PssWalkMarkerSeekToBeginning**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalkmarkerseektobeginning?branch=master) | Rewinds a walk marker back to the beginning.<br/>                                                 |
| [**PssWalkMarkerSetPosition**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalkmarkersetposition?branch=master)         | Sets the position of a walk marker.<br/>                                                          |
| [**PssWalkSnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalksnapshot?branch=master)                           | Returns information from the current snapshot position, then advances to the next position. <br/> |



 

 

 





