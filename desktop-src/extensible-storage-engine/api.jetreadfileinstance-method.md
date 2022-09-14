---
description: "Learn more about: Api.JetReadFileInstance method"
title: Api.JetReadFileInstance method 
TOCTitle: 'JetReadFileInstance method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetReadFileInstance(Microsoft.Isam.Esent.Interop.JET_INSTANCE,Microsoft.Isam.Esent.Interop.JET_HANDLE,System.Byte[],System.Int32,System.Int32@)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetreadfileinstance(v=EXCHG.10)
ms:contentKeyID: 55100781
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetReadFileInstance
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetReadFileInstance
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetReadFileInstance method

Retrieves the contents of a file opened with [JetOpenFileInstance(JET_INSTANCE, String, JET_HANDLE, Int64, Int64)](./api.jetopenfileinstance-method.md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetReadFileInstance ( _
    instance As JET_INSTANCE, _
    file As JET_HANDLE, _
    buffer As Byte(), _
    bufferSize As Integer, _
    <OutAttribute> ByRef bytesRead As Integer _
)
'Usage
Dim instance As JET_INSTANCE
Dim file As JET_HANDLE
Dim buffer As Byte()
Dim bufferSize As Integer
Dim bytesRead As IntegerApi.JetReadFileInstance(instance, _
    file, buffer, bufferSize, bytesRead)
```

``` csharp
public static void JetReadFileInstance(
    JET_INSTANCE instance,
    JET_HANDLE file,
    byte[] buffer,
    int bufferSize,
    out int bytesRead
)
```

#### Parameters

  - instance  
    Type: [Microsoft.Isam.Esent.Interop.JET_INSTANCE](./jet-instance-structure.md)  
    
    The instance to use.

<!-- end list -->

  - file  
    Type: [Microsoft.Isam.Esent.Interop.JET_HANDLE](./jet-handle-structure.md)  
    
    The file to read from.

<!-- end list -->

  - buffer  
    Type: \[\]  
    
    The buffer to read into.

<!-- end list -->

  - bufferSize  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The size of the buffer.

<!-- end list -->

  - bytesRead  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Returns the amount of data read into the buffer.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
