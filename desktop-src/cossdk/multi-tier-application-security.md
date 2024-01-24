---
description: Multi-Tier Application Security
ms.assetid: ff84eeed-ddfd-40e8-8f42-625b4d49ecd5
title: Multi-Tier Application Security
ms.topic: article
ms.date: 05/31/2018
---

# Multi-Tier Application Security

You can face difficult choices in deciding precisely where to enforce security in a multi-tier, component-based application: At the database? At the middle tier? In the components? Somewhere else? Everywhere? As security mechanisms increase in number and complexity, performance declines and application behavior becomes less predictable. Nevertheless, you must ensure that data is protected, business rules are followed, and significant activity is logged, and still have your application work for clients as intended. You must be certain that every client path through your application is correct and that the security checkpoints you have in place will suffice.

The hardest decision is often whether to enforce security at the database. Historically, this is where security is tightest because it is perceived as the one kingdom that needs to be truly secure, and database administrators are very reluctant to trust someone else to enforce security for them. But enforcing security at the database can be quite expensive and difficult to scale, which is precisely the point of writing multi-tier applications in the first place.

The general rule to follow with scalable multi-tier applications using COM+ is that, whenever possible, you should enforce detailed security in the COM+ application at the middle tier. Doing so enables you to fully leverage the scalable services provided by COM+. Authenticate at the database only when you absolutely need to, and fully weigh the performance implications of doing so.

For a discussion of issues to consider in deciding where to perform security checks, see [Deciding Where to Enforce Security](deciding-where-to-enforce-security.md).

For a discussion of some basic scenarios in securing multi-tier applications, see [Basic Scenarios for Securing Data in Multi-Tier Applications](basic-scenarios-for-securing-data-in-multi-tier-applications.md).

## Related topics

<dl> <dt>

[Client Authentication](client-authentication.md)
</dt> <dt>

[Client Impersonation and Delegation](client-impersonation-and-delegation.md)
</dt> <dt>

[Library Application Security](library-application-security.md)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> <dt>

[Role-Based Security Administration](role-based-security-administration.md)
</dt> <dt>

[Using the Software Restriction Policy in COM+](using-the-software-restriction-policy-in-com-.md)
</dt> </dl>

 

 



