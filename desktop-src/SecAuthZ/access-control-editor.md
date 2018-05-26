---
Description: A set of property sheets and property pages that enable the user to view and modify the components of an objects security descriptor.
ms.assetid: ca709f27-8463-4f11-92ac-2148796e640a
title: Access Control Editor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Access Control Editor

The access control editor is a set of property sheets and property pages that enable the user to view and modify the components of an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly). The editor consists of two main parts:

-   A [basic security property page](basic-security-property-page.md) that provides a simple interface for editing the [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) in an object's [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL). This page can include an optional **Advanced** button that displays the advanced security property sheet.
-   An [advanced security property sheet](advanced-security-property-sheet.md) with property pages that enable the user to edit the object's [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL), change the object's owner, or perform advanced editing of the object's DACL.

The [**CreateSecurityPage**](/windows/win32/Aclui/nf-aclui-createsecuritypage?branch=master) function creates the basic security property page. You can then use the [**PropertySheet**](_win32_propertysheet_cpp) function or the [**PSM\_ADDPAGE**](_win32_psm_addpage_cpp) message to add this page to a property sheet.

Alternatively, you can use the [**EditSecurity**](/windows/win32/Aclui/nf-aclui-editsecurity?branch=master) function to display a property sheet that contains the basic security property page.

For both [**CreateSecurityPage**](/windows/win32/Aclui/nf-aclui-createsecuritypage?branch=master) and [**EditSecurity**](/windows/win32/Aclui/nf-aclui-editsecurity?branch=master), the caller must pass a pointer to an implementation of the [**ISecurityInformation**](/windows/win32/Aclui/?branch=master) interface. The access control editor calls the methods of this interface to retrieve access control information about the object being edited and to pass the user's input back to your application. The **ISecurityInformation** methods have the following purposes:

-   To initialize the property pages.

    Your implementation of the [**GetObjectInformation**](/windows/win32/Aclui/?branch=master) method passes an [**SI\_OBJECT\_INFO**](/windows/win32/Aclui/ns-aclui-_si_object_info?branch=master) structure to the editor. This structure specifies the property pages that you want the editor to display and other information that determines the editing options available to the user.

-   To provide security information about the object being edited.

    Your [**GetSecurity**](/windows/win32/Aclui/?branch=master) implementation passes the object's initial [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) to the editor. The [**GetAccessRights**](/windows/win32/Aclui/?branch=master) and [**MapGeneric**](/windows/win32/Aclui/?branch=master) methods provide information about the object's access rights. The [**GetInheritTypes**](/windows/win32/Aclui/?branch=master) method provides information about how the object's ACEs can be inherited by child objects.

-   To pass the user's input back to your application.

    When the user clicks **Okay** or **Apply**, the editor calls your [**SetSecurity**](/windows/win32/Aclui/?branch=master) method to pass back a security descriptor containing the user's changes.

 

 



