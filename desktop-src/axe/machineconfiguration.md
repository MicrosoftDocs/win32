---
title: MachineConfiguration element
description: Contains elements that hold information about the computer.
ms.assetid: 7A7842D6-E1FE-45AD-803E-4DAE7976C5B8
keywords:
- MachineConfiguration element Access Execution Engine
topic_type:
- apiref
api_name:
- MachineConfiguration
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MachineConfiguration element

Contains elements that hold information about the computer.

## Usage

``` syntax
<MachineConfiguration/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                             | Description                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| [**AxeJob**](https://msdn.microsoft.com/library/windows/desktop/hh707420)<br/> | This node contains the entirety of the job used to generate a set of results.<br/> <br/> |



## Remarks

AXE adds this node when it generates the final job results file.

AXE gathers the necessary information and generates the default WinSAT System configuration data. These are the nodes AXE guarantees will be in the final job report file.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





