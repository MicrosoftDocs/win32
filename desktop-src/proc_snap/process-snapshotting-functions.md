---
title: Process Snapshotting Functions
description: The Process Snapshotting API defines the following functions.
ms.assetid: E211E589-A95F-4BE6-B9B1-74218D4B0F3A
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Process Snapshotting Functions

The Process Snapshotting API defines the following functions.



| Function                                                             | Description                                                                                             |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**PssCaptureSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psscapturesnapshot)                     | Captures a snapshot of a target process.<br/>                                                     |
| [**PssDuplicateSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssduplicatesnapshot)                 | Duplicates a snapshot handle from one process to another.<br/>                                    |
| [**PssFreeSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssfreesnapshot)                           | Frees a snapshot.<br/>                                                                            |
| [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot)                         | Queries the snapshot.<br/>                                                                        |
| [**PssWalkMarkerCreate**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkercreate)                   | Creates a walk marker.<br/>                                                                       |
| [**PssWalkMarkerFree**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkerfree)                       | Frees a walk marker created by [**PssWalkMarkerCreate**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkercreate). <br/>          |
| [**PssWalkMarkerGetPosition**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkergetposition)         | Returns the current position of a walk marker.<br/>                                               |
| [**PssWalkMarkerSeekToBeginning**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkerseektobeginning) | Rewinds a walk marker back to the beginning.<br/>                                                 |
| [**PssWalkMarkerSetPosition**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkersetposition)         | Sets the position of a walk marker.<br/>                                                          |
| [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot)                           | Returns information from the current snapshot position, then advances to the next position. <br/> |



 

 

 





