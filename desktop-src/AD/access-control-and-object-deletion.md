---
title: Access Control and Object Deletion
description: Active Directory enables you to delete an object if you have DELETE access to the object or ADS\_RIGHT\_DS\_DELETE\_CHILD access to the object type on the parent container.
ms.assetid: 87027c25-e3c9-4bad-8df3-cb6205e40ef6
ms.tgt_platform: multiple
keywords:
- Access Control and Object Deletion AD
ms.topic: article
ms.date: 05/31/2018
---

# Access Control and Object Deletion

Active Directory Domain Services enable you to delete an object if you have one of the following access rights:

-   DELETE access to the object itself
-   ADS\_RIGHT\_DS\_DELETE\_CHILD access for that object type on the parent container

Be aware that the system verifies the security descriptor for both the object and its parent before denying the deletion. This means that an ACE that explicitly denies DELETE access to a user has no effect if the user has DELETE\_CHILD access on the parent. Similarly, an ACE that denies DELETE\_CHILD access on the parent can be overridden if DELETE access is allowed on the object itself.

To perform a tree-delete operation, for example using the [**IADsDeleteOps::DeleteObject**](/windows/desktop/api/iads/nf-iads-iadsdeleteops-deleteobject) method, you must have ADS\_RIGHT\_DS\_DELETE\_TREE access to the object. If you have this access right, you can delete the object and any child objects regardless of the protections on the child objects. To delete a tree if you do not have ADS\_RIGHT\_DS\_DELETE\_TREE access, you must recursively traverse the tree, deleting each object individually. In this case, you must have the necessary DELETE or DELETE\_CHILD access for each object in the tree.

> [!WARNING]
> If users have ADS\_RIGHT\_DS\_DELETE\_TREE access for an object, this gives them the ability to delete a whole subtree, including all child objects. For this reason, you may consider revoking "Delete Subtree" access permission for all users on a parent container.

 

 

 