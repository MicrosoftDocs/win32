---
Description: The ComPropSheet function is supplied by CPSUI and can be called by CPSUI applications (including printer interface DLLs) to build property sheet pages.
ms.assetid: d9654346-1f28-4e02-8f6c-17e37ed09b92
title: PFNCOMPROPSHEET routine
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PFNCOMPROPSHEET routine

The *ComPropSheet* function is supplied by [CPSUI](https://www.bing.com/search?q=CPSUI) and can be called by CPSUI applications (including printer interface DLLs) to build property sheet pages.

## Syntax


```C++
PFNCOMPROPSHEET ComPropSheet;

LONG_PTR CALLBACK ComPropSheet(
  _In_ HANDLE hComPropSheet,
  _In_ UINT   Function,
  _In_ LPARAM lParam1,
  _In_ LPARAM lParam2
)
{ ... }
```



## Parameters

<dl> <dt>

*hComPropSheet* \[in\]
</dt> <dd>

Caller-supplied handle to a property sheet [group parent](https://www.bing.com/search?q=group+parent). For more information, see the following Remarks section.

</dd> <dt>

*Function* \[in\]
</dt> <dd>

Caller-supplied, CPSFUNC\_-prefixed ComPropSheet function codes specifying the operation to be performed by the *ComPropSheet* function.

> [!Note]  
> See the **ComPropSheet** function codes table in the **Remarks** section below.

 

</dd> <dt>

*lParam1* \[in\]
</dt> <dd>

Caller-supplied value that depends on the *ComPropSheet* function code supplied for *Function*.

</dd> <dt>

*lParam2* \[in\]
</dt> <dd>

Caller-supplied value that depends on the *ComPropSheet* function code supplied for *Function*.

</dd> </dl>

## Return value

The return value depends on the [ComPropSheet function code](https://www.bing.com/search?q=ComPropSheet+function+code) supplied for *Function*.

## Remarks

When CPSUI calls one of an application's [**PFNPROPSHEETUI**](pfnpropsheetui.md)-typed functions, it passes a pointer to the *ComPropSheet* function in a [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure. A **PFNPROPSHEETUI**-typed function can call the *ComPropSheet* function to describe property sheet pages to CPSUI.

A [printer interface DLL](https://www.bing.com/search?q=printer+interface+DLL) can call *ComPropSheet* from within its [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function or its [**DrvDevicePropertySheets**](drvdevicepropertysheets.md) function.

[User interface plug-ins](https://www.bing.com/search?q=User+interface+plug-ins) for Microsoft's [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) and [*Pscript*](wdkgloss.p#wdkgloss-pscript) drivers can call *ComPropSheet* from within their [**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md) and [**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md) methods.

The [group parent](https://www.bing.com/search?q=group+parent) handle specified for the *hComPropSheet* parameter can be either of the following:

-   The handle received in the *hComPropSheet* member of a [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure.

-   The handle received as a result of previously calling *ComPropSheet* with a [**CPSFUNC\_INSERT\_PSUIPAGE**](https://www.bing.com/search?q=**CPSFUNC\_INSERT\_PSUIPAGE**) function code, and specifying PSUIPAGEINSERT\_GROUP\_PARENT as the **Type** member for an [**INSERTPSUIPAGE\_INFO**](insertpsuipage-info.md) structure.

### ComPropSheet function codes

The following function codes can be passed to the CPSUI's **ComPropSheet** function:



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Function code</th>
<th>Description</th>
<th>Parameters and Return Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CPSFUNC_ADD_HPROPSHEETPAGE</strong></td>
<td>The <strong>CPSFUNC_ADD_HPROPSHEETPAGE</strong> function code causes the <strong>ComPropSheet</strong> function to add a property sheet page that has been created by calling the <strong>CreatePropertySheetPage</strong> function (described in the Microsoft Windows SDK documentation).<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_ADD_HPROPSHEETPAGE</strong> when it calls <strong>ComPropSheet</strong> to add a property sheet page.</li>
<li><em>lParam1</em>: Handle to a property sheet page, obtained by calling the <strong>CreatePropertySheetPage</strong> function.</li>
<li><em>lParam2</em>: Not used, must be zero.</li>
</ul>
<strong>Return Value</strong>If the operation succeeds, <strong>ComPropSheet</strong> returns a CPSUI handle to the added page; otherwise, it returns NULL.<br/></td>
</tr>
<tr class="even">
<td><strong>CPSFUNC_ADD_PCOMPROPSHEETUI</strong></td>
<td>The <strong>CPSFUNC_ADD_PCOMPROPSHEETUI</strong> function code causes the <strong>ComPropSheet</strong> function to add a set of one or more property sheet pages that are described by a <strong>COMPROPSHEETUI</strong> structure.<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_ADD_PCOMPROPSHEETUI</strong> when it calls <strong>ComPropSheet</strong> to add a set of one or more property sheet pages.</li>
<li><em>lParam1</em>: Pointer to a <strong>COMPROPSHEETUI</strong> structure.</li>
<li><em>lParam2</em>: Pointer to a 32-bit location to receive the number of pages added or, if a failure occurs, an ERR_CPSUI-prefixed error code.</li>
</ul>
<strong>Return Value</strong>If the operation succeeds, <strong>ComPropSheet</strong> returns a handle to the set of added pages; otherwise, the function returns NULL.<br/></td>
</tr>
<tr class="odd">
<td><strong>CPSFUNC_ADD_PFNPROPSHEETUI</strong></td>
<td>The <strong>CPSFUNC_ADD_PFNPROPSHEETUI</strong> function code causes the <strong>ComPropSheet</strong> function to call the specified PFNPROPSHEETUI-typed function, which must add a set of one or more property sheet pages.</td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_ADD_PFNPROPSHEETUI</strong> when it calls <strong>ComPropSheet</strong>. <strong>ComPropSheet</strong> then calls the specified PFNPROPSHEETUI-typed function to add a set of one or more property sheet pages.</li>
<li><em>lParam1</em>: Pointer to a PFNPROPSHEETUI-typed function.</li>
<li><em>lParam2</em>: A 32-bit value that is passed to the PFNPROPSHEETUI-typed function for its lParam parameter.</li>
</ul>
<strong>Return Value</strong>If the operation succeeds, <strong>ComPropSheet</strong> returns a handle to the set of added pages; otherwise, the function returns NULL.<br/></td>
</tr>
<tr class="even">
<td><strong>CPSFUNC_ADD_PROPSHEETPAGE</strong></td>
<td>The <strong>CPSFUNC_ADD_PROPSHEETPAGE</strong> function code causes the <strong>ComPropSheet</strong> function to add the type of property sheet page that is described by a <strong>PROPSHEETPAGE</strong> structure (described in the Microsoft Windows SDK documentation).</td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_ADD_PROPSHEETPAGE</strong> when it calls <strong>ComPropSheet</strong> to add the type of property sheet page described by a <strong>PROPSHEETPAGE</strong> structure. The <strong>ComPropSheet</strong> function calls the <strong>CreatePropertySheetPage</strong> function (described in the Windows SDK documentation), and passes the <strong>PROPSHEETPAGE</strong> structure's address to create the page.</li>
<li><em>lParam1</em>: Pointer to a <strong>PROPSHEETPAGE</strong> structure.</li>
<li><em>lParam2</em>: Not used, must be zero.</li>
</ul>
<strong>Return Value</strong>If the operation succeeds, <strong>ComPropSheet</strong> returns a CPSUI handle to the added page; otherwise, it returns NULL.<br/></td>
</tr>
<tr class="odd">
<td><strong>CPSFUNC_DELETE_HCOMPROPSHEET</strong></td>
<td>The <strong>CPSFUNC_DELETE_HCOMPROPSHEET</strong> function code causes the <strong>ComPropSheet</strong> function to delete a set of property sheet pages that are specified by a CPSUI handle.</td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_DELETE_HCOMPROPSHEET</strong> when it calls <strong>ComPropSheet</strong> to delete a set of property sheet pages.</li>
<li><em>lParam1</em>: CPSUI handle that refers to the set of pages to be deleted. This handle must previously have been obtained by a call to <strong>ComPropSheet</strong> with one of the following function codes:<dl> <strong>CPSFUNC_ADD_HPROPSHEETPAGE</strong><br />
<strong>CPSFUNC_ADD_PCOMPROPSHEETUI</strong><br />
<strong>CPSFUNC_ADD_PFNPROPSHEETUI</strong><br />
<strong>CPSFUNC_ADD_PROPSHEETPAGE</strong><br />
<strong>CPSFUNC_INSERT_PSUIPAGE</strong><br />
</dl></li>
<li><em>lParam2</em>: Not used, must be zero.</li>
</ul>
<strong>Return Value</strong>The <strong>ComPropSheet</strong> function returns the number of property sheet pages that were deleted.<br/></td>
</tr>
<tr class="even">
<td><strong>CPSFUNC_DO_APPLY_CPSUI</strong></td>
<td>The <strong>CPSFUNC_DO_APPLY_CPSUI</strong> function code causes the <strong>ComPropSheet</strong> function to simulate the delivery of a PSN_APPLY notification message.<br/> CPSUI responds to the <strong>CPSFUNC_DO_APPLY_CPSUI</strong> function code by delivering the <strong>CPSUICB_REASON_APPLYNOW</strong> reason to an application's _CPSUICALLBACK-typed callback function.<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_DO_APPLY_CPSUI</strong> when it calls <strong>ComPropSheet</strong> to simulate the delivery of a PSN_APPLY notification message.</li>
<li><em>lParam1</em>: CPSUI handle that points to a set of one or more property sheet pages. Typically, this handle has been previously specified as the lParam1 parameter to <strong>ComPropSheet</strong> using the <strong>CPSFUNC_IGNORE_CPSUI_PSN_APPLY</strong> function code.</li>
<li><em>lParam2</em>: This parameter is any combination of the following bit flags:<dl> APPLYCPSUI_NO_NEWDEF - Set this flag if you do not want the current default values (used for the Undo operation) to be changed. Clear this flag if you want the current values for all options to become the defaults used for the Undo operation.<br />
APPLYCPSUI_OK_CANCEL_BUTTON - Set this flag if the user selected the OK or Cancel button (or if you want to simulate this activity). Clear this flag if the user selected the Close or Apply Now button (or if you want to simulate this activity). If your code is set up to receive PSN_APPLY messages, the code should check the lParam member of the PSHNOTIFY structure. If the member is zero, this bit should be cleared. (The PSN_APPLY message and PSHNOTIFY structure are described in the Microsoft Windows SDK documentation.)<br />
<br />
</dl></li>
</ul>
<strong>Return Value</strong>If the operation succeeds, the <strong>ComPropSheet</strong> function returns a nonzero value; otherwise it returns zero and the specified pages will become active. If you use the <strong>CPSFUNC_IGNORE_CPSUI_PSN_APPLY</strong> function code to disable CPSUI's handling of the PSN_APPLY notification message, you must use the <strong>CPSFUNC_DO_APPLY_CPSUI</strong> function code to simulate delivery of the PSN_APPLY message. Otherwise, user changes to a property sheet page cannot be obtained. <br/></td>
</tr>
<tr class="odd">
<td><strong>CPSFUNC_GET_HPSUIPAGES</strong></td>
<td>The <strong>CPSFUNC_GET_HPSUIPAGES</strong> function code causes the <strong>ComPropSheet</strong> function to return an array of CPSUI handles that point to property sheet pages. These handles identify the child pages associated with the specified group parent handle.<br/> To use this function code, follow these steps:
<ol>
<li>Call <strong>ComPropSheet</strong>, specifying the <strong>CPSFUNC_GET_PAGECOUNT</strong> function code, to obtain the number of child pages associated with the specified group parent.</li>
<li>Allocate enough local memory to contain a HANDLE structure for each page.</li>
<li>Call <strong>ComPropSheet</strong> again, specifying the <strong>CPSFUNC_GET_HPSUIPAGES</strong> function code and the address of the locally allocated memory, to obtain an array of HANDLE structures.</li>
</ol>
<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_GET_HPSUIPAGES</strong> when it calls <strong>ComPropSheet</strong> to retireve an array of CPSUI handles.</li>
<li><em>lParam1</em>: Pointer to an array of HANDLE structures.</li>
<li><em>lParam2</em>: Size of the HANDLE array pointed to by lParam1.</li>
</ul>
<strong>Return Value</strong>The <strong>ComPropSheet</strong> function returns the number of handles that CPSUI places into the HANDLE array.<br/></td>
</tr>
<tr class="even">
<td><strong>CPSFUNC_GET_PAGECOUNT</strong></td>
<td>The <strong>CPSFUNC_GET_PAGECOUNT</strong> function code causes the <strong>ComPropSheet</strong> function to return the number of property sheet pages that are child pages of the specified group parent handle.</td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_GET_PAGECOUNT</strong> when it calls <strong>ComPropSheet</strong> to return the child page count.</li>
<li><em>lParam1</em>: Not used, must be zero.</li>
<li><em>lParam2</em>: Not used, must be zero.</li>
</ul>
<strong>Return Value</strong>The <strong>ComPropSheet</strong> function returns the number of pages counted.<br/></td>
</tr>
<tr class="odd">
<td><strong>CPSFUNC_GET_PFNPROPSHEETUI_ICON</strong></td>
<td>The <strong>CPSFUNC_GET_PFNPROPSHEETUI_ICON</strong> function code causes the <strong>ComPropSheet</strong> function to return a handle to the icon that is associated with a set of property sheet pages. The set of pages must have been previously created by a PFNPROPSHEETUI-typed function.<br/> The <strong>ComPropSheet</strong> function calls the PFNPROPSHEETUI-typed function associated with the specified page handle, and passes a reason value of <strong>PROPSHEETUI_REASON_GET_ICON</strong>. The PFNPROPSHEETUI-typed function then calls <strong>LoadImage</strong> (described in the Windows SDK documentation) and provides the icon size specified bylParam2 to load an icon resource.<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_GET_PFNPROPSHEETUI_ICON</strong> when it calls <strong>ComPropSheet</strong> to retrieve a handle to the icon that is associated with a set of property sheet pages.</li>
<li><em>lParam1</em>: CPSUI handle that refers to a set of property sheet pages. This handle must previously have been obtained by a call to <strong>ComPropSheet</strong> with the <strong>CPSFUNC_ADD_PFNPROPSHEETUI</strong> function code.</li>
<li><em>lParam2</em>: Specifies two WORD-sized values representing the icon's size, in pixels. The LOWORD value is the width, and the HIWORD value is the height. If these values are zero, the system metrics SM_CXICON and SM_CYICON are used. (See <strong>GetSystemMetrics</strong> in the Microsoft Windows SDK documentation.)</li>
</ul>
<strong>Return Value</strong>If the operation succeeds, the <strong>ComPropSheet</strong> function returns an icon handle; otherwise it returns NULL.<br/></td>
</tr>
<tr class="even">
<td><strong>CPSFUNC_IGNORE_CPSUI_PSN_APPLY</strong></td>
<td>The <strong>CPSFUNC_IGNORE_CPSUI_PSN_APPLY</strong> function code causes the <strong>ComPropSheet</strong> function to disable or reenable CPSUI's handling of the PSN_APPLY notification message (described in the Microsoft Windows SDK documentation).<br/> The system sends the PSN_APPLY notification message to CPSUI when a user selects a property sheet's OK or Cancel button. CPSUI responds to this message by delivering the <strong>CPSUICB_REASON_APPLYNOW</strong> reason to an application's _CPSUICALLBACK-typed callback function. If you disable CPSUI's handling of the PSN_APPLY notification message, you must use the <strong>CPSFUNC_DO_APPLY_CPSUI</strong> function code to simulate delivery of the PSN_APPLY message. Otherwise, user changes to a property sheet page cannot be obtained. If the <strong>CPSFUNC_IGNORE_CPSUI_PSN_APPLY</strong> function code is not used, CPSUI's handling of the PSN_APPLY notification message is enabled by default. <br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_IGNORE_CPSUI_PSN_APPLY</strong> when it calls <strong>ComPropSheet</strong> to disable or reenable CPSUI's handling of the PSN_APPLY notification message.</li>
<li><em>lParam1</em>: CPSUI handle that refers to a set of one or more property sheet pages. This handle must have been previously obtained by a call to <strong>ComPropSheet</strong> with a function code of <strong>CPSFUNC_ADD_PCOMPROPSHEETUI</strong>, or with a function code of <strong>CPSFUNC_INSERT_PSUIPAGE</strong> and an insertion type of <strong>PSUIPAGEINSERT_PROPSHEETPAGE</strong>.</li>
<li><em>lParam2</em>: Any nonzero value disables CPSUI's delivery of the <strong>CPSUICB_REASON_APPLYNOW</strong> reason. A zero value reenables delivery of the <strong>CPSUICB_REASON_APPLYNOW</strong> reason.</li>
</ul>
<strong>Return Value</strong>If the operation succeeds, the <strong>ComPropSheet</strong> function returns a nonzero value; otherwise it returns zero.<br/></td>
</tr>
<tr class="odd">
<td><strong>CPSFUNC_INSERT_PSUIPAGE</strong></td>
<td>The <strong>CPSFUNC_INSERT_PSUIPAGE</strong> function code causes the <strong>ComPropSheet</strong> function to insert a set of property sheet pages at a specific position.</td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_INSERT_PSUIPAGE</strong> when it calls <strong>ComPropSheet</strong> to insert a set of property sheet pages at a specific position.</li>
<li><em>lParam1</em>: Specifies a handle to a set of one or more property sheet pages. The new pages will be inserted before or after these pages, depending on the Mode member of the <strong>INSERTPSUIPAGE_INFO</strong> structure pointed to by lParam2. This handle must previously have been obtained by a call to <strong>ComPropSheet</strong> with one of the following function codes:<dl> <strong>CPSFUNC_ADD_HPROPSHEETPAGE</strong><br />
<strong>CPSFUNC_ADD_PCOMPROPSHEETUI</strong><br />
<strong>CPSFUNC_ADD_PFNPROPSHEETUI</strong><br />
<strong>CPSFUNC_ADD_PROPSHEETPAGE</strong><br />
<strong>CPSFUNC_INSERT_PSUIPAGE</strong><br />
</dl></li>
<li><em>lParam2</em>: Pointer to an <strong>INSERTPSUIPAGE_INFO</strong> structure, describing where and how the new pages should be inserted.</li>
</ul>
<strong>Return Value</strong>If the operation succeeds, the <strong>ComPropSheet</strong> function returns a handle to the set of pages that were inserted; otherwise, the function returns NULL.<br/></td>
</tr>
<tr class="even">
<td><strong>CPSFUNC_LOAD_CPSUI_ICON</strong></td>
<td>The <strong>CPSFUNC_LOAD_CPSUI_ICON</strong> function code causes the <strong>ComPropSheet</strong> function to load a CPSUI-supplied icon resource.<br/> CPSUI calls <strong>LoadImage</strong> (described in the Windows SDK documentation) to load the specified icon resource.<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_LOAD_CPSUI_ICON</strong> when it calls <strong>ComPropSheet</strong> to load a CPSUI-supplied icon resource.</li>
<li><em>lParam1</em>: Resource identifier of the CPSUI-supplied icon to be loaded. This must be an IDI_CPSUI-prefixed identifier as defined in Compstui.h.</li>
<li><em>lParam2</em>: Specifies two WORD-sized values representing the icon's size, in pixels. The LOWORD value is the width, and the HIWORD value is the height. If these values are zero, the system metrics SM_CXICON and SM_CYICON are used. (See <strong>GetSystemMetrics</strong> in the Microsoft Windows SDK documentation.)</li>
</ul>
<strong>Return Value</strong>If the operation succeeds, the <strong>ComPropSheet</strong> function returns an icon handle; otherwise it returns NULL.<br/></td>
</tr>
<tr class="odd">
<td><strong>CPSFUNC_LOAD_CPSUI_STRING</strong></td>
<td>The <strong>CPSFUNC_LOAD_CPSUI_STRING</strong> function code causes the <strong>ComPropSheet</strong> function to load a CPSUI-supplied string resource.<br/> The <strong>ComPropSheet</strong> function calls <strong>LoadString</strong> (described in the Microsoft Windows SDK documentation) to load the specified string.<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_LOAD_CPSUI_STRING</strong> when it calls ComPropSheet to load a CPSUI-supplied string resource.</li>
<li><em>lParam1</em>: An LPSTR-typed pointer to a caller-allocated buffer, into which the CPSUI-supplied string specified by HIWORD(<em>lParam2</em>) will be placed.</li>
<li><em>lParam2</em>: Contains the following two caller-supplied values:<dl> LOWORD(<em>lParam2</em>). Size, in bytes, of the buffer pointed to by lParam1.<br />
HIWORD(<em>lParam2</em>). Resource identifier of the CPSUI-supplied string to be loaded. This must be an IDS_CPSUI-prefixed identifier as defined in Compstui.h.<br />
</dl></li>
</ul>
<strong>Return Value</strong>If the operation succeeds, the <strong>ComPropSheet</strong> function returns the length of the string. If an invalid resource identifier is specified, the function returns zero. If <em>lParam1</em> is NULL or LOWORD(<em>lParam2</em>) is zero, the function returns -1.<br/></td>
</tr>
<tr class="even">
<td><strong>CPSFUNC_QUERY_DATABLOCK</strong></td>
<td>The <strong>CPSFUNC_QUERY_DATABLOCK</strong> function code causes the <strong>ComPropSheet</strong> function to retrieve a caller-supplied data block that was previously stored using the <strong>CPSFUNC_SET_DATABLOCK</strong> function code.<br/> Typically, this function code is used by a _CPSUICALLBACK-typed callback function (when the function's <strong>CPSUICBPARAM</strong> structure contains a Reason value of <strong>CPSUICB_REASON_SETACTIVE</strong>) to retrieve values associated with another page before the current page becomes inactive.<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_QUERY_DATABLOCK</strong> when it calls ComPropSheet to retrieve a caller-supplied data block.</li>
<li><em>lParam1</em>: Pointer to a <strong>CPSUIDATABLOCK</strong> structure that identifies the size and location of a buffer to receive the requested data block.</li>
<li><em>lParam2</em>: DWORD-sized identifier value, used to identify the requested <strong>CPSUIDATABLOCK</strong> structure. This value must have been specified in a previous call to <strong>ComPropSheet</strong> using the <strong>CPSFUNC_SET_DATABLOCK</strong> function code.</li>
</ul>
<strong>Return Value</strong>If the operation succeeds, the <strong>ComPropSheet</strong> function returns a value that represents the size of the retrieved data block. If <em>lParam1</em> is NULL, or if the value of any member of the supplied <strong>CPSUIDATABLOCK</strong> structure is zero, <strong>ComPropSheet</strong> returns the size required to store the data block. If an error occurs, the function returns a value less than or equal to zero.<br/></td>
</tr>
<tr class="odd">
<td><strong>CPSFUNC_SET_DATABLOCK</strong></td>
<td>The <strong>CPSFUNC_SET_DATABLOCK</strong> function code causes the <strong>ComPropSheet</strong> function to store a caller-supplied data block. You can use this function code to make the information about a property sheet page available to other pages.<br/> Typically, this function code is used by a _CPSUICALLBACK-typed callback function (when the function's <strong>CPSUICBPARAM</strong> structure contains a Reason value of <strong>CPSUICB_REASON_KILLACTIVE</strong>) to save values associated with a page before it becomes inactive.<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_SET_DATABLOCK</strong> when it calls <strong>ComPropSheet</strong> to store a caller-supplied data block.</li>
<li><em>lParam1</em>: Pointer to a <strong>CPSUIDATABLOCK</strong> structure that describes the data block to be stored.</li>
<li><em>lParam2</em>: Caller-defined DWORD-sized identifier value. It is used to identify the supplied <strong>CPSUIDATABLOCK</strong> structure in subsequent calls to <strong>ComPropSheet</strong> using the <strong>CPSFUNC_QUERY_DATABLOCK</strong> function code.</li>
</ul>
<strong>Return Value</strong>If the operation is successful, the <strong>ComPropSheet</strong> function returns a value representing the number of bytes that were stored; otherwise it returns a value less than or equal to zero.<br/></td>
</tr>
<tr class="even">
<td><strong>CPSFUNC_SET_DMPUB_HIDEBITS</strong></td>
<td>The <strong>CPSFUNC_SET_DMPUB_HIDEBITS</strong> function code causes the <strong>ComPropSheet</strong> function to &quot;hide&quot; a specified set of document property options, so that they are not displayed.<br/> You can use the <strong>CPSFUNC_SET_DMPUB_HIDEBITS</strong> function code if you want to define OPTITEM structures for one or more document property sheet options, but you do not want the options to be user-modifiable. The property sheet page must be defined using the <strong>COMPROPSHEETUI</strong> structure, and the structure's pDlgPage member must be <strong>CPSUI_PDLGPAGE_DOCPROP</strong> or <strong>CPSUI_PDLGPAGE_ADVDOCPROP</strong>. If you use the <strong>CPSFUNC_SET_DMPUB_HIDEBITS</strong> function code, it must be specified to <strong>ComPropSheet</strong> before the <strong>CPSFUNC_ADD_PCOMPROPSHEETUI</strong> or <strong>CPSFUNC_INSERT_PSUIPAGE</strong> function code is used to create the page. <br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_SET_DMPUB_HIDEBITS</strong> when it calls <strong>ComPropSheet</strong> to &quot;hide&quot; a specified set of document property options.</li>
<li><em>lParam1</em>: Pointer to a bit array that indicates the options to be hidden. This array must be created using the <strong>MAKE_DMPUB_HIDEBIT</strong>(DMPub) macro, where DMPub is the OR-combination of one or more DMPUB_-prefixed constants. The DMPUB_-prefixed constants are listed in the description of the <strong>OPTITEM</strong> structure. The macro and constants are defined in Compstui.h.</li>
<li><em>lParam2</em>: Not used, must be zero.</li>
</ul>
<strong>Return Value</strong>If the operation is successful, the <strong>ComPropSheet</strong> function returns the value specified for <em>lParam1</em>; otherwise it returns zero.<br/></td>
</tr>
<tr class="odd">
<td><strong>CPSFUNC_SET_FUSION_CONTEXT</strong></td>
<td>The <strong>CPSFUNC_SET_FUSION_CONTEXT</strong> sets a Fusion activation context for the specified page.<br/> When a page is about to be created or inserted and it does not specify an activation context in its <strong>PROPSHEETPAGE</strong> structure (described in the Windows SDK documentation), it will be created in the parent's page activation context. If the parent's activation context is not set, then Compstui.dll looks up the parent's parent, continuing until the top level parent is reached or until it finds a parent with an activation context properly set. If none of the parents has an activation context set, then Compstui.dll will not specify an activation context in the <strong>PROPSHEETPAGE</strong> structure. This means that the page will be created in the activation context of the caller of the <strong>PropertySheet</strong> API (described in the Windows SDK documentation).<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_SET_FUSION_CONTEXT</strong> when it calls <strong>ComPropSheet</strong> to set a Fusion activation context for the specified page.</li>
<li><em>lParam1</em>: Specifies the handle to the Fusion context. Compstui.dll duplicates the handle, attaching it to its internal structures, so that the caller is not obligated to retain the handle. Compstui.dll releases the passed-in context handle when the Compstui.dll handle is deleted.</li>
<li><em>lParam2</em>: Not used, must be zero.</li>
</ul>
<strong>Return Value</strong>If the operation is successful, the <strong>ComPropSheet</strong> function returns a value greater than zero. Otherwise, <strong>ComPropSheet</strong> returns a value that is less than or equal to zero. For information about the error, use <strong>GetLastError</strong>, which is described in the Microsoft Windows SDK documentation.<br/></td>
</tr>
<tr class="even">
<td><strong>CPSFUNC_SET_HSTARTPAGE</strong></td>
<td>The <strong>CPSFUNC_SET_HSTARTPAGE</strong> function code causes the <strong>ComPropSheet</strong> function to mark a specified property sheet page to be the top page of the associated property sheet. If the property sheet is currently being displayed, the specified page becomes the active page.</td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_SET_HSTARTPAGE</strong> when it calls <strong>ComPropSheet</strong> to mark a specified property sheet page to be the top page of the associated property sheet.</li>
<li><em>lParam1</em>: Caller-supplied CPSUI page handle, previously obtained by a call to <strong>ComPropSheet</strong> with one of the following function codes: <dl> <strong>CPSFUNC_ADD_HPROPSHEETPAGE</strong><br />
<strong>CPSFUNC_ADD_PCOMPROPSHEETUI</strong><br />
<strong>CPSFUNC_ADD_PFNPROPSHEETUI</strong><br />
<strong>CPSFUNC_ADD_PROPSHEETPAGE</strong><br />
<strong>CPSFUNC_INSERT_PSUIPAGE</strong><br />
</dl>If the handle represents a single page belonging to the group specified by <em>hComPropSheet</em>, CPSUI makes this page the top page. If the handle represents a group parent handle (see <strong>CPSFUNC_INSERT_PSUIPAGE</strong>), then <em>lParam2</em> represents a zero-based index into the group's pages and the page represented by the index becomes the top page.</li>
<li><em>lParam2</em>: If lParam1 represents a group parent handle, this caller-supplied value is a zero-based index into the group's pages. If <em>lParam1</em> represents a single page belonging to the group specified by <em>hComPropSheet</em>, this parameter is not used. If the handle specified by <em>lParam1</em> was obtained using the <strong>CPSFUNC_ADD_PCOMPROPSHEETUI</strong> function code, and if the <strong>pDlgPage</strong> member of the associated <strong>COMPROPSHEETUI</strong> structure was set to <strong>CPSUI_PDLGPAGE_DOCPROP</strong>, then one of the following values can be specified for <em>lParam2.</em>
<ul>
<li>SSP_STDPAGE1 - Make the Layout page the top page.</li>
<li>SSP_STDPAGE2 - Make the Paper/Quality page the top page.</li>
<li>SSP_TVPAGE - Make the Advanced page the top page.</li>
</ul></li>
</ul>
<strong>Return Value</strong>If the operation is successful, the <strong>ComPropSheet</strong> function returns the value specified for <em>lParam1</em>; otherwise it returns zero.<br/></td>
</tr>
<tr class="odd">
<td><strong>CPSFUNC_SET_PSUIPAGE_ICON</strong></td>
<td>The <strong>CPSFUNC_SET_PSUIPAGE_ICON</strong> function code causes the <strong>ComPropSheet</strong> function to add, replace, or remove the icon assigned to the tab of a property sheet page.<br/> If lParam2 contains an icon handle, and if the page specified by lParam1 is currently being displayed, CPSUI adds the icon to the specified page's tab. If an icon is already assigned to the page, the old icon is replaced with the new one. If lParam2 is zero, the current icon (if one exists) is removed. For all icons specified with the <strong>CPSFUNC_SET_PSUIPAGE_ICON</strong> function code, CPSUI sets the image size to 16 by 16 pixels. Icon handles should be obtained by calling <strong>LoadImage</strong>, which is described in the Microsoft Windows SDK documentation. <br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_SET_PSUIPAGE_ICON</strong> when it calls <strong>ComPropSheet</strong> to add, replace, or remove the icon assigned to the tab of a property sheet page.</li>
<li><em>lParam1</em>: Caller-supplied CPSUI page handle, previously obtained by a call to <strong>ComPropSheet</strong> with one of the following function codes:<dl> <strong>CPSFUNC_ADD_HPROPSHEETPAGE</strong><br />
<strong>CPSFUNC_ADD_PROPSHEETPAGE</strong><br />
<strong>CPSFUNC_INSERT_PSUIPAGE</strong> (with the Type member of the <strong>INSERTPSUIPAGE_INFO</strong> structure set to <strong>PSUIPAGEINSERT_HPROPSHEETPAGE</strong> or <strong>PSUIPAGEINSERT_PROPSHEETPAGE</strong>).<br />
</dl></li>
<li><em>lParam2</em>: Caller-supplied icon handle. You can set this parameter to zero to remove the current icon.</li>
</ul>
<strong>Return Value</strong>If the operation is successful, the <strong>ComPropSheet</strong> function returns 1. If an error is encountered, or if the specified page is not currently being displayed, the function returns zero.<br/></td>
</tr>
<tr class="even">
<td><strong>CPSFUNC_SET_PSUIPAGE_TITLE</strong></td>
<td>The <strong>CPSFUNC_SET_PSUIPAGE_TITLE</strong> function code causes the <strong>ComPropSheet</strong> function to set the tab title for a property sheet page.</td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_SET_PSUIPAGE_TITLE</strong> when it calls <strong>ComPropSheet</strong> to set the tab title for a property sheet page.</li>
<li><em>lParam1</em>: Caller-supplied CPSUI page handle, previously obtained by a call to <strong>ComPropSheet</strong> with one of the following function codes:<dl> <strong>CPSFUNC_ADD_HPROPSHEETPAGE</strong><br />
<strong>CPSFUNC_ADD_PROPSHEETPAGE</strong><br />
<strong>CPSFUNC_INSERT_PSUIPAGE</strong> (with the Type member of the <strong>INSERTPSUIPAGE_INFO</strong> structure set to <strong>PSUIPAGEINSERT_HPROPSHEETPAGE</strong> or <strong>PSUIPAGEINSERT_PROPSHEETPAGE</strong>).<br />
</dl></li>
<li><em>lParam2</em>: Caller-supplied pointer to a NULL-terminated string that specifies the new title.</li>
</ul>
<strong>Return Value</strong>If the operation is successful, the <strong>ComPropSheet</strong> function returns 1. If an error is encountered, or if the specified page is not currently being displayed, the function returns zero.<br/></td>
</tr>
<tr class="odd">
<td><strong>CPSFUNC_SET_RESULT</strong></td>
<td>The <strong>CPSFUNC_SET_RESULT</strong> function code causes the <strong>ComPropSheet</strong> function to pass a specified result value to all PFNPROPSHEETUI-typed functions associated with a specified page and its parents.<br/> For more information about how to set result values, see the description of the <strong>SETRESULT_INFO</strong> structure. The following caution applies to Unidrv- or Pscript5-based IHV UI plug-in with custom UI property sheets, and for which user settings made in the property sheets should be persistent. When the plug-in calls the <strong>ComPropSheet</strong> function with the Function parameter set to <strong>CPSFUNC_SET_RESULT</strong>, the plug-in must set the lParam2 parameter to <strong>CPSUI_OK</strong>.<br/></td>
<td><strong>Parameters</strong>
<ul>
<li><em>hComPropSheet</em>: Group parent handle.</li>
<li><em>Function</em>: Caller sets this function code parameter to <strong>CPSFUNC_SET_RESULT</strong> when it calls <strong>ComPropSheet</strong> to pass a specified result value to all PFNPROPSHEETUI-typed functions associated with a specified page and its parents.</li>
<li><em>lParam1</em>: Caller-supplied CPSUI handle to the page for which a result value is being passed. If lParam1 is NULL, the CPSUI uses the value specified by <em>hComPropSheet</em>.</li>
<li><em>lParam2</em>: Caller-supplied 32-bit DWORD result value.</li>
</ul>
<strong>Return Value</strong>If the operation is successful, the <strong>ComPropSheet</strong> function returns the number of PFNPROPSHEETUI-typed functions that were called. If the handle specified for <em>lParam1</em> is invalid, the function returns -1.<br/></td>
</tr>
</tbody>
</table>



 

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PFNCOMPROPSHEET%20routine%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




