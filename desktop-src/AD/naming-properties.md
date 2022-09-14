---
title: User Naming Attributes
description: User naming attributes identify user objects, such as logon names and IDs used for security purposes.
ms.assetid: 2192743c-cedd-4b03-a402-3992d64a4801
ms.tgt_platform: multiple
keywords:
- User Naming Attributes AD
ms.topic: article
ms.date: 05/31/2018
---

# User Naming Attributes

User naming attributes identify user objects, such as logon names and IDs used for security purposes. The **cn**, **name**, and **distinguishedName** attributes are examples of user naming attributes. A user object is a security principal object, so it also includes the following user naming attributes:

-   [userPrincipalName](#userprincipalname) — the logon name for the user
-   [objectGUID](#objectguid) — the unique identifier of a user
-   [sAMAccountName](#samaccountname) — a logon name that supports previous version of Windows
-   [objectSid](#objectsid) — security identifier (SID) of the user
-   [sIDHistory](#sidhistory) — the previous SIDs for the user object

> [!Note]  
> You can view and manage these attributes using the Active Directory User and Computers MMC snap-in, which is available in the [Remote Server Administration Tools (RSAT)](https://www.microsoft.com/download/details.aspx?id=45520).

 

## userPrincipalName

The **userPrincipalName** attribute is the logon name for the user. The attribute consists of a user principal name (UPN), which is the most common logon name for Windows users. Users typically use their UPN to log on to a domain. This attribute is an indexed string that is single-valued.

A UPN is an Internet-style login name for a user based on the Internet standard RFC 822. The UPN is shorter than a distinguished name and easier to remember. By convention, this should map to the user's email name. The point of the UPN is to consolidate the email and logon namespaces so that the user only needs to remember a single name.

### UPN Format

A UPN consists of a UPN prefix (the user account name) and a UPN suffix (a DNS domain name). The prefix is joined with the suffix using the "@" symbol. For example, "someone@ example.com". A UPN must be unique among all security principal objects within a directory forest. This means the prefix of a UPN can be reused, just not with the same suffix.

A UPN suffix has the following restrictions:

-   It must be the DNS name of a domain, but does not need to be the name of the domain that contains the user.
-   It must be the name of a domain in the current domain forest, or an alternate name listed in the **upnSuffixes** attribute of the Partitions container within the Configuration container.

### UPN Management

A UPN can be assigned, but is not required, when a user account is created. When a UPN is created, it is unaffected by changes to other attributes of the user object such as the user being renamed or moved. This allows the user to keep the same login name if a directory is restructured. However, an administrator can change a UPN. When you create a new user object, you should check the local domain and the global catalog for the proposed name to ensure it does not already exist.

When a user uses a UPN to log on to a domain, the UPN is validated by searching the local domain and then the global catalog. If the UPN is not found in the global catalog, the logon attempt fails.

## objectGUID

The **objectGUID** attribute is the unique identifier of a user. The attribute is a single-valued 128-bit Globally Unique Identifier (GUID), and is stored as an [**ADS\_OCTET\_STRING**](/windows/win32/api/iads/ns-iads-ads_octet_string) structure. The GUID is created by the Active Directory server when a user object is created.

Because an object's distinguished name changes if the object is renamed or moved, the distinguished name is not a reliable identifier of an object. In Active Directory Domain Services, an object's **objectGUID** attribute never changes, even if the object is renamed or moved. You can retrieve the string form of the **objectGUID** using the **GUID** property method in [IADs Property Methods](/windows/desktop/ADSI/iads-property-methods).

## sAMAccountName

The **sAMAccountName** attribute is a logon name used to support clients and servers from previous version of Windows, such as Windows NT 4.0, Windows 95, Windows 98, and LAN Manager. The logon name must be 20 or fewer characters and be unique among all security principal objects within the domain.

## objectSid

The **objectSid** attribute is the security identifier (SID) of the user. The SID is used by the system to identify a user and their group memberships during interactions with Windows security. The attribute is single-valued. The SID is a unique binary value used to identify the user as a security principal.

The SID is set by the system when the user is created. Each user has a unique SID issued by a Windows domain and stored in the **objectSid** attribute of the user object in the directory. Each time a user logs on, the system retrieves the user's SID from the directory and places it in the user's access token. The user's SID is also used to retrieve the SIDs for the groups of which the user is a member and places them in the user's access token. When a SID has been used as the unique identifier for a user or group, it cannot be used again to identify another user or group.

## sIDHistory

The **sIDHistory** attribute contains the previous SIDs for the user object. This is a multi-valued attribute. A user object has previous SIDs if the user was moved to another domain. Whenever a user object is moved to a new domain, a new SID is created and assigned the **objectSid** attribute, and the previous SID is added to the **sIDHistory** attribute.

## Related topics

<dl> <dt>

[User Object Attributes](user-object-attributes.md)
</dt> </dl>

 

 