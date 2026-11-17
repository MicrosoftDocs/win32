---
title: "WESP rule event modification"
description: "Windows endpoint security platform API reference for rule event modification, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_EVENT_MODIFY_TYPE
- ESP_EVENT_MODIFY
- ESP_ACCESS_MASK_MODIFICATION
- ESP_ACCESS_MASK_MODIFICATION_LIST
---

# Rule event modification

This page contains reference entries in the [Rules API family](wesp-api-reference.md#rules). Each entry includes its declaration and requirements.

## Event modification

### ESP_EVENT_MODIFY_TYPE

The enum `ESP_EVENT_MODIFY_TYPE` defines an event modification type.

#### Syntax

```cpp
typedef enum ESP_EVENT_MODIFY_TYPE
{
    ESP_EVENT_MODIFY_TYPE_NONE = 0,
    ESP_EVENT_MODIFY_TYPE_OB_CREATE_HANDLE,
    ESP_EVENT_MODIFY_TYPE_OB_DUPLICATE_HANDLE,
    ESP_EVENT_MODIFY_TYPE_FO_CREATE,
    ESP_EVENT_MODIFY_TYPE_FS_QUERY_OPEN_FILE
} ESP_EVENT_MODIFY_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_EVENT_MODIFY_TYPE_OB_CREATE_HANDLE` | The modification is for an OB create handle event. |
| `ESP_EVENT_MODIFY_TYPE_OB_DUPLICATE_HANDLE` | The modification is for an OB duplicate handle event. |
| `ESP_EVENT_MODIFY_TYPE_FO_CREATE` | The modification is for a file object create event. |
| `ESP_EVENT_MODIFY_TYPE_FS_QUERY_OPEN_FILE` | The modification is for a query open file event. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_MODIFY

The structure `ESP_EVENT_MODIFY` is used to describe modifications to make to event data if the rule is associated with matches.

#### Syntax

```cpp
typedef struct ESP_EVENT_MODIFY
{
    ESP_EVENT_MODIFY_TYPE Type;
    UINT32 DataSize;
    _Field_size_bytes_(DataSize) const void* Data;
} ESP_EVENT_MODIFY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Type | Supplies the type of modify struct the Data field points to. The supported types are:<br>OB Create Handle<br>OB Duplicate Handle<br>Reg Create Key<br>Reg Open Key<br>File Object Create<br>File Query Open |
| DataSize | Supplies the size of the struct pointed to by the Data field. |
| Data | Supplies a pointer to a per-event type struct. More details below. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_MODIFY_TYPE`](wesp-rule-event-modification.md#esp_event_modify_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_ACCESS_MASK_MODIFICATION

The structure `ESP_ACCESS_MASK_MODIFICATION` is used to describe an ACCESS_MASK modification as part of a rule.

#### Syntax

```cpp
typedef struct ESP_ACCESS_MASK_MODIFICATION
{
    ACCESS_MASK AccessToSet;
    ACCESS_MASK AccessToClear;
} ESP_ACCESS_MASK_MODIFICATION;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| AccessToSet | Specifies accesses to set if the comparison is true. |
| AccessToClear | Specifies accesses to clear if the comparison is true. Note that accesses are set before they are cleared. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_ACCESS_MASK_MODIFICATION_LIST

The structure `ESP_ACCESS_MASK_MODIFICATION_LIST` is used to describe a list of ACCESS_MASK modifications to make as part of a rule.

#### Syntax

```cpp
typedef struct ESP_ACCESS_MASK_MODIFICATION_LIST
{
    UINT32 ModificationsCount;
    _Field_size_(ModificationsCount) const ESP_ACCESS_MASK_MODIFICATION* Modifications;
} ESP_ACCESS_MASK_MODIFICATION_LIST;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ModificationsCount | Specifies the number of elements in the modifications array. |
| Modifications | Specifies an array of modifications to make to the ACCESS_MASK. The modifications are applied in order. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_MASK_MODIFICATION`](wesp-rule-event-modification.md#esp_access_mask_modification)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
