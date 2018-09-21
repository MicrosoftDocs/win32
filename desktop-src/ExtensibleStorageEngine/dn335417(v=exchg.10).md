---
title: Windows7Api.JetPrereadKeys method (JET_SESID, JET_TABLEID, Byte[][], Int32 , Int32, Int32, Int32, PrereadKeysGrbit) (Microsoft.Isam.Esent.Interop.Windows7)
TOCTitle: JetPrereadKeys method (JET_SESID, JET_TABLEID, Byte[][], Int32 , Int32, Int32, Int32, PrereadKeysGrbit)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Windows7.Windows7Api.JetPrereadKeys(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.Byte[][],System.Int32[],System.Int32,System.Int32,System.Int32@,Microsoft.Isam.Esent.Interop.Windows7.PrereadKeysGrbit)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.windows7.windows7api.jetprereadkeys(v=EXCHG.10)
ms:contentKeyID: 55104374
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Windows7.Windows7Api.JetPrereadKeys
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Windows7Api.JetPrereadKeys method (JET\_SESID, JET\_TABLEID, Byte\[\]\[\], Int32 , Int32, Int32, Int32, PrereadKeysGrbit)

If the records with the specified keys are not in the buffer cache then start asynchronous reads to bring the records into the database buffer cache.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Windows7](hh577573\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetPrereadKeys ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    keys As Byte()(), _
    keyLengths As Integer(), _
    keyIndex As Integer, _
    keyCount As Integer, _
    <OutAttribute> ByRef keysPreread As Integer, _
    grbit As PrereadKeysGrbit _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim keys As Byte()()
Dim keyLengths As Integer()
Dim keyIndex As Integer
Dim keyCount As Integer
Dim keysPreread As Integer
Dim grbit As PrereadKeysGrbitWindows7Api.JetPrereadKeys(sesid, tableid, _
    keys, keyLengths, keyIndex, keyCount, _
    keysPreread, grbit)
```

``` csharp
public static void JetPrereadKeys(
    JET_SESID sesid,
    JET_TABLEID tableid,
    byte[][] keys,
    int[] keyLengths,
    int keyIndex,
    int keyCount,
    out int keysPreread,
    PrereadKeysGrbit grbit
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_TABLEID](hh566310\(v=exchg.10\).md)  
    
    The table to issue the prereads against.

<!-- end list -->

  - keys  
    Type: \[\]  
    
    The keys to preread. The keys must be sorted.

<!-- end list -->

  - keyLengths  
    Type: \[\]  
    
    The lengths of the keys to preread.

<!-- end list -->

  - keyIndex  
    Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  
    
    The index of the first key in the keys array to read.

<!-- end list -->

  - keyCount  
    Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  
    
    The maximum number of keys to preread.

<!-- end list -->

  - keysPreread  
    Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  
    
    Returns the number of keys to actually preread.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.Windows7.PrereadKeysGrbit](hh565843\(v=exchg.10\).md)  
    
    Preread options. Used to specify the direction of the preread.

## See also

#### Reference

[Windows7Api class](dn335406\(v=exchg.10\).md)

[Windows7Api members](dn335300\(v=exchg.10\).md)

[JetPrereadKeys overload](dn335411\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Windows7 namespace](hh577573\(v=exchg.10\).md)

