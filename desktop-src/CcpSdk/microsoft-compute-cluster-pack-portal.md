---
Description: 'Compute Cluster Pack (CCP) provides secure, scalable cluster resource management, a job scheduler, and a Message Passing Interface (MPI) stack for parallel programming.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '23236b8b-03c1-4171-ac82-64b971f03f71'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Microsoft Compute Cluster Pack
---

# Microsoft Compute Cluster Pack

## Purpose

Compute Cluster Pack (CCP) provides secure, scalable cluster resource management, a job scheduler, and a Message Passing Interface (MPI) stack for parallel programming. This document provides details for writing client applications that interact with the job scheduler. For information about MPI, see [Microsoft MPI](about-microsoft-mpi.md).

You can use this SDK to schedule jobs on Microsoft Compute Cluster Server 2003 (CCS) and Microsoft HPC Server 2008 and later servers; however, you are encouraged to use the HPC SDK to write all new applications that interact with the job scheduler on HPC Server 2008 and later servers. For details on the HPC SDK, see [Microsoft HPC SDK Pack](hpc-portal.md).

## Developer audience

CCP is designed for C, C++, and .NET developers and those writing scripts.

## Run-time requirements

To run an application that uses the CCP API, the computer must have the Compute Cluster Pack Client Utilities installed.

For information about run-time requirements for a particular programming element, see the Requirements section of the reference page for that element.

## In this section

<dl> <dt>

[About CCP](about-ccp.md)
</dt> <dd>

General information about CCP.

</dd> <dt>

[Using CCP](using-ccp.md)
</dt> <dd>

Procedural guide for developing CCP client applications.

</dd> <dt>

[CCP Reference](compute-cluster-pack-reference.md)
</dt> <dd>

Reference information for the native CCP API.

</dd> <dt>

[CCP .NET Reference](https://msdn.microsoft.com/library/microsoft.computecluster.aspx)
</dt> <dd>

Reference information for the .NET CCP API.

</dd> </dl>

 

 



