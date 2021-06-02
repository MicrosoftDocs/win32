---
description: "Learn more about: InstanceParameters.LogFileDirectory property"
title: InstanceParameters.LogFileDirectory property 
TOCTitle: 'LogFileDirectory property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.InstanceParameters.LogFileDirectory
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.instanceparameters.logfiledirectory(v=EXCHG.10)
ms:contentKeyID: 55103562
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.InstanceParameters.LogFileDirectory
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.InstanceParameters.LogFileDirectory
- Microsoft.Isam.Esent.Interop.InstanceParameters.get_LogFileDirectory
- Microsoft.Isam.Esent.Interop.InstanceParameters.set_LogFileDirectory
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# InstanceParameters.LogFileDirectory property

Gets or sets the relative or absolute file system path of the folder that will contain the transaction logs for the instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property LogFileDirectory As String
    Get
    Set
'Usage
Dim instance As InstanceParameters
Dim value As String

value = instance.LogFileDirectory

instance.LogFileDirectory = value
```

``` csharp
public string LogFileDirectory { get; set; }
```

#### Property value

Type: [System.String](/dotnet/api/system.string)  

## See also

#### Reference

[InstanceParameters class](./instanceparameters-class.md)

[InstanceParameters members](./instanceparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
