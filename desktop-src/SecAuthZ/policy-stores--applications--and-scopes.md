---
description: Authorization policy stores, applications, and scopes represent different levels of organization of Authorization Manager policy.
ms.assetid: 235f236d-59c9-4a8c-aec6-60d1ddba4d5d
title: Policy Stores, Applications, and Scopes
ms.topic: article
ms.date: 05/31/2018
---

# Policy Stores, Applications, and Scopes

Authorization policy stores, applications, and scopes represent different levels of organization of Authorization Manager policy. A policy store can contain one or more applications, and an application can contain one or more scopes.

-   [Authorization Policy Stores](#authorization-policy-stores)
-   [Applications](#policy-stores-applications-and-scopes)
-   [Scopes](#policy-stores-applications-and-scopes)
-   [Delegation](#delegation)
-   [Related topics](#related-topics)

## Authorization Policy Stores

In the Authorization Manager API, an authorization policy store is represented by an [**IAzAuthorizationStore**](/windows/desktop/api/Azroles/nn-azroles-iazauthorizationstore) object. The authorization policy store contains definitions and assignments of applications, scopes, operations, tasks, roles, and user groups.

An authorization policy store can be stored either as an XML file or in Active Directory.

An application must initialize an authorization policy store before changing information in the store or using the store policy to check client access to resources.

An authorization policy store can contain one or more [**IAzApplication**](/windows/desktop/api/Azroles/nn-azroles-iazapplication) objects that each represent authorization policy for a specific application.

## Applications

In the Authorization Manager API, an application is represented by an [**IAzApplication**](/windows/desktop/api/Azroles/nn-azroles-iazapplication) object. An authorization policy store can contain authorization policy information for many applications. Using **IAzApplication** objects allows you to store different authorization policy for different applications in a single policy store.

An authorization policy store must contain at least one application.

## Scopes

In the Authorization Manager API, a scope is represented by an [**IAzScope**](/windows/desktop/api/Azroles/nn-azroles-iazscope) object. Scopes provide an additional, optional level of organization for an authorization policy. An application can contain one or more scopes, but need not contain any (Authorization Manager provides a default, application-wide scope).

A scope is a subdivision within an application that separates resources from other resources that are used by that application. If you have Authorization Manager groups, role assignments, role definitions, or task definitions that you do not want to apply to an entire application, you can create them at the scope level.

## Delegation

Authorization policy stores that are stored in Active Directory support delegation of administration. Administration can be delegated to users and groups at the store, application, or scope level. Each level defines administrative roles for the policy at that level. To delegate control to a user or group, assign them to the administrator role; to allow a user or group to read the policy, assign them to the reader role.

Administrators of a store, application, or scope can read and modify the policy store at the delegated level. Readers can read the policy store at the delegated level but cannot modify the store.

## Related topics

<dl> <dt>

[Creating an Authorization Policy Store Object in C++](creating-an-authorization-policy-store-object-in-c--.md)
</dt> <dt>

[Creating an Application Object in C++](creating-an-application-object-in-c--.md)
</dt> <dt>

[Delegating the Defining of Permissions in C++](delegating-the-defining-of-permissions-in-c--.md)
</dt> </dl>

 

 



