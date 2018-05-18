---
title: Creating a Security Descriptor for a New Directory Object
description: You can use ADSI to create a security descriptor and set it as a new object's nTSecurityDescriptor property or use it to replace an existing object's nTSecurityDescriptor property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'b9ff626f-17f1-4fc1-9d6e-4f47e29a5aeb'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Creating a Security Descriptor for a New Directory Object AD"]
---

# Creating a Security Descriptor for a New Directory Object

You can use ADSI to create a security descriptor and set it as a new object's **nTSecurityDescriptor** property or use it to replace an existing object's **nTSecurityDescriptor** property.

To create a security descriptor for an object:

1.  Use [**CoCreateInstance**](_com_cocreateinstance) to create the ADSI COM object for the new security descriptor and get an [**IADsSecurityDescriptor**](https://msdn.microsoft.com/library/aa706128) interface pointer to that object. Be aware that the class ID is **CLSID\_SecurityDescriptor**.
2.  Use the [**IADsSecurityDescriptor::put\_Owner**](https://msdn.microsoft.com/library/aa706131) method to set the owner of the object. The trustee is a user, group, or other security principal. An application should use the value from the appropriate property from the user or group object of the trustee to which to apply the ACE.
3.  Use the [**IADsSecurityDescriptor::put\_Control**](https://msdn.microsoft.com/library/aa706131) method to control whether DACLs and SACLs are inherited by the object from its parent container.
4.  Use [**CoCreateInstance**](_com_cocreateinstance) to create the ADSI COM object for the DACL for the new security descriptor and get an [**IADsAccessControlList**](https://msdn.microsoft.com/library/aa705953) interface pointer to that object. Be aware that the class ID is **CLSID\_AccessControlList**.
5.  For each ACE to add to the DACL, use [**CoCreateInstance**](_com_cocreateinstance) to create the ADSI COM object for the new ACE and get an [**IADsAccessControlEntry**](https://msdn.microsoft.com/library/aa705951) interface pointer to that object. Be aware that the class ID is CLSID\_AccessControlEntry.
6.  For each ACE to add to the DACL, set the properties of the ACE using the property methods of the ACE's [**IADsAccessControlEntry**](https://msdn.microsoft.com/library/aa705951) object. For more information about the properties to set on an ACE, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).
7.  For each ACE to add to the DACL, use the **QueryInterface** method on the [**IADsAccessControlEntry**](https://msdn.microsoft.com/library/aa705951) object to get an [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) pointer. The [**IADsAccessControlList::AddAce**](https://msdn.microsoft.com/library/aa705954) method requires an **IDispatch** interface pointer to the ACE.
8.  For each ACE to add to the DACL, use [**IADsAccessControlList::AddAce**](https://msdn.microsoft.com/library/aa705954) to add the new ACE to the DACL. Be aware that the order of the ACEs within the ACL can affect the evaluation of access to the object. The correct access to the object may require you to create a new ACL, add the ACEs from the existing ACL in the correct order to the new ACL, and then replace the existing ACL in the security descriptor with the new ACL. For more information, see [Order of ACEs in a DACL](https://msdn.microsoft.com/library/windows/desktop/aa379298).
9.  Follow Steps 4-8 to create the SACL for the new security descriptor.
10. Use the [**IADsSecurityDescriptor::put\_DiscretionaryAcl**](https://msdn.microsoft.com/library/aa706131) method to set the DACL. For more information about DACLs, see [Null DACLs and Empty DACLs](null-dacls-and-empty-dacls.md).
11. Use the [**IADsSecurityDescriptor::put\_SystemAcl**](https://msdn.microsoft.com/library/aa706131) method to set the SACL.
12. Convert the [**IADsSecurityDescriptor**](https://msdn.microsoft.com/library/aa706128) object to a [**VARIANT**](e305240e-9e11-4006-98cc-26f4932d2118) by using the **QueryInterface** method of the **IADsSecurityDescriptor** object to obtain an [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. Then set the **vt** member of the **VARIANT** to **VT\_DISPATCH** and set the **pdispVal** member of the **VARIANT** equal to the **IDispatch** pointer.
13. Obtain an [**IADs**](https://msdn.microsoft.com/library/aa705950) interface pointer to the object.
14. Use the [**IADs::Put**](https://msdn.microsoft.com/library/aa746352) method with "nTSecurityDescriptor" and the [**VARIANT**](e305240e-9e11-4006-98cc-26f4932d2118) created above to write the new security descriptor to the property cache.
15. Use the [**IADs::SetInfo**](https://msdn.microsoft.com/library/aa746354) method to update the property on the object in the directory.

 

 




