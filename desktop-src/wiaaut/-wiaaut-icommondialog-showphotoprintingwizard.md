---
title: CommonDialog.ShowPhotoPrintingWizard method
description: Starts the Photo Printing Wizard with the absolute path of a specific file or Vector of absolute paths to files.
ms.assetid: 5643a206-f312-4b85-8410-f650ac77b98a
keywords:
- ShowPhotoPrintingWizard method WIA Automation
- ShowPhotoPrintingWizard method WIA Automation , CommonDialog object
- CommonDialog object WIA Automation , ShowPhotoPrintingWizard method
topic_type:
- apiref
api_name:
- CommonDialog.ShowPhotoPrintingWizard
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CommonDialog.ShowPhotoPrintingWizard method

Starts the **Photo Printing Wizard** with the absolute path of a specific file or [**Vector**](-wiaaut-vector.md) of absolute paths to files.

## Syntax


```VB
CommonDialog.ShowPhotoPrintingWizard( _
  ByVal Files As VARIANT _
) As HRESULT
```



## Parameters

<dl> <dt>

*Files* \[in\]
</dt> <dd>

Type: **VARIANT\***

Required. **Variant** value.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Examples

The following example shows how to launch the **Photo Printing Wizard** to print some of the sample pictures from Windows XP.


```
Dim v 'As Vector

Set v = CreateObject("WIA.Vector")

v.Add "C:\WINDOWS\Web\Wallpaper\Ascent.jpg"
v.Add "C:\WINDOWS\Web\Wallpaper\Autumn.jpg"
v.Add "C:\WINDOWS\Web\Wallpaper\Azul.jpg"
v.Add "C:\WINDOWS\Web\Wallpaper\Follow.jpg"
v.Add "C:\WINDOWS\Web\Wallpaper\Red moon desert.jpg"
v.Add "C:\WINDOWS\Web\Wallpaper\Stonehenge.jpg"
v.Add "C:\WINDOWS\Web\Wallpaper\Tulips.jpg"
v.Add "C:\WINDOWS\Web\Wallpaper\Wind.jpg"

CommonDialog1.ShowPhotoPrintingWizard v
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**CommonDialog**](-wiaaut-commondialog.md)
</dt> </dl>

 

 





