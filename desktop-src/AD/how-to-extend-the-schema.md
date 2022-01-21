---
title: How to Extend the Schema
description: When the existing classes and/or attributes do not fit with the type of data that you want to store, you might want to extend the schema.
ms.assetid: 9a80ce29-8ff0-4324-8a2f-afd6c5d2272e
ms.tgt_platform: multiple
keywords:
- Schema AD , How to Extend
- Active Directory, Using, Schema
- Active Directory, Using, Schema, Extending the Schema, How to Extend
ms.topic: article
ms.date: 05/31/2018
---

# How to Extend the Schema

When the existing classes and/or attributes do not fit with the type of data that you want to store, you might want to extend the schema. For more information on deciding when to extend the schema, see [Extending the Schema](extending-the-schema.md). When you have decided that schema extension is required, use the following procedure to extend the schema.

## Verify Active Directory functionality before you apply any schema extensions

Verify Active Directory functionality before you update the schema to help ensure that the schema extension proceeds without error. At a minimum, ensure that all domain controllers for the forest are online and performing inbound replication.

**To verify Active Directory functionality before you apply the schema extension**

1.  Log on to an administrative workstation that has the Windows Support Tool Repadmin.exe installed.
    > [!Note]  
    > The Support Tools are located on the operating system installation media in the Support\\Tools folder.

     

2.  Open a command prompt, and then change directories to the folder in which the Windows Support Tools are installed.
3.  At a command prompt, type the following, and then press ENTER:

    ``` syntax
    repadmin /replsum /bysrc /bydest /sort:delta
    ```

    All domain controllers should show 0 in the Fails column, and the largest deltas (which indicate the number of changes that have been made to the Active Directory database since the last successful replication) should be less than or roughly equal to the replication frequency of the site link that is used by the domain controller for replication. The default replication frequency is 180 minutes.

    For more information about additional steps that you can take to verify Active Directory functionality before you apply the schema extension, see [article 325379 in the Microsoft Knowledge Base](https://support.microsoft.com/kb/325379).

**To Extend the Schema**

1.  Determine the method of extension. Once you have carefully designed your schema changes, the next step is to decide which method to use to extend the schema. You can use one of the following methods:
    -   Manually, using import files. See the documentation [Using the LDIFDE Tool](/previous-versions/office/developer/exchange-server-2003/ms870068(v=exchg.65)).
        > [!Note]  
        > Do not use LDIFDE to import Windows Sch\*.ldf files. Those files are required to extend the Active Directory schema in order to install domain controllers that run a newer version of Windows Server than the version that is running on the current schema master. When you need to extend the schema in order to install a new domain controller, use Adprep.exe.

         

    -   Programmatically, using an installation program. For more information, see [Programmatic Extension](programmatic-extension.md)
2.  Enable Schema Changes. For more information, see [Prerequisites for Installing a Schema Extension](prerequisites-for-installing-a-schema-extension.md) and [Enabling Schema Changes at the Schema Master](enabling-schema-changes-at-the-schema-master.md).
3.  Obtain an Object Identifier (OID) for your new attributes and/or classes, as described in [Obtaining an Object Identifier](obtaining-an-object-identifier.md).
4.  Create new attributes and classes.
5.  Use display specifiers to integrate new attributes and classes with the user interface, if necessary.
6.  Update the schema cache as described in [Updating the Schema Cache](updating-the-schema-cache.md).
7.  Verify the schema extension using LDP.exe.

## Related topics

<dl> <dt>

[Obtaining an Object Identifier](obtaining-an-object-identifier.md)
</dt> <dt>

[How To Use the Directory Service Command-Line Tools to Manage Active Directory Objects in Windows Server 2003](https://support.microsoft.com/topic/03164adb-9771-220a-6bf4-c2ea335d9ea8)
</dt> <dt>

[Using the LDIFDE Tool](/previous-versions/office/developer/exchange-server-2003/ms870068(v=exchg.65))
</dt> <dt>

[Extending the Active Directory Schema](/previous-versions/ms806972(v=msdn.10))
</dt> <dt>

[Restrictions on Schema Extension](restrictions-on-schema-extension.md)
</dt> </dl>

 

 
