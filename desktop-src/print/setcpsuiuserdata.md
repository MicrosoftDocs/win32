---
Description: 'CPSUI''s SetCPSUIUserData function allows CPSUI applications (including printer interface DLLs) to associate nondisplayed data with a property sheet dialog box.'
ms.assetid: '35119100-adf9-4376-bb1a-7317733fbcc5'
title: SetCPSUIUserData function
---

# SetCPSUIUserData function

CPSUI's `SetCPSUIUserData` function allows CPSUI applications (including printer interface DLLs) to associate nondisplayed data with a property sheet dialog box.

## Syntax


```C++
BOOL SetCPSUIUserData(
   HWND      hDlg,
   ULONG_PTR CPSUIUserData
);
```



## Parameters

<dl> <dt>

*hDlg* 
</dt> <dd>

Caller-supplied handle to a property sheet dialog box. For more information, see the following Remarks section.

</dd> <dt>

*CPSUIUserData* 
</dt> <dd>

Caller-supplied value to be stored.

</dd> </dl>

## Return value

The function returns **TRUE** if it is successful in associating the nondisplayed data with the property sheet dialog box, and **FALSE** otherwise.

## Remarks

The `SetCPSUIUserData` function should be called only from within a dialog box procedure that has been associated with a dialog box by using a [**DLGPAGE**](dlgpage.md) or an [**EXTPUSH**](extpush.md) structure.

A value that is stored by calling `SetCPSUIUserData` can be later retrieved by calling [**GetCPSUIUserData**](getcpsuiuserdata.md).

The handle specified for *hDlg* must be the handle received as input to the dialog box procedure. (Dialog box procedures are described in the Microsoft Windows SDK documentation.)

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Compstui.lib</dt> </dl>                    |
| DLL<br/>             | <dl> <dt>Compstui.dll</dt> </dl>                    |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SetCPSUIUserData%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




