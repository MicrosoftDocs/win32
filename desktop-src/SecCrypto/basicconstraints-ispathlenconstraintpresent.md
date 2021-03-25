---
description: Retrieves a Boolean value that indicates whether the path length constraint is present.
ms.assetid: 25840a62-13d1-4b54-9b09-64f77a465e06
title: BasicConstraints.IsPathLenConstraintPresent property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BasicConstraints.IsPathLenConstraintPresent
api_type: 
- COM
api_location: 
- Capicom.dll
---

# BasicConstraints.IsPathLenConstraintPresent property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**X509BasicConstraintsExtension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509basicconstraintsextension?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/previous-versions/windows/) namespace.\]

The **IsPathLenConstraintPresent** property retrieves a Boolean value that indicates whether the path length constraint is present.

## Syntax


```VB
BasicConstraints.IsPathLenConstraintPresent As Boolean
```



## Property value

If **True**, the path length constraint is present.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
