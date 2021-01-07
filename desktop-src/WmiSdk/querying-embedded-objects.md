---
description: You have several options as to the form a query takes when querying an event class that contains embedded objects. The results returned by the query vary, depending on the form of the query you use.
ms.assetid: b959a695-be15-4aa7-9368-b840962ae0da
ms.tgt_platform: multiple
title: Querying Embedded Objects
ms.topic: article
ms.date: 05/31/2018
---

# Querying Embedded Objects

You have several options as to the form a query takes when querying an event class that contains embedded objects. The results returned by the query vary, depending on the form of the query you use.

## Class Definitions

The following example shows the class definitions that are used for the WQL queries in this topic.

``` syntax
class MyClass
{
   string Prop1;
   string Prop2;
};

class MyEvent : __ExtrinsicEvent
{
   MyClass E1;
   MyClass E2;
};
```

## Examples

The following query returns both embedded classes, **E1** and **E2**, each having **Prop1** and **Prop2** populated with data.

`SELECT * FROM MyEvent`

The following query returns the **E1** embedded object, but with neither **Prop1** nor **Prop2** populated with data.

`SELECT E1 FROM MyEvent`

The following query returns the embedded class **E1** with only **Prop1** populated with data.

`SELECT E1.Prop1 FROM MyEvent`

The following query returns both embedded classes, **E1** and **E2**, each having **Prop1** and **Prop2** populated with data.

`ELECT E1.Prop1, E1.Prop2, E2.Prop1, E2.Prop2 FROM MyEvent`

This is equivalent to the first query using the asterisk (\*) instead of specifying each object and property.

## Related topics

<dl> <dt>

[Querying with WQL](querying-with-wql.md)
</dt> </dl>

 

 



