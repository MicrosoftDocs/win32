---
title: Remote procedure call (RPC)
description: Microsoft Remote Procedure Call (RPC) defines a powerful technology for creating distributed client/server programs.
ms.assetid: 27c7c352-5fc1-47cf-99b1-fdf3eca986bc
keywords:
- RPC
- RPC, (See Remote Procedure Call)
- Remote Procedure Call RPC , start page
- Remote Procedure Call RPC
ms.topic: article
ms.date: 11/09/2021
ms.custom: seo-windows-dev
---

# Remote procedure call (RPC)

Microsoft Remote Procedure Call (RPC) defines a powerful technology for creating distributed client/server programs. The RPC run-time stubs and libraries manage most of the processes relating to network protocols and communication. This enables you to focus on the details of the application rather than the details of the network.

## Where is it applicable?

You can use RPC in all client/server applications based on Windows operating systems. It can also be used to create client and server programs for heterogeneous network environments that include such operating systems as Unix and Apple.

## Developer audience

RPC is designed to be used by C/C++ programmers. Familiarity with the Microsoft Interface Definition Language (MIDL) and the MIDL compiler are required.

## Run-time requirements

The RPC run-time libraries are included with Windows. The components of the RPC development environment are installed when you install the Microsoft Windows Software Development Kit (SDK). For details, see [Installing the RPC programming environment](installing-the-rpc-programming-environment.md).

## In this section

| Topic | Description |
|-|-|
| [RPC programming best practices](best-rpc-programming-practices.md) | Guidance on RPC programming practices that help create the best possible RPC applications. |
| [Overview](overviews.md) | General information about incorporating RPC into your client/server applications. |
| [Reference](reference.md) | Documentation of RPC types, functions, and constants. |
| [RPC NDR engine](rpc-ndr-engine.md) | Documentation of the marshaling engine for RPC and DCOM components, the RPC Network Data Representation (NDR) Engine. |

## Related topics

* [Microsoft Interface Definition Language (MIDL)](/windows/desktop/Midl/midl-start-page)
