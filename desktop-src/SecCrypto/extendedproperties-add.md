---
Description: Adds an extended property to the collection.
ms.assetid: 1d6b3c39-17b0-4a7c-a5c2-4a3bd866be07
title: ExtendedProperties.Add method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExtendedProperties.Add
api_type: 
- COM
api_location: 
- Capicom.dll
---

# ExtendedProperties.Add method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use Platform Invocation Services (PInvoke) to call the Win32 API function [**CertGetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty) and obtain the properties. For information about PInvoke, see [Platform Invoke Tutorial](https://go.microsoft.com/fwlink/p/?linkid=119531). The [.NET and CryptoAPI via P/Invoke: Part 1](https://go.microsoft.com/fwlink/p/?linkid=119533) and [.NET and CryptoAPI via P/Invoke: Part 2](https://go.microsoft.com/fwlink/p/?linkid=119534) subsections of [Extending .NET Cryptography with CAPICOM and P/Invoke](https://go.microsoft.com/fwlink/p/?linkid=119532) may also be helpful.\]

The **Add** method adds an extended property to the collection.

## Syntax


```VB
ExtendedProperties.Add( _
  ByVal valProperty _
)
```



## Parameters

<dl> <dt>

*valProperty* \[in\]
</dt> <dd>

An [**ExtendedProperty**](extendedproperty.md) object that represents the extended property.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




