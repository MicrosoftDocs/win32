---
description: A wrapper structure for a DLP Request.
title: DlpRequest structure (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpRequest
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# DlpRequest structure

A wrapper structure for a DLP Request.

## Syntax

```cpp
struct DlpRequest
{
    DlpRequestId id;
    uint32_t size;
    //! The data associated with the request being performed
    union
    {
        AuthGroupOverrideRequest* authGroupOverrideRequest;
        GetFileCloudApplicationPolicyRequest* getFileCloudApplicationPolicyRequest;
        GetFileApplicationAccessRequest* getFileApplicationAccessRequest;
        GetNotificationSettingRequest* getNotificationSettingRequest;
        SendOperationEnforcementEventRequest* sendOperationEnforcementEventRequest;
        SendFileAccessEventRequest* sendFileAccessEventRequest;
    };
};
```

## Members

*id* `[in]`

The id of the request being made to Endpoint DLP.  

*size* `[in]`

The size of the request structure (e.g. `sizeof(AuthGroupOverrideRequest)`). Used for versioning of individual requests types.

*union* `[in, out]`

The union of request-specific data structures.

### Union members

The following data structures can be provided as members of the union:

#### authGroupOverrideRequest

Structure containing the parameters to include in the request when `id=RequestIdAuthorizedGroupOverrideEdge`.

[AuthGroupOverrideRequest](endpointdlp-authgroupoverriderequest.md) defines the structure of the `authGroupOverrideRequest`.

#### getFileCloudApplicationPolicyRequest

Structure containing the parameters to include in the request when `id=RequestIdGetFileCloudApplicationPolicy`.

[GetFileCloudApplicationPolicyRequest](endpointdlp-getfilecloudapplicationpolicyrequest.md) defines the structure of the `getFileCloudApplicationPolicyRequest`.

#### getFileApplicationAccessRequest

Structure containing the parameters to include in the request when `id=RequestIdGetFileApplicationAccess`.

[GetFileApplicationAccessRequest](endpointdlp-getfileapplicationaccessrequest.md) defines the structure of the `getFileApplicationAccessRequest`.

#### getNotificationSettingRequest

Structure containing the parameters to include in the request when `id=RequestIdGetNotificationSetting`.

[GetNotificationSettingRequest](endpointdlp-getnotificationsettingrequest.md) defines the structure of the `getNotificationSettingRequest`.

#### sendOperationEnforcementEventRequest

Structure containing the parameters to include in the request when `id=RequestIdSendOperationEnforcementEvent`.

[SendOperationEnforcementEventRequest](endpointdlp-sendoperationenforcementeventrequest.md) defines the structure of the `sendOperationEnforcementEventRequest`.

#### sendFileAccessEventRequest

Structure containing the parameters to include in the request when `id=RequestIdSendFileAccessEvent`.

[SendFileAccessEventRequest](endpointdlp-sendfileaccesseventrequest.md) defines the structure of the `sendFileAccessEventRequest`.

## Remarks

Represents a specific versioned request. If `id=RequestIdGetFileCloudApplicationPolicy`, then `getFileCloudApplicationPolicyRequest` should be set, etc.

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows 11, version 24H2 (Build 26100) |
| DLL                      | EndpointDlp.dll |
