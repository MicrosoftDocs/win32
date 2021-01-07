---
description: "Learn more about: EsentUnicodeTranslationFailException class"
title: EsentUnicodeTranslationFailException class
TOCTitle: EsentUnicodeTranslationFailException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentUnicodeTranslationFailException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentunicodetranslationfailexception(v=EXCHG.10)
ms:contentKeyID: 55103154
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentUnicodeTranslationFailException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentUnicodeTranslationFailException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentUnicodeTranslationFailException class

Base class for JET_err.UnicodeTranslationFail exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](./esentoperationexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentUnicodeTranslationFailException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentUnicodeTranslationFailException _
    Inherits EsentOperationException
'Usage
Dim instance As EsentUnicodeTranslationFailException
```

``` csharp
[SerializableAttribute]
public sealed class EsentUnicodeTranslationFailException : EsentOperationException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentUnicodeTranslationFailException members](./esentunicodetranslationfailexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
