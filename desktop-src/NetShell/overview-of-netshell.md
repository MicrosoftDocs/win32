---
title: Overview of NetShell
description: NetShell is a scriptable command line-based tool that enables administrators to remotely administer and configure critical network services.
ms.assetid: '237f46e1-c4ce-4dd0-a516-23675bb2e521'
keywords: ["NetShell NetSh , described"]
---

# Overview of NetShell

NetShell is a command line–based tool that enables administrators to remotely administer and configure critical network services. The NetShell command-line interface is scriptable, which enables administrators to carry out batch configurations or administration from one centralized location.

This document explains how to create NetShell contexts that operate with NetShell on Windows XP operating systems. This document is not intended to be a complete treatment of NetShell, its core functionality, or the contexts provided therein. For more information, see Windows XP Online Help or the Windows XP Resource Kit.

NetShell operates on the basis of *contexts*. A context collects administrative activities for a given area of networking functionality. Contexts are generally implemented through a NetShell *helper*. A helper is a DLL file that provides the capabilities for a given context. For example, Windows XP has a NetShell context for the Dynamic Host Configuration Protocol administration called *DHCP*. All NetShell commands associated with administering or configuring DHCP are grouped into the DHCP context. For more information, see [Components of NetShell](components-of-netshell.md).

NetShell is extensible. Windows XP includes the core functionality of NetShell, as well as many contexts that enable administrators to remotely manage various networking services. In addition to the contexts provided by Windows XP, developers can create additional contexts to manage networking services different from the contexts provided with Windows.

 

 




