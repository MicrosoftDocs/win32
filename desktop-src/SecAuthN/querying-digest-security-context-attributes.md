---
Description: The QueryContextAttributes (Digest) function provides information about the current settings of a security context.
ms.assetid: 36863f1d-ed4e-40ec-8831-1f8b9918f2d8
title: Querying Digest Security Context Attributes
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying Digest Security Context Attributes

The [**QueryContextAttributes (Digest)**](/windows/desktop/api/Sspi/) function provides information about the current settings of a [*security context*](security.s_gly#-security-security-context-gly).

Microsoft Digest supports querying the following security context attributes.



| Attribute                   | Description                                                                                                                                                                                             |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SECPKG\_ATTR\_KEY\_INFO     | Information relating to the signing and encryption algorithms in use.                                                                                                                                   |
| SECPKG\_ATTR\_PACKAGE\_INFO | General information pertaining to Microsoft Digest, such as the maximum token size permitted by the [*security package*](security.s_gly#-security-security-package-gly). |
| SECPKG\_ATTR\_SIZES         | The maximum sizes permitted for message-related data such as signatures.                                                                                                                                |



 

 

 



