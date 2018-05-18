---
title: ShellExecuteVerb element
description: A verb as described by the documentation for the shell execute API.
ms.assetid: '7A7DEAD1-4469-4DD1-BB44-B7359DFA8BAE'
keywords: ["ShellExecuteVerb element Access Execution Engine"]
topic_type:
- apiref
api_name:
- ShellExecuteVerb
api_type:
- Schema
---

# ShellExecuteVerb element

A verb as described by the documentation for the shell execute API.

## Usage

``` syntax
<ShellExecuteVerb>
  text
</ShellExecuteVerb>
```

## Attributes

There are no attributes.

## Text value

A verb as described by the documentation for the shell execute API.

## Child elements

There are no child elements.

## Parent elements



| Element                                         |
|-------------------------------------------------|
| [**ShellExecute**](shellexecute.md)<br/> |



## Remarks

This tag must contain a verb as described by the documentation for the shell execute API. Note that AXE cannot verify this as verb’s depend upon the target file. If the assessment author use an incorrect verb then AXE’s call to shell execute will fail. AXE will then report the error information using the regular AXE error reporting mechanisms (ETW and errors in results.xml).

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





