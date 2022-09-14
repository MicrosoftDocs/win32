---
title: Creating Security Descriptors for new directory objects
description: You can use ADSI to create a security descriptor and set it as a new object's nTSecurityDescriptor property or use it to replace an existing object's nTSecurityDescriptor property.
ms.assetid: b9ff626f-17f1-4fc1-9d6e-4f47e29a5aeb
ms.tgt_platform: multiple
keywords:
- Creating a Security Descriptor for a New Directory Object AD
ms.topic: article
ms.date: 05/31/2018
---

# Creating Security Descriptors for new directory objects

You can use ADSI to create a security descriptor and set it as a new object's **nTSecurityDescriptor** property or use it to replace an existing object's **nTSecurityDescriptor** property.

To create a security descriptor for an object:

1.  Use [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to create the ADSI COM object for the new security descriptor and get an [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) interface pointer to that object. Be aware that the class ID is **CLSID\_SecurityDescriptor**.
2.  Use the [**IADsSecurityDescriptor::put\_Owner**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) method to set the owner of the object. The trustee is a user, group, or other security principal. An application should use the value from the appropriate property from the user or group object of the trustee to which to apply the ACE.
3.  Use the [**IADsSecurityDescriptor::put\_Control**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) method to control whether DACLs and SACLs are inherited by the object from its parent container.
4.  Use [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to create the ADSI COM object for the DACL for the new security descriptor and get an [**IADsAccessControlList**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrollist) interface pointer to that object. Be aware that the class ID is **CLSID\_AccessControlList**.
5.  For each ACE to add to the DACL, use [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to create the ADSI COM object for the new ACE and get an [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) interface pointer to that object. Be aware that the class ID is CLSID\_AccessControlEntry.
6.  For each ACE to add to the DACL, set the properties of the ACE using the property methods of the ACE's [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) object. For more information about the properties to set on an ACE, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).
7.  For each ACE to add to the DACL, use the **QueryInterface** method on the [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) object to get an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. The [**IADsAccessControlList::AddAce**](/windows/desktop/api/iads/nf-iads-iadsaccesscontrollist-addace) method requires an **IDispatch** interface pointer to the ACE.
8.  For each ACE to add to the DACL, use [**IADsAccessControlList::AddAce**](/windows/desktop/api/iads/nf-iads-iadsaccesscontrollist-addace) to add the new ACE to the DACL. Be aware that the order of the ACEs within the ACL can affect the evaluation of access to the object. The correct access to the object may require you to create a new ACL, add the ACEs from the existing ACL in the correct order to the new ACL, and then replace the existing ACL in the security descriptor with the new ACL. For more information, see [Order of ACEs in a DACL](/windows/desktop/SecAuthZ/order-of-aces-in-a-dacl).
9.  Follow Steps 4-8 to create the SACL for the new security descriptor.
10. Use the [**IADsSecurityDescriptor::put\_DiscretionaryAcl**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) method to set the DACL. For more information about DACLs, see [Null DACLs and Empty DACLs](null-dacls-and-empty-dacls.md).
11. Use the [**IADsSecurityDescriptor::put\_SystemAcl**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) method to set the SACL.
12. Convert the [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) object to a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) by using the **QueryInterface** method of the **IADsSecurityDescriptor** object to obtain an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. Then set the **vt** member of the **VARIANT** to **VT\_DISPATCH** and set the **pdispVal** member of the **VARIANT** equal to the **IDispatch** pointer.
13. Obtain an [**IADs**](/windows/desktop/api/iads/nn-iads-iads) interface pointer to the object.
14. Use the [**IADs::Put**](/windows/desktop/api/iads/nf-iads-iads-put) method with "nTSecurityDescriptor" and the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) created above to write the new security descriptor to the property cache.
15. Use the [**IADs::SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) method to update the property on the object in the directory.

 

 