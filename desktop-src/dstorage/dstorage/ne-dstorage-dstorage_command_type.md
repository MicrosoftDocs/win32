---
UID: NE:dstorage.DSTORAGE_COMMAND_TYPE
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_COMMAND_TYPE
ms.date: 08/25/2022
targetos: Windows
description: Defines constants that specify the type of command that failed, as reported by [DSTORAGE_ERROR_FIRST_FAILURE](ns-dstorage-dstorage_error_first_failure.md).
prerelease: false
req.construct-type: enumeration
req.ddi-compliance: 
req.header: dstorage.h
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
 - dstorage.h
api_name:
 - DSTORAGE_COMMAND_TYPE
f1_keywords:
 - DSTORAGE_COMMAND_TYPE
 - dstorage/DSTORAGE_COMMAND_TYPE
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_COMMAND_TYPE
---

# DSTORAGE_COMMAND_TYPE enumeration (dstorage.h)

Defines constants that specify the type of command that failed, as reported by [DSTORAGE_ERROR_FIRST_FAILURE](ns-dstorage-dstorage_error_first_failure.md).

## Syntax

```cpp
enum DSTORAGE_COMMAND_TYPE {
  DSTORAGE_COMMAND_TYPE_NONE = -1,
  DSTORAGE_COMMAND_TYPE_REQUEST = 0,
  DSTORAGE_COMMAND_TYPE_STATUS = 1,
  DSTORAGE_COMMAND_TYPE_SIGNAL = 2,
  DSTORAGE_COMMAND_TYPE_EVENT = 3,
} ;
```

## Constants

| &nbsp; |
| -- |
| `DSTORAGE_COMMAND_TYPE_NONE`<br> Specifies no command type.|
| `DSTORAGE_COMMAND_TYPE_REQUEST`<br> Specifies a request command type.|
| `DSTORAGE_COMMAND_TYPE_STATUS`<br> Specifies a status command type.|
| `DSTORAGE_COMMAND_TYPE_SIGNAL`<br> Specifies a signal command type.|
| `DSTORAGE_COMMAND_TYPE_EVENT`<br> Specifies am event command type.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
