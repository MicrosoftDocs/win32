---
title: UnRegisterLaunchApplication method
description: The IStillImage UnRegisterLaunchApplication method removes the application from the Event Monitors list of applications that use the push model. Once this method has run, the application no longer receives device events.
ms.assetid: 01bbb784-e6db-4d59-877c-0dd19ac3fd11
keywords:
- UnRegisterLaunchApplication method Still Image
topic_type:
- apiref
api_name:
- UnRegisterLaunchApplication
api_location:
- Sti.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UnRegisterLaunchApplication method

The **IStillImage::UnRegisterLaunchApplication** method removes the application from the Event Monitor's list of applications that use the push model. Once this method has run, the application no longer receives device events.

## Syntax


```C++
HRESULT UnRegisterLaunchApplication(
  [in] PSTI   pSti,
  [in] LPWSTR pwszAppName
);
```



## Parameters

<dl> <dt>

*pSti* \[in\]
</dt> <dd>

Pointer to the **IStillImage** interface object.

</dd> <dt>

*pwszAppName* \[in\]
</dt> <dd>

The name that the application used when it registered itself using [**RegisterLaunchApplication**](istillimage-registerlaunchapplication.md).

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK.

If the method fails, the return value is the appropriate COM error.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Sti.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Sti.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sti.dll</dt> </dl> |



## See also

<dl> <dt>

[About Still Image](about-still-image.md)
</dt> <dt>

[Making an Application Still Image-Aware](making-an-application-still-image-aware.md)
</dt> </dl>

 

 





