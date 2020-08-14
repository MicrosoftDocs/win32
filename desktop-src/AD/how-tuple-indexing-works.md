---
title: How Tuple Indexing Works
description: Tuple indices are used to optimize searches that have 0 or more medial-search strings and 0 or 1 final-search strings. They can also be used to optimize searches for an initial search string if no ordinary index is available over that attribute.
ms.assetid: 0f7b3f64-70cd-4581-a9ab-bb882eabef8c
ms.tgt_platform: multiple
keywords:
- tuple indexing
- Searching Active Directory Active Directory , optimization
- Active Directory, search optimization Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# How Tuple Indexing Works

Tuple indices are used to optimize searches that have 0 or more [medial-search strings](search-string-types.md) and 0 or 1 final-search strings. They can also be used to optimize searches for an initial search string if no ordinary index is available over that attribute.

You can turn on tuple indexing for an attribute by setting bit 5, which corresponds to the value 32, in the [**searchFlags**](/windows/desktop/ADSchema/a-searchflags) attribute. This attribute is set in the schema object that represents the attribute that needs the tuple index. The performance impact of turning on tuple indexing is that any string value that is set for that attribute will be expanded into a large number of fragments in the tuple index. When an attribute expands, it consumes a larger amount of disk space in the Directory Information Tree file, and also gets updated more slowly.

Tuple indices are designed to accelerate searches of the form `*string*`. The acceleration can be considerable because this form of search cannot be optimized in any other way, and in its un-optimized form, it forces the Active Directory server to walk every object in the scope of the search to perform the query. Thus, a base search would just search one object, which would use fewer resources, an immediate children search would search just the children of an object (which could use fewer resources or more resources depending on the container size), and a subtree search will walk the entire subtree under the base object, which would usually require a lot of resources and be very slow because of the subtree size.

Tuple indices work by breaking a string into *tuples*. For example, the string "Active Directory" would be broken into the following tuples:

-   ` "Active Dir"`
-   ` "ctive Dire"`
-   ` "tive Direc"`
-   ` "ive Direct"`
-   ` "ve Directo"`
-   ` "e Director"`
-   ` " Directory"`
-   ` "Directory"`
-   ` "irectory"`
-   ` "rectory"`
-   ` "ectory"`
-   ` "ctory"`
-   ` "tory"`
-   ` "ory"`

> [!Note]  
> The directory will stop at 32767 characters when expanding a string for tuple indexing.

 

A tuple index would contain an entry for each one of these tuples. So, if a user searches for `*cto*`, then the Active Directory server will look up all the matches for "cto" in the index and, in this case, find a pointer back to the record that had a (tuple indexed) attribute with a value of "Directory".

If the medial search string (`*cto*` in the previous example) is specific enough, then the search will be quite efficient because it greatly reduces the number of objects that the Active Directory server must inspect to perform the query.

 

 