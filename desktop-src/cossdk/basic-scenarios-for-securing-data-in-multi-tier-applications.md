---
description: This topic presents a few building-block scenarios, illustrating the criteria discussed in Deciding Where to Enforce Security.
ms.assetid: e9820e53-8891-4bff-a333-00ad2dbb03a4
title: Basic Scenarios for Securing Data in Multi-Tier Applications
ms.topic: article
ms.date: 05/31/2018
---

# Basic Scenarios for Securing Data in Multi-Tier Applications

This topic presents a few building-block scenarios, illustrating the criteria discussed in [Deciding Where to Enforce Security](deciding-where-to-enforce-security.md).

## Trusted Server Scenario

-   The database fully trusts the COM+ application to authenticate and authorize end users to access data in the database.
-   Preferably, the database is secured against any access except through the application.
-   The COM+ application uses role-based security to authorize users.
-   Connections are opened under the COM+ application's identity and are fully poolable.
-   Auditing and logging can be done by the COM+ application, or this information can be passed into the database by the application.

This scenario works best for data that can be accessed by predictable categories of users that can be encapsulated in roles. For example, only "Managers," "Tellers," and "Accountants" have permission to access accounts. The business logic of what precisely each is enabled to do is enforced in the middle tier.

## Impersonation Scenario

-   The database does its own authentication and authorization of end users to help limit access to data in the database.
-   The COM+ application impersonates clients whenever it is accessing the database.
-   Connections are made on a per-call basis and can't be reused.

This scenario works best for data that is closely bound to very small classes of users. For example, each employee can access only his own personnel file, and each manager can access only the personnel files of her reports.

## Hybrid Scenario

A combination of the preceding two scenarios, where impersonation is used only when it is needed.

This scenario works best in situations where you have hybrid user-data relationships. For example, you have "Managers," "Tellers," "Accountants," and thousands of individual Web clients who can access just their own accounts. You can separate logic paths through the application, potentially with separate components, to handle the latter class of users, particularly where performance assumptions for those users are different.

## Trusted Scenario Using Microsoft SQL Server Roles

-   Microsoft SQL Server 7.0 and later can authorize access to specific rows using roles but trusts the COM+ application to authenticate and authorize users and to map them to the correct roles in the database.
-   The COM+ application authorizes users using role-based security, and the application roles correspond well to database roles.
-   Connections can be opened that are specific to a particular database role. These connections can be reused if they are held by pooled objects in the COM+ applications. For details on how to do this, see [COM+ Object Pooling](com--object-pooling.md).
-   Auditing and logging can be done by the COM+ application, or this information can be passed in to the database by the application.

This scenario works best for generally the same kinds of users and data as in the first trusted server scenario because the COM+ application is still being largely trusted to handle authorization correctly. However, it does help protect the database against unauthorized access while allowing access potentially from multiple sources outside the COM+ application, without incurring the scaling and performance penalties present with the impersonation scenario.

## Related topics

<dl> <dt>

[Deciding Where to Enforce Security](deciding-where-to-enforce-security.md)
</dt> <dt>

[Multi-Tier Application Security](multi-tier-application-security.md)
</dt> </dl>

 

 



