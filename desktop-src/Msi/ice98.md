---
description: ICE98 verifies the description field of the ODBCDataSource Table for an ODBC data source. It uses the SQLValidDSN function to check that only valid characters are used, and that the description does not exceed the maximum allowed length.
ms.assetid: ed78db96-10a1-4e42-9147-2309c9ca9c6e
title: ICE98
ms.topic: article
ms.date: 05/31/2018
---

# ICE98

ICE98 verifies the description field of the [ODBCDataSource Table](odbcdatasource-table.md) for an ODBC data source. It uses the **SQLValidDSN** function to check that only valid characters are used, and that the description does not exceed the maximum allowed length.

## Result

ICE98 posts the following warnings.



| ICE98 warning                    | Description                                                                                                                                                                                                 |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The data source name is invalid. | The value in the Description column of the [ODBCDataSource Table](odbcdatasource-table.md) either contains invalid characters or is too long, which means that it exceeds the SQL\_MAX\_DSN\_LENGTH of 32. |



 

## Example

ICE98 reports the following warnings for the example:

``` syntax
The data source name is invalid: !
The data source name is invalid: <String of length > 32>
```

[ODBCDataSource Table](odbcdatasource-table.md) (partial)



| DataSource | Description                      |
|------------|----------------------------------|
| BadChar    | !                                |
| TooLong    | <String of length > 32> |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> <dt>

[ODBCDataSource Table](odbcdatasource-table.md)
</dt> </dl>

 

 



