---
title: Setting Access Rights on an Object
description: This topic describes how to create an ACE for an access right and setting that ACE on the DACL of an object.
ms.assetid: c0b45709-4652-46c7-8d52-44076802d109
ms.tgt_platform: multiple
keywords:
- Setting Access Rights on an Object AD
- Objects AD , Setting Access Rights on an Object
ms.topic: article
ms.date: 05/31/2018
---

# Setting Access Rights on an Object

When using the ADSI COM objects [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) (security descriptor), [**IADsAccessControlList**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrollist) (DACLs and SACLs), and [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) (ACE) to add an ACE to a ACL, you are making changes to the **nTSecurityDescriptor** property of the specified object in the property cache. This means put methods on the objects that contain the new ACE and the [**IADs.SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) method must be called in order to write the updated security descriptor to the directory from the property cache.

For more information and a code example that sets an ACE on an object in Active Directory Domain Services, see [Example Code for Setting an ACE on a Directory Object](example-code-for-setting-an-ace-on-a-directory-object.md).

Use the following general process to create an ACE for an access right and setting that ACE on the DACL of an object.

1.  Get an [**IADs**](/windows/desktop/api/iads/nn-iads-iads) interface pointer to the object.
2.  Use the [**IADs.Get**](/windows/desktop/api/iads/nf-iads-iads-get) method to get the security descriptor of the object. The name of the property containing the security descriptor is **nTSecurityDescriptor**. The property will be returned as a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) containing an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer (the **vt** member is **VT\_DISPATCH**). Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) interface to use the methods on that interface to access the security descriptor's ACL.
3.  Use the [**IADsSecurityDescriptor.DiscretionaryAcl**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) property to get the DACL. The method returns an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlList**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrollist) interface to use the methods on that interface to access the individual ACEs in the ACL.
4.  Use [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to create the ADSI COM object for the new ACE and get an [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) interface pointer to that object. Be aware that the class ID is CLSID\_AccessControlEntry.
5.  Set the properties of the ACE using the [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) methods:

    1.  Use [**IADsAccessControlEntry::put\_Trustee**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) to set the trustee to whom this ACE applies. The trustee is a user, group, or other security principal. Your application should use the value from the appropriate property from the user or group object of the trustee to which you want to apply the ACE. The trustee is specified as a **BSTR** and can take the following forms:
        -   Domain account (the logon name used in a previous version of Windows NT) of the form "&lt;domain&gt;\\\<user account\>" where "&lt;domain&gt;" is the name of the Windows NT domain that contains the user and "&lt;user account&gt;" is the **sAMAccountName** property of the specified user. For example: "fabrikam\\jeffsmith".
        -   Well-known security principal that represents special identities defined by the Windows NT security system, such as everyone, local system, principal self, authenticated user, creator owner, and so on. The objects representing the well-known security principals are stored in the Well Known Security Principals container beneath the Configuration container. For example, anonymous logon.
        -   Built-in group that represent the built-in user groups defined by the Windows NT security system. It has the form "BUILTIN\\\<group name\>" where "&lt;group name&gt;" is the name of the built-in user group. The objects representing the built-in groups are stored in the Builtin container beneath the domain container. For example, "BUILTIN\\Administrators".
        -   SID (string format) of the specified user, which is the **objectSID** property of the specified user. You can convert to string form using the [**ConvertSidToStringSid**](/windows/desktop/api/sddl/nf-sddl-convertsidtostringsida) function in the Win32 Security API. For example: "S-1-5-32-548".
    2.  Use the [**IADsAccessControlEntry.AccessMask**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property to set the mask that specifies the access right. The [**ADS\_RIGHTS\_ENUM**](/windows/win32/api/iads/ne-iads-ads_rights_enum) enumeration specifies the access rights you can set on a directory object.
    3.  Use the [**IADsAccessControlEntry.AceType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property to specify whether to allow or deny the access rights set by **AccessMask**. For standard rights, this can be **ADS\_ACETYPE\_ACCESS\_ALLOWED** or **ADS\_ACETYPE\_ACCESS\_DENIED**. For object-specific rights (rights that apply to a specific part of an object or to a specific type of object), use **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT**. The [**ADS\_ACETYPE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_acetype_enum) enumeration specifies the access types you can set on an ACE.
    4.  Use the [**IADsAccessControlEntry.AceFlags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property to specify whether other containers or objects beneath the specified object can inherit the ACE. The [**ADS\_ACEFLAG\_ENUM**](/windows/win32/api/iads/ne-iads-ads_aceflag_enum) enumeration specifies the inheritance flags you can set on an ACE.
    5.  Use the [**IADsAccessControlEntry.Flags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property to specify whether the right applies to a specific part of the object, an inherited object type, or both.
    6.  If **Flags** is set to **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT**, set the [**IADsAccessControlEntry.ObjectType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property o specify a string containing the GUID of the object class (for **ADS\_RIGHT\_DS\_CREATE\_CHILD** or **ADS\_RIGHT\_DS\_DELETE\_CHILD**), property, property set, validated write, or extended right that the ACE applies to. The GUID must be specified as a string of the form produced by the [**StringFromGUID2**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromguid2) function in the COM library.
    7.  If **Flags** is set to **ADS\_FLAG\_INHERITED\_OBJECT\_TYPE\_PRESENT**, set the [**IADsAccessControlEntry.InheritedObjectType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property to specify a string that contains the GUID of the inherited object class that the ACE applies to. The GUID must be specified as a string of the form produced by the [**StringFromGUID2**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromguid2) function in the COM library.

6.  Use the **QueryInterface** method on the [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) object to get an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. The [**IADsAccessControlList.AddAce**](/windows/desktop/api/iads/nf-iads-iadsaccesscontrollist-addace) method requires an **IDispatch** interface pointer to the ACE.
7.  Use [**IADsAccessControlList.AddAce**](/windows/desktop/api/iads/nf-iads-iadsaccesscontrollist-addace) to add the new ACE to the DACL. Be aware that the order of the ACEs within the ACL can affect the evaluation of access to the object. The correct access to the object may require you to create an new ACL, add the ACEs from the existing ACL in the correct order to the new ACL, and then replace the existing ACL in the security descriptor with the new ACL. For more information, see [Order of ACEs in a DACL](/windows/desktop/SecAuthZ/order-of-aces-in-a-dacl).
8.  Use the [**IADsSecurityDescriptor.DiscretionaryAcl**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) property to write the DACL containing the new ACE to the security descriptor. For more information about DACLs, see [Null DACLs and Empty DACLs](null-dacls-and-empty-dacls.md).
9.  Use the [**IADs.Put**](/windows/desktop/api/iads/nf-iads-iads-put) method to write the security descriptor to the object's **nTSecurityDescriptor** property to the property cache.
10. Use the [**IADs.SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) method to update the property on the object in the directory.

 

 
