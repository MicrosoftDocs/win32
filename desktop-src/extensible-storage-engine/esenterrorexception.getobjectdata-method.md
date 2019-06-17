---
title: EsentErrorException.GetObjectData method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'GetObjectData method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.EsentErrorException.GetObjectData(System.Runtime.Serialization.SerializationInfo,System.Runtime.Serialization.StreamingContext)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esenterrorexception.getobjectdata(v=EXCHG.10)
ms:contentKeyID: 55101432
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentErrorException.GetObjectData
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentErrorException.GetObjectData
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentErrorException.GetObjectData method

When overridden in a derived class, sets the [SerializationInfo](https://docs.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo?redirectedfrom=MSDN) with information about the exception.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Overrides Sub GetObjectData ( _
    info As SerializationInfo, _
    context As StreamingContext _
)
'Usage
Dim instance As EsentErrorException
Dim info As SerializationInfo
Dim context As StreamingContext

instance.GetObjectData(info, context)
```

``` csharp
public override void GetObjectData(
    SerializationInfo info,
    StreamingContext context
)
```

#### Parameters

  - info  
    Type: [System.Runtime.Serialization.SerializationInfo](https://docs.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo?redirectedfrom=MSDN)  
    
    The [SerializationInfo](https://docs.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo?redirectedfrom=MSDN) that holds the serialized object data about the exception being thrown.

<!-- end list -->

  - context  
    Type: [System.Runtime.Serialization.StreamingContext](https://docs.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext?redirectedfrom=MSDN)  
    
    The [StreamingContext](https://docs.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext?redirectedfrom=MSDN) that contains contextual information about the source or destination.

#### Implements

[ISerializable.GetObjectData(SerializationInfo, StreamingContext)](https://docs.microsoft.com/dotnet/api/system.runtime.serialization.iserializable.getobjectdata?redirectedfrom=MSDN#System_Runtime_Serialization_ISerializable_GetObjectData_System_Runtime_Serialization_SerializationInfo_System_Runtime_Serialization_StreamingContext_)  
[_Exception.GetObjectData(SerializationInfo, StreamingContext)](https://docs.microsoft.com/dotnet/api/system.runtime.interopservices._exception.getobjectdata?redirectedfrom=MSDN#System_Runtime_InteropServices__Exception_GetObjectData_System_Runtime_Serialization_SerializationInfo_System_Runtime_Serialization_StreamingContext_)  

## Exceptions

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Exception</th>
<th>Condition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://docs.microsoft.com/dotnet/api/system.argumentnullexception?redirectedfrom=MSDN">ArgumentNullException</a></td>
<td><p>The info parameter is a null reference (Nothing in Visual Basic).</p></td>
</tr>
</tbody>
</table>


## See also

#### Reference

[EsentErrorException class](dn274314\(v=exchg.10\).md)

[EsentErrorException members](dn274255\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

