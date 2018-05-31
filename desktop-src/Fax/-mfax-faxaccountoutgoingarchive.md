---
Description: Accesses and configures the archive of outbound fax messages, for a particular fax account, sent successfully by the fax service. You can also use the FaxAccountOutgoingArchive object to retrieve a message from the archive by specifying its message ID.
ms.assetid: 21ed0cc8-23a3-4ac1-853f-8f7d004cf843
title: FaxAccountOutgoingArchive object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxAccountOutgoingArchive object

Accesses and configures the archive of outbound fax messages, for a particular fax account, sent successfully by the fax service. You can also use the **FaxAccountOutgoingArchive** object to retrieve a message from the archive by specifying its message ID.

A **FaxAccountOutgoingArchive** object is accessed through a [**FaxAccountFolders**](-mfax-faxaccountfolders.md) object. **FaxAccountOutgoingArchive** objects provide access to [**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md) objects and [**IFaxOutgoingMessage2**](-mfax-faxoutgoingmessage2-cpp.md) objects.

![faxaccountfolders, faxaccountoutgoingarchive, and subordinate objects to faxaccountoutgoingarchive](images/faxaccountoutgoingarchive.png)

## Members

The **FaxAccountOutgoingArchive** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxAccountOutgoingArchive** object has these methods.



| Method                                                                | Description                                                                                                                    |
|:----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**GetMessage**](-mfax-faxaccountoutgoingarchive-getmessage-vb.md)   | Returns a fax message from the archive of outbound faxes for a particular fax account, by using the fax message ID.<br/> |
| [**GetMessages**](-mfax-faxaccountoutgoingarchive-getmessages-vb.md) | Returns a new iterator (archive cursor) for the archive of outbound fax messages for a particular fax account.<br/>      |
| [**Refresh**](-mfax-faxaccountoutgoingarchive-refresh-vb.md)         | Refreshes **FaxAccountOutgoingArchive** object information for a particular fax account from the fax server. <br/>       |



 

### Properties

The **FaxAccountOutgoingArchive** object has these properties.



| Property                                                                   | Access type          | Description                                                                                                                                   |
|:---------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| [**SizeHigh**](-mfax-faxaccountoutgoingarchive-sizehigh-vb.md)<br/> | Read-only<br/> | Specifies the high-order 32-bit value of the size (in bytes) of the archive of outbound fax messages for a particular fax account.<br/> |
| [**SizeLow**](-mfax-faxaccountoutgoingarchive-sizelow-vb.md)<br/>   | Read-only<br/> | Specifies the low-order 32-bit value of the size (in bytes) of the archive of outbound fax messages for a particular fax account.<br/>  |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxAccountOutgoingArchive<br/>                                             |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxAccountOutgoingArchive**](-mfax-faxaccountoutgoingarchive-cpp.md)
</dt> </dl>

 

 




