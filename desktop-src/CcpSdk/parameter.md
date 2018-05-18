---
Description: 'Specifies the value to use for a parameter in the RunStep stage of a diagnostic test, on one node or on all of the nodes in the test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bc21c856-51e5-4c06-b747-d6ec85fa9cb2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Parameter element
---

# Parameter element

Specifies the value to use for a parameter in the RunStep stage of a diagnostic test, on one node or on all of the nodes in the test.

## Usage

``` syntax
<Parameter
  Name = "character_string"
  Value = "character_string"
  Format = "character_string"/>
```

## Attributes



| Attribute             | Type                         | Required       | Description                                                                                                                                                                                                                                                                                                                                        |
|-----------------------|------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**<br/> | character\_string<br/> | No<br/>  | Specifies that format that the diagnostic service should use when specifying the parameter and its value for the RunStep command. <br/> For this format string, {0} represents the parameter name and {1} represents the value that is specified for the parameter. The default value for this attribute is -{0}:{1}.<br/> <br/> |
| **Name**<br/>   | character\_string<br/> | Yes<br/> | Specifies the name of the parameter for which you want to specify a value.<br/> <br/>                                                                                                                                                                                                                                                  |
| **Value**<br/>  | character\_string<br/> | Yes<br/> | Specifies the value to use for the parameter for the RunStep stage. If the parameter is also defined in the XML that defines the test as a global parameter or as a RunStep-specific parameter, this value overrides any values that are specified in the test definition.<br/> <br/>                                                  |



## Child elements

There are no child elements.

## Parent elements



| Element                                                          | Description                                                                                                                                                            |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Parameters**](parameters--stepresult--element.md)<br/> | Represents a set of parameters that you want to set for the RunStep stage of a diagnostic test, on one node or on all of the nodes in the test.<br/> <br/> |



## Remarks

This element should appear in the StepResult XML only for the PreStep stage of a diagnostic test. This element should not appear in the StepResult XML for the RunStep and PostStep stages.

If the **Parameter** element is child element of a [**Parameters**](parameters--stepresult--element.md) element that is a child element of a [**Node**](node-element.md) element, the parameter value that the **Parameter** element specifies applies only to the node that corresponds to the **Node** element.

If the **Parameter** element is child element of a [**Parameters**](parameters--stepresult--element.md) element that is a child element of a [**StepResult**](stepresult-element.md) element, the parameter value that the **Parameter** element specifies applies to all of the nodes in the test.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**Parameters**](parameters--stepresult--element.md)
</dt> </dl>

 

 




