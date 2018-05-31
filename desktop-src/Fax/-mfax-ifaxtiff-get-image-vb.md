---
Description: Sets or retrieves the Image property for a FaxTiff object.
ms.assetid: 9e41ae1f-070d-4365-9d6a-a37f1979dae7
title: FaxTiff.Image property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxTiff.Image property

Sets or retrieves the **Image** property for a [FaxTiff](-mfax-faxtiff.md) object. The **Image** property is a null-terminated string that contains the full path and file name of the file represented by the FaxTiff object. The file is a Tagged Image File Format Class F (TIFF Class F) file.

This property is read/write.

## Syntax


```VB
Property Image As String
```



## Property value

A **String** that specifies or receives the fully qualified path and name of the fax image file.

## Remarks

A fax client application must set the **Image** property before retrieving another property for a [FaxTiff](-mfax-faxtiff.md) object.

A fax client application can call the **get\_Image** retrieval method to determine the name of the facsimile image file that is open as a result of a successful call to the **put\_Image** method.

A fax client application can use this retrieval method to determine the name of the facsimile image file that is open as a result of successful assignment of the **Image** property.

The **get\_Image** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxTiff**](-mfax-faxtiff-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxTiff**](-mfax-ifaxtiff.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




