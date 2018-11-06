---
title: Porting IRIS GL Get Functions
description: IRIS GL \ 0034;get \ 0034; functions take the following form
ms.assetid: 5bd6aa13-b41d-4f89-91dc-cc47481ac7b7
keywords:
- IRIS GL porting,get functions
- porting from IRIS GL,get functions
- porting to OpenGL from IRIS GL,get functions
- OpenGL porting from IRIS GL,get functions
ms.topic: article
ms.date: 05/31/2018
---

# Porting IRIS GL Get Functions

IRIS GL "get" functions take the following form:

``` syntax
int getthing();
```

and

``` syntax
int getthings( int *a, int *b);
```

Your IRIS GL code probably includes get function calls that look something like:

``` syntax
thing = getthing(); 
if (getthing() == THING) { /* some stuff here */ } 
getthings (&a, &b);
```

In OpenGL you use one of the following four types of [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) functions in place of equivalent IRIS GL get functions:

-   **glGetBooleanv**
-   **glGetIntegerv**
-   **glGetFloatv**
-   **glGetDoublev**

The functions have the following syntax:

``` syntax
glGet<Datatype>v( value, *data );
```

where *value* is of type **GLenum** and data is of type **GLdatatype**. When you call **glGet** and it returns a type different from the type expected, the type is converted appropriately. For a complete list of **glGet** parameters, see [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md).

 

 




