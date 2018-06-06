---
Description: A printer interface DLL's DrvDocumentPropertySheets function is responsible for creating property sheet pages that describe a print document's properties.
ms.assetid: fc7e98ba-5c49-4c2d-af2e-b6c13757f6e6
title: DrvDocumentPropertySheets function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DrvDocumentPropertySheets function

A printer interface DLL's **DrvDocumentPropertySheets** function is responsible for creating property sheet pages that describe a print document's properties.

## Syntax


```C++
LONG DrvDocumentPropertySheets(
  _In_opt_ PPROPSHEETUI_INFO pPSUIInfo,
           LPARAM            lParam
);
```



## Parameters

<dl> <dt>

*pPSUIInfo* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure. Can be **NULL** (see the following Remarks section).

</dd> <dt>

*lParam* 
</dt> <dd>

Caller-supplied integer value that is dependent on the contents of the **Reason** member of the PROPSHEETUI\_INFO structure, as listed in the following table.



| Reason value                         | Definition of *lParam*                                                                                                                                                                                                                                                                                                           |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROPSHEETUI\_REASON\_INIT<br/> | Pointer to a [**DOCUMENTPROPERTYHEADER**](documentpropertyheader.md) structure.<br/>                                                                                                                                                                                                                                      |
| All other reason values<br/>   | See the description of the *lParam* parameter for the [**PFNPROPSHEETUI**](pfnpropsheetui.md) function type.<br/> (The [**DOCUMENTPROPERTYHEADER**](documentpropertyheader.md) structure's address is contained in the **lParamInit** member of the [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure.)<br/> |



 

</dd> </dl>

## Return value

If *pPSUIInfo* is **NULL**, and if either *lParam* -&gt; **fMode** is zero or *lParam -*&gt; **pdmOut** is **NULL**, this function should return the size, in bytes, of the printer's [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure. Otherwise, the function's return value is the same as that described in the ReturnValue section of the [**PFNPROPSHEETUI**](pfnpropsheetui.md) function type. For more information, see the Remarks section.

## Remarks

All [printer interface DLLs](https://www.bing.com/search?q=printer+interface+DLLs) must provide a **DrvDocumentPropertySheets** function, which is defined using the [**PFNPROPSHEETUI**](pfnpropsheetui.md) function type. The function's purpose is to call the [**ComPropSheet**](compropsheet.md) function, provided by [CPSUI](https://www.bing.com/search?q=CPSUI), to specify property sheet pages containing user-modifiable properties for print documents.

If the value received for the *pPSUIInfo* parameter is not **NULL**, the NT-based operating system print spooler is calling the function indirectly, through CPSUI. The following rules apply:

-   The function should perform operations as described for the [**PFNPROPSHEETUI**](pfnpropsheetui.md) function type.

-   Flags in the **fMode** member of the [**DOCUMENTPROPERTYHEADER**](documentpropertyheader.md) structure indicate which property sheet pages to display and whether the user should be allowed to modify a document's properties. The only flags that might be set are DM\_IN\_PROMPT (or DM\_PROMPT), DM\_ADVANCED, DM\_NOPERMISSION, and DM\_OUT\_BUFFER (or DM\_COPY).

If the value received for the *pPSUIInfo* parameter is **NULL**, the print spooler is calling the function directly, without going through CPSUI. In this case, the *lParam* parameter contains the address of a DOCUMENTPROPERTYHEADER structure, and the following rules apply:

-   If the **fMode** member of the [**DOCUMENTPROPERTYHEADER**](documentpropertyheader.md) structure is zero, or if the **pdmOut** member of the same structure is **NULL**, the function should return just the total size of the printer's [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure, including public and private structure members, in the DOCUMENTPROPERTYHEADER structure's **cbOut** member.

-   If the **fMode** member of the DOCUMENTPROPERTYHEADER structure is not zero, the function should perform the operations indicated by the **fMode** flags. The only flags that might be set are DM\_IN\_BUFFER (or DM\_MODIFY), and DM\_OUT\_BUFFER (or DM\_COPY).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvDevicePropertySheets**](drvdevicepropertysheets.md)
</dt> <dt>

[**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md)
</dt> <dt>

[**DOCUMENTPROPERTYHEADER**](documentpropertyheader.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvDocumentPropertySheets%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





