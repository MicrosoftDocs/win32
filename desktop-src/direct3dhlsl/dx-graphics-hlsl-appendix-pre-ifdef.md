---
title: ' ifdef and  ifndef Directives'
description: Preprocessor directives that determine whether a specific preprocessor constant or macro is defined.
ms.assetid: c1cc2e1d-2599-45ec-9629-56c4b42e0d0e
keywords:
- ifdef and ifndef Directives HLSL
topic_type:
- apiref
api_name:
- ifdef and ifndef Directives
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# \#ifdef and \#ifndef Directives

Preprocessor directives that determine whether a specific preprocessor constant or macro is defined.



| \#ifdef *identifier* ...  |
|---------------------------|
| \#endif                   |
| \#ifndef *identifier* ... |
| \#endif                   |



 

## Parameters



| Item                                                                              | Description                                               |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------|
| <span id="identifier"></span><span id="IDENTIFIER"></span>*identifier*<br/> | Identifier of the constant or macro to check. <br/> |



 

## Remarks

You can use the \#ifdef and \#ifndef directives anywhere that the [\#if](dx-graphics-hlsl-appendix-pre-if.md) can be used. The \#ifdef statement is equivalent to ) directive. These directives check only for the presence or absence of identifiers defined using the [\#define](dx-graphics-hlsl-appendix-pre-define.md) directive, not for identifiers declared in the C or C++ source code.

These directives are provided only for compatibility with previous versions of the language. The use of the [defined](dx-graphics-hlsl-appendix-pre-if.md) operator with the \#if directive is preferred.

The \#ifndef directive checks for the opposite of the condition checked by \#ifdef. If the identifier is not defined, the condition is true (nonzero); otherwise, the condition is false (zero).

## Examples

The identifier can be passed from the command line using the /D option. Up to 30 macros can be specified with /D. This is useful for checking whether a definition exists, because a definition can be passed from the command line. The following example uses this behavior to determine whether to run an application in test mode.


```
// PROG.CPP
#ifndef test
  #define final
#endif
int main()
{
}
```



When compiled using the following command, prog.cpp will compile in test mode; otherwise, it will compile in final mode.


```
CL.EXE /Dtest prog.cpp
```



## See also

<dl> <dt>

[Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)
</dt> <dt>

[\#if, )](dx-graphics-hlsl-appendix-pre-if.md)
</dt> </dl>

 

 





