---
Description: 'Represents the environment variables that you want to set for the RunStep stage of a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '52b2b257-20b8-4ea2-90fb-653f95cb6c22'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Environment element
---

# Environment element

Represents the environment variables that you want to set for the RunStep stage of a diagnostic test.

## Usage

``` syntax
<Environment>
  child elements
</Environment>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                      | Description                                                                                                                |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**EnvironmentVariable**](envionmentvariable.md)<br/> | Represents an environment variable that you want to set for the RunStep stage of a diagnostic test.<br/> <br/> |



### Child element sequence

``` syntax
EnvironmentVariable*
```

## Parent elements



| Element                                             | Description                                                                                                                           |
|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**StepResult**](stepresult-element.md)<br/> | Represents the result of a stage in a diagnostic test and serves as the root element of a StepResult XML file.<br/> <br/> |



## Remarks

This element should contain child elements only for the PreStep stage of a diagnostic test. This element should not contain child elements for the RunStep and PostStep stages.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**StepResult**](stepresult-element.md)
</dt> </dl>

 

 




