---
Description: 'Represents an environment variable that you want to set for the RunStep stage of a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e9041b71-28c9-44be-bae6-3e6ef2d0c094'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: EnvironmentVariable element
---

# EnvironmentVariable element

Represents an environment variable that you want to set for the RunStep stage of a diagnostic test.

## Usage

``` syntax
<EnvironmentVariable
  Name = "character_string"
  Value = "character_string"/>
```

## Attributes



| Attribute            | Type                         | Required       | Description                                                                                                                    |
|----------------------|------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------|
| **Name**<br/>  | character\_string<br/> | Yes<br/> | The name of the environment variable that you want to set for the RunStep stage of the diagnostic test.<br/> <br/> |
| **Value**<br/> | character\_string<br/> | No<br/>  | The value that you want to set for the environment variable.<br/> <br/>                                            |



## Child elements

There are no child elements.

## Parent elements



| Element                                               | Description                                                                                                                   |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**Environment**](environment-element.md)<br/> | Represents the environment variables that you want to set for the RunStep stage of a diagnostic test. <br/> <br/> |



## Remarks

This element should appear in the StepResult XML only for the PreStep stage of a diagnostic test. This element should not appear in the StepResult XML for the RunStep and PostStep stages.

If the PreStepResult.xml file and the test definition XML set the same environment variable, the value that is specified in the PreStepResult.xml file overrides the value that is set globally or set for the RunStep stage in the test definition XML file.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**Environment**](environment-element.md)
</dt> </dl>

 

 




