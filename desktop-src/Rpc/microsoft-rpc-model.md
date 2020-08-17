---
title: The RPC Model
description: Remote Procedure Call (RPC) for the C and C++ programming languages is designed to help meet the needs of developers working on the next generation of software for Windows operating systems.
ms.assetid: ebab41a5-e841-4e0f-8acd-d0aab94f01c1
keywords:
- Remote Procedure Call RPC , described, the RPC model
ms.topic: article
ms.date: 05/31/2018
---

# The RPC Model

Remote Procedure Call (RPC) for the C and C++ programming languages is designed to help meet the needs of developers working on the next generation of software for Windows operating systems.

RPC is a powerful, robust, efficient, and secure interprocess communication (IPC) mechanism that enables data exchange and invocation of functionality residing in a different process. That different process can be on the same machine, on the local area network, or across the Internet. This section explains the RPC programming model and the model for distributed systems that can be implemented using RPC.

RPC fully supports 64-bit Windows. There are three types of processes: native 32-bit processes, native 64-bit processes, and 32-bit processes running under the 32-bit process emulator on a 64-bit system (often referred to as WOW64 processes). For more information about WOW64, see [Running 32-bit Applications](/windows/desktop/WinProg64/running-32-bit-applications). Using RPC, developers can transparently communicate between different types of process; RPC automatically manages process differences behind the scenes.

RPC was initially developed as an extension to OSF RPC. With the exception of some of its advanced features, RPC is interoperable with other vendors' implementations of OSF RPC.

This section also provides an overview of RPC components and their operation. The information is presented in the following topics:

-   [The Programming Model](the-programming-model.md)
-   [The Model for Distributed Systems](the-model-for-distributed-systems.md)
-   [How RPC Works](how-rpc-works.md)
-   [Microsoft RPC Components](microsoft-rpc-components.md)

 

 