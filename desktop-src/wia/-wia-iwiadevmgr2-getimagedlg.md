---
description: The IWiaDevMgr2::GetImageDlg method displays one or more dialog boxes that enable a user to acquire an image from a Windows Image Acquisition (WIA) 2.0 device and write the image to a specified file.
ms.assetid: 30a63426-150e-44cf-a03e-7b6da14450f7
title: IWiaDevMgr2::GetImageDlg method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaDevMgr2.GetImageDlg
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaDevMgr2::GetImageDlg method

The **IWiaDevMgr2::GetImageDlg** method displays one or more dialog boxes that enable a user to acquire an image from a Windows Image Acquisition (WIA) 2.0 device and write the image to a specified file. This method extends the functionality of [**IWiaDevMgr2::SelectDeviceDlg**](-wia-iwiadevmgr2-selectdevicedlg.md) to encapsulate image acquisition within a single API call.

## Syntax


```C++
HRESULT GetImageDlg(
  [in]      LONG      lFlags,
  [in]      BSTR      bstrDeviceID,
  [in]      HWND      hwndParent,
  [in]      BSTR      bstrFolderName,
  [in]      BSTR      bstrFilename,
  [in]      LONG      *plNumFiles,
  [in]      BSTR      **ppbstrFilePaths,
  [in, out] IWiaItem2 **ppItem
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Specifies dialog box behavior. Can be set to the following values:



| Flag                                 | Meaning                                                                                                                                                                     |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                                    | Default behavior.                                                                                                                                                           |
| WIA\_DEVICE\_DIALOG\_USE\_COMMON\_UI | Use the system UI instead of the vendor-supplied UI. If the system UI is not available, the vendor UI is used. If neither UI is available, the function returns E\_NOTIMPL. |



 

</dd> <dt>

*bstrDeviceID* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the scanner to use.

</dd> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **HWND**

A handle of the window that owns the **Get Image** dialog box.

</dd> <dt>

*bstrFolderName* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the name of the folder ito store the scanned files in.

</dd> <dt>

*bstrFilename* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the name of the file to write the image data to.

</dd> <dt>

*plNumFiles* \[in\]
</dt> <dd>

Type: **LONG\***

A pointer to the number of files to scan.

</dd> <dt>

*ppbstrFilePaths* \[in\]
</dt> <dd>

Type: **BSTR\*\***

The address of a pointer to an array of paths for the scanned files. Initialize the pointer to point to an array of size zero (0) before **IWiaDevMgr2::GetImageDlg** is called. See **Remarks**.

</dd> <dt>

*ppItem* \[in, out\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\*\***

The address of a pointer to the [**IWiaItem2**](-wia-iwiaitem2.md) that the images were scanned from.

</dd> </dl>

## Return value

Type: **HRESULT**

**IWiaDevMgr2::GetImageDlg** returns S\_OK if the data is transferred successfully, returns S\_FALSE if the user cancels the dialog box, or returns a standard COM error.

> [!Note]  
> The *ppbstrFilePaths* parameter is not necessarily empty, if the function returns S\_FALSE. If the user cancels, the pages that have completed scanning are processed and returned in *ppbstrFilePaths*. Even if they are not used, you must free the array. See **Remarks**.

 

## Remarks

If the application passes **NULL** for the value of the *bstrDeviceID* parameter, **IWiaDevMgr2::GetImageDlg** displays the **Select Device** dialog box so that the user can select the WIA 2.0 input device.

Use a menu item named **From scanner** on the **File** menu so that device and image selections are available in your application.

Call [SysFreeString](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-sysfreestring) on each BSTR in the array that *ppbstrFilePaths*\[i\] points to, and call [CoTaskMemFree](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) on the array itself to free associated memory. If S\_FALSE is returned, check to see if the value that *plNumFiles* points to is not zero. If the value is not zero, free the *ppbstrFilePaths*\[i\] resources in the application, because the user might cancel after scanning one or more pages. Initialize *plNumFiles* to zero before you call **IWiaDevMgr2::GetImageDlg**. If *plNumFiles* is not initialized to zero and a failure in the COM infrastructure causes the function to return S\_FALSE before **IWiaDevMgr2::GetImageDlg** is called, then *plNumFiles* will have a misleading garbage value.

The dialog box must have sufficient rights to *bstrFolderName* so that it can save the files with unique file names. Protect the folder with an access control list (ACL) because it contains user data.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl> |



 

 
