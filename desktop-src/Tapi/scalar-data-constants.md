---
description: For extensible scalar data constants, a service-provider vendor can define new values in a specified range.
ms.assetid: 62280b71-9bec-4a9d-abd2-d3e1c2cee43f
title: Scalar Data Constants
ms.topic: article
ms.date: 05/31/2018
---

# Scalar Data Constants

For extensible scalar data constants, a service-provider vendor can define new values in a specified range. Because most data constants are **DWORD**s, the range 0x00000000 through 0x7FFFFFFF is typically reserved for common future extensions, while 0x80000000 through 0xFFFFFFFF is available for vendor-specific extensions. The assumption is that a vendor would define values that are natural extensions of the datatypes defined by the API.

 

 



