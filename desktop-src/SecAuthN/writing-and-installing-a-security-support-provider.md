---
description: The design of SSPI enables additional SSPs to be written and added to the system.
ms.assetid: 0d462340-e485-4746-b627-d823752462d9
title: Writing and Installing a Security Support Provider
ms.topic: article
ms.date: 05/31/2018
---

# Writing and Installing a Security Support Provider

The design of SSPI enables additional SSPs to be written and added to the system. An [*SSP*](../secgloss/s-gly.md) specific to a security model can be developed with relative ease or great complexity, depending on the level of integration with the operating system. A client SSP that allows connections to a new type of server could be developed very quickly, whereas a full SSP that provides local impersonation would require more effort.

SSPs are installed by updating a **REG\_SZ** value in the registry, located as follows:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\    **SecurityProviders** = *Provider1.dll, Provider2.dll,*…<dl> <dt>

            Data type
</dt> <dd>            REG\_SZ</dd> </dl>

A single DLL can contain multiple SSPs.

## Related topics

<dl> <dt>

[Restrictions around Registering and Installing a Security Package](restrictions-around-registering-and-installing-a-security-package.md)
</dt> </dl>

 

 
