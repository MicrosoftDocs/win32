---
title: Collection Object Properties
description: A collection provides a set of objects over which iteration can be performed.
ms.assetid: '592dd7dc-c45f-4827-8e08-039756d0efd5'
---

# Collection Object Properties

A collection provides a set of objects over which iteration can be performed. All collection objects must provide the following properties:



| Property name | Return type  | Description                                                                                                                          |
|---------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Count**     | VT\_I4       | Returns the number of items in the collection; read only. Required.                                                                  |
| **\_NewEnum** | VT\_DISPATCH | A special property that returns an enumerator object that implements [IEnumVARIANT](139E3C93-FAEF-4003-9079-E0E94494DB3E). Required. |



 

 

 




