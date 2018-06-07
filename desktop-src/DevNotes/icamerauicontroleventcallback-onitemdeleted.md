---
Description: Occurs when an item is deleted.
ms.assetid: 008bac9d-4daa-4729-b414-b9551eb636f1
title: ICameraUIControlEventCallback::OnItemDeleted method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ICameraUIControlEventCallback::OnItemDeleted method

Occurs when an item is deleted.

## Syntax


```C++
void OnItemDeleted(
  [in] LPCWSTR pszPath
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

The path to the deleted item.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                              |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| IDL<br/>                      | <dl> <dt>CameraUIControl.idl</dt> </dl> |



## See also

<dl> <dt>

[**ICameraUIControlEventCallback**](/windows/desktop/api/camerauicontrol/nn-camerauicontrol-icamerauicontroleventcallback)
</dt> </dl>

 

 




