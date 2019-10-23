---
Description: Allows the callback object to specify that an animation be displayed while items are enumerated on a background thread. Used by IShellFolderViewCB::MessageSFVCB.
ms.assetid: 6f8b3894-f08f-4ebf-a645-87869e7d1b20
title: SFVM_GETANIMATION message
ms.topic: reference
ms.date: 05/31/2018
---

# SFVM\_GETANIMATION message

Allows the callback object to specify that an animation be displayed while items are enumerated on a background thread. Used by [**IShellFolderViewCB::MessageSFVCB**](https://msdn.microsoft.com/en-us/library/Bb774968(v=VS.85).aspx).


```C++
SFVM_GETANIMATION 

    wParam = (WPARAM)(HINSTANCE*) phinst;

    lParam = (LPARAM)(WCHAR*) pwszName;

            
```



## Parameters

<dl> <dt>

*phinst* \[out\]
</dt> <dd>

The instance handle of the module that the resource should be loaded from.

</dd> <dt>

*pwszName* \[out\]
</dt> <dd>

A pointer to a null-terminated Unicode string containing the path of the .avi file or the name of an AVI resource. Alternatively, this parameter can consist of the resource identifier in the low-order word and 0 in the high-order word. To create this value, use the [**MAKEINTRESOURCE**](https://msdn.microsoft.com/en-us/library/ms648029(v=VS.85).aspx) macro. The control loads the resource from the module specified by hinst. An AVI resource must have the "AVI" type.

</dd> </dl>

## Remarks

By default, the system folder view object displays the "flashlight" animation during a background enumeration.

*phinst* and *pwszName* will be passed to the [animation control](https://msdn.microsoft.com/library/Bb761884(v=VS.85).aspx) with an [**ACM\_OPEN**](https://msdn.microsoft.com/en-us/library/Bb761897(v=VS.85).aspx) message.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




