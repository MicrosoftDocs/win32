---
title: WNV notification structures
description: The Windows Network Virtualization (WNV) notification API defines the following structures.
ms.assetid: EDA86A8B-17F8-4060-A53A-732C6D7E48FA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WNV notification structures

The Windows Network Virtualization (WNV) notification API defines the following structures.

## In this section



| Topic                                                                                         | Description                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WNV\_IP\_ADDRESS**](/windows/previous-versions/wnvapi/ns-wnvapi-_wnv_ip_address?branch=master)<br/>                                         | Defines an IP address object.<br/>                                                                                                                                                                                                                                                          |
| [**WNV\_NOTIFICATION\_PARAM**](/windows/previous-versions/wnvapi/ns-wnvapi-_wnv_notification_param?branch=master)<br/>                         | Specifies the version, notification type, and the buffer location in a [**WnvRequestNotification**](/windows/previous-versions/wnvapi/nf-wnvapi-wnvrequestnotification?branch=master) function call.<br/>                                                                                                                                         |
| [**WNV\_OBJECT\_CHANGE\_PARAM**](/windows/previous-versions/wnvapi/ns-wnvapi-_wnv_object_change_param?branch=master)<br/>                      | Specifies the parameters of an event that causes the Windows Network Virtualization (WNV) driver to generate a **WnvObjectChangeType** type of notification.<br/>                                                                                                                           |
| [**WNV\_OBJECT\_HEADER**](/windows/previous-versions/wnvapi/ns-wnvapi-_wnv_object_header?branch=master)<br/>                                   | Specifies the major version, minor version, and buffer size of the [**WNV\_NOTIFICATION\_PARAM**](/windows/previous-versions/wnvapi/ns-wnvapi-_wnv_notification_param?branch=master) structure that is passed to the [**WnvRequestNotification**](/windows/previous-versions/wnvapi/nf-wnvapi-wnvrequestnotification?branch=master) function.<br/>                                                       |
| [**WNV\_POLICY\_MISMATCH\_PARAM**](/windows/previous-versions/wnvapi/ns-wnvapi-_wnv_policy_mismatch_param?branch=master)<br/>                  | Specifies the parameters of an event (typically an incoming packet) that causes the Windows Network Virtualization (WNV) driver to generate a **WnvPolicyMismatchType** notification.<br/>                                                                                                  |
| [**WNV\_PROVIDER\_ADDRESS\_CHANGE\_PARAM**](/windows/previous-versions/wnvapi/ns-wnvapi-_wnv_provider_address_change_param?branch=master)<br/> | Specifies the provider address's DAD (duplicate address detection) status change, which causes the Windows Network Virtualization (WNV) driver to generate a **WnvObjectChangeType** notification that specifies the **WnvProviderAddressType** object type containing this structure.<br/> |
| [**WNV\_REDIRECT\_PARAM**](/windows/previous-versions/wnvapi/ns-wnvapi-_wnv_redirect_param?branch=master)<br/>                                 | Specifies the parameters of the event (receiving an incoming Internet Control Message Protocol redirect packet) that causes the Windows Network Virtualization (WNV) driver to generate a **WnvRedirectType** notification.<br/>                                                            |



 

 

 





