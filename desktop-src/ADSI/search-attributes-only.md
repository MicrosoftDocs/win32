---
title: Search Attributes Only
description: Sometimes you perform a search to determine what type of data is available for an object.
ms.assetid: 97eccea6-6a2b-4785-afd8-4af3dc7bd657
ms.tgt_platform: multiple
keywords:
- Search Attributes Only ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Search Attributes Only

Sometimes you perform a search to determine what type of data is available for an object. In this case, you are interested only in the attributes, and not the values, of the object. To accomplish this, you set the "search attributes only" option. Specifying this option returns the attribute names without their values. However, the result set includes only those attributes that have values assigned. For example, consider an object with the following attributes:

``` syntax
First Name = Jeff
Last Name = Smith
Department = <Empty>
Phone Number = (425) 432-3442
```

When the search attributes only option is set, the result set includes:

``` syntax
First Name
Last Name
Phone Number
```

For more information about using the search attributes only option with a specific search interface, see:

-   [Returning Only Attribute Names with IDirectorySearch](returning-only-attribute-names-with-idirectorysearch.md)
-   [Searching with ActiveX Data Objects](searching-with-activex-data-objects-ado.md)
-   [Searching with OLE DB](searching-with-ole-db.md)

 

 




