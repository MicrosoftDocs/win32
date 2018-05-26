---
title: RequiresAppVersions element
description: The minimum version of an application required to be installed on the system.
ms.assetid: 0F95D6AA-AC23-4928-9E97-57B46364CDED
keywords:
- RequiresAppVersions element Access Execution Engine
topic_type:
- apiref
api_name:
- RequiresTracing
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RequiresAppVersions element

The minimum version of an application required to be installed on the system.

The path to the installed application must exist in the registry under **HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\App Paths\\appName** as the default value for the registry key. It must be a **REG\_SZ** value type.

## Usage

``` syntax
<RequiresTracing>
  child elements
</RequiresTracing>
```

## Attributes

There are no attributes.

## Child elements



| Element                                     | Description                                                       |
|---------------------------------------------|-------------------------------------------------------------------|
| [**AppVersion**](appversion.md)<br/> | Contains the application name and version.<br/> <br/> |



### Child element sequence

``` syntax
AppVersion
```

## Parent elements



| Element                                     | Description                                            |
|---------------------------------------------|--------------------------------------------------------|
| [**Properties**](properties.md)<br/> | This node describes properties.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





