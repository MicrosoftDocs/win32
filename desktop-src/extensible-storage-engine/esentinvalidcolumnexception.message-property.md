---
description: "Learn more about: EsentInvalidColumnException.Message property"
title: EsentInvalidColumnException.Message property 
TOCTitle: 'Message property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.EsentInvalidColumnException.Message
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentinvalidcolumnexception.message(v=EXCHG.10)
ms:contentKeyID: 55101925
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentInvalidColumnException.Message
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentInvalidColumnException.get_Message
- Microsoft.Isam.Esent.Interop.EsentInvalidColumnException.Message
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentInvalidColumnException.Message property

Gets a text message describing the exception.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Overrides ReadOnly Property Message As String
    Get
'Usage
Dim instance As EsentInvalidColumnException
Dim value As String

value = instance.Message
```

``` csharp
public override string Message { get; }
```

#### Property value

Type: [System.String](/dotnet/api/system.string)  

#### Implements

[_Exception.Message](/dotnet/api/system.runtime.interopservices._exception.message#System_Runtime_InteropServices__Exception_Message)  

## See also

#### Reference

[EsentInvalidColumnException class](./esentinvalidcolumnexception-class.md)

[EsentInvalidColumnException members](./esentinvalidcolumnexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
