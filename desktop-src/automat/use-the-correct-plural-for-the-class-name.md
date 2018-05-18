---
title: Use the Correct Plural for the Class Name
description: Collection classes should use the correct plural for the class name.
ms.assetid: 'e2f9284f-56b1-4af6-8dfe-9f059e78e5f5'
---

# Use the Correct Plural for the Class Name

Collection classes should use the correct plural for the class name. For example, if you have a class named Axis, store the collection of Axis objects in an Axes class. Similarly, a collection of Vertex objects should be stored in a Vertices class. In cases where English uses the same word for the plural, append the word "Collection."



| Use              | Don't use        |
|------------------|------------------|
| Axes             | Axiss            |
| SeriesCollection | CollectionSeries |
| Windows          | ColWindow        |



 

Using plurals rather than inventing new names for collections reduces the number of items a user must remember, and simplifies the selection of names for collections.

For some collections, however, this may not be appropriate, especially where a set of objects exists independently of the collection. For example, a Mail program might have a Name object that exists in several collections, such as ToList, CCList, and GroupList. In this case, you might specify the individual name collections as ToNames, CCNames, and GroupNames.

 

 




