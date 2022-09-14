---
title: Searching Domain Contents
description: Before discussing where to bind to begin a search for objects in a domain, it is helpful to understand how data is stored in Active Directory Domain Services.
ms.assetid: fd0b4556-465b-4338-87cb-375450590c44
ms.tgt_platform: multiple
keywords:
- domain contents Active Directory
- searching domain contents Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Searching Domain Contents

Before discussing where to bind to begin a search for objects in a domain, it is helpful to understand how data is stored in Active Directory Domain Services.

If you have a forest with more than one domain, Active Directory Domain Services does not store all object data on a single domain controller — for performance, scalability, and reliability reasons. A domain controller holds all information about only the domain that it is a member of (it has a full replica of the domain). But a domain controller does not hold complete information about any other domain.

If you bind to the domain object with referral chasing turned off, you can search for any object in that domain and only that domain. For more information about referral chasing, see [Referrals](referrals.md). A search can retrieve any property and can use a query filter containing any property.

In a forest, domains are arranged hierarchically as domain trees. A domain tree can be just a single domain or a domain with one or more child domains. These child domains, in turn, can have child domains beneath them. A domain tree is also a contiguous namespace. A contiguous namespace means that the child domains are a continuation of the naming hierarchy. For example, a domain fabrikam.com (or DC=Fabrikam, DC=COM) can have a child domain named mydivision (mydivision.fabrikam.com or DC=mydivision, DC=Fabrikam, DC=COM), which in turn could have a child domain named mydev (mydev.mydivision.fabrikam.com or DC=mydev, DC=mydivision, DC=Fabrikam, DC=COM).

If you bind to a domain object (with referral chasing turned on) for a domain within a domain tree, you will search that domain and the entire hierarchy within it. The search can retrieve any property and can use a query filter containing any property.

If a domain controller contains a full replica of only its own domain, you can perform a subtree search on a domain tree. A domain holds references to its child domains. When a domain controller processes a subtree search request against its own domain, the domain controller searches that domain and then returns referrals to each of its child domains to the client. A referral is the way that a directory server communicates that it does not contain the information required to complete a request (such as a query) but has a reference to a server that may contain the required information. In the case of a subtree search of a domain tree, a referral is returned for each direct child domain so that the search can be continued at a domain controller in each child domain. If referral chasing is turned on, the LDAP client library (Wldap32.dll) uses those referrals to bind to a domain controller in each child domain and continue the search. If referral chasing is turned off, the LDAP client does not resolve the referrals and the search is complete.

A subtree search on a domain tree with referral chasing turned on can be time-consuming if there is a slow connection to the domain controllers for the child domains. If you want to search only a single domain, you should turn referral chasing off to avoid having to search the child domains unnecessarily.

 

 




