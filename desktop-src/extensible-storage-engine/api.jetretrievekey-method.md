---
title: Api.JetRetrieveKey method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'JetRetrieveKey method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetRetrieveKey(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.Byte[],System.Int32,System.Int32@,Microsoft.Isam.Esent.Interop.RetrieveKeyGrbit)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetretrievekey(v=EXCHG.10)
ms:contentKeyID: 55100795
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetRetrieveKey
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetRetrieveKey
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetRetrieveKey method

Retrieves the key for the index entry at the current position of a cursor. Also see [RetrieveKey(JET_SESID, JET_TABLEID, RetrieveKeyGrbit)](dn334085\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetRetrieveKey ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    data As Byte(), _
    dataSize As Integer, _
    <OutAttribute> ByRef actualDataSize As Integer, _
    grbit As RetrieveKeyGrbit _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim data As Byte()
Dim dataSize As Integer
Dim actualDataSize As Integer
Dim grbit As RetrieveKeyGrbitApi.JetRetrieveKey(sesid, tableid, _
    data, dataSize, actualDataSize, grbit)
```

``` csharp
public static void JetRetrieveKey(
    JET_SESID sesid,
    JET_TABLEID tableid,
    byte[] data,
    int dataSize,
    out int actualDataSize,
    RetrieveKeyGrbit grbit
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](hh566310\(v=exchg.10\).md)  
    
    The cursor to retrieve the key from.

<!-- end list -->

  - data  
    Type: \[\]  
    
    The buffer to retrieve the key into.

<!-- end list -->

  - dataSize  
    Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  
    
    The size of the buffer.

<!-- end list -->

  - actualDataSize  
    Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  
    
    Returns the actual size of the data.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.RetrieveKeyGrbit](hh564639\(v=exchg.10\).md)  
    
    Retrieve key options.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

