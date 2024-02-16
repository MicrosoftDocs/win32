---
UID: NE:appxdatasource.RunOptions
title: RunOptions
description: Defines constants that specify options for the Run method.
ms.topic: reference
tech.root: appxdatasource
ms.date: 02/08/2024
targetos: Windows
prerelease: false
req.construct-type: enumeration
req.ddi-compliance: 
req.header: appxdatasource.h
req.include-header: 
req.kmdf-ver: 
req.max-support: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.typenames: 
req.umdf-ver: 
topic_type:
 - apiref
api_type:
 - HeaderDef
api_location:
 - appxdatasource.h
api_name:
 - RunOptions
f1_keywords:
 - RunOptions
 - appxdatasource/RunOptions
dev_langs:
 - c++
helpviewer_keywords:
 - RunOptions
---

# RunOptions enumeration

Defines constants that specify options for the [Run](./nf-appxdatasource-iappxstreamingdatasource4-run.md) method.

## Syntax

```cpp
typedef enum __MIDL_IAppxStreamingDataSource4_0001
{
  StageRequired = 0,
  StageDeferred = 1,
  StageRevalidate = 2,
  RunOptionsInvalid = 3
} RunOptions;
```

## Constants

| &nbsp; |
| -- |
| `StageRequired`<br> Start the stage request for the required launch chunk. |
| `StageDeferred`<br> Start the stage request for the post-launch chunk. |
| `StageRevalidate`<br> Start the stage request and re-validate all bits currently on disk. |
| `RunOptionsInvalid`<br> Specfies invalid run options. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | appxdatasource.h |
