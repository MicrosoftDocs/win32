---
title: NetShell
description: NetShell, a scriptable command line-based tool, enables administrators to remotely administer and configure critical network services.
ms.assetid: '237a1422-8126-4b93-a023-4cb0f93fe603'
keywords: ["NetShell Netsh", "Netshell Netsh , start page"]
---

# NetShell

## Purpose

NetShell is a command line–based tool that enables administrators to remotely administer and configure critical network services. The NetShell command-line interface is scriptable, which enables administrators to carry out batch configurations or management tasks from a single, centralized location.

NetShell operates on the basis of contexts. A context collects administrative activities for a given area of networking functionality. Contexts are generally implemented through a NetShell helper, which is a DLL file that provides the capabilities for a given context.

The Microsoft Windows Software Development Kit (SDK) defines the NetShell API - a collection of functions, structures, and specifications for creating helper DLLs to extend the core functionality of NetShell on Microsoft Windows operating systems.

## Where applicable

NetShell is appropriate for creating scriptable contexts that enable administrators to manage and configure critical network services. The NetShell API is appropriate for developers who want to create contexts, and thereby, enable scriptable administration of network components.

## Developer audience

The NetShell API is designed for use by C/C++ programmers. Familiarity with Windows networking is required.

## Run-time requirements

Netshell is supported on the Windows XP, Windows Vista and Windows Server 2003.

The NetShell API can be dynamically linked through Dhcpcsvc.dll.

## In this section



| Topic                                           | Description                                                                                    |
|-------------------------------------------------|------------------------------------------------------------------------------------------------|
| [Overview](overview-of-netshell.md)<br/> | General information about NetShell, including explanations of contexts and helpers.<br/> |
| [Reference](netshell-reference.md)<br/>  | Reference documentation for NetShell.<br/>                                               |



 

 

 





