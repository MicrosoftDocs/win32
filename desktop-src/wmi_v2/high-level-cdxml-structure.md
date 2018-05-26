---
title: High-level CDXML structure
description: This topic lists the structure of a CDXML document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: BB7232E1-1C2F-4308-9B3A-E2E41C2CD4F6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# High-level CDXML structure

This topic lists the structure of a CDXML document.

CDXML documents are divided into two major sections, or elements. The elements are in the "http://schemas.microsoft.com/cmdlets-over-objects/2009/11" namespace.

-   **InstanceCmdlets** element - Defines cmdlets that map to instance methods.
-   **StaticCmdlets** element - Defines cmdlets that map to static methods.

The instance cmdlets element (**InstanceCmdlets**) is further divided into the following sections.

-   **GetCmdletParameters** element - This element contains the definition of parameters that are used to retrieve class instances that will be passed to instance methods.
-   **GetCmdlet** element - This element contains the definition of the Get-&lt;noun&gt; cmdlet.
-   **Method** element - This element defines the sequence of instance cmdlet mappings.

The following list shows the structure of a CDXML document where the value before the hyphen is the CDXML element name and the text after the hyphen is the description of that element.

-   **PowerShellMetadata** - The root element for a CDXML document

    -   **Class** - Describes the CIM class. The class should have the fully qualified path of the CIM class including namespace and class name.

        -   **InstanceCmdlets** - Describes the cmdlets mapped to instance operations.

            -   **GetCmdletParameters** - A global set of query parameters used by all instance cmdlets. The cmdlet can define its own set of query parameters.
            -   **GetCmdlet** - Describes the metadata for Get Cmdlet. Get Cmdlet is treated differently than other instance cmdlets. This element is optional and is used only when overriding.
            -   **Cmdlet** - One &lt;cmdlet&gt; node that corresponds to each cmdlet defined by the CDXML.

                -   **CmdletMetadata** - Describes the metadata for the cmdlet. This includes the Noun and Verb for the cmdlet, as well as aliases and flags for specifying **ConfirmImpact** Setting.
                -   **Method** - The name of the CIM Instance method invoked by the cmdlet.

                    -   **Parameters** - Describes the parameters of the method.

                        -   **Parameter** - Individual parameters of the method. This defines the name and type of the parameter and Windows PowerShell-specific attributes such as **IsMandatory** and PipeLine binding

                -   **GetCmdletParameters** - Specified when a cmdlet replaces the global definition.

        -   **StaticCmdlets** - Describes cmdlets mapped to a static method.

            -   **Cmdlet** - One &lt;cmdlet&gt; node that corresponds to each cmdlet defined by the CDXML.

                -   **CmdletMetadata** - Describes the metadata for the cmdlet. This includes the Noun and Verb for the cmdlet, as well as aliases and flags for specifying **ConfirmImpact** Setting.
                -   **Method** - Describes static methods called by the cmdlet for a static method. There can be one method per parameter set.

                    -   **Parameters** - The collection of parameters for this method.

                        -   **Parameter** - Describes one parameter of the method and how it appears in the cmdlet signature.

                -   **GetCmdletParameters** - Used to override the default behavior for CDXML processing.

        -   **Enums** - Defines the enumerations to be used by the cmdlets.

 

 




