---
Description: The SplPromptUIInUsersSession function uses the SHOWUIPARAMS structure to hold information about the appearance and behavior of a message box.
ms.assetid: 63ee7f5c-ca95-4c2d-be17-56a769188f8c
title: SHOWUIPARAMS structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SHOWUIPARAMS structure

The [**SplPromptUIInUsersSession**](splpromptuiinuserssession.md) function uses the SHOWUIPARAMS structure to hold information about the appearance and behavior of a message box.

## Syntax


```C++
typedef struct {
  UI_TYPE           UIType;
  MESSAGEBOX_PARAMS MessageBoxParams;
} SHOWUIPARAMS, *PSHOWUIPARAMS;
```



## Members

<dl> <dt>

**UIType**
</dt> <dd>

Specifies the type of user interface element. This member can be set to a single value: **kMessageBox**.

</dd> <dt>

**MessageBoxParams**
</dt> <dd>

Specifies a [**MESSAGEBOX\_PARAMS**](messagebox-params.md) structure that contains the information about the message box.

</dd> </dl>

## Remarks

## Requirements



|                    |                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------|
| Version<br/> | This function is available in Windows XP and later operating systems.<br/>                         |
| Header<br/>  | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**SplPromptUIInUsersSession**](splpromptuiinuserssession.md)
</dt> <dt>

[**MESSAGEBOX\_PARAMS**](messagebox-params.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SHOWUIPARAMS%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





