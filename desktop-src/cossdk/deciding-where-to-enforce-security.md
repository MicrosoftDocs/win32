---
description: Trade-offs are inherent in enforcing security.
ms.assetid: f01573f3-aae6-400e-bdd9-6f34f4e262f6
title: Deciding Where to Enforce Security
ms.topic: article
ms.date: 05/31/2018
---

# Deciding Where to Enforce Security

Trade-offs are inherent in enforcing security. A database can be a natural place to put security logic, given that ultimately that data is the most important thing to protect. However, doing so has significant performance implications. Enforcing security at the database can be very expensive, scales poorly, and is inflexible.

## Enforcing Security in the Middle Tier

The general rule to follow with scalable multi-tier applications using COM+ is that, whenever possible, you should enforce detailed security in the COM+ application at the middle tier. Doing so enables you to fully leverage the scalable services provided by COM+. Enforce authentication at the database only when you absolutely need to, and fully weigh the performance implications of doing so.

The optimal situation is to be able to secure database tables so that the COM+ application is able to access them under its own identity. The database should just authenticate the COM+ application and trust it to correctly authenticate and authorize clients that will be accessing data. The benefits of this approach are as follows:

-   It enables connection pooling among all clients, as connections are completely generic.
-   It generally optimizes data access, often a problematic choke point when scaling applications.
-   It can minimize the logic overhead for enforcing security, particularly if declarative role-based security can be used.
-   It can provide great flexibility in a security policy. You can configure and reconfigure it easily, as described in [Role-Based Security Administration](role-based-security-administration.md).

But, as discussed in [Designing Roles Effectively](designing-roles-effectively.md), while roles can be easily and effectively applied to some user-data relationships, they are not a universal solution for security access decisions.

## Enforcing Security at the Database

Despite the preferability of enforcing security at the middle tier, there are a number of reasons to enforce security at the database, such as the following:

-   You don't have a choice, perhaps for legacy reasons or perhaps because the decision is simply not in your hands.
-   The database is accessed by a wide variety of applications, and its security can't be configured on the basis of a single application.
-   A database can be made predictably protected. If you keep enterprise-critical data in a database, you can draw a tight wagon around it and help control who gets to see it.
-   Authenticating original clients at the database enables detailed logging of who has done what in the database.
-   Some data is innately bound to particular users, and the logic of making extremely fine-grained access decisions might be most efficiently carried out at the database itself, close to the data.

When you do have the luxury of designing the security of the database and the COM+ application in tandem, most of these issues pertain to characteristics of the data itself and its relationship to the users accessing it. With data that can be accessed by predictable categories of users, it is efficient to control access in the middle tier using roles. With data that is intricately bound to very small classes of users, those relationships must often be expressed with the data itself and hence you must enforce some security at the database.

### Performance Implications of Enforcing Security at the Database

If you authenticate or authorize users at the database, the user identity needs to be propagated through to the database to support this. If the database trusts the middle-tier application to do so, it is possible to pass in user security information in parameters. Otherwise, the call through to the database must be made under the user's identity, meaning that the server application must impersonate the client. This can have performance implications such as the following:

-   Impersonating the client can be much slower than making the call directly under the application identity. For more detail, see [Client Impersonation and Delegation](client-impersonation-and-delegation.md).
-   A database connection made under a specific user identity cannot be pooled.
-   Adding logic in the database itself runs the risk of creating a scaling bottleneck.

## Related topics

<dl> <dt>

[Basic Scenarios for Securing Data in Multi-Tier Applications](basic-scenarios-for-securing-data-in-multi-tier-applications.md)
</dt> <dt>

[Multi-Tier Application Security](multi-tier-application-security.md)
</dt> </dl>

 

 



