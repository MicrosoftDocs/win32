---
title: Name Space
description: A name space is a context within which the names of all objects must be unambiguously resolvable.
ms.assetid: 7731f6b5-1efa-43bc-bd31-9b5183ec90dc
ms.topic: article
ms.date: 05/31/2018
---

# Name Space

A name space is a context within which the names of all objects must be unambiguously resolvable. For example, the Internet is a single DNS name space — within which all network devices with a DNS name can be resolved to a particular address: for example, www.microsoft.com to 207.46.131.13.

## Flat Name Spaces

Name spaces can be flat or hierarchical. Flat name spaces do not scale well because they can grow only so large before all available names are used up. Once a name is used more than once in a name space, the name space violates the unambiguously resolvable requirement.

## Hierarchical Name Space

A hierarchical name space is divided into different areas, which can be thought of as subname spaces. Each area is its own subname space within the overall name space. Therefore, each object must have a unique name only within its subname space in order to have an unambiguously resolvable name within the name space hierarchy. Hierarchical name spaces, then, can scale to extremely large networks — as you add more objects to the overall name space, you have to find unique names for them within only the subname space to which they belong.

All DNS name spaces are hierarchical. The subname spaces in the DNS hierarchical name space are called *domains*. The unique name of a computer within a domain is called a *relative distinguished name*. Computers with the same relative distinguished name can exist in different subname spaces (domains) of the name space hierarchy because they can be fully resolved to a unique object within the entire DNS hierarchy, using an Fully Qualified Domain Name (FQDN). For example, you could have a server called server1 in the widgets.microsoft.com domain (the widgets.microsoft.com name space), and you could have server1 in the gadgets.widgets.microsoft.com name space. Because they are in different subname spaces in the hierarchical name space, they can be resolved to different FQDNs: server1.widgets.microsoft.com and server1.gadgets.widgets.microsoft.com.

 

 




