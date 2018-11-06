---
title: DNS WMI Provider Overview
description: A provider is an architectural element of Windows Management Instrumentation (WMI).
ms.assetid: e6ada7b5-dd46-4c47-8db8-55f910429e31
keywords:
- Domain Name System, WMI provider, architecture
ms.topic: article
ms.date: 05/31/2018
---

# DNS WMI Provider Overview

A provider is an architectural element of *Windows Management Instrumentation (WMI)*. WMI defines a unified architecture for describing, accessing, and instrumenting objects. Part of this architecture is a large database of WMI classes used to carry out remote management tasks on specific objects.

WMI providers act as intermediaries between WMI and one or more managed objects. When WMI receives a request from a management application for data that is not available from the CIM repository or for notifications of events that WMI does not support, it forwards the request to a provider. Providers supply data and event notifications for managed objects that are specific to their particular domain. A provider extends the WMI schema of classes to allow WMI to work with new types of objects. The DNS WMI Provider defines classes for querying and configuring a DNS Server, along with its associated DNS zones and DNS records.

The DNS WMI provider exposes a number of DNS objects to clients, including DNS Server, DNS domain, and DNS RR objects. Through those objects, clients are able to perform DNS management activities.

Using the DNS WMI Provider, you can create your own tools to perform most DNS Server administration tasks. For example, you can create, delete, and view zones and records; reset server and zone properties; and perform routine administration operations such as updating the zone, reloading the zone, refreshing the zone, writing the zone back to a file or Active Directory, pausing and resuming the zone, clearing the cache, stopping and starting the DNS service, and viewing statistics.

The DNS WMI Provider has a set of unique behaviors not found in other providers. See the [DNS WMI Provider Reference](dns-wmi-provider-reference.md) for class details.

 

 




