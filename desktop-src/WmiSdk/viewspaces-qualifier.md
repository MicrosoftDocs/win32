---
description: The ViewSpaces qualifier defines the names and location of the namespaces where the source instances are located. You can specify any combination of namespaces on local or remote computers.
ms.assetid: 15d71bb6-842d-4f5a-b2e3-e9f60f0aea3b
ms.tgt_platform: multiple
title: ViewSpaces Qualifier
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ViewSpaces
api_type: 
- NA
api_location: 
---

# ViewSpaces Qualifier

The **ViewSpaces qualifier** defines the names and location of the namespaces where the source instances are located. You can specify any combination of namespaces on local or remote computers.

The following example lists two namespaces on the local computer.


```mof
ViewSpaces{"\\\\.\\root\\LocalNamespace",
     "\\\\.\\root\\RemoteNamespace"}
```



The [View provider](view-provider.md) matches the source queries in the [ViewSources qualifier](viewsources-qualifier.md) to the namespaces listed in the **ViewSpaces** qualifier in the order the queries and namespaces are listed. Normally, there is a one-to-one relationship between the number of namespaces listed in the **ViewSpaces** qualifier and the queries listed in the **ViewSources** qualifier. In some cases, you may want the queries listed in the ViewSources qualifier to execute against two or more namespaces. You can use a double colon "::" to separate multiple namespaces that will be evaluated by one of the queries in the **ViewSources** array.

In the following example, the first query in the [**ViewSources**](viewsources-qualifier.md) array will be run against the namespace in the first pair of quotes, the second query against the three namespaces in the second pair of quotes, and the third query against the two namespaces in the third pair of quotes.


```mof
ViewSpaces
    {
    "\\\\.\\root\\LocalNamespace",

    "\\\\.\\root\\RemoteNamespace1::
        \\\\.\\root\\RemoteNamespace2::
        \\\\.\\root\\RemoteNamespace3",

    "\\\\.\\root\\RemoteNamespace1::
        \\\\.\\root\\RemoteNamespace3"
    }
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**Qualifiers Specific to the View Provider**](qualifiers-specific-to-the-view-provider.md)
</dt> </dl>

 

 




