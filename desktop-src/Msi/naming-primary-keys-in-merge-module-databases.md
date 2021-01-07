---
description: The names of primary keys a merge module database must adhere to a standard naming convention.
ms.assetid: 72822c25-cd21-454b-ab49-846474b55ef1
title: Naming Primary Keys in Merge Module Databases
ms.topic: article
ms.date: 05/31/2018
---

# Naming Primary Keys in Merge Module Databases

The names of primary keys a merge module database must adhere to a standard naming convention. The purpose of this naming convention is to reduce the possibility of creating a name conflict between the table columns in the merge module and the target installation package. The naming convention cannot be applied to tables in which the primary key is installable data. Do not apply the naming convention to the following tables:

-   [MIME Table](mime-table.md)
-   [Extension Table](extension-table.md)
-   [Icon Table](icon-table.md)
-   [Verb Table](verb-table.md)
-   [ProgId Table](progid-table.md)

For example, do not use for the primary key of the MIME table because this is the MIME type and applying the naming procedure would change its meaning. In these cases, name conflicts depend on the meaning of the data being unique across modules.

The name of a primary key in a merge module must consist of a readable name appended with a string made from the merge module's GUID. Every merge module must have its own [*GUID*](g-gly.md). The merge module's GUID should also be authored into the [**Revision Number Summary**](revision-number-summary.md) property of the merge module. Developers can create GUIDs using a utility such as GUIDGEN.

The following procedure describes how to generate a primary database key that adheres to the standard naming convention. Apply the following procedure only to tables where the primary key is not data being installed.

**To name a primary key of a table record in a merge module**

1.  Author the readable part of the name for the primary key. Pick a readable name that identifies this record, for example, MyRowEntry.
2.  Generate or obtain the GUID of the merge module. Note that all GUIDs must be authored in uppercase. For more information about GUIDs, see [GUID](guid.md). The following is an example of a GUID: {880DE2F0-CDD8-11D1-A849-006097ABDE17}. In the following steps you modify this into a character string that must be appended to every primary key name in the merge module.
3.  Remove the curly braces from the beginning and end of the GUID.
4.  Change all the dashes to underscores.
5.  Append the result to the end of the readable part of the primary key name. Separate the readable name from the modified GUID by a period. The primary key name for the example GUID given above becomes MyRowEntry.880DE2F0\_CDD8\_11D1\_A849\_006097ABDE17.
6.  Repeat to name all the primary keys of all tables in the merge module.

 

 



