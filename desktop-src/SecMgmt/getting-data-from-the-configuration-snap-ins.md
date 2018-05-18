---
Description: 'The attachment snap-in extension has no way to directly query the security database to retrieve information. Instead, it must query this information from the Security Configuration snap-ins using ISceSvcAttachmentData::GetData.'
ms.assetid: '1171beed-5b28-4f31-b33f-533e3c631b0d'
title: 'Getting Data from the Configuration Snap-ins'
---

# Getting Data from the Configuration Snap-ins

The attachment snap-in extension has no way to directly query the security database to retrieve information. Instead, it must query this information from the Security Configuration snap-ins using [**ISceSvcAttachmentData::GetData**](iscesvcattachmentdata-getdata.md).

The attachment snap-in can retrieve all of the data when it initializes itself, or it can retrieve information when its node is opened.

> [!Note]  
> You must use the [**ISceSvcAttachmentData::FreeBuffer**](iscesvcattachmentdata-freebuffer.md) method to free the buffer allocated by the Security Configuration snap-in method [**ISceSvcAttachmentData::GetData**](iscesvcattachmentdata-getdata.md).

 

 

 



