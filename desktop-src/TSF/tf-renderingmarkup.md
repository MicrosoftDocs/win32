---
title: TF_RENDERINGMARKUP structure
description: The TF\_RENDERINGMARKUP structure structure contains a range and the display attribute information.
ms.assetid: 206e679b-f2eb-4f28-ac2a-58f3c222a020
keywords:
- TF_RENDERINGMARKUP structure Text Services Framework
topic_type:
- apiref
api_name:
- TF_RENDERINGMARKUP
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TF\_RENDERINGMARKUP structure

The [**TF\_RENDERINGMARKUP**](/windows/desktop/api/Msctf/ns-msctf-tf_da_color) structure structure contains a range and the display attribute information.

## Syntax


```C++
typedef struct {
  ITfRange*           pRange;
  TF_DISPLAYATTRIBUTE tfDisplayAttr;
} TF_RENDERINGMARKUP;
```



## Members

<dl> <dt>

**pRange**
</dt> <dd>

A pointer to an [ITfRange](/windows/desktop/api/Msctf/nn-msctf-itfrange) interface.

</dd> <dt>

**tfDisplayAttr**
</dt> <dd>

Display attribute information.

</dd> </dl>

## Remarks

This structure is not currently in the public header files. To use this API, you must MIDL-compile the [prototype](prototypes.md).

 

 




