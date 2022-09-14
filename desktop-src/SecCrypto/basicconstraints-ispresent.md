---
description: Retrieves a Boolean value that indicates whether the basic constraints extension is present. This is the default property.
ms.assetid: 775b37fc-5015-4096-9e94-608f13a5ed14
title: BasicConstraints.IsPresent property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BasicConstraints.IsPresent
api_type: 
- COM
api_location: 
- Capicom.dll
---

# BasicConstraints.IsPresent property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**X509BasicConstraintsExtension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509basicconstraintsextension) in the [**System.Security.Cryptography.X509Certificates**](/previous-versions/windows/) namespace.\]

The **IsPresent** property retrieves a Boolean value that indicates whether the basic constraints extension is present. This is the default property.

This property is read-only.

## Syntax


```VB
BasicConstraints.IsPresent As Boolean
```



## Property value

If **true**, the basic constraints extension is present.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**BasicConstraints**](basicconstraints.md)
</dt> </dl>

 

 
