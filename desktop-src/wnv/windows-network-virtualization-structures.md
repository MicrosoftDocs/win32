---
title: WNV notification structures
description: The Windows Network Virtualization (WNV) notification API defines the following structures.
ms.assetid: EDA86A8B-17F8-4060-A53A-732C6D7E48FA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WNV notification structures

The Windows Network Virtualization (WNV) notification API defines the following structures.

## In this section



| Topic                                                                                         | Description                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WNV\_IP\_ADDRESS**](/previous-versions/windows/desktop/api/wnvapi/ns-wnvapi-_wnv_ip_address)<br/>                                         | Defines an IP address object.<br/>                                                                                                                                                                                                                                                          |
| [**WNV\_NOTIFICATION\_PARAM**](/previous-versions/windows/desktop/api/wnvapi/ns-wnvapi-_wnv_notification_param)<br/>                         | Specifies the version, notification type, and the buffer location in a [**WnvRequestNotification**](/previous-versions/windows/desktop/api/wnvapi/nf-wnvapi-wnvrequestnotification) function call.<br/>                                                                                                                                         |
| [**WNV\_OBJECT\_CHANGE\_PARAM**](/previous-versions/windows/desktop/api/wnvapi/ns-wnvapi-_wnv_object_change_param)<br/>                      | Specifies the parameters of an event that causes the Windows Network Virtualization (WNV) driver to generate a **WnvObjectChangeType** type of notification.<br/>                                                                                                                           |
| [**WNV\_OBJECT\_HEADER**](/previous-versions/windows/desktop/api/wnvapi/ns-wnvapi-_wnv_object_header)<br/>                                   | Specifies the major version, minor version, and buffer size of the [**WNV\_NOTIFICATION\_PARAM**](/previous-versions/windows/desktop/api/wnvapi/ns-wnvapi-_wnv_notification_param) structure that is passed to the [**WnvRequestNotification**](/previous-versions/windows/desktop/api/wnvapi/nf-wnvapi-wnvrequestnotification) function.<br/>                                                       |
| [**WNV\_POLICY\_MISMATCH\_PARAM**](/previous-versions/windows/desktop/api/wnvapi/ns-wnvapi-_wnv_policy_mismatch_param)<br/>                  | Specifies the parameters of an event (typically an incoming packet) that causes the Windows Network Virtualization (WNV) driver to generate a **WnvPolicyMismatchType** notification.<br/>                                                                                                  |
| [**WNV\_PROVIDER\_ADDRESS\_CHANGE\_PARAM**](/previous-versions/windows/desktop/api/wnvapi/ns-wnvapi-_wnv_provider_address_change_param)<br/> | Specifies the provider address's DAD (duplicate address detection) status change, which causes the Windows Network Virtualization (WNV) driver to generate a **WnvObjectChangeType** notification that specifies the **WnvProviderAddressType** object type containing this structure.<br/> |
| [**WNV\_REDIRECT\_PARAM**](/previous-versions/windows/desktop/api/wnvapi/ns-wnvapi-_wnv_redirect_param)<br/>                                 | Specifies the parameters of the event (receiving an incoming Internet Control Message Protocol redirect packet) that causes the Windows Network Virtualization (WNV) driver to generate a **WnvRedirectType** notification.<br/>                                                            |



 

 

 





