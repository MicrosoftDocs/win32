---
description: ICE79 validates the references to components and features entered in the database fields using the Condition data type.
ms.assetid: f0a8ceac-084a-4693-b27d-f610eec4702a
title: ICE79
ms.topic: article
ms.date: 05/31/2018
---

# ICE79

ICE79 validates the references to components and features entered in the database fields using the [Condition](condition.md) data type.

## Result

ICE79 posts two warnings.



| ICE79 warning                                                                      | Description                                                      |
|------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Database is missing \_Validation table. Could not completely check property names. | Database is missing [\_Validation table](-validation-table.md). |
| Error retrieving values from column \[2\] in table \[1\]. Skipping Column.         | Error retrieving value.                                          |



 

ICE79 posts two errors.



| ICE79 error                                                          | Description                               |
|----------------------------------------------------------------------|-------------------------------------------|
| Component '%ls' referenced in column '%s'.'%s' of row %s is invalid. | An invalid component reference was found. |
| Feature '%ls' referenced in column '%s'.'%s' of row %s is invalid.   | An invalid feature reference was found    |



 

## Example

ICE79 reports the following errors for the example:

``` syntax
Component 'NoSuchComponent' referenced in column 
'InstallExecuteSequence'.'Condition' of row Custom2 is invalid.
Feature 'NoSuchFeature' referenced in column 
'InstallExecuteSequence'.'Condition' of row Custom1 is invalid.
```

In this example, NoSuchComponent is absent from the [Component table](component-table.md) and NoSuchFeature is absent from the [Feature table](feature-table.md).

[InstallExecuteSequence Table](installexecutesequence-table.md) (partial)



| Action  | Condition                                |
|---------|------------------------------------------|
| Custom1 | TESTACTION=1046 AND &NoSuchFeature>2  |
| Custom2 | TESTACTION=146 AND $NoSuchComponent>2 |



 

To fix these errors, enter valid records for NoSuchFeature and NoSuchComponent in the Feature and Component tables.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



