---
description: The Manifest property is used to set or get the active activation context.
ms.assetid: 5ad16c7b-3d66-4083-bc0f-f8294757764f
title: ActCtx.Manifest property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ActCtx.Manifest
api_type: 
- COM
api_location: 
- Sxsoa.dll
---

# ActCtx.Manifest property

The **Manifest** property is used to set or get the active activation context.

This property is read-only.

## Syntax


```JScript
propVal = ActCtx.Manifest
```



## Property value

## Remarks

If an activation context can be created with the manifest file provided, the following script sets the Manifest property and activates the activation constant specified by the manifest. If an activation context cannot be created from the manifest, the activation context remains set to the currently active activation context.

ActCtxObj.Manifest = "<*manifest file name*>";

If an activation context has previously been created or activated, the following script sets the **Manifest** property to the current activation context. If an activation context has not previously been created or activated, this sets the **Manifest** property to an empty string.

"BSTR bstrManifest = ActCtxObj.Manifest"

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Sxsoa.dll</dt> </dl> |
| IID<br/>                      | IID\_IActCtx is defined as 8FA7728F-B69B-4EE5-99F2-E2AA021BEF28<br/>           |



 

 




