---
description: Displays a dialog box to the user to prepare for image acquisition.
ms.assetid: 2d7246ec-fb90-4538-b717-b9e3813c1696
title: IWiaItem2::DeviceDlg method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2.DeviceDlg
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2::DeviceDlg method

Displays a dialog box to the user to prepare for image acquisition.

## Syntax


```C++
HRESULT DeviceDlg(
  [in]      LONG      lFlags,
  [in]      HWND      hwndParent,
  [in]      BSTR      bstrFolderName,
  [in]      BSTR      bstrFilename,
  [in]      LONG      *plNumFiles,
  [in, out] BSTR      **ppbstrFilePaths,
  [in, out] IWiaItem2 **ppIWiaItem2
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Specifies a set of flags that control the dialog box's operation. The value can be either 0 to represent the default behavior or any of the WIA\_DEVICE\_DIALOG flags described in [**WiaFlag**](-wia-wiaflag.md).

</dd> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **HWND**

A handle to the parent window.

</dd> <dt>

*bstrFolderName* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the folder name where the files are to be transferred.

</dd> <dt>

*bstrFilename* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the template file name.

</dd> <dt>

*plNumFiles* \[in\]
</dt> <dd>

Type: **LONG\***

A pointer to the number of items in the *ppbstrFilePaths* array.

</dd> <dt>

*ppbstrFilePaths* \[in, out\]
</dt> <dd>

Type: **BSTR\*\***

The address of a pointer to an array of paths for the scanned files. Initialize the pointer to point to an array of size zero (0) before **IWiaItem2::DeviceDlg** is called.

</dd> <dt>

*ppIWiaItem2* \[in, out\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\*\***

The address of an array of pointers to [**IWiaItem2**](-wia-iwiaitem2.md) interfaces.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method displays a dialog box to the user that an application uses to gather all the information required for image acquisition. It is also used to specify image scan properties such as brightness and contrast.

After this method returns, the application can use the [**IWiaTransfer**](-wia-iwiatransfer.md) interface to acquire the image.

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method for each element in the array of interface pointers they receive through the *ppIWiaItem2* parameter. Applications must also free the array using [CoTaskMemFree](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
