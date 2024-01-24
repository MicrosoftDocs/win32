---
description: For extensible bit-flag data constants, a service-provider vendor can define new values for specified bits.
ms.assetid: bf3ca2b0-a9fb-4e63-87de-6d5cbe5cd746
title: Bit-Flag Data Constants
ms.topic: article
ms.date: 05/31/2018
---

# Bit-Flag Data Constants

For extensible bit-flag data constants, a service-provider vendor can define new values for specified bits. Because most bit-flag constants are **DWORD**s, a specific number of the lower bits are usually reserved for common extensions, while the remaining upper bits are available for vendor-specific extensions. Common bit flags are assigned from bit zero up, and vendor-specific extensions should be assigned from bit 31 down. This scheme provides maximum flexibility in assigning bit positions to common extensions, as opposed to vendor-specific extensions. A vendor is expected to define new values that are natural extensions of the bit flags defined by the API.

Extensible data structures have a variably sized field that is reserved for device-specific use. Because the field is variably sized, the service provider decides the field's amount of information and interpretation. A vendor that defines a device-specific field is expected to make these natural extensions of the original data structure defined by the API.

 

 



