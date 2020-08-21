---
title: Referrals (AD DS)
description: Active Directory Domain Services maintain referral data in crossRef objects stored in the partitions container (crossRefContainer) in the configuration container.
ms.assetid: e4d6cc8a-9c2c-4e0f-acca-e9ecdd5e879b
ms.tgt_platform: multiple
keywords:
- Referrals AD
- Active Directory, Referrals
ms.topic: article
ms.date: 05/31/2018
---

# Referrals (AD DS)

Active Directory Domain Services maintain referral data in [**crossRef**](/windows/desktop/ADSchema/c-crossref) objects stored in the partitions container ([**crossRefContainer**](/windows/desktop/ADSchema/c-crossrefcontainer)) in the configuration container. In the [Deciding Where to Search](where-to-search.md) topic, referrals are discussed in the context of a domain within a domain tree and the generation of referrals to subordinate domains on a subtree search.

Active Directory Domain Services create and maintains [**crossRef**](/windows/desktop/ADSchema/c-crossref) objects for all domains in the forest. In addition, there are **crossRef** objects for the configuration and schema containers. These **crossRef** objects are used to generate referrals in response to queries that request data about objects that exist in the forest, but not contained on the directory server handling the request. These are called *internal cross references*, because they refer to domains, schema, and configuration containers within the forest.

If referral chasing is not enabled and a subtree search is performed, the search will return all objects within the specified domain that meet the search criteria. The search will also return referrals to any subordinate domains that are direct descendants of the directory server domain. The client must resolve the referrals by binding to the path specified by the referral and submitting another query.

If referral chasing is turned on and a subtree search is performed, the underlying LDAP API will automatically attempt to bind to any referrals and add the search results to the result set. In most cases, the referral chasing will be transparent to the caller. If the referral is to an object in a different domain or forest, the underlying LDAP API will attempt to use the current credentials to bind to the target of the referral. If this is successful, the referral chasing will be transparent. If this is not successful, the referral and a referral error code will be returned.

For more information about setting the referral chasing search preference, see [Specifying Other Search Options](specifying-other-search-options.md).

In addition to the [**dnsRoot**](/windows/desktop/ADSchema/a-dnsroot) (DNS name of the domain) and [**nCName**](/windows/desktop/ADSchema/a-ncname) (distinguished name for the domain) properties, the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object also contains the **nETBIOSName** (NetBIOS name of the domain) and **trustParent** (distinguished name for the **crossRef** object that represents the domain's direct parent domain) properties.

Active Directory Domain Services can also have *external cross references* that refer to objects outside of the forest. External cross references must be added explicitly by an administrator. Be aware that the target server of the external cross reference must have a DNS root; that is, it must adhere to RFC 2247.

An external cross reference refers to an object on any other forest, as long as the name is unique in the target forest. For example, LDAP client applications that are used by your company can submit operations to your directory servers for Fabrikam.com. You create a [**crossRef**](/windows/desktop/ADSchema/c-crossref) object for Fabrikam.com. Now, instead of returning an Object Not Found error, your directory servers can return a referral to an object in the Fabrikam.com domain and the clients can chase the referral. For example, if you have an object with the following distinguished name:


```C++
CN=SomeObject,OU=SomeOU,DC=Fabrikam,DC=Com
```



You can add an external cross reference for an object with the name "ChildOfSomeObject".


```C++
CN=ChildOfSomeObject,CN=SomeObject,OU=SomeOU,DC=Fabrikam,DC=Com
```



A subtree search that contains "SomeObject" will also return a referral to "ChildOfSomeObject". Be aware that there must be an LDAP server at the address that is specified by the referral (one of the properties on the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object) and that this LDAP server must serve the namespace that is identified by "ChildOfSomeObject".

Because [**crossRef**](/windows/desktop/ADSchema/c-crossref) objects are stored in the configuration container, each domain controller (DC) has a copy of all **crossRef** objects. Therefore, every DC contains data about every domain in the forest as well as their superior/subordinate relationships. This enables each DC to generate referrals to any domain in the forest and referrals for unexplored subordinate domain, schema, or configuration containers on a subtree search.

For more information about referrals, see:

-   [When Referrals Are Generated](when-referrals-are-generated.md)
-   [Creating an External Referral](creating-an-external-referral.md)

For more information and a code example that shows how to obtain the distinguished name of the partitions container, see [Example Code for Locating the Partitions Container](example-code-for-locating-the-partitions-container.md).

 

 