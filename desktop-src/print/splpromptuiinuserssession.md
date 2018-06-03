---
Description: The SplPromptUIInUsersSession function displays a standard message box in the session indicated by the printer handle and job ID.
ms.assetid: 5e458e3b-cfe2-4d48-b386-34d2a6c1d15e
title: SplPromptUIInUsersSession function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SplPromptUIInUsersSession function

The `SplPromptUIInUsersSession` function displays a standard message box in the session indicated by the printer handle and job ID.

## Syntax


```C++
BOOL SplPromptUIInUsersSession(
  _In_  HANDLE        hPrinter,
  _In_  DWORD         JobId,
  _In_  PSHOWUIPARAMS pUIParams,
  _Out_ DWORD         *pResponse
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

Handle to the printer.

</dd> <dt>

*JobId* \[in\]
</dt> <dd>

Specifies the print job.

</dd> <dt>

*pUIParams* \[in\]
</dt> <dd>

Pointer to a [**SHOWUIPARAMS**](showuiparams.md) structure that contains values that determine the appearance and behavior of the message box.

</dd> <dt>

*pResponse* \[out\]
</dt> <dd>

Pointer to a memory location that contains either the user's response or the IDASYNC constant. For more information, see the Remarks section.

</dd> </dl>

## Return value

On success, the `SplPromptUIInUsersSession` function returns **TRUE**; otherwise it returns **FALSE**.

## Remarks

If *pUIParams* -&gt;**bWait** is **FALSE**, this function returns immediately without waiting for the user's response. In that case, \**pResponse* is set to IDASYNC.

If you plan to use this function in a driver intended to run under Windows 2000, you must load spoolss.dll by a call to the **LoadLibrary** function, and then find the address of this function within that DLL by a call to the **GetProcAddress** function. (**LoadLibrary** and **GetProcAddress** are described in the Microsoft Windows SDK documentation.) If the call to **GetProcAddress** fails, you must use an alternative mechanism to display user interface elements.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Version<br/>         | The SplPromptUIInUsersSession function is available in Windows XP and later<br/>                   |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                   |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**SHOWUIPARAMS**](showuiparams.md)
</dt> <dt>

[**SplIsSessionZero**](splissessionzero.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SplPromptUIInUsersSession%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





