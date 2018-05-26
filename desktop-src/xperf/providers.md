---
title: providers
description: Displays the providers query options.
ms.assetid: de14fff1-1d86-4c11-b3d3-36ddccc5a45b
keywords:
- providers Windows Performance Analyzer
topic_type:
- apiref
api_name:
- providers
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# providers

Displays the providers query options.

``` syntax
xperf -providers [Installed|I] [Registered|R] [KernelFlags|KF] [KernelGroups|KG] [Kernel|K]
```

### Comments

This option queries all installed/known and registered providers, as well as all known kernel flags and groups.

The options in the following table are supported.



| Help option                  | Description                                                       |
|------------------------------|-------------------------------------------------------------------|
| I, Installed <br/>     | Include Installed/known providers.<br/>                     |
| R, Registered <br/>    | Include Registered providers.<br/>                          |
| KF, KernelFlags <br/>  | Include Kernel Flags.<br/>                                  |
| KG, KernelGroups <br/> | Include Kernel Groups.<br/>                                 |
| K, Kernel <br/>        | Include Kernel flags and groups; shortcut for "KF KG".<br/> |



 

If no options are specified, all providers are included in the output.

 

 





