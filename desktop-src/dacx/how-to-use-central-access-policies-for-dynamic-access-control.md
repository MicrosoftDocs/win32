---
title: How to use central access policies for dynamic access control
description: You can use Central Access Policies (CAP) to control access dynamically.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 11967171-9C7D-488A-9DC2-5C7953FC8096
ms.prod: windows-server-dev
ms.technology: dynamic-access-control
ms.tgt_platform: multiple
keywords:
- Dynamic Access Control developer extensibility DACx , central access policies for dynamic access control
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to use central access policies for dynamic access control

You can use Central Access Policies (CAP) to control access dynamically.

There are two options for programmatic access to the Dynamic Access Control objects in Active Directory:

<dl> **Using Windows PowerShell**  
This is the preferred option as it greatly simplifies the developer experience. Microsoft has provided Windows PowerShell Cmdlets that encapsulate all of the rules, constraints, and methods required to work with DAC objects. For more information about the Windows PowerShell Cmdlets see, [AD DS Administration Cmdlets in Windows PowerShell](https://technet.microsoft.com/library/hh852274.aspx)  
The relevant cmdlets are:  

-   Set/Get/New/Remove ADClaimType
-   Set/Get/New/Remove ADResourceProperty
-   Set/Get/New/Remove ADCentralAccessRule
-   Set/Get/New/Remove ADCentralAccessPolicy

**Using LDAP**  
LDAP offers better performance; however, it is more complex. You must take great care to follow the rules and constraints for these objects. For more information about LDAP options see the remaining How-to topics in this section beginng with, [Dynamic Access Control objects in Active Directory](dynamic-access-control-containers-in-active-directory.md).  
</dl>

For development environments where it is important for your code to interact with Active Directory over other interfaces directly (for example: LDAP), you must consider the following constrains for managing claim type, resource property, central access rules, central access policies, and resource property list objects.

In general, validations stated in this topic apply to create and set operations. On read operation, you must keep the validation consistent with schema requirements to allow proper display of the existing information.

## What you need to know

### Technologies

-   [Active Directory](https://msdn.microsoft.com/library/aa772170)
-   [LDAP](https://msdn.microsoft.com/library/aa367008)
-   [PowerShell](https://technet.microsoft.com/library/bb978526.aspx)

### Prerequisites

-   If you are using Active Directory module for PowerShell, it provides proper validation for data input. For more information, see the [Deploy a Central Access Policy (Demonstration Steps)](https://technet.microsoft.com/library/hh846167.aspx) on TechNet.

## Steps

<dl> <dt>

[Dynamic Access Control objects in Active Directory](dynamic-access-control-containers-in-active-directory.md)
</dt> <dd>

All the objects mentioned in this scenario live in configuration naming context in Active Directory, the objects will be replicated throughout the entire forest

</dd> <dt>

[How to read Dynamic Access Control objects using LDAP](how-to-enumerate-active-directory-definitions-for-user-and-device-claims-and-resource-properties.md)
</dt> <dd>

This code sample will enumerate all of the Dynamic Access Control objects in Active Directory.

</dd> <dt>

[How to set up a claim type](how-to-set-up-a-claim-type.md)
</dt> <dd>

Claim type (msDS-ClaimType) resides in msDS-ClaimTypes container and is used in ACL expressions and central access rule expressions.

</dd> <dt>

[How to set up a resource property](how-to-set-up-a-resource-property.md)
</dt> <dd>

Resource Property (msDS-ResourceProperty) resides in msDS-ResourceProperties container, and is used to classify files on Windows Server 2012 File Server as well as used in central access rule expression.

</dd> <dt>

[How to setup a central access rule](how-to-setup-a-central-access-rule.md)
</dt> <dd>

This topic describes a Central Access Rule (CAR).

</dd> <dt>

[How to setup a central access policy](how-to-setup-a-central-access-policy.md)
</dt> <dd>

This topic describes a Central Access Policy (CAP).

</dd> </dl>

## Additional resources

-   [Deploy a Central Access Policy (Demonstration Steps)](https://technet.microsoft.com/library/hh846167.aspx)
-   [The Extensible File Classification Infrastructure](https://msdn.microsoft.com/windowsserver2008r2trainingcourse_fileclassifictioninfrastructure_unit)
-   [Working with File Classification](https://technet.microsoft.com/library/dd758765.aspx)
-   [How to enrich audit reporting](enrich-audit-reporting.md)

 

 




