---
Description: CPSUI's CommonPropertySheetUI function displays property sheet pages and allows user modifications to displayed values.
ms.assetid: 63d88589-455a-4923-bb3a-61d977732603
title: CommonPropertySheetUI function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CommonPropertySheetUI function

CPSUI's **CommonPropertySheetUI** function displays property sheet pages and allows user modifications to displayed values.

## Syntax


```C++
LONG CommonPropertySheetUI(
   HWND           hWndOwner,
   PFNPROPSHEETUI pfnPropSheetUI,
   LPARAM         lParam,
   LPDWORD        pResult
);
```



## Parameters

<dl> <dt>

*hWndOwner* 
</dt> <dd>

Caller-supplied window handle identifying the window into which new property sheet pages are to be placed.

</dd> <dt>

*pfnPropSheetUI* 
</dt> <dd>

Caller-supplied pointer to a [**PFNPROPSHEETUI**](pfnpropsheetui.md)-typed callback function.

</dd> <dt>

*lParam* 
</dt> <dd>

Caller-supplied value that is used as an input argument to the *pfnPropSheetUI* function. This value can be a pointer.

</dd> <dt>

*pResult* 
</dt> <dd>

Caller-supplied pointer to a DWORD that receives the *pfnPropSheetUI* function's final return status. If **NULL**, the final return status is not returned. For more information, see the following Remarks section.

</dd> </dl>

## Return value

The **CommonPropertySheetUI** function returns one of the following values:



| Return code                                                                                                   | Description                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**CPSUI\_CANCEL**</dt> </dl>                  | The *pfnPropSheetUI* function returned a negative value.<br/>                                                                                     |
| <dl> <dt>**CPSUI\_OK**</dt> </dl>                      | The operation succeeded.<br/>                                                                                                                     |
| <dl> <dt>**CPSUI\_REBOOTSYSTEM**</dt> </dl>            | The operation succeeded, and a dialog box procedure sent the PSM\_REBOOTSYSTEM message (defined in the Microsoft Windows SDK documentation).<br/> |
| <dl> <dt>**CPSUI\_RESTARTWINDOWS**</dt> </dl>          | The operation succeeded, and a dialog box procedure sent the PSM\_RESTARTWINDOWS message (defined in the Windows SDK documentation).<br/>         |
| <dl> <dt>**ERR\_CPSUI-prefixed error code**</dt> </dl> | A failure occurred. The ERR\_CPSUI-prefixed error codes are defined in compstui.h.<br/>                                                           |



 

## Remarks

The **CommonPropertySheetUI** function is CPSUI's entry point for applications. A CPSUI application (such as the Microsoft NT-based operating system print spooler) can call the function to add one or more property sheet pages to a predefined parent window. CPSUI displays the pages, allows the user to modify them, and notifies the application of user activity through callback functions.

The NT-based operating system print spooler calls the **CommonPropertySheetUI** function when a Win32 application calls the spooler's DocumentProperties or PrinterProperties functions, which are described in the Windows SDK documentation.

The callback function specified by the *pfnPropSheetUI* parameter is responsible for describing the property sheet pages to be added. For more information, see the description of the [**PFNPROPSHEETUI**](pfnpropsheetui.md) function type.

The sequence of operation is as follows:

1.  The **CommonPropertySheetUI** function calls the *pfnPropSheetUI* callback so the callback can describe the pages to be added by calling CPSUI's [**ComPropSheet**](compropsheet.md) function.

2.  If the *pfnPropSheetUI* callback succeeds, the **CommonPropertySheetUI** function displays the new property sheet pages and allows the user to modify page values.

3.  If the user modifies page values, a [page event callback](https://www.bing.com/search?q=page event callback) notifies the application of the changes.

4.  When the user chooses the **OK** or **Cancel** button, the **CommonPropertySheetUI** function destroys the displayed pages and returns.

For more information about the sequence of operation, see [Using CPSUI with Printer Drivers](https://www.bing.com/search?q=Using CPSUI with Printer Drivers), in the section entitled [CPSUI](https://www.bing.com/search?q=CPSUI).

The **CommonPropertySheetUI** function actually calls the *pfnPropSheetUI* callback several times, specifying different **Reason** member values in the callback's [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure. Each time the callback returns, it places a result status in the PROPSHEETUI\_INFO structure's **Result** member. When the **CommonPropertySheetUI** function returns, it copies the final contents of **Result** into the location pointed to by *pResult*.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20CommonPropertySheetUI%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




