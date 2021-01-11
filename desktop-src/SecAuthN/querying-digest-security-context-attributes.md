---
description: The QueryContextAttributes (Digest) function provides information about the current settings of a security context.
ms.assetid: 36863f1d-ed4e-40ec-8831-1f8b9918f2d8
title: Querying Digest Security Context Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Querying Digest Security Context Attributes

The [**QueryContextAttributes (Digest)**](/windows/win32/api/rrascfg/nn-rrascfg-ieapproviderconfig) function provides information about the current settings of a [*security context*](../secgloss/s-gly.md).

Microsoft Digest supports querying the following security context attributes.



| Attribute                   | Description                                                                                                                                                                                             |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SECPKG\_ATTR\_KEY\_INFO     | Information relating to the signing and encryption algorithms in use.                                                                                                                                   |
| SECPKG\_ATTR\_PACKAGE\_INFO | General information pertaining to Microsoft Digest, such as the maximum token size permitted by the [*security package*](../secgloss/s-gly.md). |
| SECPKG\_ATTR\_SIZES         | The maximum sizes permitted for message-related data such as signatures.                                                                                                                                |



 

 

 
