---
Description: 'Windows HPC Server provide a set of diagnostic tests that help HPC cluster administrators check that their cluster is working properly.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4e04ddf7-6833-443e-a75c-821706ad66a9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'Diagnostics Extensibility in Windows HPC Server 2008 R2 Step-by-Step Guide'
---

# Diagnostics Extensibility in Windows HPC Server 2008 R2 Step-by-Step Guide

Windows HPC Server 2008 and Windows HPC Server 2008 R2 provide a set of diagnostic tests that help HPC cluster administrators check that their cluster is working properly. Cluster administrators can view a list of these diagnostic tests, run them, and view the results in HPC Cluster Manager or by using cmdlets in the HPC snap-in for the Windows PowerShell command-line interface.

In Windows HPC Server 2008 R2, cluster administrators and partners can create custom diagnostic tests. Partners include independent software vendors (ISVs), independent hardware vendors (IHVs), original equipment manufacturers (OEMs), and system integrators. Cluster administrators can add these tests to the list of diagnostic tests for their HPC cluster, and then run them in the same way as the built-in diagnostic tests for Windows HPC Server 2008 R2. By adding support for custom diagnostic tests, Windows HPC Server 2008 R2 allows cluster administrators to test more easily that custom and non-Microsoft software or hardware that they have added to their HPC cluster works correctly.

This guide describes custom diagnostic tests, how to define and implement several types of custom diagnostic tests, and how to add custom diagnostic tests to an HPC cluster.

## In this guide

[Diagnostic Test Stages](diagnostic-test-phases.md)

[Types of Diagnostic Tests](types-of-diagnostic-tests.md)

[Overview of the Steps for Creating a Custom Diagnostic Test](overiew-of-the-steps-for-creating-a-custom-diagnostic-test.md)

[Diagnostic Test Definition Schema](diagnostic-test-definition-schema.md)

[Diagnostic Test Step Result Schema](diagnostic-test-step-result-schema.md)

 

 



