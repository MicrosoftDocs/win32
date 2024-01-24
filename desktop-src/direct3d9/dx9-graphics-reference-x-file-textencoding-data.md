---
description: Data objects contain the actual data or a reference to that data. Each data object has a corresponding template that specifies the data type. The following sections discuss the form and parts of data objects.
ms.assetid: 61dbe241-2658-4dd0-af89-3db204b56fad
title: Data (X file format, text encoding)
ms.topic: article
ms.date: 05/31/2018
---

# Data (X file format, text encoding)

Data objects contain the actual data or a reference to that data. Each data object has a corresponding template that specifies the data type. The following sections discuss the form and parts of data objects.

## Form, Identifier, and Name

Data objects have the following form.


```
        <Identifier> [name] { [<UUID>]
    <member 1>;
...
    <member n>;
}
```



The identifier is compulsory and must match a previously defined data type or primitive. However, the name is optional.

## Data Members

Data members can be one of the following: data object, data reference, integer list, float list, or string list.

A data object is a nested data object. This enables the hierarchical nature of the file format to be expressed. The types of nested data objects allowed in the hierarchy may be restricted.

A data reference is a reference to a previously encountered data object as shown in the following example.


```
{
  name |
  UUID |
  name UUID
}
```



An integer list is a semicolon-separated list of integers, as shown in the following example.


```
1; 2; 3;
```



A float list is a semicolon-separated list of floats, as shown in the following example.


```
1.0; 2.0; 3.0;
```



A string list is a semicolon-separated list of strings, as shown in the following example.


```
"Moose"; "Goats"; "Sheep";
```



## Related topics

<dl> <dt>

[Text Encoding](text-encoding.md)
</dt> </dl>

 

 



