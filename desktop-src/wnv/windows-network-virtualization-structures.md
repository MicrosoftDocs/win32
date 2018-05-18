---
title: WNV notification structures
description: The Windows Network Virtualization (WNV) notification API defines the following structures.
ms.assetid: 'EDA86A8B-17F8-4060-A53A-732C6D7E48FA'
---

# WNV notification structures

The Windows Network Virtualization (WNV) notification API defines the following structures.

## In this section



| Topic                                                                                         | Description                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WNV\_IP\_ADDRESS**](wnv-ip-address.md)<br/>                                         | Defines an IP address object.<br/>                                                                                                                                                                                                                                                          |
| [**WNV\_NOTIFICATION\_PARAM**](wnv-notification-param.md)<br/>                         | Specifies the version, notification type, and the buffer location in a [**WnvRequestNotification**](wnvrequestnotification.md) function call.<br/>                                                                                                                                         |
| [**WNV\_OBJECT\_CHANGE\_PARAM**](wnv-object-change-param.md)<br/>                      | Specifies the parameters of an event that causes the Windows Network Virtualization (WNV) driver to generate a **WnvObjectChangeType** type of notification.<br/>                                                                                                                           |
| [**WNV\_OBJECT\_HEADER**](wnv-object-header.md)<br/>                                   | Specifies the major version, minor version, and buffer size of the [**WNV\_NOTIFICATION\_PARAM**](wnv-notification-param.md) structure that is passed to the [**WnvRequestNotification**](wnvrequestnotification.md) function.<br/>                                                       |
| [**WNV\_POLICY\_MISMATCH\_PARAM**](wnv-policy-mismatch-param.md)<br/>                  | Specifies the parameters of an event (typically an incoming packet) that causes the Windows Network Virtualization (WNV) driver to generate a **WnvPolicyMismatchType** notification.<br/>                                                                                                  |
| [**WNV\_PROVIDER\_ADDRESS\_CHANGE\_PARAM**](wnv-provider-address-change-param.md)<br/> | Specifies the provider address's DAD (duplicate address detection) status change, which causes the Windows Network Virtualization (WNV) driver to generate a **WnvObjectChangeType** notification that specifies the **WnvProviderAddressType** object type containing this structure.<br/> |
| [**WNV\_REDIRECT\_PARAM**](wnv-redirect-param.md)<br/>                                 | Specifies the parameters of the event (receiving an incoming Internet Control Message Protocol redirect packet) that causes the Windows Network Virtualization (WNV) driver to generate a **WnvRedirectType** notification.<br/>                                                            |



 

 

 





