---
title: JET_COLUMNID.ToString method (String, IFormatProvider) (Microsoft.Isam.Esent.Interop)
TOCTitle: ToString method (String, IFormatProvider)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_COLUMNID.ToString(System.String,System.IFormatProvider)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_columnid.tostring(v=EXCHG.10)
ms:contentKeyID: 39513695
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_COLUMNID.ToString
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_COLUMNID.ToString method (String, IFormatProvider)

Formats the value of the current instance using the specified format.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function ToString ( _
    format As String, _
    formatProvider As IFormatProvider _
) As String
'Usage
Dim instance As JET_COLUMNID
Dim format As String
Dim formatProvider As IFormatProvider
Dim returnValue As String

returnValue = instance.ToString(format, _
    formatProvider)
```

``` csharp
public string ToString(
    string format,
    IFormatProvider formatProvider
)
```

#### Parameters

  - format  
    Type: [System.String](https://msdn.microsoft.com/en-us/library/s1wwdcbf)  
    
    The [String](https://msdn.microsoft.com/en-us/library/s1wwdcbf) specifying the format to use. -or- null to use the default format defined for the type of the [IFormattable](https://msdn.microsoft.com/en-us/library/bk5yxz0f) implementation.

<!-- end list -->

  - formatProvider  
    Type: [System.IFormatProvider](https://msdn.microsoft.com/en-us/library/efh2ww9y)  
    
    The [IFormatProvider](https://msdn.microsoft.com/en-us/library/efh2ww9y) to use to format the value. -or- null to obtain the numeric format information from the current locale setting of the operating system.

#### Return value

Type: [System.String](https://msdn.microsoft.com/en-us/library/s1wwdcbf)  
A [String](https://msdn.microsoft.com/en-us/library/s1wwdcbf) containing the value of the current instance in the specified format.  

#### Implements

[IFormattable.ToString(String, IFormatProvider)](https://msdn.microsoft.com/en-us/library/bhf180ey)  

## See also

#### Reference

[JET_COLUMNID structure](hh564510\(v=exchg.10\).md)

[JET_COLUMNID members](hh558343\(v=exchg.10\).md)

[ToString overload](hh558497\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

