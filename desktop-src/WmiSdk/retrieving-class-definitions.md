---
description: Schema queries are WQL statements that request class definitions and information about schema associations.
ms.assetid: cb65e99f-9046-4c63-ab56-60dedc45bcef
ms.tgt_platform: multiple
title: Retrieving Class Definitions
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Class Definitions

Schema queries are WQL statements that request class definitions and information about [schema associations](schema-associations.md). Class providers use schema queries in their instances of the [**\_\_ClassProviderRegistration**](--classproviderregistration.md) class to specify the classes that they support when they register with WMI. Schema queries are placed in the **ResultSetQueries**, **ReferencedSetQueries**, and **UnsupportedQueries** properties of the **\_\_ClassProviderRegistration** instance.

Schema queries are similar to data queries in that they support the following WQL statements:

-   [SELECT](select-statement-for-schema-queries.md)
-   [ASSOCIATORS OF](schema-associations.md)
-   [REFERENCES OF](schema-associations.md)
-   [ISA](isa-operator-for-schema-queries.md)

A schema query is similar to a [REFERENCES OF](references-of-statement.md) data query that specifies the **ClassDefsOnly** keyword; in other words, that returns a result set of class definition objects rather than actual instances of association classes. However, REFERENCES OF returns class definitions only if there are instances present. A schema query returns class definitions whether or not instances are present.

 

 



