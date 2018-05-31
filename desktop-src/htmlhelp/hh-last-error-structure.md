---
title: HH\_LAST\_ERROR structure
description: This structure returns the last HtmlHelp() error code and description.
ms.assetid: A22A642C-213B-4732-8E4F-A5E20455B79F
keywords:
- HH_LAST_ERROR structure HTML Help Workshop
topic_type:
- apiref
api_name:
- HH_LAST_ERROR
api_location:
- HHError.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# HH\_LAST\_ERROR structure

This structure returns the last **HtmlHelp()** error code and description.

## Syntax


```C++
typedef struct tagHH_LAST_ERROR {
  int     cbStruct;
  HRESULT hr;
  BSTR    description;
} HH_LAST_ERROR;
```



## Members

<dl> <dt>

**cbStruct**
</dt> <dd>

Specifies the size of the structure. This value must always be filled in before passing the structure to **HtmlHelp()**.

</dd> <dt>

**hr**
</dt> <dd>

Specifies the last error code.

</dd> <dt>

**description**
</dt> <dd>

Specifies a Unicode string containing a description of the error.

</dd> </dl>

## Used by

-   [HH\_GET\_LAST\_ERROR](hh-get-last-error-command.md)

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>HHError.h</dt> </dl> |



## See also

<dl> <dt>

[About Structures](about-structures.md)
</dt> </dl>

 

 





