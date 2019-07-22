---
Description: .
ms.assetid: 1fa34b69-ae34-40e5-b71a-cb9c74f3fc3a
title: Assessment Execution Engine
ms.topic: article
ms.date: 05/31/2018
---

# Assessment Execution Engine

## Purpose

The Assessment Execution Engine (AXE) enables the management and execution of Windows system assessments. Assessments can help a person understand the state of a system and remedy problems with performance, reliability, or functionality. AXE provides infrastructure needed to manage assessments using a UX tool or script, run assessments, make measurements, process raw data into results, run diagnostics, and publish the results.

## Developer audience

This documentation is intended for software developers who want to write assessments or solutions that use the Assessment Execution Engine (AXE.) It contains complete descriptions of the application programming interfaces and elements. The header files for using the unmanaged C++ version of the AXE APIs are installed with the "Windows Assessment Toolkit" feature of the [Windows Assessment and Deployment Kit (ADK)](https://msdn.microsoft.com/en-us/library/Hh825420(v=WIN.10).aspx).

The AXE object model is a managed assembly used for programmatically creating, reading and writing assessment and job manifests. It is contained in the "Microsoft.Assessments.dll" in the [Windows Assessment and Deployment Kit (ADK)](https://msdn.microsoft.com/en-us/library/Hh825420(v=WIN.10).aspx) under the "Windows Assessment Toolkit" installation. Currently, the only documentation for the interface is the public APIs discoverable through reflection.

## Run-time requirements

AXE and AXE assessments can be installed and run on Windows 7, Windows Server 2008 R2, Windows 8, or Windows Server 2012.

## In this section

-   [Unmanaged C++ Version of the AXE API](https://docs.microsoft.com/previous-versions/windows/desktop/axe/unmanaged-c---version-of-the-axe-api)
-   [AXE Schema Reference](https://docs.microsoft.com/previous-versions/windows/desktop/axe/axe-schema-reference)

 

 



