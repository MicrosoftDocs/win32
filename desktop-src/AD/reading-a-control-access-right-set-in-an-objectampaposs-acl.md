---
title: Reading a Control Access Right Set in an Object's ACL
description: The properties of the IADsAccessControlEntry interface is used to grant or deny control access rights.
ms.assetid: 2c6fef91-990e-4954-9aff-c9ec72d13972
ms.tgt_platform: multiple
keywords:
- Reading a Control Access Right Set in an Object's ACL Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Reading a Control Access Right Set in an Object's ACL

Using ADSI, you read a control access right ACE just as you would any other ACE in an ACL. Be aware that you can also use the Win32 security APIs to read ACLs on directory objects. However, control access rights use the properties of the [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) interface in a manner that is specific to granting and denying control access rights:

-   [**AccessMask**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) must contain **ADS\_RIGHT\_DS\_CONTROL\_ACCESS**.
-   [**Flags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) value is **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT**.
-   [**ObjectType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) is the string form of the **rightsGUID** attribute of the control access right. The string format of the GUID is the same string format as the [**StringFromGUID2**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromguid2) COM Library function.
-   [**AceType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) is either **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** to grant the trustee the control access right or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT** to deny the trustee the control access right.
-   [**Trustee**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) is the security principal; that is the user, group, computer, and so on, to which the ACE applies.

Use the following procedure to read an ACE for an ADSI object. The following procedure applies to C and C++ applications.

**To read an ACE for an ADSI object**

1.  Get an [**IADs**](/windows/desktop/api/iads/nn-iads-iads) interface pointer to the object.
2.  Use the [**IADs::Get**](/windows/desktop/api/iads/nf-iads-iads-get) method to get the security descriptor of the object. The name of the property that contains the security descriptor is "nTSecurityDescriptor". The property will be returned as a **VARIANT** that contains an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. Be aware that the **vt** member is **VT\_DISPATCH**. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) interface to use the methods on that interface to access the security descriptor ACL.
3.  Use the [**IADsSecurityDescriptor::get\_DiscretionaryAcl**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) method to get the ACL. The method returns an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlList**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrollist) interface to use the methods on that interface to access the individual ACEs in the ACL.
4.  Use the [**IADsAccessControlList::get\_\_NewEnum**](/windows/desktop/api/iads/nf-iads-iadsaccesscontrollist-get__newenum) method to enumerate the ACEs. The method returns an [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) pointer. Call **QueryInterface** on that **IUnknown** pointer to get an [**IEnumVARIANT**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) interface.
5.  Use the [**IEnumVARIANT::Next**](/windows/win32/api/oaidl/nf-oaidl-ienumvariant-next) method to enumerate the ACEs in the ACL. The property is returned as a **VARIANT** that contains an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. Be aware that the **vt** member is **VT\_DISPATCH**. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) interface to read the ACE.
6.  Call the [**IADsAccessControlEntry::get\_AccessMask**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) method to get the **AccessMask** and verify that the **AccessMask** value for the **ADS\_RIGHT\_DS\_CONTROL\_ACCESS** flag. If it has this flag, the ACE contains a control access right.
7.  Call the [**IADsAccessControlEntry::get\_Flags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) method to get the flag for the object type.
8.  Check [**Flags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) value for **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT** flag. If **Flags** is set to **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT**, call the **IADsAccessControlEntry::get\_ObjectType** method to get a string that contains the rightsGUID of the control access right that the ACE applies to.
9.  Call the [**IADsAccessControlEntry::get\_AceType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) method to get the ACE type. The type will be an **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** to grant the trustee the control access right or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT** to deny the control access right.
10. Call the [**IADsAccessControlEntry::get\_Trustee**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) method to get the security principal; that is user, group, computer, and so on to which the ACE applies.
11. When finished with the [**ObjectType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) and **Trustee** strings, use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory for those strings.
12. When finished with the interfaces, call **Release** to decrement or release all the interface references.

 

 