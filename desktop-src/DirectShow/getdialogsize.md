---
description: The GetDialogSize function retrieves the size of a resource dialog box.
ms.assetid: b6c42f96-0381-493a-9503-f3bd4c6a8e1e
title: GetDialogSize function (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetDialogSize
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# GetDialogSize function

The **GetDialogSize** function retrieves the size of a resource dialog box.

## Syntax


```C++
BOOL WINAPI GetDialogSize(
   int     iResourceID,
   DLGPROC pDlgProc,
   LPARAM  lParam,
   SIZE    *pResult
);
```



## Parameters

<dl> <dt>

*iResourceID* 
</dt> <dd>

Dialog box resource identifier.

</dd> <dt>

*pDlgProc* 
</dt> <dd>

Pointer to the dialog box procedure.

</dd> <dt>

*lParam* 
</dt> <dd>

Value passed in the WM\_INITDIALOG message sent to the temporary dialog box just after it is created.

</dd> <dt>

*pResult* 
</dt> <dd>

Pointer to a **SIZE** structure that receives the dimensions of the dialog box, in screen pixels.

</dd> </dl>

## Return value

Returns **TRUE** if the dialog box resource was found, or **FALSE** otherwise.

## Remarks

Property pages can use this function to return the actual display size they require. Most property pages are dialog boxes and, as such, have dialog box templates stored in resource files. Templates use dialog box units that do not map directly onto screen pixels. However, a property page's [**GetPageInfo**](cbasepropertypage-getpageinfo.md) function must return the actual display size in pixels. The property page can call `GetDialogSize` to calculate the display size.

This function creates a temporary instance of the dialog box. To avoid having the dialog box appear on the screen, the dialog box template in the resource file should not have a WS\_VISIBLE property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Property Page Helper Functions](property-page-helper-functions.md)
</dt> </dl>

 

 




