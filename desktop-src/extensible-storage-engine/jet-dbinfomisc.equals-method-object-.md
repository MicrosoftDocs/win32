---
title: JET_DBINFOMISC.Equals method (Object)
TOCTitle: Equals method (Object)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.Equals(System.Object)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.equals(v=EXCHG.10)
ms:contentKeyID: 39513216
ms.date: 07/30/2014
ms.topic: reference
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

Determines whether the specified [Object](/dotnet/api/system.object) is equal to the current [Object](/dotnet/api/system.object).

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
    Type: [System.Object](/dotnet/api/system.object)  
    
    The [Object](/dotnet/api/system.object) to compare with the current [Object](/dotnet/api/system.object).

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
True if the specified [Object](/dotnet/api/system.object) is equal to the current [Object](/dotnet/api/system.object); otherwise, false.  

## See also

#### Reference

[JET_DBINFOMISC class](hh538867\(v=exchg.10\).md)

[JET_DBINFOMISC members](hh566148\(v=exchg.10\).md)

[Equals overload](hh577631\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)