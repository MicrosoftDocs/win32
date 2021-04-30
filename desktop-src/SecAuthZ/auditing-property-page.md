---
description: The access control editor can include an Auditing property page that enables the user to view and edit the access control entries (ACEs) in an objects system access control list (SACL). For more information about SACLs, see Access Control Lists (ACLs).
ms.assetid: 2a9152b7-c72d-4f03-bc3f-b75927fb4b6c
title: Auditing Property Page
ms.topic: article
ms.date: 05/31/2018
---

# Auditing Property Page

The access control editor can include an **Auditing** property page that enables the user to view and edit the [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) in an object's [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL). For more information about SACLs, see [Access Control Lists](access-control-lists.md) (ACLs).

**To view the Auditing property page**

-   On the [basic security property page](basic-security-property-page.md), click **Advanced**. The **Auditing** property page is in the [advanced security property sheet](advanced-security-property-sheet.md).

To include the **Auditing** property page, set the **SI\_ADVANCED** and **SI\_EDIT\_AUDITS** flags in the [**SI\_OBJECT\_INFO**](/windows/desktop/api/Aclui/ns-aclui-si_object_info) structure returned by your [**ISecurityInformation::GetObjectInformation**](/windows/win32/api/aclui/nf-aclui-isecurityinformation-getobjectinformation) implementation.

 

 
