---
Description: 'A set of property sheets and property pages that enable the user to view and modify the components of an object's security descriptor.'
ms.assetid: 'ca709f27-8463-4f11-92ac-2148796e640a'
title: Access Control Editor
---

# Access Control Editor

The access control editor is a set of property sheets and property pages that enable the user to view and modify the components of an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly). The editor consists of two main parts:

-   A [basic security property page](basic-security-property-page.md) that provides a simple interface for editing the [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) in an object's [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL). This page can include an optional **Advanced** button that displays the advanced security property sheet.
-   An [advanced security property sheet](advanced-security-property-sheet.md) with property pages that enable the user to edit the object's [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL), change the object's owner, or perform advanced editing of the object's DACL.

The [**CreateSecurityPage**](createsecuritypage.md) function creates the basic security property page. You can then use the [**PropertySheet**](_win32_propertysheet_cpp) function or the [**PSM\_ADDPAGE**](_win32_psm_addpage_cpp) message to add this page to a property sheet.

Alternatively, you can use the [**EditSecurity**](editsecurity.md) function to display a property sheet that contains the basic security property page.

For both [**CreateSecurityPage**](createsecuritypage.md) and [**EditSecurity**](editsecurity.md), the caller must pass a pointer to an implementation of the [**ISecurityInformation**](isecurityinformation.md) interface. The access control editor calls the methods of this interface to retrieve access control information about the object being edited and to pass the user's input back to your application. The **ISecurityInformation** methods have the following purposes:

-   To initialize the property pages.

    Your implementation of the [**GetObjectInformation**](isecurityinformation-getobjectinformation.md) method passes an [**SI\_OBJECT\_INFO**](si-object-info.md) structure to the editor. This structure specifies the property pages that you want the editor to display and other information that determines the editing options available to the user.

-   To provide security information about the object being edited.

    Your [**GetSecurity**](isecurityinformation-getsecurity.md) implementation passes the object's initial [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) to the editor. The [**GetAccessRights**](isecurityinformation-getaccessrights.md) and [**MapGeneric**](isecurityinformation-mapgeneric.md) methods provide information about the object's access rights. The [**GetInheritTypes**](isecurityinformation-getinherittypes.md) method provides information about how the object's ACEs can be inherited by child objects.

-   To pass the user's input back to your application.

    When the user clicks **Okay** or **Apply**, the editor calls your [**SetSecurity**](isecurityinformation-setsecurity.md) method to pass back a security descriptor containing the user's changes.

 

 



