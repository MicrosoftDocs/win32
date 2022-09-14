---
description: Displays a dialog box that enables users to create, modify, and delete scan profiles.
ms.assetid: 208ec527-f7ad-4d45-b433-6d7d3658ca26
title: IScanProfileUI::ScanProfileDialog method (Scanprofileui.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileUI.ScanProfileDialog
api_type: 
- COM
api_location: 
- Scanprofileui.h
---

# IScanProfileUI::ScanProfileDialog method

Displays a dialog box that enables users to create, modify, and delete scan profiles.

## Syntax


```C++
HRESULT ScanProfileDialog(
  [in] HWND hwndParent
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **HWND**

The handle of the parent window that owns the dialog box.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The dialog box is modal; the user cannot switch to the parent window until the dialog box closes.

The values of the `<ProfileName>` element and the `<WiaItem>` element can be changed in the dialog box. The `<Default>` element can be added or deleted. No other changes to the scan profile can be made in the dialog box.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Scanprofileui.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Scanprofiles.idl</dt> </dl> |



## See also

<dl> <dt>

[**IScanProfileUI**](-wia-iscanprofileui.md)
</dt> <dt>

[Scan Profile Schema](-wia-scan-profile-schema.md)
</dt> </dl>

 

 




