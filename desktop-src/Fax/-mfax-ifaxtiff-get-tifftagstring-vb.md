---
Description: Retrieves the TiffTagString property for a FaxTiff object. The TiffTagString property is a null-terminated string that contains the value of a specified Tagged Image File Format (TIFF) tag (field).
ms.assetid: ec519cec-74e9-42ff-bbc3-b05cdcaff064
title: FaxTiff.TiffTagString property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxTiff.TiffTagString property

Retrieves the **TiffTagString** property for a [FaxTiff](-mfax-faxtiff.md) object. The **TiffTagString** property is a null-terminated string that contains the value of a specified Tagged Image File Format (TIFF) tag (field).

This property is read/write.

## Syntax


```VB
Property TiffTagString As String
```



## Property value

A **String** that specifies or receives the value of the TIFF tag specified by *tagID*.

## Remarks

For more information about Tagged Image File Format Class F (TIFF Class F) files, see [Fax Image Format](-mfax-fax-image-format.md). For current information about TIFF tags, or for the list of valid TIFF tag numbers, contact Adobe Systems Incorporated.

A fax client application must set the [**Image**](-mfax-ifaxtiff-get-image-vb.md) property before retrieving another property for a [FaxTiff](-mfax-faxtiff.md) object.

The **get\_TiffTagString** method sets the *pVal* parameter to a string that represents the value of the TIFF tag, if it is available. If the information is not available, the method returns "Unavailable".

The **TiffTagString** property is a string that represents the value of the TIFF tag, if it is available. If the information is not available, **TiffTagString** is an empty string.

You can call the **get\_TiffTagString** to retrieve information about any TIFF tag, including those that the fax service does not support. Note that you can retrieve this property only for the first page of a TIFF file.

The **TiffTagString** property contains information about any TIFF tag, including those that the fax service does not support. Note that this property only contains information for the first page of a TIFF file.

The **get\_TiffTagString** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxTiff**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxtiff)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




