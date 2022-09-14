---
title: Reading the defaultSecurityDescriptor for an Object Class
description: Using ADSI, you can obtain the defaultSecurityDescriptor attribute for an object class with the IADs interface.
ms.assetid: 12d1e77a-bd70-4c64-9b4f-ac5caaf5fe40
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , reading the defaultSecurityDescriptor for an Object Class
ms.topic: article
ms.date: 05/31/2018
---

# Reading the defaultSecurityDescriptor for an Object Class

Using ADSI, you can obtain the **defaultSecurityDescriptor** attribute for an object class with the [**IADs**](/windows/desktop/api/iads/nn-iads-iads) interface. To obtain the **defaultSecurityDescriptor** attribute for an object class, perform the following steps.

1.  Get an [**IADs**](/windows/desktop/api/iads/nn-iads-iads) interface pointer to the **classSchema** object for the object class.
2.  Use the [**IADs.Get**](/windows/desktop/api/iads/nf-iads-iads-get) method to get the default security descriptor of the object. The name of the property that contains the security descriptor is "defaultSecurityDescriptor". The property will be returned as a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) containing a BSTR with the default security descriptor in SDDL string format.
3.  Use the [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora) function to convert the SDDL string form to a security descriptor.
4.  Use the [**GetSecurityDescriptorDacl**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptordacl), [**GetSecurityDescriptorSacl**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorsacl), [**GetSecurityDescriptorOwner**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorowner), and [**GetSecurityDescriptorControl**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorcontrol) Security APIs to read the parts of the security descriptor.

For a code example that demonstrates how to do this, see [Example Code for Reading defaultSecurityDescriptor](example-code-for-reading-defaultsecuritydescriptor.md).

 

 