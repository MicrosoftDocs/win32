---
description: In many scenarios, role-based security is a very effective mechanism, but there are situations where it is less effective.
ms.assetid: 6a1e6cf3-7a8c-4249-926d-675a54061adf
title: Designing Roles Effectively
ms.topic: article
ms.date: 05/31/2018
---

# Designing Roles Effectively

In many scenarios, role-based security is a very effective mechanism, but there are situations where it is less effective. You should take a number of factors into consideration when deciding where and how to apply role-based security to a particular application.

## User and Data Characteristics and the Suitability of Roles

Roles work very well to characterize groups of users and, on that basis, filter what actions those users can perform. Often, this is carried out in practice by creating roles that reflect a user's place within an organization—for example, the roles "Managers" and "Tellers," "Administrators" and "Readers," "Project One Employees" and "Project Two Employees." In such cases, where the data being accessed is fairly generic relative to the users, roles can be used efficiently to enforce business rules such as the following:

-   "Managers can transfer any amount of money. Tellers can transfer only up to $10,000."

-   "Administrators can change anything. Everyone else can only read."

-   "Project One employees can access a certain database. No one else can."

Users might naturally fall into multiple roles, depending on how the roles model the organizational structure of a business.

However, roles don't work very well when a security access decision rests on the characteristics of a particular piece of data. For example, it would be difficult to use roles to reflect complicated user-data relationships such as the following:

-   "A particular manager can access personnel data for only her reports."

-   "Joe Consumer can look up his account balance."

In such cases, security checking must often be done at the database itself, where it is easier to take into account innate characteristics of the data being accessed. This means that you must use *impersonation* to pass the client identity along to the database and let the database validate the request. This can affect performance and can affect the application's design—for example, connection pooling might not work when a connection is opened under a particular user identity. For a discussion of issues involved, see [Multi-Tier Application Security](multi-tier-application-security.md) and [Client Impersonation and Delegation](client-impersonation-and-delegation.md).

## Complexity and Scalability of a Role-Based Authorization Policy

Whatever security policy you put in place will be only as effective as its implementation by the system administrators deploying your application. If administrators make mistakes in assigning users to the correct roles according to your security policy, your policy won't work as intended. Problems are most likely to occur under the following circumstances:

-   You have made a very intricate role-based policy, with many roles and users mapping to numerous roles.
-   You create roles with ambiguous criteria for who should belong to them.
-   There are many users at the site where the application is installed, and users are frequently moving within the organization, changing with respect to the roles you have created.
-   There are many administrators at the site where the application is installed, with division of responsibilities, so that an administrator familiar with the security requirements of your application is potentially unfamiliar with the large groups of users that must use it. This is of particular concern as users move within the organization—such information needs to be well communicated.

Additionally, as the number of roles assigned to an application increases, so does the amount of time COM+ must spend looking up caller membership in those roles, with a likely degradation in performance.

To manage complexity and mitigate these concerns, you can use the following guidelines:

-   Choose role names that are self-descriptive. Make it as obvious as possible which users should belong to which roles.
-   Make your role-based policy as simple as possible (and no simpler). Choose as few roles as you can, while maintaining an effective policy.
-   Clearly document the role-based policy that you construct for administrators, whether role membership is obvious (to you). In particular, use the description field available for each role to describe the intent of the role. If you can't describe generally who should belong to the role in a couple of sentences, it is probably too complicated.
-   Strongly suggest that administrators of your application populate roles with user groups instead of individual users. This is a much more scalable solution. It makes it easier to reassign or remove users as they move within the organization and insulates administrators from a certain amount of oversight and problems in communication.

## Related topics

<dl> <dt>

[Security Boundaries](security-boundaries.md)
</dt> <dt>

[Security Call Context Information](security-call-context-information.md)
</dt> <dt>

[Security Context Property](security-context-property.md)
</dt> <dt>

[Using Roles for Client Authorization](using-roles-for-client-authorization.md)
</dt> </dl>

 

 



