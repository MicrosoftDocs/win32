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

When overridden in a derived class, sets the [SerializationInfo](http://msdn2.microsoft.com/en-us/library/a9b6042e) with information about the exception.

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
    Type: [System.Runtime.Serialization.SerializationInfo](http://msdn2.microsoft.com/en-us/library/a9b6042e)  
    
    The [SerializationInfo](http://msdn2.microsoft.com/en-us/library/a9b6042e) that holds the serialized object data about the exception being thrown.

<!-- end list -->

  - context  
    Type: [System.Runtime.Serialization.StreamingContext](http://msdn2.microsoft.com/en-us/library/t16abws5)  
    
    The [StreamingContext](http://msdn2.microsoft.com/en-us/library/t16abws5) that contains contextual information about the source or destination.

#### Implements

[ISerializable.GetObjectData(SerializationInfo, StreamingContext)](http://msdn2.microsoft.com/en-us/library/27cxsdk6)  
[\_Exception.GetObjectData(SerializationInfo, StreamingContext)](http://msdn2.microsoft.com/en-us/library/854b9522)  

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
<td><a href="http://msdn2.microsoft.com/en-us/library/27426hcy">ArgumentNullException</a></td>
<td><p>The info parameter is a null reference (Nothing in Visual Basic).</p></td>
</tr>
</tbody>
</table>


## See also

#### Reference

[EsentErrorException class](dn274314\(v=exchg.10\).md)

[EsentErrorException members](dn274255\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

