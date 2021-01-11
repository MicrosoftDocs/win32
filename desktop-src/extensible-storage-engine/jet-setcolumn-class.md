---
description: "Learn more about: JET_SETCOLUMN class"
title: JET_SETCOLUMN class
TOCTitle: JET_SETCOLUMN class
ms:assetid: T:Microsoft.Isam.Esent.Interop.JET_SETCOLUMN
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_setcolumn(v=EXCHG.10)
ms:contentKeyID: 55103847
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_SETCOLUMN
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_SETCOLUMN
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_SETCOLUMN class

Contains input and output parameters for [JetSetColumns(JET_SESID, JET_TABLEID, \[\], Int32)](./api.jetsetcolumns-method.md). Fields in the structure describe what column value to set, how to set it, and where to get the column set data.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  Microsoft.Isam.Esent.Interop.JET_SETCOLUMN  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Class JET_SETCOLUMN _
    Implements IContentEquatable(Of JET_SETCOLUMN), IDeepCloneable(Of JET_SETCOLUMN)
'Usage
Dim instance As JET_SETCOLUMN
```

``` csharp
public class JET_SETCOLUMN : IContentEquatable<JET_SETCOLUMN>, 
    IDeepCloneable<JET_SETCOLUMN>
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[JET_SETCOLUMN members](./jet-setcolumn-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
