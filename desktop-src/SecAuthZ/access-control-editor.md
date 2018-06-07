---
Description: 'A set of property sheets and property pages that enable the user to view and modify the components of an object's security descriptor.'
ms.assetid: 'ca709f27-8463-4f11-92ac-2148796e640a'
title: Access Control Editor
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Access Control Editor

The access control editor is a set of property sheets and property pages that enable the user to view and modify the components of an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly). The editor consists of two main parts:

-   A [basic security property page](basic-security-property-page.md) that provides a simple interface for editing the [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) in an object's [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL). This page can include an optional **Advanced** button that displays the advanced security property sheet.
-   An [advanced security property sheet](advanced-security-property-sheet.md) with property pages that enable the user to edit the object's [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL), change the object's owner, or perform advanced editing of the object's DACL.

The [**CreateSecurityPage**](/windows/desktop/api/Aclui/nf-aclui-createsecuritypage) function creates the basic security property page. You can then use the [**PropertySheet**](https://www.bing.com/search?q=**PropertySheet**) function or the [**PSM\_ADDPAGE**](https://www.bing.com/search?q=**PSM\_ADDPAGE**) message to add this page to a property sheet.

Alternatively, you can use the [**EditSecurity**](/windows/desktop/api/Aclui/nf-aclui-editsecurity) function to display a property sheet that contains the basic security property page.

For both [**CreateSecurityPage**](/windows/desktop/api/Aclui/nf-aclui-createsecuritypage) and [**EditSecurity**](/windows/desktop/api/Aclui/nf-aclui-editsecurity), the caller must pass a pointer to an implementation of the [**ISecurityInformation**](/windows/desktop/api/Aclui/) interface. The access control editor calls the methods of this interface to retrieve access control information about the object being edited and to pass the user's input back to your application. The **ISecurityInformation** methods have the following purposes:

-   To initialize the property pages.

    Your implementation of the [**GetObjectInformation**](/windows/desktop/api/Aclui/) method passes an [**SI\_OBJECT\_INFO**](/windows/desktop/api/Aclui/ns-aclui-_si_object_info) structure to the editor. This structure specifies the property pages that you want the editor to display and other information that determines the editing options available to the user.

-   To provide security information about the object being edited.

    Your [**GetSecurity**](/windows/desktop/api/Aclui/) implementation passes the object's initial [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) to the editor. The [**GetAccessRights**](/windows/desktop/api/Aclui/) and [**MapGeneric**](/windows/desktop/api/Aclui/) methods provide information about the object's access rights. The [**GetInheritTypes**](/windows/desktop/api/Aclui/) method provides information about how the object's ACEs can be inherited by child objects.

-   To pass the user's input back to your application.

    When the user clicks **Okay** or **Apply**, the editor calls your [**SetSecurity**](/windows/desktop/api/Aclui/) method to pass back a security descriptor containing the user's changes.

 

 



