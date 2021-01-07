---
description: It is strongly recommended that you run validation on every new or newly modified installation package before attempting to install the package for the first time.
ms.assetid: 47168c0b-82ab-4f1b-84d7-98c8f64d6da0
title: Package Validation
ms.topic: article
ms.date: 05/31/2018
---

# Package Validation

It is strongly recommended that you run validation on every new or newly modified installation package before attempting to install the package for the first time.

Package validation includes the following three processes:

-   [Internal Validation](internal-validation.md)
-   [String-Pool Validation](string-pool-validation.md)
-   [Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md)

Merge modules should be validated by using the method described in [Validating Merge Modules](validating-merge-modules.md).

Evalcom2.dll provides a COM object that implements validation operations for installation packages and merge modules. The main object implements interfaces for C/C++ programs. For more information, see [Validation Automation](validation-automation.md).

 

 



