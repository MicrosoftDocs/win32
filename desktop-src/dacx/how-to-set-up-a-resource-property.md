---
title: How to set up a resource property
description: Resource Property (msDS-ResourceProperty) resides in msDS-ResourceProperties container, and is used to classify files on Windows Server 2012 File Server as well as used in central access rule expression.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'E72808CD-6ED5-4E61-BAE3-72E9C25E61BC'
ms.prod: 'windows-server-dev'
ms.technology: 'dynamic-access-control'
ms.tgt_platform: multiple
keywords: ["Dynamic Access Control developer extensibility DACx , resource properties"]
---

# How to set up a resource property

Resource Property (msDS-ResourceProperty) resides in msDS-ResourceProperties container, and is used to classify files on Windows Server 2012 File Server as well as used in central access rule expression.

### Prerequisites

You must set up the default permissions.

-   Read: All authenticated users.
-   Write: Enterprise Administrator.

## Instructions

### Step 1: Validations and recommendations

This is the unique ID of a resource property.

**Resource property ID (name)**

1.  Keep the ID short as it will be included in the security descriptors. We recommend that the maximum number of characters be less than or equal to 41 characters.
2.  We recommend keeping the format of the ID consistent with what Active Directory module for PowerShell enforces. The ID must:

    -   start with 1 to 15 characters
    -   be followed by an underscore
    -   be followed by 1 to 16 characters
    -   does not contain word spaces, \\, \*, ?, ", &lt;, &gt;, \|

    An example is "BusinessImpact\_85DF".

**Enabled**

-   This attribute indicates if a resource property is enabled, which means that it is shown in the File Server and ACL UI.

**Share suggested values with (msDS-ClaimSharesPossibleValuesWith)**

1.  This attribute is used to indicate that the resource property is referencing a claim type for its possible values. If the resource property is referencing a claim type:

    -   Its value type must be compatible with claim type’s value type (See Resource Property Value Type section for the mapping.)
    -   Its suggested value must not exist as it should share claim type’s suggested value.
    -   The referenced claim type must exist and be valid for the resource property to be valid.
    -   The referenced claim type must have suggested values.

2.  Suggested values (msDS-ClaimPossibleValues): This is a list of values that are suggested to the user when assigning value for each resource properties. This attribute contains a XML blob that describes multiple suggested value entries. Each suggested value entry includes following 4 major elements:

    -   ValueGUID: The alternative ID assigned to a suggested value. This is optional to be assigned. It can be used by additional work-flows for localization key.
    -   ValueDisplayName: The display name of the value. This will be displayed in ACL UI and File Server out of the box. It is recommended to require user fill this when they are creating suggested values. It is also recommended to keep this value unique. It is also recommended to provide a length restriction so the value will be displayed properly. For example, 255 characters limit is used by Active Directory Administrative Center for this field reserving 1 character for ending character (total 256 characters).
    -   ValueDescription: This is the description of the value, and optional. It is recommended to set a restriction for the description to limit the size of the blob. For example, 1023 characters limit is used by Active Directory Administrative Center for this field reserving 1 character for ending character (total 1024 characters).
    -   Value: This is the unique value of each entry. Uniqueness must be checked to ensure the integrity of the data. This field only supports following resource property value type:

        -   MS-DS-OrderedList - must be an integer value
        -   MS-DS-MultiValuedChoice - suggested value must not exist as it should share claim type’s suggested value
        -   MS-DS-SingleValuedChoice

        Only if a resource property value type (msDS-ValueTypeReference) is of the above three supported suggested value type, it is a valid resource property. For a full list of supported value types for resource properties, see the Value Type Class section. The total size of the XML must not exceed 1024\*1024 bytes.

3.  Value Space Restricted (msDS-ClaimIsValueSpaceRestricted) This attribute is used in downstream UI to determine if a user can enter values other than suggested values. Following combinations are the ones that ACL UI and File Server support. This is recommended to allow user to only enter following valid combination if you want to leverage these downstream UIs.

    -   If Suggested Value exists, Value space restricted is set to **true**.
    -   If Suggested Value doesn't exist, Value space restricted is set to **false**.

### Step 2: Resource property value type (msDS-ValueTypeReference)

This attribute describes resource property syntax. It refers to an msDS-ValueType object that describes the value type of this resource property. In Windows Server 2012, File Server only recognizes a list of out-of-the-box msDS-ValueType. Thus, msDS-ValueTypeReference must refer to one of the out-of-the-box value types.

### Step 3: Value type class (msDS-ValueType)

Value type includes the following attributes:

-   Name
-   Is single valued (msDS-ClaimIsSingleValued) - this attribute indicates whether a resource property can hold multiple values.
-   Value type (msDS-ClaimValueType) - This is the primary syntax of a resource property. A claim type and a resource property in an ACL expression or central access rule can only be compared if they have matching value type.
-   Must have suggested values (msDS-IsPossibleValuesPresent) - This attribute indicates whether a resource property has suggested values.

    -   When this is set to true, the resource property must have Suggested Values.
    -   When it is false, the resource property must not have Suggested Values.

-   Is Value Space Restricted (msDS-ClaimIsValueSpaceRestricted) - Similar to its use in claim type, this attribute is used in downstream UI. It determines whether a user can enter more data other than the ones in the suggested values.

### Step 4: Applies to Resource Types (msDS-AppliesToResourceTypes)

This multi-valued attribute describes what type of resource the property will apply to. One can supply any string in this field. File Server only supports two options, "Container" and "Object". When this attribute contains "Container", the property can be applied to a file folder. When this attribute contains "Object", the property can be applied to files.

By default we use a container and object for any resource types used for authorization.

### Step 5: Is Used for Authorization (msDS-IsUsedAsResourceSecurityAttribute)

When this attribute is set to **true**, the resource property can be used in central access policy and DACL for authorization purposes. By default, this is set to **true** except for .when the msDS-ValueTypeReference is set to "DateTime", or any other value other than the [out-of-the-box value types](#out-of-the-box-msds-valuetype-values), this field must be **false**, as "DateTime" is not a supported in ACL UI.

### Step 6: Resource Property List (msDS-ResourcePropertyList)

Resource property list is an object that contains multiple resource properties as its member (msDS-MembersOfResourcePropertyList). It is used to group resource properties, so that they can be published to different clients and file servers by using group policy. This allows the file administrator or content owner to see only the relevant resource properties instead of being confused by additional irrelevant resource properties. For example, the list of resource properties on financial department file servers may be different from the ones on human resource file servers. "Global Resource Property List" is used as a global list by Windows Server 2012. You should add all the newly created resource properties to that list to keep that expectation.

## Remarks

### Out-of-the-box msDS-ValueType values

The following is a list of the out-of-the-box msDS-ValueType values:

-   **MS-DS-YesNo**

    Indicates the Boolean value mentioned for the AD Property Definition.

    msDS-ClaimIsSingleValued: True

    msDS-ClaimValueType: **BOOL**

    msDS-IsPossibleValuesPresent: False

    msDS-ClaimIsValueSpaceRestricted: No

-   **MS-DS-Number**

    Specifies the integer value of the AD Property Definition.

    msDS-ClaimIsSingleValued: True

    msDS-ClaimValueType: **INT**

    msDS-IsPossibleValuesPresent: False

    msDS-ClaimIsValueSpaceRestricted: No

-   **MS-DS-DateTime**

    Specifies the date and time of the AD Property Definition. This value type cannot be used in authorization.

    msDS-ClaimIsSingleValued: True

    msDS-ClaimValueType: **INT**

    msDS-IsPossibleValuesPresent: False

    msDS-ClaimIsValueSpaceRestricted: No

-   **MS-DS-OrderedList**

    Specifies the list of integer type possible values of the AD Property Definition. You should provide a default interval in between user input, so a new item can be inserted later on easily.

    msDS-ClaimIsSingleValued: True

    msDS-ClaimValueType: **INT**

    msDS-IsPossibleValuesPresent: True

    msDS-ClaimIsValueSpaceRestricted: Yes

-   **MS-DS-Text**

    Specifies an arbitrary string value provided for an AD Property Definition.

    msDS-ClaimIsSingleValued: True

    msDS-ClaimValueType: **STRING**

    msDS-IsPossibleValuesPresent: False

    msDS-ClaimIsValueSpaceRestricted: No

-   **MS-DS-MultiValuedChoice**

    Specifies the list of string type possible values of the AD Property Definition.

    msDS-ClaimIsSingleValued: True

    msDS-ClaimValueType: **STRING**

    msDS-IsPossibleValuesPresent: True

    msDS-ClaimIsValueSpaceRestricted: Yes

-   **MS-DS-MultiValuedChoice**

    Specifies the list of string type possible values of the AD Property Definition.

    msDS-ClaimIsSingleValued: False

    msDS-ClaimValueType: **STRING**

    msDS-IsPossibleValuesPresent: False

    msDS-ClaimIsValueSpaceRestricted: No

-   **MS-DS-MultiValuedChoice**

    Specifies one or more arbitrary string values provided for an AD Property Definition.

    msDS-ClaimIsSingleValued: False

    msDS-ClaimValueType: **STRING**

    msDS-IsPossibleValuesPresent: True

    msDS-ClaimIsValueSpaceRestricted: Yes

## Related topics

<dl> <dt>

[How to use central access policies for dynamic access control (Intro Page)](how-to-use-central-access-policies-for-dynamic-access-control.md)
</dt> </dl>

 

 




