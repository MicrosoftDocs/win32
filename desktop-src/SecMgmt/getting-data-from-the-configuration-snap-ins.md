---
description: The attachment snap-in extension has no way to directly query the security database to retrieve information. Instead, it must query this information from the Security Configuration snap-ins using ISceSvcAttachmentData::GetData.
ms.assetid: 1171beed-5b28-4f31-b33f-533e3c631b0d
title: Getting Data from the Configuration Snap-ins
ms.topic: article
ms.date: 05/31/2018
---

# Getting Data from the Configuration Snap-ins

The attachment snap-in extension has no way to directly query the security database to retrieve information. Instead, it must query this information from the Security Configuration snap-ins using [**ISceSvcAttachmentData::GetData**](/windows/desktop/api/Scesvc/nf-scesvc-iscesvcattachmentdata-getdata).

The attachment snap-in can retrieve all of the data when it initializes itself, or it can retrieve information when its node is opened.

> [!Note]  
> You must use the [**ISceSvcAttachmentData::FreeBuffer**](/windows/desktop/api/Scesvc/nf-scesvc-iscesvcattachmentdata-freebuffer) method to free the buffer allocated by the Security Configuration snap-in method [**ISceSvcAttachmentData::GetData**](/windows/desktop/api/Scesvc/nf-scesvc-iscesvcattachmentdata-getdata).

 

 

 



