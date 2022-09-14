---
title: Disabling Existing Classes and Attributes
description: Schema additions are permanent.
ms.assetid: 13ffd2f5-cf1d-4cde-a3d5-74cb5a44b6fc
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Disabling Existing Classes and Attributes

Schema additions are permanent. You cannot delete **attributeSchema** and **classSchema** objects. In a distributed system, it is difficult to guarantee that there are no instances of a given class or attribute. Removing the definition of a class or attribute damages existing instances of that class or attribute.

You can disable an existing class or attribute by marking it as "defunct". This does not affect existing instances of the class or attribute so marked, but it prevents the creation of new instances.

The following restrictions apply when disabling schema classes and attributes:

-   You cannot disable a Category 1 class or attribute.
-   You cannot disable an attribute that is a member of a class that is not also disabled. This is because an attribute might be required for the (not disabled) class, and disabling the attribute prevents new instances of the class from being created.

To disable an attribute, set the **isDefunct** attribute of its **attributeSchema** object to **TRUE**. When an attribute is disabled, new instances of the attribute cannot be created. To re-enable the attribute set the **isDefunct** attribute to **FALSE**.

To disable a class, set the **isDefunct** attribute of its **classSchema** object to **TRUE**. When a class is disabled, new instances of the class cannot be created. To re-enable the class set the **isDefunct** attribute to **FALSE**.

Setting schema objects as defunct can be useful in production environments. When a test version of a schema extension is no longer required, mark it as defunct. You can restore it by removing the **isDefunct** attribute or setting the attribute value to **FALSE**. This also protects against an unintended removal of a schema object by setting it to defunct because the operation can be easily reversed.

Be aware that the Active Directory server does not clean up existing instances of an attribute or class when you make a schema object defunct. If you remove the **isDefunct** property, any instances become valid, normal objects again.

The following list includes other consequences of marking an **attributeSchema** or **classSchema** object defunct:

-   Addition or modification of an instance fails.
-   Error codes behave as if a defunct class never existed.
-   Search and delete behave as if no schema objects have been made defunct.
-   Only allow deleting entire attribute from object.

The following list includes additional options in a production environment for reducing the impact of defunct schema extensions:

-   Remove all **mayHave** attribute values from a defunct class.
-   Reduce the size of all **mustHave** attribute values from a defunct class.
-   Remove a defunct attribute from the global catalog.
-   Remove a defunct attribute from any index.

Other options for removing unwanted schema changes in a production environment are for developers to use a private domain controller for testing. In this case, you can:

-   "Reset" the Active Directory server by using Dcpromo.exe to demote the DC. After the demote completes, use Dcpromo.exe again to promote the server back to a DC. The developer can then use LDIF scripts to reload any required classes, attributes, and object instances.
-   Use Ntbackup.exe to perform a system-state backup to an available disk partition. Reboot to Safe/Directory Service Restore mode to restore.

For Windows Server 2003 operating systems, when you set a class or attribute to defunct, you can immediately reuse the **ldapDisplayName**, **schemaIdGuid**, **OID** and **mapiID** values of the defunct schema element when you create a new class or attribute to replace it. The defunct version of the class or attribute is maintained in the Schema container, but it is hidden in the MMC snap-in. To reactivate the old schema element, set **isDefunct** to **FALSE**.

The following LDIF code example shows how to modify the **isDefunct** attribute and change the RDN so that it is not confused with the new class that you create to replace it.

``` syntax
 dn: CN=MyClass,CN=Schema,CN=Configuration,DC=X
   changetype: modify
   replace: isDefunct
   isDefunct: TRUE
   -

   dn: CN=MyClass,CN=Schema,CN=Configuration,DC=X
   changetype: modrdn
   newrdn: cn=MyClassOld
   deleteoldrdn: 1

   dn:
   changetype: modify
   add: schemaUpdateNow
   schemaUpdateNow: 1
   -
```

Use the following command to run the LDIF code example against a forest for a computer running on Windows Server 2003 operating systems.

**ldifde /i /f rdn.ldf /c "DC=X" "dc=mydomain,dc=com"**

(Where "DC=X" is a constant)

 

 




