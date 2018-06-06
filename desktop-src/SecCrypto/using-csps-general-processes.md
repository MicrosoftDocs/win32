---
Description: When using cryptographic service providers CSPs, keep the following conventions in mind.
ms.assetid: 70053b89-4d39-4a86-985a-0e8f05fbc9c0
title: 'Using CSPs: General Processes'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using CSPs: General Processes

When using [*cryptographic service providers*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) CSPs, keep the following conventions in mind.

## Private Key Caching

A CSP can cache some [*private keys*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a). It is possible to control this private key caching on a global, but not an application-specific, basis. Caching changes are made by modifying certain registry settings. For more information, see [**Private Key Caching Constants**](private-key-caching-constants.md).

## Example Code Conventions

To provide more concise, more readable code, some principles of good programming practice are not always followed in the examples. In particular:

-   Only limited error responses are shown. Well-written, complete programs check returned error codes and perform appropriate actions when an error is encountered.
-   Only limited memory and resource management is done. Well-written, complete programs destroy all keys and [*hashes*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323), free all allocated memory, close all files, and release all handles. These examples provide only limited demonstrations of the use of functions that perform these tasks. These examples perform no memory or resource management tasks in the case of program termination due to errors.

The following topics present general information about procedure examples as well as sample code.

-   [Retrieving Data of Unknown Length](retrieving-data-of-unknown-length.md)
-   [Enumerating Supported Protocols](enumerating-supported-protocols.md)

 

 



