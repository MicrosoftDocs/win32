---
title: Reading a Control Access Right Set in an Object's ACL
description: The properties of the IADsAccessControlEntry interface is used to grant or deny control access rights.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 2c6fef91-990e-4954-9aff-c9ec72d13972
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Reading a Control Access Right Set in an Object's ACL Active Directory
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reading a Control Access Right Set in an Object's ACL

Using ADSI, you read a control access right ACE just as you would any other ACE in an ACL. Be aware that you can also use the Win32 security APIs to read ACLs on directory objects. However, control access rights use the properties of the [**IADsAccessControlEntry**](https://msdn.microsoft.com/library/aa705951) interface in a manner that is specific to granting and denying control access rights:

-   [**AccessMask**](https://msdn.microsoft.com/library/aa705952) must contain **ADS\_RIGHT\_DS\_CONTROL\_ACCESS**.
-   [**Flags**](https://msdn.microsoft.com/library/aa705952) value is **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT**.
-   [**ObjectType**](https://msdn.microsoft.com/library/aa705952) is the string form of the **rightsGUID** attribute of the control access right. The string format of the GUID is the same string format as the [**StringFromGUID2**](5f437658-b749-416b-805a-2afdac682660) COM Library function.
-   [**AceType**](https://msdn.microsoft.com/library/aa705952) is either **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** to grant the trustee the control access right or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT** to deny the trustee the control access right.
-   [**Trustee**](https://msdn.microsoft.com/library/aa705952) is the security principal; that is the user, group, computer, and so on, to which the ACE applies.

Use the following procedure to read an ACE for an ADSI object. The following procedure applies to C and C++ applications.

**To read an ACE for an ADSI object**

1.  Get an [**IADs**](https://msdn.microsoft.com/library/aa705950) interface pointer to the object.
2.  Use the [**IADs::Get**](https://msdn.microsoft.com/library/aa746347) method to get the security descriptor of the object. The name of the property that contains the security descriptor is "nTSecurityDescriptor". The property will be returned as a **VARIANT** that contains an [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) pointer. Be aware that the **vt** member is **VT\_DISPATCH**. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsSecurityDescriptor**](https://msdn.microsoft.com/library/aa706128) interface to use the methods on that interface to access the security descriptor ACL.
3.  Use the [**IADsSecurityDescriptor::get\_DiscretionaryAcl**](https://msdn.microsoft.com/library/aa706131) method to get the ACL. The method returns an [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) pointer. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlList**](https://msdn.microsoft.com/library/aa705953) interface to use the methods on that interface to access the individual ACEs in the ACL.
4.  Use the [**IADsAccessControlList::get\_\_NewEnum**](https://msdn.microsoft.com/library/aa705956) method to enumerate the ACEs. The method returns an [**IUnknown**](33f1d79a-33fc-4ce5-a372-e08bda378332) pointer. Call **QueryInterface** on that **IUnknown** pointer to get an [**IEnumVARIANT**](https://msdn.microsoft.com/windows/desktop/139e3c93-faef-4003-9079-e0e94494db3e) interface.
5.  Use the [**IEnumVARIANT::Next**](https://msdn.microsoft.com/windows/desktop/691c1624-8d01-41e0-890e-a4782eba1f59) method to enumerate the ACEs in the ACL. The property is returned as a **VARIANT** that contains an [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) pointer. Be aware that the **vt** member is **VT\_DISPATCH**. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlEntry**](https://msdn.microsoft.com/library/aa705951) interface to read the ACE.
6.  Call the [**IADsAccessControlEntry::get\_AccessMask**](https://msdn.microsoft.com/library/aa705952) method to get the **AccessMask** and verify that the **AccessMask** value for the **ADS\_RIGHT\_DS\_CONTROL\_ACCESS** flag. If it has this flag, the ACE contains a control access right.
7.  Call the [**IADsAccessControlEntry::get\_Flags**](https://msdn.microsoft.com/library/aa705952) method to get the flag for the object type.
8.  Check [**Flags**](https://msdn.microsoft.com/library/aa705952) value for **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT** flag. If **Flags** is set to **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT**, call the **IADsAccessControlEntry::get\_ObjectType** method to get a string that contains the rightsGUID of the control access right that the ACE applies to.
9.  Call the [**IADsAccessControlEntry::get\_AceType**](https://msdn.microsoft.com/library/aa705952) method to get the ACE type. The type will be an **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** to grant the trustee the control access right or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT** to deny the control access right.
10. Call the [**IADsAccessControlEntry::get\_Trustee**](https://msdn.microsoft.com/library/aa705952) method to get the security principal; that is user, group, computer, and so on to which the ACE applies.
11. When finished with the [**ObjectType**](https://msdn.microsoft.com/library/aa705952) and **Trustee** strings, use [**SysFreeString**](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) to free the memory for those strings.
12. When finished with the interfaces, call **Release** to decrement or release all the interface references.

 

 




