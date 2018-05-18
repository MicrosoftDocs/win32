---
title: Extension Extensions property
description: The Extensions property returns the Extensions object for the extension snap-in. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bec3a7f4-1b39-416a-a704-64a267e78e63'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Extensions property MMC", "Extensions property MMC , Extension object", "Extension object MMC , Extensions property", "Extensions property MMC , Extension interface", "Extension interface MMC , Extensions property"]
topic_type:
- apiref
api_name:
- Extension.Extensions
- Extension.Extensions
api_location:
- Mmcndmgr.dll
api_type:
- COM
---

# Extension::Extensions property

The **Extensions** property returns the [**Extensions**](extensions-collection.md) object for the extension snap-in. This property is read-only.

## Syntax


```VB
Property Extensions As Extensions
```



## Property value

The [**Extensions**](extensions-collection.md) object for the snap-in.

## Remarks

The [**Extension**](extension-object.md) object is a snap-in, and the **Extensions** property represents the extensions that can extend the **Extension** object.

## Examples


```VB
' Retrieve the Extensions property.
Dim objExts2 As MMC20.Extensions
Set objExts2 = objExt.Extensions
 
' Use the Extensions object.
' This code displays Extensions.Count.
MsgBox ("Number of Extensions: " & objExts2.Count)
 
' Free the object when done.
Set objExts2 = Nothing
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Extension is defined as AD4D6CA6-912F-409b-A26E-7FD234AEF542<br/>            |



## See also

<dl> <dt>

[**Extension.EnableAllExtensions**](extension-enableallextensions.md)
</dt> <dt>

[**Extensions collection**](extensions-collection.md)
</dt> </dl>

 

 





