---
Description: The IScanProfileUI interface enables applications to display a dialog box so that users can create, modify, and delete scan profiles.
ms.assetid: d0c7edcc-00d8-49b2-a0f7-fe4bbba90bfb
title: IScanProfileUI interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IScanProfileUI interface

The **IScanProfileUI** interface enables applications to display a dialog box so that users can create, modify, and delete scan profiles.

## Members

The **IScanProfileUI** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IScanProfileUI** also has these types of members:

-   [Methods](#methods)

### Methods

The **IScanProfileUI** interface has these methods.



| Method                                                             | Description                                                                                      |
|:-------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**ScanProfileDialog**](-wia-iscanprofileui-scanprofiledialog.md) | Displays a dialog box that enables users to create, modify, and delete scan profiles.<br/> |



 

## Remarks

The dialog box is modal; the user cannot switch to the parent window until the dialog box closes.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Scanprofileui.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Scanprofiles.idl</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[Scan Profile Schema](-wia-scan-profile-schema.md)
</dt> </dl>

 

 




