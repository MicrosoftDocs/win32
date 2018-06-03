---
title: AppVersion element
description: Contains the application name and version.
ms.assetid: 2613E81E-201C-4E91-9E97-E18163C12EED
keywords:
- AppVersion element Access Execution Engine
topic_type:
- apiref
api_name:
- AppVersion
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AppVersion element

Contains the application name and version.

## Usage

``` syntax
<AppVersion>
  child elements
</AppVersion>
```

## Attributes

There are no attributes.

## Child elements



| Element                               | Description                                                                                                                   |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**App**](app.md)<br/>         | The name of the application that undergoes the version check.<br/> <br/>                                          |
| [**Version**](version.md)<br/> | The version node has four mandatory sub nodes making up a standard Microsoft four part version number.<br/> <br/> |



### Child element sequence

``` syntax
AppVersion
```

## Parent elements



| Element                                                       | Description                                                                                          |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**RequiresAppVersions**](requiresappversions.md)<br/> | The minimum version of an application required to be installed on the system.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





