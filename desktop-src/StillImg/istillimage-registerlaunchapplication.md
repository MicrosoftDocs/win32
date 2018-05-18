---
title: RegisterLaunchApplication method
description: The IStillImage RegisterLaunchApplication method puts an application in the Event Monitor's list of currently running applications that use the push model.
ms.assetid: '4d3057ac-030d-45db-9a86-af3c7bcdb94d'
keywords: ["RegisterLaunchApplication method Still Image"]
topic_type:
- apiref
api_name:
- RegisterLaunchApplication
api_location:
- Sti.dll
api_type:
- COM
---

# RegisterLaunchApplication method

The **IStillImage::RegisterLaunchApplication** method puts an application in the Event Monitor's list of currently running applications that use the push model.

## Syntax


```C++
HRESULT RegisterLaunchApplication(
  [in] LPWSTR pwszAppName,
  [in] LPWSTR pwszCommandLine
);
```



## Parameters

<dl> <dt>

*pwszAppName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that contains the name of the application. This name is used in the Control Panel property sheet where you associate applications with device events.

</dd> <dt>

*pwszCommandLine* \[in\]
</dt> <dd>

Pointer to a null-terminated string that contains the full path to the executable file for this application. Additional command line arguments can be appended to this command. Two pairs of quotation marks should be used, for example, "\\"C:\\Program Files\\MyExe.exe\\" /arg1".

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK.

If the method fails, the return value is the appropriate COM error.

## Remarks

This method must be called after an application is launched. It tells the Event Monitor to add the application to its list of currently running applications that use the push model.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Sti.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Sti.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sti.dll</dt> </dl> |



## See also

<dl> <dt>

[About Still Image](about-still-image.md)
</dt> <dt>

[Making an Application Still Image-Aware](making-an-application-still-image-aware.md)
</dt> </dl>

 

 





