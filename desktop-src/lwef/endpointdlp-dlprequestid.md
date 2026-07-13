---
description: An enum to identify the type of DLP Request being made.
title: DlpRequestId Enum (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpRequestId
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# DlpRequestId Enum

An enum to identify the type of request being made to Endpoint DLP.

## Syntax

```cpp
enum DlpRequestId
{
    Reserved0,
    Reserved1,
    Reserved2,
    RequestIdAuthorizedGroupOverrideEdge,
    RequestIdGetFileCloudApplicationPolicy,
    RequestIdGetFileApplicationAccess,
    RequestIdGetNotificationSetting,
    RequestIdSendOperationEnforcementEvent,
    RequestIdSendFileAccessEvent
};
```

## Constants

*RequestIdAuthorizedGroupOverrideEdge*

Indicates that a [DlpRequest](endpointdlp-dlprequest.md) contains a [AuthGroupOverrideRequest](endpointdlp-authgroupoverriderequest.md) . 

*RequestIdGetFileCloudApplicationPolicy*

Indicates that a [DlpRequest](endpointdlp-dlprequest.md)  contains a [GetFileCloudApplicationPolicyRequest](endpointdlp-getfilecloudapplicationpolicyrequest.md).

*RequestIdGetFileApplicationAccess*

Indicates that a [DlpRequest](endpointdlp-dlprequest.md)  contains a [GetFileApplicationAccessRequest](endpointdlp-getfileapplicationaccessrequest.md).

*RequestIdGetNotificationSetting*

Indicates that a [DlpRequest](endpointdlp-dlprequest.md)  contains a [GetNotificationSettingRequest](endpointdlp-getnotificationsettingrequest.md).

*RequestIdSendFileAccessEvent*

Indicates that a [DlpRequest](endpointdlp-dlprequest.md)  contains a [SendFileAccessEventRequest](endpointdlp-sendfileaccesseventrequest.md).

*RequestIdSendOperationEnforcementEvent*

Indicates that a [DlpRequest](endpointdlp-dlprequest.md)  contains a [SendOperationEnforcementEventRequest](endpointdlp-sendoperationenforcementeventrequest.md).

## Remarks

This enum describes the specific request to send to EndpointDlp. The last five constants map directly to the existing APIs. For example, *RequestIdGetFileCloudApplicationPolicy* maps to [DlpGetFileCloudApplicationPolicyEx](endpointdlp-dlpgetfilecloudapplicationpolicyex.md), *RequestIdGetFileApplicationAccess* maps to [DlpGetFileApplicationAccessEx](endpointdlp-dlpgetfileapplicationaccessex.md), etc.
