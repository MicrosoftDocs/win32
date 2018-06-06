---
Description: The SplIsSessionZero function determines whether a certain print job (print handle plus job ID) was issued in session zero.
ms.assetid: 9d68a41d-0f2b-4cf0-92c6-8e05ce6b4378
title: SplIsSessionZero function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SplIsSessionZero function

The `SplIsSessionZero` function determines whether a certain print job (print handle plus job ID) was issued in [*session zero*](https://msdn.microsoft.com/5f6fec1a-1134-4765-81be-9b50939e5e66).

## Syntax


```C++
DWORD SplIsSessionZero(
  _In_  HANDLE hPrinter,
  _In_  DWORD  JobID,
  _Out_ BOOL   *pIsSessionZero
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

Is a handle to the printer.

</dd> <dt>

*JobID* \[in\]
</dt> <dd>

Specifies the print job.

</dd> <dt>

*pIsSessionZero* \[out\]
</dt> <dd>

Pointer to a memory location that is set to **TRUE** if the SessionID for the session is zero; otherwise, this value is set to **FALSE**.

</dd> </dl>

## Return value

On success, the `SplIsSessionZero` function returns ERROR\_SUCCESS; otherwise this function returns a Win32 error code.

## Remarks

A driver that displays custom user interface elements can use the `SplIsSessionZero` function to determine whether the current job was issued in session 0. Such a driver can use this information to enable it to present user interface elements in the user's session, rather than in session zero. A related function, [**SplPromptUIInUsersSession**](splpromptuiinuserssession.md), displays a standard Windows message box in the user's session.

If you plan to use this function in a driver intended to run under Windows 2000, you must load spoolss.dll by a call to the **LoadLibrary** function, and then find the address of this function within that DLL by a call to the **GetProcAddress** function. (**LoadLibrary** and **GetProcAddress** are described in the Microsoft Windows SDK documentation.) If the call to **GetProcAddress** fails, you must use an alternative mechanism to display user interface elements.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Version<br/>         | This function is available in Windows XP and later. <br/>                                          |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                   |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**SplPromptUIInUsersSession**](splpromptuiinuserssession.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SplIsSessionZero%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





