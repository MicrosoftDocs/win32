---
Description: 'Sets or retrieves the Tsid property of a FaxDoc object. The Tsid property is a null-terminated string that contains a user-defined transmitting station identifier (TSID).'
ms.assetid: 'aa6854d7-4097-4890-97fb-1f4ca5956548'
title: 'FaxDoc.Tsid property'
---

# FaxDoc.Tsid property

Sets or retrieves the **Tsid** property of a [FaxDoc](-mfax-faxdoc.md) object. The **Tsid** property is a null-terminated string that contains a user-defined transmitting station identifier (TSID).

This property is read/write.

## Syntax


```VB
Property Tsid As String
```



## Property value

A **String** that specifies or receives a user-defined TSID associated with the fax transmission.

## Remarks

If the fax server allows user-defined TSID strings, the service will transmit the value of the *pVal* parameter to the receiving fax device instead of the TSID associated with the sending device. You can call the [**UseDeviceTsid**](-mfax-ifaxserver-get-usedevicetsid-vb.md) method to determine whether the fax server is configured to permit user-specified TSIDs.

If the fax server allows user-defined TSID strings, the service will transmit the value of *pVal* to the receiving fax device instead of the TSID associated with the sending device. You can use the [**UseDeviceTsid**](-mfax-ifaxserver-get-usedevicetsid-vb.md) property to determine whether the fax server is configured to permit user-specified TSIDs.

The TSID is typically the fax number of the device sending the transmission. Note that the T.30 specification of the International Telecommunication Union (ITU) restricts the value of a TSID to 20 ASCII characters. If a fax client application specifies a TSID that contains non-ASCII characters, the fax service removes them. If the TSID exceeds 20 characters, the service truncates the extra characters.

The **get\_Tsid** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxDoc**](-mfax-ifaxdoc.md)
</dt> <dt>

[**UseDeviceTsid**](-mfax-ifaxserver-get-usedevicetsid-vb.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




