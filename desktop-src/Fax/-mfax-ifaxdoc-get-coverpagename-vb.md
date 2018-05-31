---
Description: Sets or retrieves the CoverpageName property for a FaxDoc object. The CoverpageName property is a null-terminated string that contains the name of the cover page template file (.cov) associated with the object.
ms.assetid: 6d2fbcb1-fb94-4fe1-8481-f64f55878906
title: FaxDoc.CoverpageName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDoc.CoverpageName property

Sets or retrieves the **CoverpageName** property for a [FaxDoc](-mfax-faxdoc.md) object. The **CoverpageName** property is a null-terminated string that contains the name of the cover page template file (.cov) associated with the object.

This property is read/write.

## Syntax


```VB
Property CoverpageName As String
```



## Property value

A **String** that specifies or receives the name of the cover page file to associate with the fax document.

## Remarks

To send a cover page with a fax document, the following are required:

-   The **SendCoverpage** property must be equal to **True**.
-   The **CoverpageName** property must specify a valid cover page file.

In addition, the [**ServerCoverpage**](-mfax-ifaxdoc-get-servercoverpage-vb.md) property must be equal to **True** if the cover page file is a common cover page file.

You can call the [**ServerCoverpage**](-mfax-ifaxserver-get-servercoverpage-vb.md) method to determine whether the fax server is configured to permit personal cover pages.

The **CoverpageName** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

For more information, see [Cover Pages](-mfax-cover-pages.md) and [Sending a Cover Page](-mfax-sending-a-cover-page.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxDoc**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxdoc)
</dt> <dt>

[**FileName**](-mfax-ifaxdoc-get-filename-vb.md)
</dt> <dt>

[**ServerCoverpage**](-mfax-ifaxdoc-get-servercoverpage-vb.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




