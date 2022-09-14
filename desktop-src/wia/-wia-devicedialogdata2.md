---
description: DEVICEDIALOGDATA2 structure - Defines the data needed to call a device dialog.
ms.assetid: 544238de-310f-4fc3-b519-bb4e6b309272
title: DEVICEDIALOGDATA2 structure (Wiadefd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DEVICEDIALOGDATA2
api_type: 
- HeaderDef
api_location: 
- Wiadefd.h
---

# DEVICEDIALOGDATA2 structure

Defines the data needed to call a device dialog.

## Syntax


```C++
typedef struct {
  DWORD     cbSize;
  IWiaItem2 *pIWiaItemRoot;
  DWORD     dwFlags;
  HWND      hwndParent;
  BSTR      bstrFolderName;
  BSTR      bstrFilename;
  LONG      lNumFiles;
  BSTR      *pbstrFilePaths;
  IWiaItem2 *ppWiaItem;
} DEVICEDIALOGDATA2;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Specifies the size of this structure in bytes.

</dd> <dt>

**pIWiaItemRoot**
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\***

</dd> <dd>

Points to an [**IWiaItem2**](-wia-iwiaitem2.md) interface that represents the valid root item in the application item tree.

</dd> <dt>

**dwFlags**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Specifies a set of flags that control the dialog box's operation. Can be set to any of the following values:



| Flag                                 | Meaning                                                                                                                                                                                     |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                                    | Default behavior.                                                                                                                                                                           |
| WIA\_DEVICE\_DIALOG\_SINGLE\_IMAGE   | Restrict image selection to a single image in the device image acquisition dialog box.                                                                                                      |
| WIA\_DEVICE\_DIALOG\_USE\_COMMON\_UI | Use the system UI, if available, rather than the vendor-supplied UI. If the system UI is not available, the vendor UI is used. If neither UI is available, the function returns E\_NOTIMPL. |



 

</dd> <dt>

**hwndParent**
</dt> <dd>

Type: **HWND**

</dd> <dd>

Specifies the handle to the parent window of the dialog.

</dd> <dt>

**bstrFolderName**
</dt> <dd>

Type: **BSTR**

</dd> <dd>

Specifies the folder name where the files are transferred.

</dd> <dt>

**bstrFilename**
</dt> <dd>

Type: **BSTR**

</dd> <dd>

Specifies the filename template to be used for files transferred from WIA items to the destination folder designated by **bstrFolderName**. An arbitrary number of unique file names can be created by appending additional characters to the file name template.

</dd> <dt>

**lNumFiles**
</dt> <dd>

Type: **LONG**

</dd> <dd>

Receives the number of strings written to the **pbstrFilePaths** array.

</dd> <dt>

**pbstrFilePaths**
</dt> <dd>

Type: **BSTR\***

</dd> <dd>

Pointer to an array of BSTR pointers. Each array element points to a BSTR that contains the destination name of a file that was successfully transferred to the folder identified by bstrFolderName. The method must allocate the storage for this member.

</dd> <dt>

**ppWiaItem**
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\***

</dd> <dd>

Pointer to the [**IWiaItem2**](-wia-iwiaitem2.md) interface of the WIA item that transfers data to the file or files named in the **pbstrFilePaths** array.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadefd.h</dt> </dl> |



 

 




