---
Description: 'Represents a table in the report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'df5fd98a-5b48-4fa3-b880-af3f1ba9ddf4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Table element
---

# Table element

Represents a table in the report for a diagnostic test.

## Usage

``` syntax
<Table
  Description = "character_string"
  Name = "character_string"
  Tags = "character_string">
  child elements
</Table>
```

## Attributes



| Attribute                  | Type                         | Required       | Description                                                                                                                       |
|----------------------------|------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Description**<br/> | character\_string<br/> | No<br/>  | Specifies a description of the table. The description is typically displayed before the table in a report.<br/> <br/> |
| **Name**<br/>        | character\_string<br/> | Yes<br/> | Specifies a name for the table. The name is typically used as a heading before the table in a report.<br/> <br/>      |
| **Tags**<br/>        | character\_string<br/> | No<br/>  | Specifies tags for the table.<br/> <br/>                                                                              |



## Child elements



| Element                               | Description                                                                                          |
|---------------------------------------|------------------------------------------------------------------------------------------------------|
| [**Columns**](columns.md)<br/> | Represents the set of columns in a table in the report for a diagnostic test.<br/> <br/> |
| [**Rows**](rows.md)<br/>       | Represents the set of rows in a table in the report for a diagnostic test.<br/> <br/>    |



### Child element sequence

``` syntax
Columns+Rows*
```

## Parent elements



| Element                                     | Description                                                                               |
|---------------------------------------------|-------------------------------------------------------------------------------------------|
| [**Tables**](tables-element.md)<br/> | Represents the set of tables in the report for a diagnostic test. <br/> <br/> |



## Remarks

This element should appear in the StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not appear in the StepResult XML for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[**Tables**](tables-element.md)
</dt> </dl>

 

 




