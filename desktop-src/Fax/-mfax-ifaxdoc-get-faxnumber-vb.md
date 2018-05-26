---
Description: Sets or retrieves the FaxNumber property of a FaxDoc object. The FaxNumber property is a null-terminated string that contains the fax number to which the fax server will send the fax transmission.
ms.assetid: 5629caa5-f505-4880-950d-189334778907
title: FaxDoc.FaxNumber property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDoc.FaxNumber property

Sets or retrieves the **FaxNumber** property of a [FaxDoc](-mfax-faxdoc.md) object. The **FaxNumber** property is a null-terminated string that contains the fax number to which the fax server will send the fax transmission.

This property is read/write.

## Syntax


```VB
Property FaxNumber As String
```



## Property value

A **String** that specifies or receives the fax number of the recipient of the transmission.

## Remarks

The recipient's fax number can appear on the cover page.

The **FaxNumber** property is required to send a fax transmission using a call to the [**Send**](-mfax-ifaxdoc-send-vb.md) method. For more information, see [Transmitting Faxes](-mfax-transmitting-faxes.md).

The **FaxNumber** property is required to send a fax transmission using a call to the [**Send**](-mfax-ifaxdoc-send-vb.md) method. For more information, see [Transmitting Faxes](-mfax-transmitting-faxes.md).

The **get\_FaxNumber** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxDoc**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxdoc?branch=master)
</dt> <dt>

[**Send**](-mfax-ifaxdoc-send-vb.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




