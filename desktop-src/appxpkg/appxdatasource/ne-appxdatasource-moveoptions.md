---
UID: NE:appxdatasource.MoveOptions
title: MoveOptions
description: Defines constants that specify options for the Move method.
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
 - MoveOptions
f1_keywords:
 - MoveOptions
 - appxdatasource/MoveOptions
dev_langs:
 - c++
helpviewer_keywords:
 - MoveOptions
---

# MoveOptions enumeration

Defines constants that specify options for the [Move](./nf-appxdatasource-iappxstreamingdatasource4-move.md) method.

## Syntax

```cpp
typedef enum __MIDL_IAppxStreamingDataSource4_0002
{
  BeginMove = 0,
  EndMove = 1,
  RollbackMove = 2,
  MoveOptionsInvalid = 3
} MoveOptions;
```

## Constants

| &nbsp; |
| -- |
| `BeginMove`<br> Begin the move operation from the source to the target volume. |
| `EndMove`<br> End the move operation from the source to the target volume (for example, delete source files). |
| `RollbackMove`<br> Abort the move operation, and restore files to the source volume. |
| `MoveOptionsInvalid`<br> Specfies invalid move options. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | appxdatasource.h |
