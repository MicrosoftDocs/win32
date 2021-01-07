---
description: "Learn more about: Update.Save method (Byte , Int32, Int32)"
title: Update.Save method (Byte , Int32, Int32)
TOCTitle: Save method (Byte , Int32, Int32)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Update.Save(System.Byte[],System.Int32,System.Int32@)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.update.save(v=EXCHG.10)
ms:contentKeyID: 55107759
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Update.Save
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Update.Save method (Byte , Int32, Int32)

Update the tableid.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Sub Save ( _
    bookmark As Byte(), _
    bookmarkSize As Integer, _
    <OutAttribute> ByRef actualBookmarkSize As Integer _
)
'Usage
Dim instance As Update
Dim bookmark As Byte()
Dim bookmarkSize As Integer
Dim actualBookmarkSize As Integer

instance.Save(bookmark, bookmarkSize, _
    actualBookmarkSize)
```

``` csharp
public void Save(
    byte[] bookmark,
    int bookmarkSize,
    out int actualBookmarkSize
)
```

#### Parameters

  - bookmark  
    Type: \[\]  
    
    Returns the bookmark of the updated record. This can be null.

<!-- end list -->

  - bookmarkSize  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The size of the bookmark buffer.

<!-- end list -->

  - actualBookmarkSize  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Returns the actual size of the bookmark.

## Remarks

Save is the final step in performing an insert or an update. The update is begun by calling creating an Update object and then by calling JetSetColumn or JetSetColumns one or more times to set the record state. Finally, Update is called to complete the update operation. Indexes are updated only by Update or and not during JetSetColumn or JetSetColumns.

## See also

#### Reference

[Update class](./update-class.md)

[Update members](./update-members.md)

[Save overload](./update.save-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
