---
description: Because the Windows Installer keeps all information about the installation in a relational database, the installation of an application or product can be customized for particular user groups by applying transform operations to the package.
ms.assetid: 98c5cda2-a01a-4bdd-840f-76c0ffacd194
title: Customization
ms.topic: article
ms.date: 05/31/2018
---

# Customization

Because the Windows Installer keeps all information about the installation in a relational database, the installation of an application or product can be customized for particular user groups by applying transform operations to the package. Transforms can be used to encapsulate the various customizations of a base package required by different workgroups. For more information, see [Merges and Transforms](merges-and-transforms.md).

Multiple transforms of a base package can be applied on-the-fly during installation. This provides a mechanism for efficiently assigning customized installations to different groups of users. For example, this would be useful in organizations where the finance and staff support departments require different installations of a particular product. The product can be made available to everyone in the organization by an [administrative installation](administrative-installation.md) of the base package to a single administrative installation point. Each work group can then automatically receive their appropriate customization by means of an on-the-fly transform when they install the product.

 

 



