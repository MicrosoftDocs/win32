---
title: PCMSCALLBACK callback function
description: The function ApplyCallbackFunction is a callback function which updates the WCS configuration data while the dialog box displayed by the SetupColorMatching function is executing.
ms.assetid: '0f98f6ca-d772-4214-b0aa-f439b214ce4e'
keywords: ["ApplyCallbackFunction callback function Windows Color System", "PCMSCALLBACK"]
topic_type:
- apiref
api_name:
- ApplyCallbackFunction
api_location:
- Icm.h
api_type:
- UserDefined
---

# PCMSCALLBACK callback function

The function **ApplyCallbackFunction** is a callback function which updates the WCS configuration data while the dialog box displayed by the **SetupColorMatching** function is executing. The name **ApplyCallbackFunction** is a placeholder. The actual name of this callback function is supplied by the application using ICM.

## Syntax


```C++
BOOL ApplyCallbackFunction(
   COLORMATCHSETUP *pColorMatchSetup,
   LPARAM          lParam
);
```



## Parameters

<dl> <dt>

*pColorMatchSetup* 
</dt> <dd>

Pointer to a [**COLORMATCHSETUP**](colormatchsetup.md) structure that contains WCS configuration data.

</dd> <dt>

*lParam* 
</dt> <dd>

Contains a value supplied by the application.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. The callback function can set the extended error information by calling [**SetLastError**](wcs-setlasterror).

## Remarks

The **ApplyCallbackFunction** function is used to change the WCS configuration for a device while the Color Management dialog box is displayed. The Color Management dialog box is displayed by the [**SetupColorMatching**](setupcolormatching.md) function.

If the callback function is provided, an **Apply** button is displayed in the lower right of the dialog box. When you select the **Apply** button, the callback function immediately updates the configuration for the device being set up. The Color Management dialog box remains on the screen.

An application supplies a callback function to WCS by storing the address of the callback function in the [**COLORMATCHSETUP**](colormatchsetup.md) structure that is passed to the [**SetupColorMatching**](setupcolormatching.md) function. The address is stored in the [**lPfnApplyCallback**](wcs-ipfnapplycallback) member of the **COLORMATCHSETUP** structure. The **dwFlags** member should be set to CMS\_USEAPPLYCALLBACK, or the callback function will be ignored.

A value supplied by the application may be passed to the callback function. Prior to invoking the [**SetupColorMatching**](setupcolormatching.md) function, the application can store a value in the [**lParamApplyCallback**](wcs-iparamapplycallback) member of the [**COLORMATCHSETUP**](colormatchsetup.md) structure. When the callback function is invoked, the value in the **lParamApplyCallback** structure member will be passed to the callback function in its *lParam* parameter.

The callback function is completely optional. If it is not supplied, the **Apply** button does not appear in the Color Management dialog box. Microsoft strongly recommends that your application supplies a callback function.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**SetupColorMatching**](setupcolormatching.md)
</dt> <dt>

[**COLORMATCHSETUP**](colormatchsetup.md)
</dt> </dl>

 

 





