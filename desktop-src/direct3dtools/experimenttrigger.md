---
description: Represents experiment trigger information.
MS-HAID: vspixengine.ExperimentTrigger
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ExperimentTrigger structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 3CAA67E5-9C43-4BCD-9388-63EF06AB1C0E
api_name: 
 - ExperimentTrigger
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.experimenttrigger"></span>ExperimentTrigger structure

Represents experiment trigger information.

## Syntax


```C++
} ExperimentTrigger;
```

## Members

**type**  
The kind of experiment (capture) triggered.

**key**  
When type is equal to EXPERIMENTTRIGGERTYPE::KEY, the key used to trigger capture.

**frameNumber**  
When type is equal to EXPERIMENTTRIGGERTYPE::FRAMENUMBER, the frame number that will trigger capture.

**captureCount**  
The number of sequential frames to capture.

**actionIID**  
The ID of the action event (screenshot, frame capture, etc).

**actionPlayload**  
A pointer to the action event payload.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



