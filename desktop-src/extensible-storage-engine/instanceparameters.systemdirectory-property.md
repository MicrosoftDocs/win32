---
title: InstanceParameters.SystemDirectory property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'SystemDirectory property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.InstanceParameters.SystemDirectory
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.instanceparameters.systemdirectory(v=EXCHG.10)
ms:contentKeyID: 55103561
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.InstanceParameters.SystemDirectory
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.InstanceParameters.set_SystemDirectory
- Microsoft.Isam.Esent.Interop.InstanceParameters.SystemDirectory
- Microsoft.Isam.Esent.Interop.InstanceParameters.get_SystemDirectory
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# InstanceParameters.SystemDirectory property

Gets or sets the relative or absolute file system path of the folder that will contain the checkpoint file for the instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property SystemDirectory As String
    Get
    Set
'Usage
Dim instance As InstanceParameters
Dim value As String

value = instance.SystemDirectory

instance.SystemDirectory = value
```

``` csharp
public string SystemDirectory { get; set; }
```

#### Property value

Type: [System.String](https://msdn.microsoft.com/en-us/library/s1wwdcbf)  

## See also

#### Reference

[InstanceParameters class](dn350942\(v=exchg.10\).md)

[InstanceParameters members](dn350943\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

