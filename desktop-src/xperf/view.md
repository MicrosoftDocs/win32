---
title: view
description: Displays help for xperfview, which is used to explore performance traces visually.
ms.assetid: 6a3fa9a3-2326-41c1-b331-152e0c91cb28
keywords:
- view Windows Performance Analyzer
topic_type:
- apiref
api_name:
- view
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# view

Displays help for **xperfview**, which is used to explore performance traces visually.

``` syntax
xperfview [-i] trace.etl ... [-tti] [-h | /?]
```

## Parameters

<dl> <dt>

<span id="_______-tti______"></span><span id="_______-TTI______"></span> **-tti** 
</dt> <dd>

Process the trace even in the presence of time inversions

</dd> <dt>

<span id="_______-h__________"></span><span id="_______-H__________"></span> **-h**, **/?** 
</dt> <dd>

Help message

</dd> </dl>

### Comments

Xperf automatically forwards compatible command lines to Xperfview if they start with trace paths.

 

 




