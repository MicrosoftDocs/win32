---
title: Batched Statements
description: Batched Statements
ms.assetid: '0e4c61e3-8a0d-465c-8e2b-fc7c84c8635e'
---

# Batched Statements

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Batched statements allow you to set and execute SQL statements, optionally separated by semicolons ( ; ), as one command. You can batch [SET statements](set-statement.md) with [CREATE VIEW statements](create-view-statement.md) and, optionally, with a single following [SELECT statement](select-statement.md).

``` syntax
SET_Statement | CREATE_VIEW_Statement
[ [;]  SET_Statement | CREATE_VIEW_Statement ] ...
[ SELECT_Statement ]
```

### Parameters

<dl> <dt>

<span id="SET_Statement"></span><span id="set_statement"></span><span id="SET_STATEMENT"></span>*SET\_Statement*
</dt> <dd>

For details about *SET\_Statement*, see [SET Statement](set-statement.md).

</dd> <dt>

<span id="CREATE_VIEW_Statement"></span><span id="create_view_statement"></span><span id="CREATE_VIEW_STATEMENT"></span>*CREATE\_VIEW\_Statement*
</dt> <dd>

For details about *CREATE\_VIEW\_Statement*, see [CREATE VIEW Statement](create-view-statement.md).

</dd> <dt>

<span id="SELECT_Statement"></span><span id="select_statement"></span><span id="SELECT_STATEMENT"></span>*SELECT\_Statement*
</dt> <dd>

For details about *SELECT\_Statement*, see [SELECT Statement](select-statement.md).

</dd> </dl>

### Remarks

The duration of batched **SET** and **CREATE VIEW** statements is the length of the session with Indexing Service.

If included, a **SELECT** statement must appear as the last item in the batch.

### Example

The following example represents a batched **SET**, **CREATE VIEW**, and **SELECT** statement.


```
SET PROPERTYNAME 'D5CDD502-2E9C-101B-9397-08002B2CF9AE'
    PROPID 14 AS MyProperty
    TYPE DBTYPE_STR;
CREATE VIEW #MyView AS
    SELECT FileName, MyProperty
        FROM SCOPE('"/CheckIn"');
SELECT * FROM #MyView
```



## Related topics

<dl> <dt>

[CREATE VIEW Statement](create-view-statement.md)
</dt> <dt>

[SELECT Statement](select-statement.md)
</dt> <dt>

[SET Statement](set-statement.md)
</dt> </dl>

 

 




