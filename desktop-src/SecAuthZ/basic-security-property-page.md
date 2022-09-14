---
description: The starting page of the property sheet displayed by the EditSecurity function. You can also use the CreateSecurityPage function to create a basic security property page to insert in your own property sheet.
ms.assetid: 6623fe7e-e91d-49c7-9ad0-7791c178d12b
title: Basic Security Property Page
ms.topic: article
ms.date: 05/31/2018
---

# Basic Security Property Page

The basic security property page is the starting page of the property sheet displayed by the [**EditSecurity**](/windows/desktop/api/Aclui/nf-aclui-editsecurity) function. You can also use the [**CreateSecurityPage**](/windows/desktop/api/Aclui/nf-aclui-createsecuritypage) function to create a basic security property page to insert in your own property sheet.

The property page displays a list of the [trustees](trustees.md) named in the [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) of the object's [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL). The page also contains a list of the access rights supported by the object. When the user selects a name from the list of trustees, the check boxes next to each access right indicate the rights that are allowed or denied for that trustee. The user can then select or clear the check boxes to modify the trustee's access rights. The user can also add or remove trustees from the list.

The basic security property page cannot display complex ACEs, such as [object-specific ACEs](object-specific-aces.md), or ACE inheritance information. To enable the user to view or edit such information, you can include an **Advanced** button on the basic security page. The user can click the **Advanced** button to display an [advanced security property sheet](advanced-security-property-sheet.md). This property sheet has property pages that enable the user to edit the object's [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL), change the object's owner, or perform advanced editing of the object's DACL. To display the **Advanced** button, set the SI\_ADVANCED flag in the [**SI\_OBJECT\_INFO**](/windows/desktop/api/Aclui/ns-aclui-si_object_info) structure returned by your [**ISecurityInformation::GetObjectInformation**](/windows/win32/api/aclui/nf-aclui-isecurityinformation-getobjectinformation) implementation.

You can use the **pszPageTitle** member of the [**SI\_OBJECT\_INFO**](/windows/desktop/api/Aclui/ns-aclui-si_object_info) structure to specify the title of the basic security property page. The default title is **Security**.

 

 
