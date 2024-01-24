---
description: "Learn more about: Update.SaveAndGotoBookmark method"
title: Update.SaveAndGotoBookmark method 
TOCTitle: 'SaveAndGotoBookmark method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Update.SaveAndGotoBookmark
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.update.saveandgotobookmark(v=EXCHG.10)
ms:contentKeyID: 55104204
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Update.SaveAndGotoBookmark
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Update.SaveAndGotoBookmark
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Update.SaveAndGotoBookmark method

Update the tableid and position the tableid on the record that was modified. This can be useful when inserting a record because by default the tableid remains in its old location.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Sub SaveAndGotoBookmark
'Usage
Dim instance As Update

instance.SaveAndGotoBookmark()
```

``` csharp
public void SaveAndGotoBookmark()
```

## Remarks

Save is the final step in performing an insert or an update. The update is begun by calling creating an Update object and then by calling JetSetColumn or JetSetColumns one or more times to set the record state. Finally, Update is called to complete the update operation. Indexes are updated only by Update or and not during JetSetColumn or JetSetColumns.

## See also

#### Reference

[Update class](./update-class.md)

[Update members](./update-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
