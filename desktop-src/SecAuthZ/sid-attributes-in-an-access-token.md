---
description: Each user and group security identifier (SID) in an access token has a set of attributes that control how the system uses the SID in an access check. The following table lists the attributes that control access checking.
ms.assetid: c902f876-f05e-4b0c-ab65-a0c6cebca933
title: SID Attributes in an Access Token
ms.topic: article
ms.date: 05/31/2018
---

# SID Attributes in an Access Token

Each user and group [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID) in an [*access token*](/windows/desktop/SecGloss/a-gly) has a set of attributes that control how the system uses the SID in an access check. The following table lists the attributes that control access checking.



| Attribute                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SE\_GROUP\_ENABLED              | A SID with this attribute is enabled for access checks. When the system performs an access check, it checks for access-allowed and access-denied [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) that apply to one of the enabled SIDs in the access token. A SID without this attribute is ignored during an access check unless the SE\_GROUP\_USE\_FOR\_DENY\_ONLY attribute is set.<br/> |
| SE\_GROUP\_USE\_FOR\_DENY\_ONLY | A SID with this attribute is a deny-only SID. When the system performs an access check, it checks for access-denied ACEs that apply to the SID, but it ignores access-allowed ACEs for the SID. If this attribute is set, the SE\_GROUP\_ENABLED attribute is not set and the SID cannot be reenabled.<br/>                                                                                                                                                          |



 

To set or clear the SE\_GROUP\_ENABLED attribute of a group SID, use the [**AdjustTokenGroups**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokengroups) function. You cannot disable a group SID that has the SE\_GROUP\_MANDATORY attribute. You cannot use **AdjustTokenGroups** to disable the user SID of an access token.

To determine whether a SID is enabled in a token, that is, whether it has the SE\_GROUP\_ENABLED attribute, call the [**CheckTokenMembership**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-checktokenmembership) function.

To set the SE\_GROUP\_USE\_FOR\_DENY\_ONLY attribute of a SID, include the SID in the list of deny-only SIDs that you specify when you call the [**CreateRestrictedToken**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken) function. **CreateRestrictedToken** can apply the SE\_GROUP\_USE\_FOR\_DENY\_ONLY attribute to any SID, including the user SID and group SIDs that have the SE\_GROUP\_MANDATORY attribute. However, you cannot remove the deny-only attribute from a SID, nor can you use [**AdjustTokenGroups**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokengroups) to set the SE\_GROUP\_ENABLED attribute on a deny-only SID.

To get the attributes of a SID, call the [**GetTokenInformation**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) function with the TokenGroups value. The function returns an array of [**SID\_AND\_ATTRIBUTES**](/windows/desktop/api/Winnt/ns-winnt-sid_and_attributes) structures that identify the group SIDs and their attributes.

 

