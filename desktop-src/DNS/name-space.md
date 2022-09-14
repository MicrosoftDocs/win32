---
title: Namespace
description: A namespace is a context within which the names of all objects must be unambiguously resolvable.
ms.assetid: 7731f6b5-1efa-43bc-bd31-9b5183ec90dc
ms.topic: article
ms.date: 05/31/2018
---

# Namespace

A namespace is a context within which the names of all objects must be unambiguously resolvable. For example, the internet is a single DNS name space, within which all network devices with a DNS name can be resolved to a particular address (for example, `www.microsoft.com` resolves to 207.46.131.13).

## Flat namespace

A namespace can be flat or hierarchical. A flat namespace doesn't scale well because it can grow only so large before all available names are used up. Once a name is used more than once in a namespace, the namespace violates the unambiguously resolvable requirement.

## Hierarchical namespace

A hierarchical namespace is divided into different areas, which can be thought of as sub-namespaces. Each area is its own sub-namespace within the overall namespace. Therefore, each object must have a unique name only within its sub-namespace in order to have an unambiguously resolvable name within the namespace hierarchy. Hierarchical namespaces, then, can scale to extremely large networks&mdash;as you add more objects to the overall name space, you have to find unique names for them within only the sub-namespace to which they belong.

All DNS namespaces are hierarchical. The sub-namespaces in the DNS hierarchical namespace are called *domains*. The unique name of a computer within a domain is called a *relative distinguished name*. Computers with the same relative distinguished name can exist in different sub-namespaces (domains) of the namespace hierarchy because they can be fully resolved to a unique object within the entire DNS hierarchy, using a fully-qualified domain name (FQDN). For example, you could have a server named *server1* in the *widgets.microsoft.com* domain (the *widgets.microsoft.com* namespace), and you could have *server1* in the *gadgets.widgets.microsoft.com* namespace. Because they are in different sub-namespaces in the hierarchical namespace, they can be resolved to different FQDNs&mdash;*server1.widgets.microsoft.com* and *server1.gadgets.widgets.microsoft.com*.
