---
Description: The MESSAGEBOX\_PARAMS structure is used by the SplPromptUIInUsersSession function to hold information about the appearance and behavior of a message box.
ms.assetid: 28a94e25-9beb-46a1-9e9d-9fe4823372be
title: MESSAGEBOX\_PARAMS structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MESSAGEBOX\_PARAMS structure

The MESSAGEBOX\_PARAMS structure is used by the [**SplPromptUIInUsersSession**](splpromptuiinuserssession.md) function to hold information about the appearance and behavior of a message box.

## Syntax


```C++
typedef struct {
  DWORD  cbSize;
  LPWSTR pTitle;
  LPWSTR pMessage;
  DWORD  Style;
  DWORD  dwTimeout;
  BOOL   bWait;
} MESSAGEBOX_PARAMS, *PMESSAGEBOX_PARAMS;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Specifies the size, in bytes, of this structure.

</dd> <dt>

**pTitle**
</dt> <dd>

Pointer to a null-terminated string that is used in the title bar of the message box.

</dd> <dt>

**pMessage**
</dt> <dd>

Pointer to a null-terminated string that contains the message to display.

</dd> <dt>

**Style**
</dt> <dd>

Specifies the contents and behavior of the message box. For a complete list of the values to which this member can be set, see the description of the **MessageBox** function in the Microsoft Windows SDK documentation.

</dd> <dt>

**dwTimeout**
</dt> <dd>

Specifies the time, in seconds, to wait for the user's response, provided that the **bWait** member is **TRUE**.

</dd> <dt>

**bWait**
</dt> <dd>

Specifies whether the **SplPromptUIInUsersSession** function should wait for a user's response. If **bWait** is **TRUE**, **SplPromptUIInUsersSession** does not return until either the user responds or the time-out interval elapses. If **dwTimeout** is zero, **SplPromptUIInUsersSession** does not return until the user responds. If **bWait** is **FALSE**, the function returns immediately with \**pResponse* set to IDASYNC.

</dd> </dl>

## Remarks

One member of the [**SHOWUIPARAMS**](showuiparams.md) structure is a MESSAGEBOX\_PARAMS structure.

## Requirements



|                    |                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------|
| Version<br/> | This structure is available in Windows XP and later operating systems.<br/>                        |
| Header<br/>  | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**SplPromptUIInUsersSession**](splpromptuiinuserssession.md)
</dt> <dt>

[**SHOWUIPARAMS**](showuiparams.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20MESSAGEBOX_PARAMS%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





