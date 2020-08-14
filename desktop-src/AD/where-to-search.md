---
title: Deciding Where to Search
description: This topic explains the different searches that can be performed in Active Directory Domain Services.
ms.assetid: 4b7428c8-c246-41fc-8811-892220c4270f
ms.tgt_platform: multiple
keywords:
- Deciding Where to Search AD
- Active Directory AD , Searching, Deciding Where to Search
ms.topic: article
ms.date: 05/31/2018
---

# Deciding Where to Search

This topic explains the different searches that can be performed in Active Directory Domain Services.

All searches are performed in one of the following naming contexts:

-   Domain, including application directory partitions
-   Schema container
-   Configuration container
-   Global catalog

## Searching a Domain

Domains contain most of the highly used objects such as users, contacts, groups, organizational units, computers, and so on. Most queries will search a domain. For more information about searching a domain, see [Searching Domain Contents](searching-domain-contents.md).

## Searching the Schema Container

The schema container contains the [**classSchema**](/windows/desktop/ADSchema/c-classschema) and [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) objects that provide the formal definition of every class and attribute that can exist in Active Directory Domain Services. To search for objects in the schema container, bind to the schema container on any domain controller. The schema container is available on all domain controllers. The distinguished name of the schema container is obtained from the **schemaNamingContext** attribute from rootDSE. For more information about rootDSE and the **schemaNamingContext** attribute, see [Serverless Binding and RootDSE](serverless-binding-and-rootdse.md).

For more information about reading from the schema or abstract schema container, see [Guidelines for Binding to the Schema](guidelines-for-binding-to-the-schema.md).

## Searching the Configuration Container

The configuration container contains configuration information, such as sites, services and display specifiers, for the entire forest. To search for objects in the configuration container, bind to the configuration container on any domain controller. The configuration container is available on all domain controllers. The distinguished name of the configuration container is obtained from the **configurationNamingContext** attribute from rootDSE. For more information about rootDSE and the **configurationNamingContext** attribute, see [Serverless Binding and RootDSE](serverless-binding-and-rootdse.md).

## Searching the Global Catalog

The global catalog holds a replica of every object in Active Directory Domain Services, but with only a small number of their attributes. The attributes in the global catalog are those most frequently used in search operations, such as a user's first and last names, login names, and so on. For more information about searching the global catalog, see [Searching the Global Catalog](searching-global-catalog-contents.md).

 

 