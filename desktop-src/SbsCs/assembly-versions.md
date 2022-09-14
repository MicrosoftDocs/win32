---
description: Every side-by-side assembly must have a version.
ms.assetid: 0b78ecf6-fbff-4172-9b0d-09f993666db1
title: Assembly Versions
ms.topic: article
ms.date: 05/31/2018
---

# Assembly Versions

Every side-by-side assembly must have a version. Each assembly version is associated with a version number having four parts separated by periods: *major.minor.build.revision*. If a change is made to an assembly making it incompatible with existing versions, the *major* or *minor* parts of the version number must be changed. A version number that changes only in the *build* or *revision* parts indicates that the assembly is backward compatible with prior versions.

The version must be specified in **assemblyIdentity** elements of [manifests](manifests.md). Use the four-part version format: mmmmm.nnnnn.ooooo.ppppp. Each of the parts separated by periods can be 0-65535 inclusive.

 

 



