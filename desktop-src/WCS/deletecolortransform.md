---
title: DeleteColorTransform function
description: The DeleteColorTransform function deletes a given color transform.
ms.assetid: 2efd98d8-851f-4a6c-b91b-2430895a7a53
keywords:
- DeleteColorTransform function Windows Color System
topic_type:
- apiref
api_name:
- DeleteColorTransform
api_location:
- mscms.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DeleteColorTransform function

The **DeleteColorTransform** function deletes a given color transform.

## Syntax


```C++
BOOL WINAPI DeleteColorTransform(
   HTRANSFORM hColorTransform
);
```



## Parameters

<dl> <dt>

*hColorTransform* 
</dt> <dd>

Identifies the color transform to delete.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**The COLOR Structure**](color.md#-color-the-color-structure)
</dt> <dt>

[**CreateMultiProfileTransform**](createmultiprofiletransform.md)
</dt> </dl>

 

 





