---
title: How to set up a claim type
description: Claim type (msDS-ClaimType) resides in msDS-ClaimTypes container and is used in ACL expressions and central access rule expressions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 975AB529-6C0E-4071-B979-67E34F89CE8D
ms.prod: windows-server-dev
ms.technology: dynamic-access-control
ms.tgt_platform: multiple
keywords:
- Dynamic Access Control developer extensibility DACx , claim types
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to set up a claim type

Claim type (msDS-ClaimType) resides in msDS-ClaimTypes container and is used in ACL expressions and central access rule expressions.

### Prerequisites

You must set up the default permissions.

-   Read: All authenticated users.
-   Write: Enterprise Administrator.

## Instructions

### Step 1: Validations and recommendations

This is the unique ID of a claim.

**Claim ID (name)**

1.  Keep the ID short as it will be included in the token to identify the claim. A large ID could contribute to token bloat. We recommend maximum number of characters be less than or equal to 41 characters.
2.  We recommend keep the format of the ID consistent with what Active Directory module for PowerShell enforces. The ID must:

    -   start with "ad://ext/"
    -   be followed by 1 to 32 characters
    -   not contain word spaces, \\, \*, ?, ", &lt;, &gt;, \|
    -   if a "/" is introduced after "ad://ext/", then the "/" must be surrounded by a character on each side. The surrounding character must not be ":", "/", or in the list specified in the previous bullet item.

    An example is "ad://ext/BusinessImpact".

**Enabled**

-   This attribute indicates if a claim type is enabled. Once it is enabled, the attribute will be issued a Kerberos token for users in the forest.

**Share possible values with (ms-DS-ClaimSharesPossibleValuesWith)**

-   This attribute is reserved for future development and should always be empty for a claim type.

### Step 2: Source type (ms-DS-Claim-Source-Type)

Windows Server 2012 claim types can be created from three categories and describes the source of the claim type. The three types are:

-   Active Directory attribute (represented as the value "AD")
-   Certificate (represented as the value "certificate")
-   Transformation engine for claims that travel through trusted forest boundaries (represented as the value "TransformPolicy")

Any other values than the ones just listed are treated as an invalid claim type and will not be understood by access engine. Other values are reserved for future development.

-   When Source Type is of "AD" the Source Attribute must exist.
-   When Source Type is of "certificate" the Source OID must exist.
-   Source Attribute and Source OID are mutually exclusive. When Source Type is of "TransformPolicy", SourceAttribute and SourceOID should not exist.

### Step 3: Claim types that have their source from the Active Directory attribute

When a claim types comes from the Active Directory attribute, you must enforce the following constraints:

-   **cn** and **displayName** must be unique
-   **msDS-ClaimTypeAppliesToClass** must be or inherit from user/computer/MSA/inetorgperson
-   **msDS-ClaimAttributeSource** should be an attribute for all the classes in **msDS-ClaimTypeAppliesToClass**
-   **msDS-ClaimAttributeSource** must contain a replicated attribute
-   **msDS-ClaimAttributeSource** must contain a replicated attribute that is not RODC filtered
-   **msDS-ClaimAttributeSource** must contain an attribute that has one of the following syntaxes:

    -   String: 2.5.5.1, 2.5.5.12, or 2.5.5.15
    -   Integer: 2.5.5.9, 2.5.5.16, or 2.5.5.2
    -   Boolean: 2.5.5.8

-   **msDS-ClaimAttributeSource** must contain an attribute that is NOT one of the password attributes:

    -   dBCSPwd
    -   lmPwdHistory
    -   dBCSPwd
    -   unicodePwd

### Step 4: Claim types that have their source from the certificate

When a claim type is based on an OID, you must enforce the following constraints:

-   **cn** and **display-Name** must be unique
-   **msDS-ClaimPossibleValues** cannot be specified if your claim is sourced from an OID
-   **msDS-ClaimAttributeSource** cannot be specified

### Step 5: Claim types that have their source from the transform policy

This type of claim types will be used only in cross forest transformation. It is used to mirror a claim type that is in the trusted forest. The syntax of the claim type should match with the claim type in the trusted forest with its source attribute being set. Thus, when using this claim type, following attribute must not be set to conflict with the syntax of a claim type that is comes from a different source type.

-   Qualified source attributes (ms-DS-Claim-Attribute-Source)
-   Source OID (msDS-ClaimSource)

Extra validation to ensure the two syntax matches is good but not required. It they do not match, the claim will not be issued in the trusting forest.

## Related topics

<dl> <dt>

[How to use central access policies for dynamic access control (Intro Page)](how-to-use-central-access-policies-for-dynamic-access-control.md)
</dt> </dl>

 

 




