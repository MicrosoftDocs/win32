---
title: JET_PFNREALLOC delegate (Microsoft.Isam.Esent.Interop)
TOCTitle: JET_PFNREALLOC delegate
ms:assetid: T:Microsoft.Isam.Esent.Interop.JET_PFNREALLOC
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_pfnrealloc(v=EXCHG.10)
ms:contentKeyID: 39515764
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_PFNREALLOC
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_PFNREALLOC..ctor
- Microsoft.Isam.Esent.Interop.JET_PFNREALLOC.BeginInvoke
- Microsoft.Isam.Esent.Interop.JET_PFNREALLOC.EndInvoke
- Microsoft.Isam.Esent.Interop.JET_PFNREALLOC.Invoke
- Microsoft.Isam.Esent.Interop.JET_PFNREALLOC
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_PFNREALLOC delegate

Callback used by JetEnumerateColumns to allocate memory for its output buffers.

This API is not CLS-compliant. 

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<CLSCompliantAttribute(False)> _
Public Delegate Function JET_PFNREALLOC ( _
    context As IntPtr, _
    memory As IntPtr, _
    requestedSize As UInteger _
) As IntPtr
'Usage
Dim instance As New JET_PFNREALLOC(AddressOf HandlerMethod)
```

``` csharp
[CLSCompliantAttribute(false)]
public delegate IntPtr JET_PFNREALLOC(
    IntPtr context,
    IntPtr memory,
    uint requestedSize
)
```

#### Parameters

  - context  
    Type: [System.IntPtr](https://msdn.microsoft.com/en-us/library/5he14kz8)  
    
    Context given to JetEnumerateColumns.

<!-- end list -->

  - memory  
    Type: [System.IntPtr](https://msdn.microsoft.com/en-us/library/5he14kz8)  
    
    If non-zero, a pointer to a memory block previously allocated by this callback.

<!-- end list -->

  - requestedSize  
    Type: [System.UInt32](https://msdn.microsoft.com/en-us/library/ctys3981)  
    
    The new size of the memory block (in bytes). If this is 0 and a memory block is specified, that memory block will be freed.

#### Return value

Type: [System.IntPtr](https://msdn.microsoft.com/en-us/library/5he14kz8)  
A pointer to newly allocated memory. If memory could not be allocated then [Zero](https://msdn.microsoft.com/en-us/library/c61h0w61) should be returned.  

## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

