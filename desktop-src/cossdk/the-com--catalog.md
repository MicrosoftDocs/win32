---
description: The COM+ catalog stores COM+ application attributes, class attributes, and computer-level attributes. It guarantees consistency among these attributes and provides common operations on top of these attributes.
ms.assetid: '1838757c-aa8e-4678-8042-207498fb0bbc'
title: The COM+ Catalog
ms.topic: article
ms.date: 05/31/2018
---

# The COM+ Catalog

The COM+ catalog stores COM+ application attributes, class attributes, and computer-level attributes. It guarantees consistency among these attributes and provides common operations on top of these attributes.

The COM+ catalog uses two different stores, as follows:

-   The COM+ registration database
-   The Windows registry (**HKEY\_CLASSES\_ROOT**)

The catalog presents a unified, logical view of these two stores and exposes them through the COM+ Administration Library. This library provides, through a scripting language, all the functionality of the Component Services administrative tool.

For existing COM components that do not require any new COM+ services, lookup occurs in the existing Windows registry. The COM+ catalog also uses the Windows registry for type library and interface proxy/stub registration.

## Split Registration

For new components that are actually already existing COM components that are used in the services environment (for example, MTS components), the basic COM aspect of the registration is stored in the Windows registry and new services and attributes (for example, queued components) are stored in the COM+ registration database. This is known as a *split registration*.

Each attribute is stored in only one location: either the Windows registry or the COM+ registration database. New COM components are registered exclusively in the COM+ registration database, with some duplication in the Windows registry so that existing tools can use them.

## Transactional Updates to the Catalog

Some operations on the catalog are performed in a transactional manner. When you invoke the COM+ Administration Library from a transactional component, the updates to the COM+ registration database will take place within the calling component's transaction boundary.

However, updates that involve changes to other stores (such as the file system and Windows registry) are not guaranteed to be fully transactional. An aborted transaction can leave these stores in a state that is inconsistent with any changes made to one another or to the COM+ registration database.

## Related topics

<dl> <dt>

[Creating Installation Packages for COM+ Applications](creating-installation-packages-for-com--applications.md)
</dt> <dt>

[Deploying Application Proxies](deploying-application-proxies.md)
</dt> <dt>

[The COMREPL Replication Utility](the-comrepl-replication-utility.md)
</dt> </dl>

 

 



