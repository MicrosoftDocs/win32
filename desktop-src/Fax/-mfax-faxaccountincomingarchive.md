---
Description: 'Used by a fax client application to access and configure the archive of inbound fax messages received successfully by the fax service for a particular fax account.'
ms.assetid: 'd2ae93a1-6325-4b8f-a227-4eb0678702d2'
title: FaxAccountIncomingArchive object
---

# FaxAccountIncomingArchive object

Used by a fax client application to access and configure the archive of inbound fax messages received successfully by the fax service for a particular fax account. You can also use the **FaxAccountIncomingArchive** object to retrieve a message from the archive by specifying its message ID.

A **FaxAccountIncomingArchive** object is accessed through a [**FaxAccountFolders**](-mfax-faxaccountfolders.md) object. **FaxAccountIncomingArchive** objects provide access to [**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md) objects and [**IFaxIncomingMessage2**](-mfax-faxincomingmessage2-cpp.md) objects.

![faxaccountfolders, faxaccountincomingarchive, and faxaccountincomingmessageiterator](images/faxaccountincomingarchive.png)

## Members

The **FaxAccountIncomingArchive** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxAccountIncomingArchive** object has these methods.



| Method                                                                | Description                                                                                                                    |
|:----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**GetMessage**](-mfax-faxaccountincomingarchive-getmessage-vb.md)   | Returns a fax message from the archive of inbound faxes, for a particular fax account, by using the fax message ID.<br/> |
| [**GetMessages**](-mfax-faxaccountincomingarchive-getmessages-vb.md) | Returns a new iterator (archive cursor) for the archive of inbound fax messages for a particular fax account.<br/>       |
| [**Refresh**](-mfax-faxaccountincomingarchive-refresh-vb.md)         | Refreshes **FaxAccountIncomingArchive** object information for a particular fax account from the fax server. <br/>       |



 

### Properties

The **FaxAccountIncomingArchive** object has these properties.



| Property                                                                   | Access type          | Description                                                                                                                             |
|:---------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| [**SizeHigh**](-mfax-faxaccountincomingarchive-sizehigh-vb.md)<br/> | Read-only<br/> | Specifies the high 32-bit value (in bytes) for the size of the archive of inbound fax messages for a particular fax account.<br/> |
| [**SizeLow**](-mfax-faxaccountincomingarchive-sizelow-vb.md)<br/>   | Read-only<br/> | Specifies the low 32-bit value (in bytes) for the size of the archive of inbound fax messages for a particular fax account.<br/>  |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxAccountIncomingArchive<br/>                                             |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxAccountIncomingArchive**](-mfax-faxaccountincomingarchive-cpp.md)
</dt> </dl>

 

 




