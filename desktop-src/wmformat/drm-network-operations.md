---
title: DRM Network Operations
description: DRM Network Operations
ms.assetid: 4a10c811-2aa1-4b97-8a72-61e8b04075a8
keywords:
- Windows Media Format SDK,DRM network operations
- Advanced Systems Format (ASF),DRM network operations
- ASF (Advanced Systems Format),DRM network operations
- digital rights management (DRM),network operations
- DRM (digital rights management),network operations
ms.topic: article
ms.date: 05/31/2018
---

# DRM Network Operations

Several DRM-related operations require your application to connect to a service running on a network. These operations include individualization, license acquisition, license revocation, and license backup and restoration.

As with any network transaction, your application should account for a variety of difficulties when including features that require network operations. Your application should track the status of the operation to whatever extent is possible for the specific feature, usually by handling status messages. You should provide feedback to the user about status. If an operation fails on the first try, you should give the user the opportunity to retry. In many cases, the first attempt encounters difficulty, but a subsequent try completes without error.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> </dl>

 

 




