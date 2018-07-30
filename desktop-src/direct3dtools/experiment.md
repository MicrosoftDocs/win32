---
Description: Represents information about an experiment (capture).
MS-HAID: vspixengine.Experiment
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: Experiment structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# <span id="vspixengine.experiment"></span>Experiment structure

Represents information about an experiment (capture).

## Syntax


```C++
} Experiment;
```

## Members

**processId**  
The associated process ID.

**applicationName**  
A COM string containing the name of the application to run the experiment on.

**commandLineArguments**  
A COM string containing the command line arguments.

**workingDirectory**  
A COM string containing the path of the working directory.

**tempPixRunFile**  
A COM string containing the filepath of the temporary file used to perform the experiment.

**startOption**  
The start option associated with the experiment.

**experimentType**  
The kind of experiment (capture).

**uiLocale**  
The ID of the locale used for UI overlay elements during the experiement (capture). This is passed from the host (such as Visual Studio Graphics Diagnostics) to the capture engine.

**registryRoot**  
A COM string containing the registry root. This is passed from the host (such as Visual Studio Graphics Diagnostics) to the capture engine.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



