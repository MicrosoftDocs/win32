---
description: Data queries are WQL statements that request instances of classes. To issue a data query, applications call the IWbemServices::ExecQuery or IWbemServices::ExecQueryAsync method.
ms.assetid: a8b9bf2f-300d-4570-8b30-7532f3421d39
ms.tgt_platform: multiple
title: Requesting Class Instance Data
ms.topic: article
ms.date: 05/31/2018
---

# Requesting Class Instance Data

Data queries are WQL statements that request instances of classes. To issue a data query, applications call the [**IWbemServices::ExecQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execquery) or [**IWbemServices::ExecQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execqueryasync) method.

The following statements are used to make data queries:

-   [SELECT](select-statement-for-data-queries.md)
-   [ASSOCIATORS OF](associators-of-statement.md)
-   [REFERENCES OF](references-of-statement.md)
-   [ISA](isa-operator-for-data-queries.md)

The WQL SELECT statement is the standard Structured Query Language (SQL) statement for retrieving information, with a few restrictions and extensions specific to WQL. Although the SQL SELECT statement is typically used in the database environment to retrieve particular columns from tables, the WQL SELECT statement is used in WMI to retrieve instances of a single class. WQL does not support queries across multiple classes.

The ASSOCIATORS OF and REFERENCES OF statements are specific to WQL and are not part of standard SQL. The ASSOCIATORS OF statement retrieves all class instances that are associated with a particular source class instance, and REFERENCES OF retrieves all instances that refer to a particular source instance. Associations are represented by instances of an [association class](declaring-an-association-class.md).

 

 



