---
title: JET_ENUMCOLUMN.pvData property 
TOCTitle: 'pvData property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMN.pvData
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_enumcolumn.pvdata(v=EXCHG.10)
ms:contentKeyID: 55103500
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMN.pvData
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMN.pvData
- Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMN.get_pvData
- Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMN.set_pvData
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_ENUMCOLUMN.pvData property

Gets the value that was enumerated for the column. This member is only used if [err](dn335086\(v=exchg.10\).md) is equal to [ColumnSingleValue](hh557250\(v=exchg.10\).md). This points to memory allocated with the [JET_PFNREALLOC](hh566077\(v=exchg.10\).md) allocator callback passed to [JetEnumerateColumns(JET_SESID, JET_TABLEID, Int32, \[\], Int32, \[\], JET_PFNREALLOC, IntPtr, Int32, EnumerateColumnsGrbit)](dn292148\(v=exchg.10\).md). Remember to release the memory when finished.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property pvData As IntPtr
    Get
    Friend Set
'Usage
Dim instance As JET_ENUMCOLUMN
Dim value As IntPtr

value = instance.pvData
```

``` csharp
public IntPtr pvData { get; internal set; }
```

#### Property value

Type: [System.IntPtr](/dotnet/api/system.intptr)  

## See also

#### Reference

[JET_ENUMCOLUMN class](dn335081\(v=exchg.10\).md)

[JET_ENUMCOLUMN members](dn335133\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)