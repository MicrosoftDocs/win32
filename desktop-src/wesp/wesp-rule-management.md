---
title: "WESP rule creation and management"
description: "Windows endpoint security platform API reference for rule creation and management, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspCreateRule
- EspGetRuleId
- EspCloseRule
- EspUpdateRules
- EspRemoveAllRulesForClient
- EspRemoveRulesForClient
- EspEnumerateAllRulesForClient
- EspEnumerateRuleIds
- ESP_RULE
- ESP_RULE_FLAGS
- ESP_RULE_ACTION
- ESP_BLOCK_REASON
- ESP_RULE_LIFETIME
- ESP_RULE_UPDATE_TYPE
- ESP_RULE_UPDATE_FLAGS
- ESP_RULE_DESCRIPTOR
- ESP_RULE_UPDATE_ENTRY
---

# Rule creation and management

This page contains reference entries in the [Rules API family](wesp-api-reference.md#rules). Each entry includes its declaration and requirements.

## Rule functions

### EspCreateRule

The API `EspCreateRule` creates a rule. Note that this API simply creates the rule object. The rule does not take effect until it is added to the client by calling `EspUpdateRules`.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateRule(
    _In_ const ESP_RULE_DESCRIPTOR* Descriptor,
    _Out_ ESP_RULE* Rule
    );
```

#### Parameters

##### `Descriptor`

Supplies an `ESP_RULE_DESCRIPTOR` structure that describes the rule to create.

##### `Rule`

Receives a reference to the rule. This reference must be closed by calling `EspCloseRule` once it is no longer needed. Note that rules must be added by calling `EspUpdateRules` before they take effect.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_RULE`](wesp-rule-management.md#esp_rule)
- [`ESP_RULE_DESCRIPTOR`](wesp-rule-management.md#esp_rule_descriptor)
- [`EspUpdateRules`](wesp-rule-management.md#espupdaterules)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetRuleId

The API `EspGetRuleId` retrieves the ID from a rule.

#### Syntax

```cpp
HRESULT
WINAPI
EspGetRuleId(
    _In_ ESP_RULE Rule,
    _Out_ GUID* RuleId
    );
```

#### Parameters

##### `Rule`

Specifies the rule.

##### `RuleId`

Receives the rule ID.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_RULE`](wesp-rule-management.md#esp_rule)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCloseRule

The API `EspCloseRule` closes a client's local reference to the rule, and frees memory associated with this reference. Client's should close their rule once they no longer need the reference. Note that closing a rule does not remove the rule from WESP.

#### Syntax

```cpp
HRESULT
WINAPI
EspCloseRule(
    _In_ _Post_invalid_ ESP_RULE Rule
    );
```

#### Parameters

##### `Rule`

Supplies the rule to close. The supplied "Rule" cannot be used after this API returns.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_RULE`](wesp-rule-management.md#esp_rule)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspUpdateRules

The API `EspUpdateRules` updates a set of rules. Clients can use this API to add, remove, enable, or disable rules. Rule updates are applied atomically, and in the same order as the specified "Entries" array.

#### Syntax

```cpp
HRESULT
WINAPI
EspUpdateRules(
    _In_ ESP_CLIENT Client,
    _In_ ESP_RULE_UPDATE_FLAGS Flags,
    _In_ UINT32 EntriesCount,
    _In_reads_(EntriesCount) const ESP_RULE_UPDATE_ENTRY* Entries
    );
```

#### Parameters

##### `Client`

Specifies the client for which to update rules. Each rule specified in the entries array must have been created for this client.

##### `Flags`

Specifies flags for updating the rules.

##### `EntriesCount`

Specifies the number of elements in the entries array.

##### `Entries`

Specifies an array of `ESP_RULE_UPDATE_ENTRY` structures that describe the rule updates to make. The rule updates are applied in the same order as specified in this array. There can only be 1 update per rule.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_RULE_UPDATE_ENTRY`](wesp-rule-management.md#esp_rule_update_entry)
- [`ESP_RULE_UPDATE_FLAGS`](wesp-rule-management.md#esp_rule_update_flags)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspRemoveAllRulesForClient

Removes all rules for the specified WESP client.

#### Syntax

```cpp
HRESULT
WINAPI
EspRemoveAllRulesForClient(
    _In_ ESP_CLIENT Client
    );
```

#### Parameters

##### `Client`

Specifies the client to remove all rules for.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspRemoveRulesForClient

The API `EspRemoveRulesForClient` removes rules with the specified lifetime for the client.

#### Syntax

```cpp
HRESULT
WINAPI
EspRemoveRulesForClient(
    _In_ ESP_CLIENT Client,
    _In_ ESP_RULE_LIFETIME Lifetime
    );
```

#### Parameters

##### `Client`

Specifies the client to remove rules for.

##### `Lifetime`

Specifies the rule lifetime to remove.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_RULE_LIFETIME`](wesp-rule-management.md#esp_rule_lifetime)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspEnumerateAllRulesForClient

The API `EspEnumerateAllRulesForClient` enumerates all rule IDs for a client.

#### Syntax

```cpp
HRESULT
WINAPI
EspEnumerateAllRulesForClient(
    _In_ ESP_CLIENT Client,
    _Out_ UINT32* RulesCount,
    _Outptr_result_buffer_all_(*RulesCount) GUID** RuleIds
    );
```

#### Parameters

##### `Client`

Specifies the client to enumerate rules for.

##### `RulesCount`

Receives the number of elements in the rule IDs array.

##### `RuleIds`

Receives the array of rule IDs. This array must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspEnumerateRuleIds

The API `EspEnumerateRuleIds` enumerates rule IDs for a client.

#### Syntax

```cpp
HRESULT
WINAPI
EspEnumerateRuleIds(
    _In_ ESP_CLIENT Client,
    _In_ ESP_RULE_LIFETIME Lifetime,
    _Out_ UINT32* RulesCount,
    _Outptr_result_buffer_all_(*RulesCount) GUID** RuleIds
    );
```

#### Parameters

##### `Client`

Specifies the client to enumerate rules for.

##### `Lifetime`

Specifies the lifetime of the rules to enumerate.

##### `RulesCount`

Receives the number of elements in the rule IDs array.

##### `RuleIds`

Receives the array of rule IDs. This array must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_RULE_LIFETIME`](wesp-rule-management.md#esp_rule_lifetime)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Rule handle and types

### ESP_RULE

Identifies a WESP rule.

#### Syntax

```cpp
DECLARE_HANDLE(ESP_RULE);
```

#### Remarks

Obtain this handle with `EspCreateRule`. Release it with `EspCloseRule`.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_RULE_FLAGS

The enum `ESP_RULE_FLAGS` defines rule flags.

#### Syntax

```cpp
typedef enum ESP_RULE_FLAGS
{
    ESP_RULE_FLAGS_NONE                  = 0x00000000,
    ESP_RULE_FLAGS_DISABLED              = 0x00000001,
    ESP_RULE_FLAGS_NOTIFY_ON_COMPLETION  = 0x00000002
} ESP_RULE_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_RULE_FLAGS_DISABLED` | Indicates to disable the rule by default. |
| `ESP_RULE_FLAGS_NOTIFY_ON_COMPLETION` | For event types that support notify on completion, a rule may request a completion notification by specifying this flag. If the rule matches during pre-operation evaluation, WESP records that completion notification was requested for that operation. When the operation completes, WESP dispatches a completion event.<br>Notify on completion events are only processed by a client if the client explicitly expressed interest in the event through this flag. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_RULE_ACTION

The enum `ESP_RULE_ACTION` defines a rule action.

#### Syntax

```cpp
typedef enum ESP_RULE_ACTION
{
    ESP_RULE_ACTION_NONE = 0,
    ESP_RULE_ACTION_NOTIFY,
    ESP_RULE_ACTION_NOTIFY_ON_COMPLETION,
    ESP_RULE_ACTION_NO_NOTIFY,
    ESP_RULE_ACTION_IGNORE,
    ESP_RULE_ACTION_BLOCK,
    ESP_RULE_ACTION_ALLOW,
    ESP_RULE_ACTION_MATCH_SUBRULES,
    ESP_RULE_ACTION_CONTINUE_MATCHING_NEXT_RULE,
    ESP_RULE_ACTION_CONTINUE_MATCHING_NEXT_SUBRULE
} ESP_RULE_ACTION;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_RULE_ACTION_NOTIFY` | Notifies the client of the event asynchronously. The notify action is typically used to observe events. |
| `ESP_RULE_ACTION_NOTIFY_ON_COMPLETION` | Notifies the client of the event asynchronously when it completes. The notify-on-completion action is typically used to observe the completion of an event. Notify on completion events are only dispatched when requested by the client. A client requests a completion event when a rule that specifies `ESP_RULE_FLAGS_NOTIFY_ON_COMPLETION` matches during pre-operation evaluation. Note that not all events support the NotifyOnCompletion action. |
| `ESP_RULE_ACTION_NO_NOTIFY` | The client is not notified if the rule matches. The no-notify action is typically used to update context keys or modify event data without notifying the client. It is similar to the continue-matching-next-rule action with the difference being that rule evaluation ends for the clients if a rule with the no-notify action matches. |
| `ESP_RULE_ACTION_IGNORE` | Ignore the event. Clients can use this rule action to stop rule processing early. For example, a client may have an ignore rule for events originating from their own process. |
| `ESP_RULE_ACTION_BLOCK` | Blocks the event if the rule matches |
| `ESP_RULE_ACTION_ALLOW` | Explicitly allows the event. If one client decides to explicitly allow an event, another client can still block the event. The allow action can only be used with a small subset of events (e.g. boot driver load). |
| `ESP_RULE_ACTION_MATCH_SUBRULES` | The rule's subrules should be evaluated. This allows the client to logically chain rules together. Additionally, it ensures that certain rules are only evaluated if a parent rule has matched. Multiple rules with the match subrules action can be chained. |
| `ESP_RULE_ACTION_CONTINUE_MATCHING_NEXT_RULE` | Indicates to continue matching the next rule. The next top-level client rule is evaluated. This can be useful if a client wants to update a context key and/or be notified asynchronously when the rule matches, but doesn't want to stop rule processing. |
| `ESP_RULE_ACTION_CONTINUE_MATCHING_NEXT_SUBRULE` | Indicates to continue matching the next subrule. The next subrule is evaluated. This is similar to the "Continue Matching Next Rule" action, but instead of moving to the next top-level rule, the rule engine moves to the next subrule. This action can only be set on a subrule. A rule with this action can only be added indirectly when the parent rule is added since a top-level rule cannot use this action. This is validated when the rule is added to the WESP driver. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BLOCK_REASON

The enum `ESP_BLOCK_REASON` defines a block reason.

#### Syntax

```cpp
typedef enum ESP_BLOCK_REASON
{
    ESP_BLOCK_REASON_NONE = 0,
    ESP_BLOCK_REASON_VIRUS_INFECTED,
    ESP_BLOCK_REASON_ACCESS_DENIED,
    ESP_BLOCK_REASON_NOT_FOUND,
    ESP_BLOCK_REASON_BAD_IMAGE,
    ESP_BLOCK_REASON_BAD_IMAGE_BOOT_CRITICAL
} ESP_BLOCK_REASON;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_BLOCK_REASON_VIRUS_INFECTED` | The event is blocked with STATUS_VIRUS_INFECTED. |
| `ESP_BLOCK_REASON_ACCESS_DENIED` | The event is blocked with STATUS_ACCESS_DENIED. |
| `ESP_BLOCK_REASON_NOT_FOUND` | The event is blocked with STATUS_NOT_FOUND. |
| `ESP_BLOCK_REASON_BAD_IMAGE` | This block reason can only be used with the boot driver load event. It indicates to block loading a boot driver with the classification BdCbClassificationKnownBadImage. |
| `ESP_BLOCK_REASON_BAD_IMAGE_BOOT_CRITICAL` | This block reason can only be used with the boot driver load event. It indicates to block loading a boot driver with the classification BdCbClassificationKnownBadImageBootCritical. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_RULE_LIFETIME

The enum `ESP_RULE_LIFETIME` specifies the lifetime for a rule.

#### Syntax

```cpp
typedef enum ESP_RULE_LIFETIME
{
    ESP_RULE_LIFETIME_NONE = 0,
    ESP_RULE_LIFETIME_CLIENT_SESSION,
    ESP_RULE_LIFETIME_BOOT_SESSION,
    ESP_RULE_LIFETIME_PERSISTED,
    ESP_RULE_LIFETIME_PERSISTED_EARLY_BOOT
} ESP_RULE_LIFETIME;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_RULE_LIFETIME_CLIENT_SESSION` | The rule's lifetime is tied to the client's session. If the client disconnects, the rule is removed. |
| `ESP_RULE_LIFETIME_BOOT_SESSION` | The rule's lifetime is tied to the current boot session. The rule is deleted when the machine reboots. |
| `ESP_RULE_LIFETIME_PERSISTED` | The rule is persisted across boot sessions. The rule will continue to be applied after the machine reboots. If a rule is persisted, it can only be associated with a persisted event queue. |
| `ESP_RULE_LIFETIME_PERSISTED_EARLY_BOOT` | The rule is persisted across boot sessions. The rule will continue to be applied after the machine reboots. Additionally, the rule will be applied during the ELAM phase of early boot. If a rule is persisted, it can only be associated with a persisted event queue.<br>This lifetime is only supported for registry events and the boot driver load event. Additionally, if a rule specifies this lifetime, the rule cannot reference any filesystem related objects in the rule configuration since the filesystem stack is not initialized yet during early boot.<br>Early boot rules continue to apply after the ELAM phase. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_RULE_UPDATE_TYPE

The enum `ESP_RULE_UPDATE_TYPE` defines a rule update type.

#### Syntax

```cpp
typedef enum ESP_RULE_UPDATE_TYPE
{
    ESP_RULE_UPDATE_TYPE_NONE = 0,
    ESP_RULE_UPDATE_TYPE_ADD,
    ESP_RULE_UPDATE_TYPE_ADD_OR_REPLACE,
    ESP_RULE_UPDATE_TYPE_REMOVE,
    ESP_RULE_UPDATE_TYPE_ENABLE,
    ESP_RULE_UPDATE_TYPE_DISABLE
} ESP_RULE_UPDATE_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_RULE_UPDATE_TYPE_ADD` | Adds the rule. If the rule already exists, the update fails. |
| `ESP_RULE_UPDATE_TYPE_ADD_OR_REPLACE` | Adds the rule. If the rule already exists, it will be replaced. |
| `ESP_RULE_UPDATE_TYPE_REMOVE` | Removes the rule. If the rule has not been added, this is a no-op. |
| `ESP_RULE_UPDATE_TYPE_ENABLE` | Enables the rule. If the rule is already enabled, this is a no-op. If the rule doesn't exist, the update fails. |
| `ESP_RULE_UPDATE_TYPE_DISABLE` | Disables the rule. If the rule is already disabled, this is a no-op. If the rule doesn't exist, the update fails. If a rule is disabled, it won't be enforced until it is re-enabled. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_RULE_UPDATE_FLAGS

The enum `ESP_RULE_UPDATE_FLAGS` specifies flags for updating rules.

#### Syntax

```cpp
typedef enum ESP_RULE_UPDATE_FLAGS
{
    ESP_RULE_UPDATE_FLAGS_NONE                = 0x00000000,
    ESP_RULE_UPDATE_FLAGS_REMOVE_ALL_EXISTING = 0x00000001
} ESP_RULE_UPDATE_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_RULE_UPDATE_FLAGS_REMOVE_ALL_EXISTING` | All existing rules should be removed as part of the update. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_RULE_DESCRIPTOR

The structure `ESP_RULE_DESCRIPTOR` describes a rule. It is supplied to the API `EspCreateRule` to create a rule.

#### Syntax

```cpp
typedef struct ESP_RULE_DESCRIPTOR
{
    GUID RuleId;
    UINT64 OrderGroup;
    ESP_RULE_LIFETIME Lifetime;
    ESP_RULE_FLAGS RuleFlags;
    ESP_EVENT_TYPE EventType;
    ESP_RULE_CONFIG RuleConfig;
    ESP_EVENT_MODIFY EventModify;
    ESP_RULE_ACTION Action;

    union
    {
        struct
        {
            ESP_BLOCK_REASON Reason;
            ESP_EVENT_QUEUE AsyncEventQueue;
        } Block;

        struct
        {
            ESP_EVENT_QUEUE AsyncEventQueue;
        } Allow, Notify, NotifyOnCompletion;

        struct
        {
            UINT32 SubrulesCount;
            _Field_size_(SubrulesCount) ESP_RULE* Subrules;
        } MatchSubrules;
    } u;
} ESP_RULE_DESCRIPTOR;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RuleId | The "RuleId" is used to uniquely identify the rule. Each rule must have a unique id. The client can pass a zeroed GUID to indicate that a random rule id should be generated. |
| OrderGroup | The "OrderGroup" field defines the precedence order for the rules. Order groups do not need to be sequential. The WESP rule engine will process rules for a given client in ascending order based on their order group. Order groups are not shared amongst clients. The rule processing ordering between clients is determined by their respective altitudes.<br>When an event is emitted, the WESP framework will process the event based on the altitude ordering of each connected client. For a given client, the rule engine will check if a rule matches the event. If there is a matching rule, the rule engine will stop processing rules for that client, and take action based on the matched rule's descriptor. If the action taken by the client for which the rule matched results in the event being blocked or explicitly allowed, other clients will not get a chance to process the event. If the action does not result in blocking or explicitly allowing the event, the rule engine will process the event for the next client's set of rules.<br>Multiple rules can use the same order group. In that case, there are no ordering guarantees within the order group. Rules within an order group may be re-ordered by the WESP framework as an optimization. If clients require specific ordering between certain rules, they should be in different order groups.<br>This parameter is ignored for subrules. Order groups are only used for top-level rules. |
| Lifetime | Specifies the lifetime of the rule. The following values are supported:<br>Client Session: The rule will be automatically removed if the client disconnects.<br>Boot Session: The rule's lifetime is tied to the current boot session. The rule is deleted when the machine reboots.<br>Persisted: The rule will persist across boot sessions, and continue to be enforced when the client is disconnected.<br>Persisted Early Boot: : The rule will persist across boot sessions, and continue to be enforced when the client is disconnected.  Additionally, the rule will be applied during the ELAM phase of driver start.<br>This parameter is ignored for subrules. Rule lifetime only applies to top-level rules. If a top-level rule is persisted, all its sub-rules will be transitively persisted. |
| RuleFlags | Defines a mask of flags for the rule. The currently supported values are list below:<br>Disabled: Indicates that the rule should be disabled. By default, rules are enabled when they are added by a client. |
| EventType | The "EventType" field defines the event type the rule applies to. The set of supported events is listed at the beginning of this document. |
| RuleConfig | Specifies an `ESP_RULE_CONFIG` structure that contains various configurations for the event such as filters, context key updates, binding keys, etc. |
| EventModify | Specifies an `ESP_EVENT_MODIFY` structure that describes how the event data should be modified. For example, a client could define a modification that strips write access when a handle to their process is opened. The modifications are applied prior to notifying the client.<br> |
| Action | Specifies the action to take if the rule matches. The following actions are supported:<br>Notify: Notifies the client of the event asynchronously. The notify action is typically used to observe events.<br>NotifyOnCompletion: Notifies the client of the event asynchronously when it completes. The notify-on-completion action is typically used to observe the completion of an event. Notify on completion events are only dispatched when requested by the client. A client requests a completion event when a rule that specifies `ESP_RULE_FLAGS_NOTIFY_ON_COMPLETION` matches during pre-operation evaluation. Note that not all events support the NotifyOnCompletion action. <br>NoNotify: The client is not notified if the rule matches. The no-notify action is typically used to update context keys or modify event data without notifying the client.<br>Ignore: Ignore the event. This can be used to stop rule processing early. For example, a client may have an ignore rule for events originating from their own process.<br>Block: Blocks the event if the rule matches. Clients can optionally receive asynchronous notifications for events they block through the field "Block.AsyncEventQueue".<br>Allow: Explicitly allows the event. If one client allows an event, another client can still block the event. Clients can optionally receive asynchronous notifications for events they allow through the field "Allow.AsyncEventQueue".<br>Match Subrules: The rule's subrules should be evaluated. This allows the client to logically chain rules together. Additionally, it ensures that certain rules are only evaluated if a parent rule has matched. Multiple rules with the match subrules action can be chained. <br>Continue Matching Next Rule: Indicates to continue matching rules. The next top-level client rule is evaluated. This can be useful if a client wants to update a context key and/or be notified asynchronously when the rule matches, but doesn't want to stop rule processing.<br>Continue Matching Next Subrule: Indicates to continue matching rules. The next subrule is evaluated. This is similar to the "Continue Matching Next Rule" action, but instead of moving to the next top-level rule, the rule engine moves to the next subrule. This action can only be set on a subrule. A rule with this action can only be added indirectly when the parent rule is added since a top-level rule cannot use this action. This is validated when the rule is added to the WESP driver. |
| Block.Reason | If the action is "Block", this field specifies the reason for blocking the event. |
| Block.AsyncEventQueue | Optionally specifies an asynchronous event queue that receives a notification if the block rule matches. If the rule's lifetime is persisted, the event queue's lifetime must also be persisted. |
| Allow.AsyncEventQueue | Optionally specifies an asynchronous event queue that receives a notification if the allow rule matches. If the rule's lifetime is persisted, the event queue's lifetime must also be persisted. |
| Notify.AsyncEventQueue | Optionally specifies an asynchronous event queue that receives a notification if the notify rule matches. If the rule's lifetime is persisted, the event queue's lifetime must also be persisted. |
| NotifyOnCompletion.AsyncEventQueue | Optionally specifies an asynchronous event queue that receives a notification if the notify on completion rule matches. If the rule's lifetime is persisted, the event queue's lifetime must also be persisted. |
| MatchSubrules.SubrulesCount | Specifies the number of elements in the Subrules array. |
| MatchSubrules.Subrules | Specified an array of subrules. Subrules are processed by the rule engine in the same order as this array.<br>Note that a rule can be a subrule as long as the event type is the same as the parent rule, and it is not already a top-level rule. A rule cannot be both a subrule and a top-level rule. Additionally, the same subrule can be specified multiple times in the same rule tree. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BLOCK_REASON`](wesp-rule-management.md#esp_block_reason)
- [`ESP_EVENT_MODIFY`](wesp-rule-event-modification.md#esp_event_modify)
- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [`ESP_EVENT_TYPE`](wesp-event-shared-types.md#esp_event_type)
- [`ESP_RULE`](wesp-rule-management.md#esp_rule)
- [`ESP_RULE_ACTION`](wesp-rule-management.md#esp_rule_action)
- [`ESP_RULE_CONFIG`](wesp-rule-configuration.md#esp_rule_config)
- [`ESP_RULE_FLAGS`](wesp-rule-management.md#esp_rule_flags)
- [`ESP_RULE_LIFETIME`](wesp-rule-management.md#esp_rule_lifetime)
- [`EspCreateRule`](wesp-rule-management.md#espcreaterule)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_RULE_UPDATE_ENTRY

The structure `ESP_RULE_UPDATE_ENTRY` represents an update to a rule. It is supplied as part of the API `EspUpdateRules`.

#### Syntax

```cpp
typedef struct ESP_RULE_UPDATE_ENTRY
{
    ESP_RULE_UPDATE_TYPE UpdateType;

    union
    {
        GUID RuleId;
        ESP_RULE Rule;
    } u;
} ESP_RULE_UPDATE_ENTRY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| UpdateType | Specifies the update type for the rule. The supported update types are:<br>Add: Adds the rule. Once the rule has been added to the WESP driver, it will start taking effect. If the rule already exists, `EspUpdateRules` will fail.<br>Remove: Removes the rule. If the rule has not been added, this is a no-op.<br>Add or Replace: Adds the rule. If the rule already exists, it will be replaced.<br>Enable: Enables the rule. If the rule is already enabled, this is a no-op. If the rule doesn't exist, `EspUpdateRules` will fail. Rules are enabled by default when they are added, unless the disabled rule flag is set in the rule descriptor.<br>Disable: Disables the rule. If the rule is already disabled, this is a no-op. If the rule doesn't exist, `EspUpdateRules` will fail. If a rule is disabled, it won't be enforced until it is re-enabled. |
| RuleId | If the update type is "Remove", "Enable", or "Disable", specifies the rule id to update. |
| Rule | If the update type is "Add" or "Add-or-Replace", specifies the rule to add. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_RULE`](wesp-rule-management.md#esp_rule)
- [`ESP_RULE_UPDATE_TYPE`](wesp-rule-management.md#esp_rule_update_type)
- [`EspUpdateRules`](wesp-rule-management.md#espupdaterules)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
