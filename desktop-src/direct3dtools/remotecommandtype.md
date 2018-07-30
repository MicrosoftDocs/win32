---
Description: An enum used to communicate between the capture engine and a host (such as Visual Studio Graphics Diagnostics).
MS-HAID: vspixengine.RemoteCommandType
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: RemoteCommandType enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# <span id="vspixengine.remotecommandtype"></span>RemoteCommandType enumeration

An enum used to communicate between the capture engine and a host (such as Visual Studio Graphics Diagnostics).

## Syntax


```C++
};
```

## Constants

<span id="BeginCommunication"></span><span id="begincommunication"></span><span id="BEGINCOMMUNICATION"></span>**BeginCommunication**  
Starts communication.

<span id="RunExperiment"></span><span id="runexperiment"></span><span id="RUNEXPERIMENT"></span>**RunExperiment**  
Starts a Graphics Diagnostics capture session (an experiment).

<span id="RunAction"></span><span id="runaction"></span><span id="RUNACTION"></span>**RunAction**  
Starts a capture (same as hitting print screen). Sent by a host when capturing a frame.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



