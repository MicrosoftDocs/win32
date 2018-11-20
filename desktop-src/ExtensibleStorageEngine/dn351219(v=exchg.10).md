---
title: JET_OPENTEMPORARYTABLE.cbVarSegMac property  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'cbVarSegMac property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.cbVarSegMac
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.vista.jet_opentemporarytable.cbvarsegmac(v=EXCHG.10)
ms:contentKeyID: 55104115
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.cbVarSegMac
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.cbVarSegMac
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.get_cbVarSegMac
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.set_cbVarSegMac
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_OPENTEMPORARYTABLE.cbVarSegMac property

Gets or sets maximum amount of data that will be used from any variable lengthcolumn to construct a key for a given row. This parameter may be used to control the amount of key space consumed by any given key column. This limit is in bytes. If this parameter is zero or is the same as the [cbKeyMost](dn335290\(v=exchg.10\).md) property then no limit is in effect.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cbVarSegMac As Integer
    Get
    Set
'Usage
Dim instance As JET_OPENTEMPORARYTABLE
Dim value As Integer

value = instance.cbVarSegMac

instance.cbVarSegMac = value
```

``` csharp
public int cbVarSegMac { get; set; }
```

#### Property value

Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  

## See also

#### Reference

[JET\_OPENTEMPORARYTABLE class](dn351217\(v=exchg.10\).md)

[JET\_OPENTEMPORARYTABLE members](dn335285\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

