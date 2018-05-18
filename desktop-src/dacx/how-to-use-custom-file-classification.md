---
title: How to create a custom file classification mechanism
description: The File Classification Infrastructure (FCI) provides a set of classification mechanisms by default.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'C53AD469-5740-45EE-B2B6-3D0CD12B1E31'
ms.prod: 'windows-server-dev'
ms.technology: 'dynamic-access-control'
ms.tgt_platform: multiple
keywords: ["Dynamic Access Control developer extensibility DACx , custom file classification"]
---

# How to create a custom file classification mechanism

The File Classification Infrastructure (FCI) provides a set of classification mechanisms by default. When mroe custom logic is required to classify files, a classification plug-in can be created. These plug-ins represent a primary developer extensibility points for file classification.

The [Microsoft Windows SDK for Windows 7 and .NET Framework 4](http://www.microsoft.com/download/details.aspx?id=8279) contains the following samples.

-   [Customization through FCI plug-in based samples](#customization-through-fci-plug-in-based-samples)
-   [Sample for enumerating classification properties using the FCI API](#sample-for-enumerating-classification-properties-using-the-fci-api)

### Customization through FCI plug-in based samples

Each of these SDK samples results in a DLL and comes with a registration script for registering the plug-in through COM+, setting up an execution environment for the COM server. COM servers can also be hosted in more custom ways. This registration script registers the plug-in for FCI by using its **GUID**.

Any FCI classification rule specifies one classification plug-in. For more information, see [Module Design](https://msdn.microsoft.com/library/jj200583#module-design) in [How to develop a custom FCI Classifier in Managed Code](https://msdn.microsoft.com/library/jj200583). To allow for behavior variation for a single plug-in between rules, each rule may include zero or more name-value pairs that are passed to the plug-in. These pairs are configured in the rule through COM, WMI, or PowerShell.

-   **PowerShell host classifier sample**

    This sample consists of a plugin that allows an administrator to specify a PowerShell script to provide a property value through FCI.

    **Windows Server 2008 R2:** This functionality is not available in the operating system; therefore, this sample shows how this was done before it was integrated into the operating system.

    This sample is installed by default at C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Samples\\winbase\\FSRM\\PowerShellHostClassifier.

-   **IFilter based classifier sample**

    This sample plugin processes the content of files. However plug-ins are provided with a binary stream of the file contents. The sample invokes an [**IFilter**](https://msdn.microsoft.com/library/windows/desktop/bb266451) that translates the binary stream of a file into text by file type. **IFilter**s are what the search indexer uses to extract text from a file. The search for the keyword is a simple string search.

    This sample is installed by default at C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Samples\\winbase\\FSRM\\SampleIFilterBasedClassifier.

-   **Text based classifier sample**

    Similar to the [**IFilter**](https://msdn.microsoft.com/library/windows/desktop/bb266451) based classification sample, this sample plug-in searches a specified file for a specified string. If given a binary file, it searches it as it would a text file.

    This sample is installed by default at C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Samples\\winbase\\FSRM\\SampleTextBasedClassifier.

-   **Managed content classifier sample**

    This sample is the same as the text based classifier sample but it is built using C# instead of C++.

    This sample is installed by default at C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Samples\\winbase\\FSRM\\ManagedContentClassifier.

### Sample for enumerating classification properties using the FCI API

For application developers who want to access the classification properties of a file, there are [FSRM Classes](https://msdn.microsoft.com/library/jj658610) for working with the properties of a given set of files.

-   **Enumerate classification properties sample**

    This sample is installed by default at C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Samples\\winbase\\FSRM\\EnumClassificationProperties.

-   **Managed get enumerated properties sample**

    This sample is installed by default at C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Samples\\winbase\\FSRM\\ManagedGetEnumProperties.

 

 




