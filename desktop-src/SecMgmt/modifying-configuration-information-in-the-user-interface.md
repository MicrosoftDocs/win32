---
Description: 'An attachment snap-in extension must allow the user to modify configuration information about the service.'
ms.assetid: 'fb36fcce-5a69-49cd-8cd3-b0b048f2f566'
title: Modifying Configuration Information in the User Interface
---

# Modifying Configuration Information in the User Interface

An attachment snap-in extension must allow the user to modify configuration information about the service. The modified information should be stored by the attachment snap-in extension until the Security Configuration snap-in calls methods of the [**ISceSvcAttachmentPersistInfo**](iscesvcattachmentpersistinfo.md) interface to retrieve the information.

To avoid memory leaks, free memory allocated by the snap-in extension by calling [**ISceSvcAttachmentPersistInfo::FreeBuffer**](iscesvcattachmentpersistinfo-freebuffer.md).

 

 



