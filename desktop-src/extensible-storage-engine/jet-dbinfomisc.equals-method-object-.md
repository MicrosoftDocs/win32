---
title: JET_DBINFOMISC.Equals method (Object) (Microsoft.Isam.Esent.Interop)
TOCTitle: Equals method (Object)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.Equals(System.Object)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_dbinfomisc.equals(v=EXCHG.10)
ms:contentKeyID: 39513216
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.Equals method (Object)

Determines whether the specified [Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN) is equal to the current [Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Overrides Function Equals ( _
    obj As Object _
) As Boolean
'Usage
Dim instance As JET_DBINFOMISC
Dim obj As Object
Dim returnValue As Boolean

returnValue = instance.Equals(obj)
```

``` csharp
public override bool Equals(
    Object obj
)
```

#### Parameters

  - obj  
    Type: [System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
    
    The [Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN) to compare with the current [Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN).

#### Return value

Type: [System.Boolean](https://docs.microsoft.com/dotnet/api/system.boolean?redirectedfrom=MSDN)  
True if the specified [Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN) is equal to the current [Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN); otherwise, false.  

## See also

#### Reference

[JET_DBINFOMISC class](hh538867\(v=exchg.10\).md)

[JET_DBINFOMISC members](hh566148\(v=exchg.10\).md)

[Equals overload](hh577631\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

